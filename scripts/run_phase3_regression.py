from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
RESULTS = []


def check(name: str, condition: bool) -> None:
    RESULTS.append((name, bool(condition)))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


# ============================================================
# 1. Skills 9–17
# ============================================================

skills = [
    ("9", "traceability", "SKILL.md"),
    ("10", "blueprint-generator", "SKILL.md"),
    ("11", "implementation-readiness", "SKILL.md"),
    ("12", "implementation", "implementation-SKILL-v1.0.md"),
    ("13", "implementation-plan", "SKILL.md"),
    ("14", "implementation-validator", "SKILL.md"),
    ("15", "implementation-executor", "SKILL.md"),
    ("16", "implementation-verification", "SKILL.md"),
    ("17", "implementation-closure", "SKILL.md"),
]

skills_root = ROOT / ".codex" / "BA contrains"

# ============================================================
# 1. Skills 9–17
# ============================================================

skills = [
    ("9", "traceability", "SKILL.md"),
    ("10", "blueprint-generator", "SKILL.md"),
    ("11", "implementation-readiness", "SKILL.md"),
    ("12", "implementation", "implementation-SKILL-v1.0.md"),
    ("13", "implementation-plan", "SKILL.md"),
    ("14", "implementation-validator", "SKILL.md"),
    ("15", "implementation-executor", "SKILL.md"),
    ("16", "implementation-verification", "SKILL.md"),
    ("17", "implementation-closure", "SKILL.md"),
]

skills_root = ROOT / ".codex" / "BA contrains"

# Phase 3 regression baseline is the authoritative record
# for the lifecycle lock state.
regression_path = ROOT / "projects/regression/phase3-regression.md"
regression_text = read_text(regression_path)

for number, folder, filename in skills:
    path = skills_root / folder / filename
    text = read_text(path)

    check(
        f"Skill {number} definition exists",
        path.exists(),
    )

    version_match = re.search(
        r"(?:\*\*Version:\*\*|Version:|version:)\s*`?v?1\.0`?",
        text,
        re.IGNORECASE,
    )

    check(
        f"Skill {number} version 1.0",
        version_match is not None,
    )

    # The locked state is checked against the Phase 3
    # Locked Skill Baseline rather than requiring every
    # historical SKILL.md to repeat the LOCKED label.
    escaped_path = re.escape(f"{folder}/{filename}")

    lock_match = re.search(
        rf"\|\s*Skill\s+{number}\s*\|\s*`?{escaped_path}`?\s*\|\s*`?v?1\.0`?\s*\|\s*`?LOCKED`?\s*\|",
        regression_text,
        re.IGNORECASE,
    )

    check(
        f"Skill {number} locked",
        lock_match is not None,
    )


# ============================================================
# 2. Phase 3 core artifacts
# ============================================================

artifacts = [
    "projects/self-storage/e2e/PHASE-3.md",
    "projects/self-storage/e2e/BA-baseline-index.md",
    "projects/self-storage/implementation-readiness/implementation-readiness.md",
    "projects/self-storage/implementation/implementation-scope.md",
    "projects/self-storage/implementation/implementation.md",
    "projects/self-storage/implementation-plan/implementation-plan.md",
    "projects/self-storage/implementation-validator/implementation-plan-validation.md",
    "projects/self-storage/implementation-executor/execution-record-phase3.md",
    "projects/self-storage/implementation-verification/verification-record-phase3.md",
    "projects/self-storage/closure/closure-record-phase3.md",
    "projects/regression/phase3-regression.md",
    "projects/self-storage/implementation-traceability/implementation-traceability-matrix.md",
    "projects/self-storage/demo-approval/demo-scope.md",
    "projects/self-storage/implementation-demo/index.html",
    "projects/self-storage/implementation-demo/app.js",
    "projects/self-storage/implementation-demo/styles.css",
]

for artifact in artifacts:
    check(
        f"artifact exists: {artifact}",
        (ROOT / artifact).exists(),
    )


# ============================================================
# 3. Read Phase 3 lifecycle artifacts
# ============================================================

phase3_path = ROOT / "projects/self-storage/e2e/PHASE-3.md"
implementation_path = ROOT / "projects/self-storage/implementation/implementation.md"
scope_path = ROOT / "projects/self-storage/implementation/implementation-scope.md"
plan_path = ROOT / "projects/self-storage/implementation-plan/implementation-plan.md"
validator_path = (
    ROOT
    / "projects/self-storage/implementation-validator/implementation-plan-validation.md"
)
executor_path = (
    ROOT
    / "projects/self-storage/implementation-executor/execution-record-phase3.md"
)
verification_path = (
    ROOT
    / "projects/self-storage/implementation-verification/verification-record-phase3.md"
)
closure_path = ROOT / "projects/self-storage/closure/closure-record-phase3.md"
regression_path = ROOT / "projects/regression/phase3-regression.md"
traceability_path = (
    ROOT
    / "projects/self-storage/implementation-traceability/implementation-traceability-matrix.md"
)
demo_approval_path = ROOT / "projects/self-storage/demo-approval/demo-scope.md"

phase3 = read_text(phase3_path)
impl = read_text(implementation_path)
scope = read_text(scope_path)
plan = read_text(plan_path)
validator = read_text(validator_path)
executor = read_text(executor_path)
verification = read_text(verification_path)
closure = read_text(closure_path)
regression = read_text(regression_path)
traceability = read_text(traceability_path)
demo_approval = read_text(demo_approval_path)


# ============================================================
# 4. Phase 3 master state
# ============================================================

check(
    "PHASE-3 status COMPLETE",
    bool(
        re.search(
            r"\*\*Status:\*\*\s*`COMPLETE`",
            phase3,
            re.IGNORECASE,
        )
    ),
)

check(
    "PHASE-3 regression PASS",
    "FULL FRAMEWORK REGRESSION: PASS" in phase3,
)

check(
    "PHASE-3 production BLOCKED",
    "PRODUCTION SCOPE: BLOCKED" in phase3,
)

check(
    "PHASE-3 demo CLOSED_WITH_GAPS",
    "DEMO SCOPE: CLOSED_WITH_GAPS" in phase3,
)


# ============================================================
# 5. Lifecycle state consistency
# ============================================================

check(
    "implementation demo completed",
    bool(
        re.search(
            r"\*\*Demo implementation:\*\*\s*`?COMPLETED`?",
            impl,
            re.IGNORECASE,
        )
    ),
)

check(
    "implementation production blocked",
    bool(
        re.search(
            r"\*\*Production readiness:\*\*\s*`?BLOCKED`?",
            impl,
            re.IGNORECASE,
        )
    ),
)

check(
    "scope has demo 1",
    "IMP-SS-DEMO-001" in scope,
)

check(
    "scope has demo 2",
    "IMP-SS-DEMO-002" in scope,
)

check(
    "plan has demo plan item 1",
    "IP-SS-DEMO-001" in plan,
)

check(
    "plan has demo plan item 2",
    "IP-SS-DEMO-002" in plan,
)

check(
    "plan contains completed state",
    "COMPLETED" in plan,
)

check(
    "validator allows open items",
    "PASS WITH OPEN ITEMS" in validator,
)

check(
    "executor records NO_ACTION",
    "NO_ACTION" in executor,
)

check(
    "executor does not execute production",
    bool(
        re.search(
            r"No production implementation was executed\.",
            executor,
            re.IGNORECASE,
        )
    ),
)

# Verification must contain both demo items and VERIFIED.
check(
    "verification demo 1 verified",
    "IP-SS-DEMO-001" in verification
    and "VERIFIED" in verification,
)

check(
    "verification demo 2 verified",
    "IP-SS-DEMO-002" in verification
    and "VERIFIED" in verification,
)

# Closure must explicitly record CLOSED_WITH_GAPS.
check(
    "closure overall closed with gaps",
    "CLOSED_WITH_GAPS" in closure,
)


# ============================================================
# 6. Traceability and production boundary
# ============================================================

check(
    "traceability matrix includes demo 1",
    "IMP-SS-DEMO-001" in traceability,
)

check(
    "traceability matrix includes demo 2",
    "IMP-SS-DEMO-002" in traceability,
)

check(
    "traceability matrix PASS",
    "IMPLEMENTATION TRACEABILITY: PASS" in traceability,
)

check(
    "demo approval is non-production",
    bool(
        re.search(
            r"Non-production demo",
            demo_approval,
            re.IGNORECASE,
        )
    ),
)

check(
    "demo approval excludes production payment",
    bool(
        re.search(
            r"No production payment",
            demo_approval,
            re.IGNORECASE,
        )
    ),
)

check(
    "demo approval technical decision is plain HTML/CSS/JavaScript",
    "plain HTML, CSS, and JavaScript" in demo_approval,
)

check(
    "implementation excludes databases",
    "databases" in impl
    and "does not implement" in impl,
)

check(
    "verification production not verified",
    bool(
        re.search(
            r"BLOCKED\s*/\s*NOT VERIFIED",
            verification,
            re.IGNORECASE,
        )
    ),
)

check(
    "closure production not closed",
    bool(
        re.search(
            r"BLOCKED\s*/\s*NOT CLOSED",
            closure,
            re.IGNORECASE,
        )
    ),
)

check(
    "regression has actual results",
    bool(
        re.search(
            r"Actual Result|Actual Status|final_result:\s*PASS|78\s*/\s*78\s*PASS",
            regression,
            re.IGNORECASE,
        )
    ),
)


# ============================================================
# 7. Historical evidence
# ============================================================

history = [
    "projects/self-storage/e2e-lifecycle-report-r2.md",
    "projects/self-storage/implementation/implementation-r2.md",
    "projects/self-storage/implementation-readiness/implementation-readiness-r2.md",
    "projects/self-storage/implementation-plan/implementation-plan-r2.md",
    "projects/self-storage/implementation-validator/implementation-plan-validation-r2.md",
    "projects/self-storage/implementation-executor/execution-record-r2.md",
    "projects/self-storage/implementation-verification/verification-result-r2.md",
    "projects/self-storage/implementation-closure/closure-result-r2.md",
]

for historical in history:
    check(
        f"history preserved: {historical}",
        (ROOT / historical).exists(),
    )


# ============================================================
# 8. Phase 1 / Phase 2 evidence
# ============================================================

phase2_path = ROOT / "governance/PHASE-2.md"

check(
    "phase2 governance document exists",
    phase2_path.exists(),
)

# Phase 1 foundation commit.
phase1_commit_ok = (
    subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "cat-file",
            "-e",
            "99cf6fb^{commit}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode
    == 0
)

check(
    "phase1 foundation commit exists",
    phase1_commit_ok,
)


# ============================================================
# 9. Phase 3 merge chain #4 -> #12
# ============================================================

try:
    git_log = subprocess.check_output(
        [
            "git",
            "-C",
            str(ROOT),
            "log",
            "--oneline",
            "--all",
        ],
        text=True,
        stderr=subprocess.STDOUT,
    )

    required_prs = range(4, 13)

    merge_chain_ok = all(
        f"Merge pull request #{pr}" in git_log
        for pr in required_prs
    )

except subprocess.CalledProcessError:
    merge_chain_ok = False

check(
    "phase3 merge chain #4-#12 present",
    merge_chain_ok,
)


# ============================================================
# 10. Final report
# ============================================================

total = len(RESULTS)
passed = sum(condition for _, condition in RESULTS)
failed = total - passed

print(f"TOTAL {total}")
print(f"PASS {passed}")
print(f"FAIL {failed}")

for name, condition in RESULTS:
    prefix = "PASS " if condition else "FAIL "
    print(prefix + name)

sys.exit(0 if failed == 0 else 1)