#!/usr/bin/env python3
"""Minimal dependency-free regression tests for the CI checker."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "scripts" / "implementation_traceability_check.py"

def run(project: Path) -> int:
    result = subprocess.run([sys.executable, str(CHECKER), str(project)], cwd=ROOT, check=False)
    return result.returncode

def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "project"
        (base / "implementation").mkdir(parents=True)
        (base / "implementation-traceability").mkdir(parents=True)
        (base / "backend").mkdir()
        (base / "implementation" / "implementation.md").write_text(
            "# Implementation\nIMP-TEST-001\n", encoding="utf-8"
        )
        (base / "backend" / "server.js").write_text("// test artifact\n", encoding="utf-8")
        (base / "implementation-traceability" / "implementation-traceability-matrix.md").write_text(
            "| Artifact | Implementation item | Approved upstream evidence |\n"
            "| backend/server.js | IMP-TEST-001 | FR-TEST-001 |\n",
            encoding="utf-8",
        )
        (base / "requirements.md").write_text("FR-TEST-001\n", encoding="utf-8")
        assert run(base) == 0, "valid fixture must pass"

        (base / "backend" / "server.js").unlink()
        assert run(base) != 0, "missing artifact must fail"

    print("Traceability checker regression tests: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
