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
    assert answer_path == _trial_dir() / "artifacts" / "answer.txt"
    assert answer_path.is_file()
    answer = answer_path.read_text(encoding="utf-8")
    assert answer.strip()


# concern: trajectory_schema_validity
def test_trajectory_uses_the_supported_schema():
    assert _trajectory_path() == _trial_dir() / "agent" / "trajectory.json"
    assert _trajectory_path().is_file()

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


# concern: corpus_only_evidence
def test_corpus_inventory_matches_the_task_sources():
    expected = {
        "company_profiles.json",
        "financials/balance_sheet/dal_balance_sheet.json",
        "financials/cash_flow/aal_cash_flow.json",
        "financials/cash_flow/dal_cash_flow.json",
        "financials/cash_flow/luv_cash_flow.json",
        "financials/cash_flow/ual_cash_flow.json",
        "financials/income_statement/aal_income_statement.json",
        "financials/income_statement/dal_income_statement.json",
        "financials/income_statement/luv_income_statement.json",
        "financials/income_statement/ual_income_statement.json",
        "press_releases/dal_2025-06-10_8-k.txt",
        "press_releases/dal_2025-07-10_8-k.txt",
        "press_releases/dal_2025-09-11_8-k.txt",
        "press_releases/dal_2025-10-09_8-k.txt",
        "press_releases/dal_2025-12-03_8-k.txt",
        "press_releases/dal_2026-01-13_8-k.txt",
        "press_releases/dal_2026-03-17_8-k.txt",
        "press_releases/dal_2026-04-08_8-k.txt",
        "sec_filings/10-k/dal_2023_10-k.txt",
        "sec_filings/10-k/dal_2024_10-k.txt",
        "sec_filings/10-k/dal_2025_10-k.txt",
        "sec_filings/10-q/dal_2024q2_10-q.txt",
        "sec_filings/10-q/dal_2024q3_10-q.txt",
        "sec_filings/10-q/dal_2025q1_10-q.txt",
        "sec_filings/10-q/dal_2025q2_10-q.txt",
        "sec_filings/10-q/dal_2025q3_10-q.txt",
        "sec_filings/10-q/dal_2026q1_10-q.txt",
        "sec_filings/s-1/dal_2004_s-1.txt",
    }
    corpus_root = _corpus_dir().resolve()
    actual = set()

    for path in _corpus_files():
        resolved = path.resolve()
        assert path.is_file()
        assert corpus_root in resolved.parents
        actual.add(resolved.relative_to(corpus_root).as_posix())

    assert actual == expected


# concern: citation_resolution
def test_every_file_like_answer_token_resolves_to_a_corpus_file():
    answer = _answer_path().read_text(encoding="utf-8")
    tokens = _citation_tokens(answer)
    cited_files = _cited_files(answer)
    corpus_root = _corpus_dir().resolve()
    corpus_files = _corpus_files()

    assert tokens
    assert cited_files

    corpus_by_path = {}
    for path in corpus_files:
        resolved = path.resolve()
        assert corpus_root in resolved.parents
        corpus_by_path[resolved] = (
            resolved.relative_to(corpus_root).as_posix(),
            resolved.name,
        )

    matched = set()
    for token in tokens:
        normalized = token.replace("\\", "/")
        token_matches = {
            resolved
            for resolved, forms in corpus_by_path.items()
            if normalized == forms[0]
            or normalized == forms[1]
            or normalized.endswith("/" + forms[0])
        }
        assert token_matches
        matched.update(token_matches)

    cited_resolved = {path.resolve() for path in cited_files}
    assert matched == cited_resolved
    assert cited_resolved.issubset(set(corpus_by_path))


# concern: corpus_only_evidence
def test_all_cited_files_are_regular_files_below_corpus_root():
    answer = _answer_path().read_text(encoding="utf-8")
    corpus_root = _corpus_dir().resolve()
    corpus_files = {path.resolve() for path in _corpus_files()}
    cited_files = _cited_files(answer)

    assert cited_files
    for path in cited_files:
        resolved = path.resolve()
        assert resolved in corpus_files
        assert corpus_root in resolved.parents
        assert resolved.is_file()


# concern: evidence_exposed_before_write
def test_each_cited_corpus_file_was_exposed_before_the_answer_write():
    steps = _load_steps()
    write_index = _answer_write_index(steps)

    assert write_index is not None
    assert 0 <= write_index < len(steps)

    answer = _answer_path().read_text(encoding="utf-8")
    cited_files = _cited_files(answer)
    exposed = _paths_exposed_before(steps, write_index)
    corpus_root = _corpus_dir().resolve()

    assert cited_files
    assert isinstance(exposed, str)

    for path in cited_files:
        resolved = path.resolve()
        relative = resolved.relative_to(corpus_root).as_posix()
        assert (
            str(path) in exposed
            or resolved.as_posix() in exposed
            or relative in exposed
            or resolved.name in exposed
        )
