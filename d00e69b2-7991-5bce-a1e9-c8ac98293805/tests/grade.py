"""3-task LLM judge that scores the agent's analysis against ground truth.

Task 1: Hallucination check (heavy, full data context). Returns unverifiable_claims.
Task 2: Per-move hit check (light, no data context). Uses flagged claims to mark moves_tainted.
Task 3: Synthesis check (light, no data context).

Scoring cascade is the standard move-tainted discount.
"""

import json
import os
import re
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from google.genai import Client
from google.genai.types import GenerateContentConfig

ANSWER_PATH = Path("/app/answer.txt")
GROUND_TRUTH_PATH = Path(os.environ.get("GROUND_TRUTH_PATH") or "/tests/ground_truth.txt")
DATA_DIR = Path(os.environ.get("DATA_DIR") or "/app/data")
REWARD_PATH = Path(os.environ.get("REWARD_PATH") or "/logs/verifier/reward.txt")
DETAILS_PATH = Path(os.environ.get("DETAILS_PATH") or "/logs/verifier/details.json")

MODEL = "gemini-3.1-pro-preview"

PROMPTS_DIR = Path(__file__).parent
TASK1_PROMPT = (PROMPTS_DIR / "grading_prompt_task1.md").read_text()
TASK2_PROMPT = (PROMPTS_DIR / "grading_prompt_task2.md").read_text()
TASK3_PROMPT = (PROMPTS_DIR / "grading_prompt_task3.md").read_text()


# Require whitespace + non-space after the dot: without it a wrapped rubric line
# beginning "2026. was a strong year" parses as a phantom theme, inflating
# num_themes so themes_covered == num_themes (and thus 4/4) becomes unreachable.
THEME_LINE_RE = re.compile(r"^\d+\.\s+(?=\S)")
MOVE_LINE_RE = re.compile(r"^\s*\[[a-z]\]\s+", re.MULTILINE)


def parse_theme_move_counts(ground_truth: str) -> list[tuple[str, int]]:
    """Return [(theme_label, n_moves), ...] in rubric order.

    The threshold for "covered" is computed in code as min(n_moves - 1, 3).
    """
    lines = ground_truth.split("\n")
    theme_starts = [i for i, line in enumerate(lines) if THEME_LINE_RE.match(line.strip())]
    result: list[tuple[str, int]] = []
    for k, start in enumerate(theme_starts):
        end = theme_starts[k + 1] if k + 1 < len(theme_starts) else len(lines)
        block = "\n".join(lines[start:end])
        label = re.sub(r"^\d+\.\s*", "", lines[start].strip())
        n_moves = len(MOVE_LINE_RE.findall(block))
        result.append((label, n_moves))
    return result


def coverage_threshold(n_moves: int) -> int:
    """One move of slack, capped at 3 so very-rich themes don't ratchet to all-required."""
    return max(1, min(n_moves - 1, 3))


def discover_cited_files(answer_text: str, data_dir: Path) -> list[Path]:
    """Return data files the agent explicitly references by name or relative path.

    Instruction.md tells the agent to inline-cite every claim with a file path,
    so we only verify against files actually named in the answer. Peer-ticker
    expansion and auto-included canonical files (company_profiles.json) were
    intentionally removed — they blew past Gemini's 1M-token input cap when the
    agent wrote a long answer touching multiple peer tickers.
    """
    if not data_dir.exists():
        return []
    cited: list[Path] = []
    for path in sorted(data_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(data_dir)
        if str(rel) in answer_text or path.name in answer_text:
            cited.append(path)
    return cited


def build_cited_data_block(files: list[Path], data_dir: Path) -> str:
    if not files:
        return "(The agent did not cite any data files, or no cited file could be located.)"
    blocks: list[str] = []
    for path in files:
        rel = path.relative_to(data_dir)
        try:
            content = path.read_text(errors="replace")
        except Exception as e:
            content = f"<error reading file: {e}>"
        header = f"\n=== FILE: data/{rel} ===\n"
        blocks.append(header + content)
    return "".join(blocks)


def write_failure(reason: str, extra: dict | None = None) -> None:
    REWARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    DETAILS_PATH.parent.mkdir(parents=True, exist_ok=True)
    REWARD_PATH.write_text("0")
    payload: dict = {"error": reason, "score": 0}
    if extra:
        payload.update(extra)
    DETAILS_PATH.write_text(json.dumps(payload, indent=2))


def _parse_json_with_fallback(raw: str) -> dict | None:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0]
    raw = re.sub(r",(\s*[}\]])", r"\1", raw)
    try:
        return json.loads(raw.strip())
    except json.JSONDecodeError:
        try:
            return json.JSONDecoder().raw_decode(raw.strip())[0]
        except json.JSONDecodeError:
            return None


def _call_judge(client: Client, prompt: str, max_attempts: int = 2) -> dict | None:
    config = GenerateContentConfig(
        temperature=0,
        response_mime_type="application/json",
        max_output_tokens=16384,
    )
    for _ in range(max_attempts):
        response = client.models.generate_content(model=MODEL, contents=prompt, config=config)
        parsed = _parse_json_with_fallback(response.text)
        if parsed is not None:
            return parsed
    return None


def task1_hallucination_check(answer: str, data_context: str, client: Client) -> dict | None:
    """None means the judge failed — NOT that the answer was clean.

    Defaulting to {"hallucinations_detected": False} on failure granted a free
    pass: no claims flagged means no moves tainted. Meanwhile a task-2 failure
    scored 0. That asymmetry made grader flakiness indistinguishable from a bad
    rubric when validating tasks end-to-end.
    """
    prompt = TASK1_PROMPT.format(data_context=data_context, agent_answer=answer)
    return _call_judge(client, prompt)


def task2_per_move_check(answer: str, ground_truth: str, num_themes: int, flagged_claims: list, client: Client) -> dict | None:
    """None means the judge failed — NOT that the answer covered nothing."""
    claims_block = (
        json.dumps(flagged_claims, indent=2) if flagged_claims else "(No claims were flagged as hallucinations.)"
    )
    prompt = TASK2_PROMPT.format(
        ground_truth=ground_truth,
        agent_answer=answer,
        flagged_claims_block=claims_block,
        num_themes=num_themes,
    )
    return _call_judge(client, prompt)


def task3_synthesis_check(answer: str, ground_truth: str, client: Client) -> dict:
    prompt = TASK3_PROMPT.format(ground_truth=ground_truth, agent_answer=answer)
    return _call_judge(client, prompt) or {"synthesis_found": None}


def grade():
    if not ANSWER_PATH.exists():
        write_failure("No answer.txt found")
        return

    agent_answer = ANSWER_PATH.read_text().strip()
    ground_truth = GROUND_TRUTH_PATH.read_text().strip()
    theme_counts = parse_theme_move_counts(ground_truth)
    num_themes = len(theme_counts)

    if not agent_answer:
        write_failure("answer.txt is empty")
        return

    cited_files = discover_cited_files(agent_answer, DATA_DIR)

    client = Client()
    cited_data_block = build_cited_data_block(cited_files, DATA_DIR)
    data_context = (
        "The block below contains the contents of the data files the agent cited in "
        "their answer. Treat this as the ground truth for factual verification.\n\n"
        f"<cited_data>\n{cited_data_block}\n</cited_data>"
    )

    # Task 1 first (provides claims to Task 2)
    t1 = task1_hallucination_check(agent_answer, data_context, client)
    if t1 is None:
        # Grounding drives tainting; without it we cannot score honestly. Mark the
        # trial invalid rather than silently crediting an unchecked answer.
        write_failure(
            "task1 (grounding) judge returned unparsable output — trial invalid, not scored",
            extra={"judge_failure": "task1", "valid_trial": False},
        )
        return
    claims = t1.get("unverifiable_claims") or []

    # Tasks 2 and 3 in parallel
    with ThreadPoolExecutor(max_workers=2) as pool:
        f2 = pool.submit(task2_per_move_check, agent_answer, ground_truth, num_themes, claims, client)
        f3 = pool.submit(task3_synthesis_check, agent_answer, ground_truth, client)
        t2 = f2.result()
        t3 = f3.result()

    if t2 is None:
        write_failure(
            "task2 (coverage) judge returned unparsable output — trial invalid, not scored",
            extra={"judge_failure": "task2", "valid_trial": False},
        )
        return

    # Compute coverage per theme with move-tainted discounting (same scoring as monolithic)
    judge_themes = t2.get("themes") or []
    themes_hit: list[dict] = []
    themes_missed: list[dict] = []
    # Match the judge's themes by label first. Positional indexing silently
    # attributes moves to the wrong theme if the judge reorders or drops one.
    judge_by_label = {
        str(j.get("label", "")).strip().lower(): j
        for j in judge_themes
        if isinstance(j, dict) and str(j.get("label", "")).strip()
    }
    for i, (label, n_moves) in enumerate(theme_counts):
        judge = judge_by_label.get(label.strip().lower())
        if judge is None:
            judge = judge_themes[i] if i < len(judge_themes) else {}
        moves_hit_letters = [str(m).strip("[]") for m in (judge.get("moves_hit") or [])]
        moves_missed_letters = [str(m).strip("[]") for m in (judge.get("moves_missed") or [])]
        moves_tainted_letters = {str(m).strip("[]") for m in (judge.get("moves_tainted") or [])}
        valid_hit_letters = [m for m in moves_hit_letters if m not in moves_tainted_letters]
        threshold = coverage_threshold(n_moves)
        bucket = themes_hit if len(valid_hit_letters) >= threshold else themes_missed
        bucket.append(
            {
                "label": label,
                "moves_hit": moves_hit_letters,
                "moves_missed": moves_missed_letters,
                "moves_tainted": sorted(moves_tainted_letters),
                "move_reasoning": judge.get("move_reasoning") or {},
                "n_moves": n_moves,
                "threshold": threshold,
            }
        )
    themes_covered = len(themes_hit)

    synth = t3.get("synthesis_found")
    has_synthesis = bool(synth) and synth != "null"

    # instruction.md tells the agent exactly which themes to cover, so we require
    # all of them for the top dense tiers. Move-level thresholds (within each theme)
    # remain flexible via coverage_threshold().
    # Guard: a rubric with no parseable themes should always score 0.
    if num_themes == 0:
        score = 0
    elif themes_covered == num_themes and has_synthesis:
        score = 4
    elif themes_covered == num_themes:
        score = 3
    elif themes_covered >= 2:
        score = 2
    elif themes_covered >= 1:
        score = 1
    else:
        score = 0

    # Normalize hallucinations_detected: only real True / "true" counts — a
    # stringified "false" would be truthy in Python and misreport in details.json.
    hall_raw = t1.get("hallucinations_detected")
    hallucinations_detected = hall_raw is True or hall_raw == "true"

    result = {
        "score": score,
        # Hedge-Bench 4.3: only valid trials enter any metric. A judge failure now
        # sets this False (see write_failure calls above) instead of scoring 0.
        "valid_trial": True,
        "themes_covered": themes_covered,
        "themes_hit": themes_hit,
        "themes_missed": themes_missed,
        "hallucinations_detected": hallucinations_detected,
        "unverifiable_claims": claims,
        "synthesis_found": synth,
        "sparse_reward": 1 if score == 4 else 0,
        "cited_files": [str(p.relative_to(DATA_DIR)) for p in cited_files],
    }

    REWARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    DETAILS_PATH.parent.mkdir(parents=True, exist_ok=True)
    REWARD_PATH.write_text(str(result["sparse_reward"]))
    DETAILS_PATH.write_text(json.dumps(result, indent=2))

    print(f"Score: {score}/4  (sparse={result['sparse_reward']})")
    print(f"Hallucinations: {result['hallucinations_detected']}")
    print(f"Themes hit: {[t['label'] for t in themes_hit]}")
    print(f"Themes missed: {[t['label'] for t in themes_missed]}")
    print(f"Cited files: {len(cited_files)}")


if __name__ == "__main__":
    try:
        grade()
    except Exception as exc:
        try:
            write_failure(f"Grader crashed: {exc}", extra={"traceback": traceback.format_exc()})
        except Exception:
            pass
        raise
