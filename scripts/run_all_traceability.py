#!/usr/bin/env python3
"""Run implementation traceability checks for every project that has a matrix."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
CHECKER = ROOT / "scripts" / "implementation_traceability_check.py"

def main() -> int:
    targets = sorted(p.parent.parent for p in PROJECTS.glob("*/implementation-traceability/implementation-traceability-matrix.md"))
    if not targets:
        print("FAIL: no projects with implementation-traceability matrix found")
        return 1
    failed = False
    for project in targets:
        print(f"\n=== {project.relative_to(ROOT)} ===")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(project)],
            cwd=ROOT,
            check=False,
        )
        failed |= result.returncode != 0
    print("\nALL PROJECTS: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
