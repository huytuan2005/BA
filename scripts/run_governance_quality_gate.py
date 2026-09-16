#!/usr/bin/env python3
"""Dependency-free governance quality gate for BA projects.

The gate validates repository governance configuration and project artifact
integrity without making business decisions. It combines objective checks:
1) implementation traceability,
2) required governance artifacts,
3) declared-ID integrity (duplicate declarations),
4) required project artifact presence (manifest-driven),
5) automated project regression tests (manifest-driven).

A project may legitimately be OPEN/BLOCKED as a business state; this gate
checks whether the governance evidence is structurally valid, not whether the
project itself is necessarily ready for production.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACEABILITY_RUNNER = ROOT / "scripts" / "run_all_traceability.py"

DECL_ID_RE = re.compile(
    r"(?im)^(?:#{1,6}\s+|[-*]\s+|\*\*)"
    r"(?P<id>(?:FR|BR|NFR|FN|UC|BP|IR|IMP|PLAN|VERIFY|CLOSE)-[A-Z0-9][A-Z0-9_-]*)"
    r"(?:\*\*|\s*(?:—|-|:))"
)

FORBIDDEN_PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def required_repo_files() -> list[str]:
    return [
        ".github/workflows/governance.yml",
        ".github/CODEOWNERS",
        ".github/CONTRIBUTING.md",
        ".github/pull_request_template.md",
        ".github/branch-protection.md",
        "scripts/implementation_traceability_check.py",
        "scripts/run_all_traceability.py",
        "scripts/tests/test_implementation_traceability_check.py",
    ]


def load_manifest(project: Path) -> dict:
    manifest = project / "governance" / "quality-gate.json"
    if not manifest.exists():
        return {"required_files": [], "tests": []}
    return json.loads(manifest.read_text(encoding="utf-8"))


def check_required_files(base: Path, files: list[str]) -> tuple[bool, str]:
    missing = [p for p in files if not (base / p).is_file()]
    if missing:
        return False, "required artifacts missing: " + ", ".join(missing)
    return True, f"required artifacts present ({len(files)})"


def check_duplicate_declarations(project: Path) -> tuple[bool, str]:
    """Reject duplicate ID declarations within the same artifact file.

    References to the same approved ID across downstream artifacts are valid
    traceability links, so cross-file repetition is not treated as a duplicate.
    """
    duplicate_files: list[str] = []
    declared_count = 0
    for path in sorted(project.rglob("*.md")):
        if "/.git/" in path.as_posix():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        ids = [m.group("id") for m in DECL_ID_RE.finditer(text)]
        declared_count += len(set(ids))
        duplicates = sorted({item_id for item_id in ids if ids.count(item_id) > 1})
        if duplicates:
            duplicate_files.append(f"{path} -> {', '.join(duplicates)}")
    if duplicate_files:
        return False, "duplicate ID declarations within file: " + "; ".join(duplicate_files)
    return True, f"no duplicate ID declarations ({declared_count} declarations checked)"

def check_placeholders(project: Path, allow_files: list[str]) -> tuple[bool, str]:
    offenders: list[str] = []
    allow = {str((project / p).resolve()) for p in allow_files}
    for path in sorted(project.rglob("*.md")):
        if str(path.resolve()) in allow:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if FORBIDDEN_PLACEHOLDER_RE.search(text):
            offenders.append(str(path))
    if offenders:
        return False, "unresolved TODO/TBD/FIXME markers: " + ", ".join(offenders)
    return True, "no unresolved TODO/TBD/FIXME markers in governed artifacts"


def run_project_tests(project: Path, tests: list[dict]) -> list[tuple[bool, str]]:
    results: list[tuple[bool, str]] = []
    for spec in tests:
        name = spec.get("name", "unnamed test")
        cmd = spec["command"]
        rc, output = run(cmd, ROOT)
        if rc != 0:
            tail = output[-800:] if output else "no output"
            results.append((False, f"{name} failed (exit {rc}): {tail}"))
        else:
            results.append((True, f"{name} passed"))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", action="append", dest="projects")
    args = parser.parse_args()

    if args.projects:
        projects = [Path(p).resolve() for p in args.projects]
    else:
        projects = sorted(
            p for p in (ROOT / "projects").iterdir()
            if p.is_dir() and (p / "implementation-traceability" / "implementation-traceability-matrix.md").exists()
        )

    checks: list[tuple[bool, str]] = []
    for rel in required_repo_files():
        if not (ROOT / rel).is_file():
            checks.append((False, f"repository governance file missing: {rel}"))
    if all(ok for ok, _ in checks) or not checks:
        checks.append((True, "repository governance baseline present"))

    rc, out = run([sys.executable, str(TRACEABILITY_RUNNER)], ROOT)
    checks.append((rc == 0, "implementation traceability runner: " + ("PASS" if rc == 0 else "FAIL")))
    if rc != 0 and out:
        checks.append((False, out.splitlines()[-1]))

    if not projects:
        checks.append((False, "no governed projects discovered"))
    else:
        for project in projects:
            if not project.is_dir():
                checks.append((False, f"project not found: {project}"))
                continue
            manifest = load_manifest(project)
            checks.append(check_required_files(project, manifest.get("required_files", [])))
            checks.append(check_duplicate_declarations(project))
            checks.append(check_placeholders(project, manifest.get("allow_placeholders_in", [])))
            checks.extend(run_project_tests(project, manifest.get("tests", [])))

    failed = [message for ok, message in checks if not ok]
    print("BA Governance — Quality Gate")
    for ok, message in checks:
        print(f"[{ 'PASS' if ok else 'FAIL' }] {message}")
    if failed:
        print("\nRESULT: FAIL")
        return 1
    print("\nRESULT: PASS")
    print(f"Checks passed: {len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
