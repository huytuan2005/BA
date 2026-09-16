# BA Governance — Phase 2: Automated Quality Gate

## Purpose

Phase 2 upgrades the existing GitHub Actions check from a single implementation-traceability check into a broader, dependency-light quality gate.

The existing GitHub job name remains:

`Implementation Traceability`

This keeps the already-configured required status check stable while expanding the checks executed inside that job.

## Automated checks

1. Repository governance baseline exists.
2. All governed projects pass implementation traceability.
3. Manifest-required project artifacts exist.
4. Duplicate ID declarations inside a single artifact are rejected.
5. Unresolved `TODO` / `TBD` / `FIXME` markers are rejected.
6. Implementation-traceability regression tests pass.
7. Self-Storage governance regression tests pass.
8. Self-Storage API edge-case tests pass against a real backend/API/database runtime.

## Important boundary

This gate checks governance and artifact integrity. It does not invent or resolve business decisions. Legitimate `OPEN`, `UNKNOWN`, and `BLOCKED` states remain valid project states and are not automatically treated as CI failures.

## Local execution

```text
python scripts/run_governance_quality_gate.py
```

Expected:

```text
RESULT: PASS
```

The same command runs in GitHub Actions for pull requests and pushes to `main`.
