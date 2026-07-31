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
def test_answer_artifact_is_canonical_nonempty_text():
    answer_path = _answer_path()
    assert answer_path == _trial_dir() / "artifacts" / "answer.txt"
    assert answer_path.is_file()
    assert answer_path.stat().st_size > 0
    answer = answer_path.read_text(encoding="utf-8")
    assert answer.strip()


# concern: citation_resolution
def test_every_citation_token_resolves_to_a_corpus_file():
    answer = _answer_path().read_text(encoding="utf-8")
    tokens = _citation_tokens(answer)
    cited_paths = {path.resolve() for path in _cited_files(answer)}
    corpus_root = _corpus_dir().resolve()
    corpus_paths = {path.resolve() for path in _corpus_files()}

    assert tokens
    assert tokens == sorted(set(tokens))
    assert cited_paths

    matched_paths = set()
    for token in tokens:
        normalized = token.replace("\\", "/")
        if normalized.startswith("./"):
            normalized = normalized[2:]

        matches = {
            path
            for path in corpus_paths
            if normalized == path.name
            or normalized == path.relative_to(corpus_root).as_posix()
            or normalized.endswith(
                "/" + path.relative_to(corpus_root).as_posix()
            )
        }
        assert matches, f"Unresolved citation token: {token}"
        assert matches <= cited_paths
        matched_paths.update(matches)

    assert cited_paths == matched_paths


# concern: corpus_only_evidence
def test_cited_evidence_is_confined_to_the_declared_corpus():
    declared_paths = {
        "company_profiles.json",
        "financials/balance_sheet/crm_balance_sheet.json",
        "financials/cash_flow/adbe_cash_flow.json",
        "financials/cash_flow/crm_cash_flow.json",
        "financials/cash_flow/now_cash_flow.json",
        "financials/cash_flow/orcl_cash_flow.json",
        "financials/income_statement/adbe_income_statement.json",
        "financials/income_statement/crm_income_statement.json",
        "financials/income_statement/now_income_statement.json",
        "financials/income_statement/orcl_income_statement.json",
        "press_releases/crm_2025-05-28_8-k.txt",
        "press_releases/crm_2025-07-09_8-k.txt",
        "press_releases/crm_2025-09-03_8-k.txt",
        "press_releases/crm_2025-11-18_8-k.txt",
        "press_releases/crm_2025-12-03_8-k.txt",
        "press_releases/crm_2026-02-25_8-k.txt",
        "press_releases/crm_2026-03-16_8-k.txt",
        "press_releases/crm_2026-05-27_8-k.txt",
        "sec_filings/10-k/crm_2024_10-k.txt",
        "sec_filings/10-k/crm_2025_10-k.txt",
        "sec_filings/10-k/crm_2026_10-k.txt",
        "sec_filings/10-q/crm_2024q2_10-q.txt",
        "sec_filings/10-q/crm_2024q3_10-q.txt",
        "sec_filings/10-q/crm_2025q1_10-q.txt",
        "sec_filings/10-q/crm_2025q2_10-q.txt",
        "sec_filings/10-q/crm_2025q3_10-q.txt",
        "sec_filings/10-q/crm_2026q1_10-q.txt",
        "sec_filings/s-1/crm_2003_s-1.txt",
    }
    corpus_root = _corpus_dir().resolve()
    corpus_paths = {path.resolve() for path in _corpus_files()}
    corpus_relpaths = {
        path.relative_to(corpus_root).as_posix() for path in corpus_paths
    }
    answer = _answer_path().read_text(encoding="utf-8")
    cited_paths = {path.resolve() for path in _cited_files(answer)}

    assert "sec_filings/10-k/crm_2026_10-k.txt" in corpus_relpaths
    assert cited_paths
    for path in cited_paths:
        assert path in corpus_paths
        relative_path = path.relative_to(corpus_root).as_posix()
        assert relative_path in declared_paths
        assert path.is_file()


# concern: trajectory_schema_validity
def test_trajectory_has_only_the_guaranteed_structural_requirements():
    trajectory = _load_trajectory()
    required_keys = {
        "schema_version",
        "session_id",
        "agent",
        "steps",
        "final_metrics",
    }

    assert isinstance(trajectory, dict)
    assert required_keys <= set(trajectory)
    assert _trajectory_path() == _trial_dir() / "agent" / "trajectory.json"
    assert _trajectory_path().is_file()

    steps = trajectory.get("steps")
    assert isinstance(steps, list)
    assert steps == _load_steps()

    for step in steps:
        assert isinstance(step, dict)
        assert step.get("source") in {"user", "agent"}
        assert isinstance(step.get("message"), str)

        if "tool_calls" in step:
            assert isinstance(step["tool_calls"], list)
            for tool_call in step["tool_calls"]:
                assert isinstance(tool_call, dict)
                assert "function_name" in tool_call
                assert "arguments" in tool_call
            assert _tool_calls(step) == step["tool_calls"]


# concern: evidence_exposed_before_write
def test_all_cited_corpus_paths_were_exposed_before_the_first_answer_write():
    steps = _load_steps()
    write_index = _answer_write_index(steps)

    assert write_index is not None
    assert 0 <= write_index < len(steps)

    exposed = _paths_exposed_before(steps, write_index)
    assert isinstance(exposed, str)

    answer = _answer_path().read_text(encoding="utf-8")
    cited_paths = _cited_files(answer)
    corpus_root = _corpus_dir().resolve()

    assert cited_paths
    for path in cited_paths:
        resolved = path.resolve()
        relative_path = resolved.relative_to(corpus_root).as_posix()
        assert (
            relative_path in exposed
            or resolved.name in exposed
            or str(resolved) in exposed
        ), f"Cited corpus file was not exposed before the answer write: {relative_path}"
