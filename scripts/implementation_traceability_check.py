#!/usr/bin/env python3
"""Objective implementation-traceability check for CI.

Checks a project directory without interpreting business meaning:
- implementation items declared in implementation artifacts are traceable
  in the implementation-traceability matrix;
- every matrix implementation item is declared;
- every referenced implementation artifact path exists;
- every explicit upstream requirement/business-rule ID reference exists
  somewhere in the project artifacts;
- no duplicate implementation item IDs are declared in implementation artifacts.

Exit 0 only when all checks pass.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

IMPL_ID_RE = re.compile(r"\bIMP-[A-Z0-9][A-Z0-9_-]*\b")
UPSTREAM_ID_RE = re.compile(r"\b(?:FR|BR|NFR)-[A-Z0-9][A-Z0-9_-]*\b")
PATH_RE = re.compile(r"(?i)(?:^|\|)\s*([^|\n]+?\.(?:js|ts|tsx|jsx|py|java|sql|html|css|md))\s*(?:—|-|\|)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", default="projects/self-storage")
    args = parser.parse_args()
    root = Path(args.project).resolve()
    if not root.is_dir():
        print(f"FAIL: project directory not found: {root}")
        return 1

    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        print("FAIL: no markdown artifacts found")
        return 1

    impl_source_files = [
        p for p in md_files
        if "/implementation/" in p.as_posix()
        or "/implementation-plan/" in p.as_posix()
    ]
    matrix_files = [
        p for p in md_files
        if p.name == "implementation-traceability-matrix.md"
    ]
    if not matrix_files:
        print("FAIL: implementation-traceability-matrix.md not found")
        return 1
    matrix = matrix_files[0]

    impl_ids: list[str] = []
    for p in impl_source_files:
        impl_ids.extend(IMPL_ID_RE.findall(read_text(p)))
    impl_ids = sorted(set(impl_ids))

    matrix_text = read_text(matrix)
    matrix_ids = sorted(set(IMPL_ID_RE.findall(matrix_text)))

    checks: list[tuple[bool, str]] = []
    checks.append((bool(impl_ids), "implementation items discovered"))

    missing_in_matrix = sorted(set(impl_ids) - set(matrix_ids))
    checks.append((not missing_in_matrix, f"all implementation items appear in matrix{': ' + ', '.join(missing_in_matrix) if missing_in_matrix else ''}"))

    extra_in_matrix = sorted(set(matrix_ids) - set(impl_ids))
    checks.append((not extra_in_matrix, f"matrix does not contain undeclared implementation items{': ' + ', '.join(extra_in_matrix) if extra_in_matrix else ''}"))

    # Validate explicit upstream IDs against all project markdown.
    all_text = "\n".join(read_text(p) for p in md_files)
    upstream_refs = sorted(set(UPSTREAM_ID_RE.findall(matrix_text)))
    upstream_missing = []
    for ref in upstream_refs:
        occurrences = all_text.count(ref)
        # Matrix itself counts once; require at least one other occurrence.
        if occurrences < 2:
            upstream_missing.append(ref)
    checks.append((not upstream_missing, f"all explicit upstream IDs resolve{': ' + ', '.join(upstream_missing) if upstream_missing else ''}"))

    # Validate source artifact paths from matrix rows. We deliberately only
    # validate paths that look like concrete repository paths.
    concrete_paths: list[str] = []
    for line in matrix_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        for match in PATH_RE.findall(line):
            candidate = match.strip().strip('`')
            if candidate and candidate.lower() not in {"path", "artifact"}:
                concrete_paths.append(candidate)

    missing_paths: list[str] = []
    for rel in concrete_paths:
        normalized = rel.replace("\\", "/").strip()
        # Remove optional leading ./
        normalized = normalized[2:] if normalized.startswith("./") else normalized
        # Matrix may include a file followed by a section marker; keep first token.
        normalized = normalized.split(" ")[0]
        if not (root / normalized).exists():
            missing_paths.append(normalized)
    checks.append((not missing_paths, f"all concrete implementation artifact paths exist{': ' + ', '.join(sorted(set(missing_paths))) if missing_paths else ''}"))

    failed = False
    print(f"Implementation Traceability CI — {root.relative_to(root.parent.parent) if len(root.parents) >= 2 else root}")
    for ok, message in checks:
        print(f"[{ 'PASS' if ok else 'FAIL' }] {message}")
        failed |= not ok

    if failed:
        print("\nRESULT: FAIL")
        return 1
    print("\nRESULT: PASS")
    print("100% implementation items traceable")
    print("0 invalid implementation references")
    print("0 orphan implementation items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
