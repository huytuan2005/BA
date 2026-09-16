#!/usr/bin/env python3
"""Regression tests for governance quality-gate helpers."""
from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("quality_gate", ROOT / "scripts" / "run_governance_quality_gate.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        project = root / "project"
        project.mkdir()
        (project / "implementation.md").write_text("# Implementation\n- IMP-001 — item\n", encoding="utf-8")
        ok, _ = MOD.check_duplicate_declarations(project)
        assert ok

        (project / "duplicate.md").write_text("# Another\n- IMP-001 — duplicate\n- IMP-001 — duplicate again\n", encoding="utf-8")
        ok, message = MOD.check_duplicate_declarations(project)
        assert not ok and "IMP-001" in message

        (project / "todo.md").write_text("TBD\n", encoding="utf-8")
        ok, _ = MOD.check_placeholders(project, [])
        assert not ok

        ok, _ = MOD.check_placeholders(project, ["todo.md"])
        assert ok

    print("Governance quality-gate regression tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
