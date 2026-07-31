import json
import os
import re
from pathlib import Path

import pytest


# === FIXED DETERMINISTIC INVARIANTS ===
_REQUIRED_TRAJECTORY_KEYS = {"schema_version", "session_id", "agent", "steps", "final_metrics"}
_WRITE_TOOLS = {"write", "write_file", "writefile"}
_MINIMUM_STEPS = 3
_CITATION_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:/app/data/)?"
    r"([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\."
    r"(?:txt|json|csv|md|pdf|html?|xml|xlsx?))"
    r"(?![A-Za-z0-9_.-])",
    re.IGNORECASE,
)


def _trial_dir():
    return Path(os.environ["TRIAL_DIR"])


def _corpus_dir():
    return Path(os.environ["CORPUS_DIR"])


def _answer_path():
    return _trial_dir() / "artifacts" / "answer.txt"


def _trajectory_path():
    return _trial_dir() / "agent" / "trajectory.json"


def _load_trajectory():
    return json.loads(_trajectory_path().read_text(encoding="utf-8"))


def _load_steps():
    trajectory = _load_trajectory()
    assert isinstance(trajectory, dict), "trajectory must be a JSON object"
    steps = trajectory.get("steps")
    assert isinstance(steps, list), "trajectory steps must be a list"
    return steps


def _corpus_files():
    root = _corpus_dir()
    return [path for path in sorted(root.rglob("*")) if path.is_file()]


def _cited_files(answer):
    root = _corpus_dir()
    return [
        path
        for path in _corpus_files()
        if str(path.relative_to(root)) in answer or path.name in answer
    ]


def _citation_tokens(answer):
    return sorted(set(_CITATION_RE.findall(answer)))


def _tool_calls(step):
    calls = step.get("tool_calls") if isinstance(step, dict) else None
    return [call for call in calls if isinstance(call, dict)] if isinstance(calls, list) else []


def _answer_write_index(steps):
    for index, step in enumerate(steps):
        for call in _tool_calls(step):
            name = call.get("function_name")
            arguments = call.get("arguments")
            if not isinstance(name, str) or not isinstance(arguments, dict):
                continue
            path = arguments.get("file_path") or arguments.get("path")
            normalized = path.replace("\\", "/") if isinstance(path, str) else ""
            if name.casefold() in _WRITE_TOOLS and normalized == "/app/answer.txt":
                return index
            command = arguments.get("command")
            if (
                name.casefold() in {"bash", "shell"}
                and isinstance(command, str)
                and re.search(r"(?:>|tee\s+)(?:\s*)/app/answer\.txt", command)
            ):
                return index
    return None


def _paths_exposed_before(steps, end_index):
    parts = []
    for step in steps[:end_index]:
        for call in _tool_calls(step):
            arguments = call.get("arguments")
            parts.append(json.dumps(arguments, default=str))
    return "\n".join(parts)


# concern: answer_artifact_integrity
def test_answer_artifact_integrity():
    answer_path = _answer_path()
    assert answer_path.is_file(), "canonical artifacts/answer.txt is missing"
    answer = answer_path.read_text(encoding="utf-8").strip()
    minimum = int(os.environ.get("KANG_VERIFY_MIN_ANSWER_CHARS", "500"))
    assert answer, "canonical answer is empty"
    assert len(answer) >= minimum, f"answer has {len(answer)} characters; expected at least {minimum}"


# concern: trajectory_schema_validity
def test_trajectory_schema_validity():
    trajectory_path = _trajectory_path()
    assert trajectory_path.is_file(), "agent/trajectory.json is missing"
    trajectory = _load_trajectory()
    assert isinstance(trajectory, dict), "trajectory must be a JSON object"
    missing = sorted(_REQUIRED_TRAJECTORY_KEYS - trajectory.keys())
    assert not missing, f"trajectory is missing required keys: {missing}"
    assert isinstance(trajectory["steps"], list), "trajectory steps must be a list"


# concern: trajectory_schema_validity
def test_minimum_trajectory_step_count():
    steps = _load_steps()
    assert len(steps) >= _MINIMUM_STEPS, f"trajectory has {len(steps)} steps; expected at least {_MINIMUM_STEPS}"


# concern: citation_resolution
def test_citations_resolve():
    answer = _answer_path().read_text(encoding="utf-8")
    root = _corpus_dir()
    cited = _cited_files(answer)
    available = {
        candidate
        for path in _corpus_files()
        for candidate in (str(path.relative_to(root)), path.relative_to(root).as_posix(), path.name)
    }
    unresolved = [token for token in _citation_tokens(answer) if token not in available]
    assert cited, "answer does not name any file available in CORPUS_DIR"
    assert not unresolved, f"answer cites files absent from CORPUS_DIR: {unresolved}"


# concern: corpus_only_evidence
def test_corpus_only_evidence():
    answer = _answer_path().read_text(encoding="utf-8")
    root = _corpus_dir().resolve()
    outside = [str(path) for path in _cited_files(answer) if not path.resolve().is_relative_to(root)]
    assert not outside, f"cited corpus entries resolve outside CORPUS_DIR: {outside}"


# concern: evidence_exposed_before_write
def test_evidence_exposed_before_write():
    steps = _load_steps()
    write_index = _answer_write_index(steps)
    assert write_index is not None, "trajectory has no canonical /app/answer.txt write step"
    exposed = _paths_exposed_before(steps, write_index)
    root = _corpus_dir()
    answer = _answer_path().read_text(encoding="utf-8")
    unexposed = [
        str(path.relative_to(root))
        for path in _cited_files(answer)
        if str(path.relative_to(root)) not in exposed and path.name not in exposed
    ]
    if unexposed:
        pytest.fail(
            "cited files were not exposed in any pre-write tool call "
            f"(Bash/Agent/Read): {unexposed}"
        )


# === TASK-SPECIFIC DETERMINISTIC CHECKS ===

# concern: answer_artifact_integrity
def test_answer_artifact_exists_at_canonical_path_and_is_nonempty():
    answer_path = _answer_path()
    expected_path = _trial_dir() / "artifacts" / "answer.txt"
    assert answer_path == expected_path
    assert answer_path.exists()
    assert answer_path.is_file()
    assert answer_path.resolve().parent == expected_path.parent.resolve()
    assert answer_path.stat().st_size > 0
    assert answer_path.read_text(encoding="utf-8").strip()


# concern: trajectory_schema_validity
def test_trajectory_has_only_the_required_real_schema_constraints():
    trajectory_path = _trajectory_path()
    assert trajectory_path == _trial_dir() / "agent" / "trajectory.json"
    assert trajectory_path.exists()
    assert trajectory_path.is_file()

    trajectory = _load_trajectory()
    assert isinstance(trajectory, dict)
    assert {
        "schema_version",
        "session_id",
        "agent",
        "steps",
        "final_metrics",
    }.issubset(trajectory)

    steps = trajectory.get("steps")
    assert isinstance(steps, list)
    assert steps == _load_steps()

    for step in steps:
        assert isinstance(step, dict)
        assert step.get("source") in {"user", "agent"}
        assert isinstance(step.get("message"), str)
        if "tool_calls" in step:
            assert isinstance(step["tool_calls"], list)
            for call in step["tool_calls"]:
                assert isinstance(call, dict)
                assert "function_name" in call
                assert "arguments" in call


# concern: citation_resolution
def test_every_file_like_citation_token_resolves_to_a_corpus_file():
    answer = _answer_path().read_text(encoding="utf-8")
    tokens = _citation_tokens(answer)
    corpus_root = _corpus_dir().resolve()
    corpus_files = _corpus_files()
    cited_files = _cited_files(answer)

    assert tokens
    assert all(isinstance(token, str) and token for token in tokens)
    assert tokens == sorted(set(tokens))
    assert cited_files

    matched_files = set()
    for token in tokens:
        normalized = token.replace("\\", "/").strip(
            " \t\r\n`'\"()[]{}<>,;"
        )
        token_matches = []
        for corpus_file in corpus_files:
            resolved = corpus_file.resolve()
            assert corpus_root in resolved.parents
            relative = resolved.relative_to(corpus_root).as_posix()
            if (
                normalized == corpus_file.name
                or normalized == relative
                or normalized == corpus_file.as_posix()
                or normalized == resolved.as_posix()
                or normalized.endswith("/" + relative)
            ):
                token_matches.append(corpus_file)
        assert token_matches, token
        matched_files.update(token_matches)

    assert set(cited_files) == matched_files


# concern: corpus_only_evidence
def test_cited_files_are_regular_files_from_the_declared_task_corpus():
    allowed_relative_paths = {
        "company_profiles.json",
        "financials/balance_sheet/sbux_balance_sheet.json",
        "financials/cash_flow/dpz_cash_flow.json",
        "financials/cash_flow/mcd_cash_flow.json",
        "financials/cash_flow/sbux_cash_flow.json",
        "financials/cash_flow/yum_cash_flow.json",
        "financials/income_statement/dpz_income_statement.json",
        "financials/income_statement/mcd_income_statement.json",
        "financials/income_statement/sbux_income_statement.json",
        "financials/income_statement/yum_income_statement.json",
        "press_releases/sbux_2025-07-29_8-k.txt",
        "press_releases/sbux_2025-09-25_8-k.txt",
        "press_releases/sbux_2025-10-29_8-k.txt",
        "press_releases/sbux_2025-11-03_8-k.txt",
        "press_releases/sbux_2026-01-28_8-k.txt",
        "press_releases/sbux_2026-04-02_8-k.txt",
        "press_releases/sbux_2026-04-28_8-k.txt",
        "press_releases/sbux_2026-05-20_8-k.txt",
        "sec_filings/10-k/sbux_2023_10-k.txt",
        "sec_filings/10-k/sbux_2024_10-k.txt",
        "sec_filings/10-k/sbux_2025_10-k.txt",
        "sec_filings/10-q/sbux_2024q1_10-q.txt",
        "sec_filings/10-q/sbux_2024q3_10-q.txt",
        "sec_filings/10-q/sbux_2025q1_10-q.txt",
        "sec_filings/10-q/sbux_2025q2_10-q.txt",
        "sec_filings/10-q/sbux_2025q3_10-q.txt",
        "sec_filings/10-q/sbux_2026q2_10-q.txt",
    }
    answer = _answer_path().read_text(encoding="utf-8")
    cited_files = _cited_files(answer)
    corpus_files = set(_corpus_files())
    corpus_root = _corpus_dir().resolve()

    assert cited_files
    for cited_file in cited_files:
        assert cited_file in corpus_files
        assert cited_file.is_file()
        resolved = cited_file.resolve()
        assert corpus_root in resolved.parents
        relative = resolved.relative_to(corpus_root).as_posix()
        assert relative in allowed_relative_paths


# concern: evidence_exposed_before_write
def test_all_cited_corpus_paths_were_exposed_before_the_answer_write():
    steps = _load_steps()
    write_index = _answer_write_index(steps)

    assert isinstance(steps, list)
    assert write_index is not None
    assert 0 <= write_index < len(steps)

    exposed = _paths_exposed_before(steps, write_index)
    assert isinstance(exposed, str)

    answer = _answer_path().read_text(encoding="utf-8")
    cited_files = _cited_files(answer)
    corpus_root = _corpus_dir().resolve()
    assert cited_files

    for cited_file in cited_files:
        resolved = cited_file.resolve()
        relative = resolved.relative_to(corpus_root).as_posix()
        assert any(
            variant in exposed
            for variant in (
                cited_file.as_posix(),
                resolved.as_posix(),
                relative,
                cited_file.name,
            )
        )
