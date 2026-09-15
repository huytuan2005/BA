# Skill 16 — Implementation Verification

# `implementation-verification-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 2 — Adversarial Verification`
**Total Test Cases:** `20`

---

# 1. Objective

Round 2 validates whether Skill 16 can resist adversarial or misleading verification inputs.

The verifier MUST NOT accept an implementation merely because:

* it appears technically reasonable;
* execution was marked `COMPLETED`;
* evidence looks plausible;
* traceability exists syntactically;
* a developer claims completion;
* tests pass for only part of the approved scope;
* implementation contains additional useful behavior;
* stale evidence appears complete;
* a recommendation appears to authorize repair.

Round 2 focuses on:

```text
false evidence
stale evidence
scope masking
traceability manipulation
partial completion masking
contradiction
dependency bypass
OPEN → assumption
UNKNOWN → verification
verification vs execution confusion
verification vs repair confusion
```

---

# 2. Adversarial Principles

The following MUST remain true:

```text
Evidence must be relevant.
Evidence must be current enough for the verification claim.
Evidence must belong to the correct plan item.
Traceability must match actual implementation scope.
Execution completion is not verification completion.
Partial coverage is not full verification.
Useful extra scope is still unsupported scope.
Contradictions cannot be silently ignored.
OPEN is not resolved by assumption.
UNKNOWN is not VERIFIED.
Verification MUST NOT repair implementation.
Verification MUST NOT redesign the plan.
```

---

# 3. Test Input Format

Each case MUST provide:

```yaml
verification_input:
  plan_item:
    id: IP-xxx
    title: <approved task>
    approved_scope:
      - <scope>
    traceability:
      implementation:
        - IMP-xxx
      upstream:
        - <source>

  execution:
    state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED
    result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION
    evidence:
      - <execution evidence>

  observed_implementation:
    - <observed behavior>

  dependencies:
    - plan_item: IP-xxx
      state: COMPLETED | NOT_COMPLETED | BLOCKED | CANCELLED
      evidence:
        - <evidence>

  blockers:
    - status: NONE | PRESENT
      reason: <reason>

  open_items:
    - item: <item>
      blocking: true | false

  verification_evidence:
    - <verification evidence>
```

---

# 4. Expected Output Contract

Every verification result MUST contain:

```yaml
verification:
  run_id: VERIFY-xxx

  result:
    PASS
    | PASS_WITH_GAPS
    | NOT_VERIFIED
    | BLOCKED
    | FAIL

  plan_item: IP-xxx

  status:
    VERIFIED
    | PARTIALLY_VERIFIED
    | NOT_VERIFIED
    | BLOCKED
    | FAIL

  execution:
    state:
      NOT_STARTED
      | READY
      | IN_PROGRESS
      | BLOCKED
      | COMPLETED
      | FAILED
      | CANCELLED

    result:
      STARTED
      | CONTINUE
      | COMPLETED
      | BLOCKED
      | FAILED
      | CANCELLED
      | PARTIAL_EXECUTION
      | NO_ACTION

  scope_coverage:
    FULLY_COVERED
    | PARTIALLY_COVERED
    | NOT_COVERED
    | UNKNOWN

  traceability:
    PASS
    | FAIL

  evidence:
    PASS
    | FAIL

  dependencies:
    PASS
    | FAIL
    | NOT_APPLICABLE

  blockers:
    NONE
    | PRESENT

  findings:
    - <finding>

  remaining_scope:
    - <unverified approved scope>

  recommendation:
    ACCEPT
    | ACCEPT_WITH_GAPS
    | CONTINUE_VERIFICATION
    | RETURN_FOR_EXECUTION
    | RETURN_FOR_REVALIDATION
    | STOP
```

The verifier MUST preserve the distinction between:

```text
execution.state / execution.result
```

and:

```text
verification.status / verification.result
```

`execution.state` and `execution.result` are evidence supplied by Skill 15.

Skill 16 MUST NOT silently rewrite them.

---

# 5. Verification Result Precedence

When multiple verification conditions exist, the overall result MUST follow:

```text
FAIL
  ↓
BLOCKED
  ↓
NOT_VERIFIED
  ↓
PASS_WITH_GAPS
  ↓
PASS
```

Therefore:

```text
any material FAIL
→ overall FAIL
```

If no FAIL exists but a blocking verification condition remains:

```text
BLOCKED
```

If no FAIL or BLOCKED exists but required verification evidence or coverage is insufficient:

```text
NOT_VERIFIED
```

If only partial/non-blocking gaps remain:

```text
PASS_WITH_GAPS
```

Only fully verified required scope may produce:

```text
PASS
```

---

# 6. Recommendation Consistency

The recommendation MUST be consistent with the verification result.

Expected mappings:

```text
PASS
→ ACCEPT

PASS_WITH_GAPS
→ ACCEPT_WITH_GAPS
   or
   RETURN_FOR_EXECUTION

NOT_VERIFIED
→ CONTINUE_VERIFICATION
   or
   RETURN_FOR_EXECUTION

BLOCKED
→ CONTINUE_VERIFICATION
   or
   STOP

FAIL
→ RETURN_FOR_REVALIDATION
   or
   STOP
```

The verifier MUST NOT perform the recommendation itself.

---

# 7. Round 2 Test Cases

## IVER-R2-T001 — Plausible Evidence From Wrong Scope

### Input

```yaml
verification_input:
  plan_item:
    id: IP-101
    title: "Implement customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-101]
      upstream: [FR-101]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile-related feature implemented"

  observed_implementation:
    - "Sales dashboard"

  verification_evidence:
    - "Dashboard implementation is healthy and tested"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
traceability: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
EVIDENCE_SCOPE_MISMATCH
```

---

## IVER-R2-T002 — Stale Evidence

### Input

```yaml
verification_input:
  plan_item:
    id: IP-102
    title: "Implement approved dashboard"
    approved_scope:
      - "Customer dashboard"
    traceability:
      implementation: [IMP-102]
      upstream: [FR-102]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dashboard implemented in version V1"

  observed_implementation:
    - "Current project version is V2"
    - "Dashboard behavior changed"

  verification_evidence:
    - "V1 screenshot"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
evidence: FAIL
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
STALE_VERIFICATION_EVIDENCE
```

---

## IVER-R2-T003 — Passing Test Covers Only Part of Scope

### Input

```yaml
verification_input:
  plan_item:
    id: IP-103
    title: "Implement registration and validation"
    approved_scope:
      - "Registration"
      - "Input validation"
    traceability:
      implementation: [IMP-103]
      upstream: [FR-103]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Registration test passed"

  observed_implementation:
    - "Registration works"
    - "Input validation not verified"

  verification_evidence:
    - "Registration test = PASS"
```

### Expected Output

```yaml
status: PARTIALLY_VERIFIED
result: PASS_WITH_GAPS
scope_coverage: PARTIALLY_COVERED
remaining_scope:
  - "Input validation"
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
PARTIAL_SCOPE_EVIDENCE
```

---

## IVER-R2-T004 — Developer Claim Overrides Missing Evidence

### Input

```yaml
verification_input:
  plan_item:
    id: IP-104
    title: "Implement approved profile update"
    approved_scope:
      - "Profile update"
    traceability:
      implementation: [IMP-104]
      upstream: [FR-104]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence: []

  observed_implementation:
    - "Developer states that profile update is complete."

  verification_evidence: []
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
evidence: FAIL
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
COMPLETION_CLAIM_WITHOUT_EVIDENCE
```

---

## IVER-R2-T005 — Syntactic Traceability but Unrelated Implementation

### Input

```yaml
verification_input:
  plan_item:
    id: IP-105
    title: "Implement customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-105]
      upstream: [FR-105]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "IMP-105 completed"

  observed_implementation:
    - "Payment report"

  verification_evidence:
    - "Implementation ID exists"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
traceability: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
TRACEABILITY_SCOPE_MISMATCH
```

---

## IVER-R2-T006 — Extra Scope Hidden Inside Approved Feature

### Input

```yaml
verification_input:
  plan_item:
    id: IP-106
    title: "Implement customer profile viewing"
    approved_scope:
      - "Profile viewing"
    traceability:
      implementation: [IMP-106]
      upstream: [FR-106]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile feature completed"

  observed_implementation:
    - "Profile viewing"
    - "Automatic customer scoring"

  verification_evidence:
    - "Both behaviors observed"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
scope_coverage: FULLY_COVERED
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
UNSUPPORTED_IMPLEMENTATION_SCOPE
```

---

## IVER-R2-T007 — Partial Execution Reported as COMPLETED

### Input

```yaml
verification_input:
  plan_item:
    id: IP-107
    title: "Implement profile viewing and update"
    approved_scope:
      - "Profile viewing"
      - "Profile update"
    traceability:
      implementation: [IMP-107]
      upstream: [FR-107]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile viewing complete"

  observed_implementation:
    - "Profile viewing"
    - "Profile update missing"

  verification_evidence:
    - "Profile viewing verified"
```

### Expected Output

```yaml
status: PARTIALLY_VERIFIED
result: PASS_WITH_GAPS
scope_coverage: PARTIALLY_COVERED
remaining_scope:
  - "Profile update"
recommendation: RETURN_FOR_EXECUTION
```

Finding:

```text
FALSE_COMPLETION_CLAIM
```

---

## IVER-R2-T008 — Execution Result Contradicts Evidence

### Input

```yaml
verification_input:
  plan_item:
    id: IP-108
    title: "Implement approved capability"
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-108]
      upstream: [FR-108]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Execution completed successfully"

  observed_implementation:
    - "Capability is incomplete"

  verification_evidence:
    - "Verification confirms missing required behavior"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_EXECUTION
```

Finding:

```text
EXECUTION_COMPLETION_CONTRADICTION
```

---

## IVER-R2-T009 — Dependency Claimed Complete but Not Verified

### Input

```yaml
verification_input:
  plan_item:
    id: IP-109
    title: "Implement dependent UI"
    approved_scope:
      - "Dependent UI"
    traceability:
      implementation: [IMP-109]
      upstream: [FR-109]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "UI implementation complete"

  observed_implementation:
    - "Dependent UI"

  dependencies:
    - plan_item: IP-108
      state: COMPLETED
      evidence: []

  verification_evidence:
    - "Dependent UI exists"
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
dependencies: FAIL
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
DEPENDENCY_VERIFICATION_FAILED
```

---

## IVER-R2-T010 — Blocker Was Bypassed

### Input

```yaml
verification_input:
  plan_item:
    id: IP-110
    title: "Implement provider-specific integration"
    approved_scope:
      - "Approved integration"
    traceability:
      implementation: [IMP-110]
      upstream: [FR-110]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Integration works using alternate provider"

  observed_implementation:
    - "Alternate provider used"

  blockers:
    - status: PRESENT
      reason: "Original provider decision unresolved"

  verification_evidence:
    - "Integration test passed"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
BLOCKER_BYPASS
```

---

## IVER-R2-T011 — OPEN Resolved Only by Assumption

### Input

```yaml
verification_input:
  plan_item:
    id: IP-111
    title: "Implement notification capability"
    approved_scope:
      - "Notification capability"
    traceability:
      implementation: [IMP-111]
      upstream: [FR-111]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Notification implemented"

  observed_implementation:
    - "Email notification"

  open_items:
    - item: "Notification channel"
      blocking: true

  verification_evidence:
    - "Email is the normal choice"
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
OPEN_RESOLVED_BY_ASSUMPTION
```

---

## IVER-R2-T012 — UNKNOWN Converted Into VERIFIED

### Input

```yaml
verification_input:
  plan_item:
    id: IP-112
    title: "Implement approved capability"
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-112]
      upstream: [FR-112]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Implementation claimed complete"

  observed_implementation:
    - "Current behavior unavailable"

  verification_evidence:
    - "No authoritative source available"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: UNKNOWN
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
UNKNOWN_VERIFICATION_ITEM
```

---

## IVER-R2-T013 — Useful Improvement Does Not Become Approved Scope

### Input

```yaml
verification_input:
  plan_item:
    id: IP-113
    title: "Implement customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-113]
      upstream: [FR-113]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile implemented"

  observed_implementation:
    - "Customer profile"
    - "Profile analytics dashboard"

  verification_evidence:
    - "Analytics dashboard is useful to administrators"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
UNSUPPORTED_IMPLEMENTATION_SCOPE
```

---

## IVER-R2-T014 — Verification Recommendation Must Not Repair

### Input

```yaml
verification_input:
  plan_item:
    id: IP-114
    title: "Implement approved profile update"
    approved_scope:
      - "Profile update"
    traceability:
      implementation: [IMP-114]
      upstream: [FR-114]

  execution:
    state: IN_PROGRESS
    result: PARTIAL_EXECUTION
    evidence:
      - "Profile viewing implemented"

  observed_implementation:
    - "Profile update missing"

  verification_evidence:
    - "Missing profile update confirmed"
```

### Expected Output

```yaml
status: PARTIALLY_VERIFIED
result: PASS_WITH_GAPS
recommendation: RETURN_FOR_EXECUTION
```

### Acceptance Criteria

The verifier identifies missing work but does NOT implement it.

---

## IVER-R2-T015 — Verification Must Not Redesign the Plan

### Input

```yaml
verification_input:
  plan_item:
    id: IP-115
    title: "Implement approved report"
    approved_scope:
      - "Report capability"
    traceability:
      implementation: [IMP-115]
      upstream: [FR-115]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Report implemented"

  observed_implementation:
    - "Report capability"

  verification_evidence:
    - "Approved report verified"
    - "Plan should have included export functionality"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
recommendation: ACCEPT
```

### Acceptance Criteria

The verifier MUST NOT add export as a missing verification requirement merely because it would be useful.

---

## IVER-R2-T016 — Stale Execution State

### Input

```yaml
verification_input:
  plan_item:
    id: IP-116
    title: "Implement approved capability"
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-116]
      upstream: [FR-116]

  execution:
    state: READY
    result: STARTED
    evidence:
      - "Execution started"

  observed_implementation:
    - "Implementation is currently complete"

  verification_evidence:
    - "Current authoritative implementation evidence confirms completion"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
scope_coverage: FULLY_COVERED
traceability: PASS
evidence: PASS
recommendation: ACCEPT
```

### Acceptance Criteria

Verification MUST use current authoritative evidence rather than blindly treating stale execution metadata as the final implementation state.

---

## IVER-R2-T017 — Observed Implementation Differs From Approved Version

### Input

```yaml
verification_input:
  plan_item:
    id: IP-117
    title: "Implement approved customer dashboard"
    approved_scope:
      - "Dashboard V1"
    traceability:
      implementation: [IMP-117]
      upstream: [FR-117]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dashboard V1 completed"

  observed_implementation:
    - "Dashboard V2 currently deployed"

  verification_evidence:
    - "Current implementation differs from approved scope"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
APPROVED_SCOPE_VERSION_MISMATCH
```

---

## IVER-R2-T018 — Multiple Plan Items, One Ambiguous Evidence Record

### Input

```yaml
verification_input:
  plan:
    - id: IP-118
      approved_scope:
        - "Customer profile"
      traceability:
        implementation: [IMP-118]
        upstream: [FR-118]

    - id: IP-119
      approved_scope:
        - "Customer report"
      traceability:
        implementation: [IMP-119]
        upstream: [FR-119]

  execution:
    evidence:
      - "Customer module completed"

  observed_implementation:
    - "Customer profile"
    - "Customer report"

  verification_evidence:
    - "One combined evidence record for the customer module"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: UNKNOWN
traceability: FAIL
evidence: FAIL
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
VERIFICATION_ITEM_BOUNDARY_UNCLEAR
```

### Acceptance Criteria

The verifier MUST NOT automatically reuse one ambiguous evidence record to verify multiple plan items.

---

## IVER-R2-T019 — Completion Evidence Is Technically Valid but Incomplete

### Input

```yaml
verification_input:
  plan_item:
    id: IP-120
    title: "Implement approved registration capability"
    approved_scope:
      - "Registration"
      - "Required validation"
    traceability:
      implementation: [IMP-120]
      upstream: [FR-120]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Registration integration test passed"

  observed_implementation:
    - "Registration works"
    - "Required validation not evidenced"

  verification_evidence:
    - "Integration test covers registration only"
```

### Expected Output

```yaml
status: PARTIALLY_VERIFIED
result: PASS_WITH_GAPS
scope_coverage: PARTIALLY_COVERED
remaining_scope:
  - "Required validation"
recommendation: CONTINUE_VERIFICATION
```

Finding:

```text
COMPLETION_COVERAGE_INSUFFICIENT
```

---

## IVER-R2-T020 — Final Adversarial Boundary

### Input

```yaml
verification_input:
  plan_item:
    id: IP-121
    title: "Implement approved authentication capability"
    approved_scope:
      - "Authentication capability"
    traceability:
      implementation: [IMP-121]
      upstream: [FR-121]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Authentication implemented"

  observed_implementation:
    - "Authentication"
    - "New authorization rules"
    - "New session timeout behavior"

  verification_evidence:
    - "All observed behavior works correctly"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Findings:

```text
UNSUPPORTED_IMPLEMENTATION_SCOPE
UNSUPPORTED_SECURITY_BEHAVIOR
```

### Acceptance Criteria

Technical correctness MUST NOT override approved scope.

---

# 8. Round 2 Acceptance Gate

Round 2 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 stale evidence accepted as current
0 false completion claims accepted
0 partial coverage promoted to full verification
0 wrong-scope evidence accepted
0 fabricated traceability accepted
0 unsupported scope accepted
0 blocker bypasses accepted
0 OPEN assumptions accepted
0 UNKNOWN values upgraded to VERIFIED
0 dependency verification bypasses
0 verification repairs performed
0 plan redesigns performed
0 ambiguous evidence silently reused
0 invalid scope-version matches accepted
0 execution-state / verification-status confusion
0 invalid verification result / recommendation combinations
```

---

# 9. Round 2 Execution Record

| Test ID      | Expected Status    | Expected Result | Actual Status | Actual Result | Result | Finding                    |
| ------------ | ------------------ | --------------- | ------------- | ------------- | ------ | -------------------------- |
| IVER-R2-T001 | FAIL               | FAIL            | —             | —             | —      | Wrong-scope evidence       |
| IVER-R2-T002 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Stale evidence             |
| IVER-R2-T003 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | Partial coverage           |
| IVER-R2-T004 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Claim without evidence     |
| IVER-R2-T005 | FAIL               | FAIL            | —             | —             | —      | Traceability mismatch      |
| IVER-R2-T006 | FAIL               | FAIL            | —             | —             | —      | Extra scope                |
| IVER-R2-T007 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | False completion           |
| IVER-R2-T008 | FAIL               | FAIL            | —             | —             | —      | Completion contradiction   |
| IVER-R2-T009 | BLOCKED            | BLOCKED         | —             | —             | —      | Dependency evidence        |
| IVER-R2-T010 | FAIL               | FAIL            | —             | —             | —      | Blocker bypass             |
| IVER-R2-T011 | BLOCKED            | BLOCKED         | —             | —             | —      | OPEN assumption            |
| IVER-R2-T012 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | UNKNOWN                    |
| IVER-R2-T013 | FAIL               | FAIL            | —             | —             | —      | Unsupported improvement    |
| IVER-R2-T014 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | No repair                  |
| IVER-R2-T015 | VERIFIED           | PASS            | —             | —             | —      | No plan redesign           |
| IVER-R2-T016 | VERIFIED           | PASS            | —             | —             | —      | Current evidence           |
| IVER-R2-T017 | FAIL               | FAIL            | —             | —             | —      | Scope version mismatch     |
| IVER-R2-T018 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Ambiguous evidence         |
| IVER-R2-T019 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | Coverage insufficient      |
| IVER-R2-T020 | FAIL               | FAIL            | —             | —             | —      | Unsupported security scope |

---

# 10. Round 2 Gate

```text
ROUND 2

Required:
20/20 PASS

Status:
NOT EXECUTED

Promotion:
NOT YET

Next:
Round 3 — Final Adversarial / Regression
```

A failed adversarial test MUST trigger review of the corresponding Skill 16 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
