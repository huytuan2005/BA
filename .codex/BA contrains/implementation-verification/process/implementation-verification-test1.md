# Skill 16 — Implementation Verification

# `implementation-verification-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 1`
**Total Test Cases:** `20`

---

# 1. Objective

Validate that Skill 16 can correctly verify executed implementation work against the approved implementation plan while preserving:

* plan-to-execution traceability;
* approved scope;
* implementation coverage;
* execution evidence;
* completion criteria;
* dependency verification;
* blocker verification;
* OPEN / UNKNOWN boundaries;
* contradiction detection;
* verification status;
* verification result;
* separation between execution and verification.

Round 1 focuses on baseline verification correctness.

It does not yet stress sophisticated evidence forgery, stale artifacts, adversarial scope manipulation, or multi-stage recovery. Those belong to later rounds.

---

# 2. Core Verification Rules

Round 1 MUST enforce:

```text
Verify, do not implement.
Verify approved scope, not ideal scope.
Execution completion does not automatically mean verification completion.
Partial execution remains partial.
Missing evidence prevents unsupported verification.
OPEN remains OPEN without resolving evidence.
UNKNOWN remains UNKNOWN without evidence.
Traceability must be valid.
Extra implementation scope must not be accepted.
Missing approved scope must not be hidden.
```

---

# 3. Explicit Test Input Format

Each test case MUST provide:

```yaml
verification_input:
  plan_item:
    id: IP-xxx
    title: <approved implementation task>
    approved_scope:
      - <approved scope>
    traceability:
      implementation:
        - IMP-xxx
      upstream:
        - <approved source>

  execution:
    state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED
    result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION
    evidence:
      - <execution evidence>

  observed_implementation:
    - <observed implementation>

  dependencies:
    - plan_item: IP-xxx
      state: COMPLETED | NOT_COMPLETED | BLOCKED | CANCELLED
      evidence:
        - <dependency evidence>

  blockers:
    - status: NONE | PRESENT
      reason: <reason>

  open_items:
    - item: <open item>
      blocking: true | false
      evidence:
        - <optional evidence>

  verification_evidence:
    - <verification evidence>
```

---

# 4. Explicit Expected Output Format

Every verification result MUST contain:

```yaml
verification:
  run_id: VERIFY-xxx
  result: PASS | PASS_WITH_GAPS | NOT_VERIFIED | BLOCKED | FAIL

  plan_item: IP-xxx

  status: VERIFIED | PARTIALLY_VERIFIED | NOT_VERIFIED | BLOCKED | FAIL

  execution_state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED

  execution_result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION

  scope_coverage: FULLY_COVERED | PARTIALLY_COVERED | NOT_COVERED | UNKNOWN

  traceability: PASS | FAIL

  evidence: PASS | FAIL

  dependencies: PASS | FAIL | NOT_APPLICABLE

  blockers: NONE | PRESENT

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

---

# 5. Round 1 Test Cases

## IVER-R1-T001 — Fully Executed and Fully Evidenced

### Input

```yaml
verification_input:
  plan_item:
    id: IP-001
    title: "Implement approved customer profile viewing"
    approved_scope:
      - "Customer profile viewing"
    traceability:
      implementation: [IMP-001]
      upstream: [FR-001]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile viewing implementation verified"

  observed_implementation:
    - "Customer profile viewing"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Observed profile viewing matches approved scope"
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

All approved scope is evidenced.

---

## IVER-R1-T002 — Execution Completed, Verification Evidence Sufficient

### Input

```yaml
verification_input:
  plan_item:
    id: IP-002
    title: "Implement approved registration capability"
    approved_scope:
      - "Registration capability"
    traceability:
      implementation: [IMP-002]
      upstream: [FR-002]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Registration implementation completed"

  observed_implementation:
    - "Registration capability"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Registration behavior verified against approved scope"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
scope_coverage: FULLY_COVERED
```

### Acceptance Criteria

`COMPLETED + COMPLETED` from Skill 15 does not automatically cause PASS; verification evidence must also support the conclusion.

---

## IVER-R1-T003 — Execution Completed but Verification Evidence Missing

### Input

```yaml
verification_input:
  plan_item:
    id: IP-003
    title: "Implement approved dashboard"
    approved_scope:
      - "Customer dashboard"
    traceability:
      implementation: [IMP-003]
      upstream: [FR-003]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence: []

  observed_implementation:
    - "Dashboard appears to exist"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

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
COMPLETION_EVIDENCE_INSUFFICIENT
```

### Acceptance Criteria

Execution completion alone MUST NOT establish verification.

---

## IVER-R1-T004 — Partial Execution

### Input

```yaml
verification_input:
  plan_item:
    id: IP-004
    title: "Implement approved profile capability"
    approved_scope:
      - "Profile viewing"
      - "Profile update"
    traceability:
      implementation: [IMP-004]
      upstream: [FR-004]

  execution:
    state: IN_PROGRESS
    result: PARTIAL_EXECUTION
    evidence:
      - "Profile viewing implemented"

  observed_implementation:
    - "Profile viewing"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

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

### Acceptance Criteria

The verifier MUST NOT mark the entire item `VERIFIED`.

---

## IVER-R1-T005 — No Approved Scope Implemented

### Input

```yaml
verification_input:
  plan_item:
    id: IP-005
    title: "Implement approved customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-005]
      upstream: [FR-005]

  execution:
    state: NOT_STARTED
    result: NO_ACTION
    evidence: []

  observed_implementation: []

  dependencies: []
  blockers:
    - status: PRESENT
      reason: "Implementation not started"

  open_items: []

  verification_evidence: []
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: NOT_COVERED
recommendation: RETURN_FOR_EXECUTION
```

---

## IVER-R1-T006 — Extra Unapproved Scope

### Input

```yaml
verification_input:
  plan_item:
    id: IP-006
    title: "Implement profile viewing"
    approved_scope:
      - "Profile viewing"
    traceability:
      implementation: [IMP-006]
      upstream: [FR-006]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile feature implemented"

  observed_implementation:
    - "Profile viewing"
    - "Profile export"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Profile export observed but not present in approved scope"
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

### Acceptance Criteria

The approved feature MUST NOT be accepted merely because the extra implementation works.

---

## IVER-R1-T007 — Valid Many-to-One Traceability

### Input

```yaml
verification_input:
  plan_item:
    id: IP-007
    title: "Implement approved customer account capability"
    approved_scope:
      - "Account viewing"
      - "Account update"
    traceability:
      implementation: [IMP-007]
      upstream: [FR-007, FR-008]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Account viewing and update implemented"

  observed_implementation:
    - "Account viewing"
    - "Account update"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Both approved scope elements verified"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
traceability: PASS
scope_coverage: FULLY_COVERED
```

---

## IVER-R1-T008 — Missing Execution Traceability

### Input

```yaml
verification_input:
  plan_item:
    id: IP-008
    title: "Implement approved capability"
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: []
      upstream: [FR-008]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Implementation completed"

  observed_implementation:
    - "Approved capability"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Capability appears implemented"
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
INVALID_EXECUTION_TRACEABILITY
```

### Acceptance Criteria

A working implementation without valid execution traceability is not verified.

---

## IVER-R1-T009 — Traceability Scope Mismatch

### Input

```yaml
verification_input:
  plan_item:
    id: IP-009
    title: "Implement customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-009]
      upstream: [FR-009]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Implementation evidence"

  observed_implementation:
    - "Sales report"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Observed implementation belongs to another capability"
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

## IVER-R1-T010 — Dependency Verified

### Input

```yaml
verification_input:
  plan_item:
    id: IP-010
    title: "Implement approved UI integration"
    approved_scope:
      - "UI integration"
    traceability:
      implementation: [IMP-010]
      upstream: [FR-010]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "UI integration implemented"

  observed_implementation:
    - "UI integration"

  dependencies:
    - plan_item: IP-009
      state: COMPLETED
      evidence:
        - "Dependency implementation verified"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "UI integration and dependency verified"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
dependencies: PASS
```

---

## IVER-R1-T011 — Dependency Not Verified

### Input

```yaml
verification_input:
  plan_item:
    id: IP-011
    title: "Implement dependent UI"
    approved_scope:
      - "Dependent UI"
    traceability:
      implementation: [IMP-011]
      upstream: [FR-011]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "UI implementation completed"

  observed_implementation:
    - "Dependent UI"

  dependencies:
    - plan_item: IP-010
      state: COMPLETED
      evidence: []

  blockers:
    - status: NONE
  open_items: []

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

## IVER-R1-T012 — Blocking Condition Remains

### Input

```yaml
verification_input:
  plan_item:
    id: IP-012
    title: "Implement provider-specific integration"
    approved_scope:
      - "Approved integration"
    traceability:
      implementation: [IMP-012]
      upstream: [FR-012]

  execution:
    state: BLOCKED
    result: BLOCKED
    evidence: []

  observed_implementation: []

  dependencies: []
  blockers:
    - status: PRESENT
      reason: "Required integration decision unresolved"

  open_items: []

  verification_evidence: []
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
recommendation: RETURN_FOR_EXECUTION
```

---

## IVER-R1-T013 — Non-Blocking OPEN Item

### Input

```yaml
verification_input:
  plan_item:
    id: IP-013
    title: "Implement approved report boundary"
    approved_scope:
      - "Report boundary"
    traceability:
      implementation: [IMP-013]
      upstream: [FR-013]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Approved report boundary implemented"

  observed_implementation:
    - "Report boundary"

  dependencies: []
  blockers:
    - status: NONE

  open_items:
    - item: "Exact future export label"
      blocking: false
      evidence: []

  verification_evidence:
    - "Approved report boundary verified"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
scope_coverage: FULLY_COVERED
recommendation: ACCEPT
```

### Acceptance Criteria

The verifier MUST NOT treat a non-blocking unrelated OPEN item as implementation failure.

---

## IVER-R1-T014 — Blocking OPEN Item

### Input

```yaml
verification_input:
  plan_item:
    id: IP-014
    title: "Implement provider-specific notification"
    approved_scope:
      - "Provider-specific notification"
    traceability:
      implementation: [IMP-014]
      upstream: [FR-014]

  execution:
    state: READY
    result: STARTED
    evidence: []

  observed_implementation: []

  dependencies: []
  blockers:
    - status: NONE

  open_items:
    - item: "Notification provider unresolved"
      blocking: true
      evidence: []

  verification_evidence: []
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
OPEN_VERIFICATION_ITEM
```

---

## IVER-R1-T015 — UNKNOWN Evidence

### Input

```yaml
verification_input:
  plan_item:
    id: IP-015
    title: "Implement approved capability"
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-015]
      upstream: [FR-015]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Implementation claimed complete"

  observed_implementation:
    - "Capability status unknown"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "No authoritative verification evidence available"
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

## IVER-R1-T016 — Execution Failed

### Input

```yaml
verification_input:
  plan_item:
    id: IP-016
    title: "Implement approved feature"
    approved_scope:
      - "Approved feature"
    traceability:
      implementation: [IMP-016]
      upstream: [FR-016]

  execution:
    state: FAILED
    result: FAILED
    evidence:
      - "Execution failed before feature completion"

  observed_implementation: []

  dependencies: []
  blockers:
    - status: PRESENT
      reason: "Implementation failure"

  open_items: []

  verification_evidence:
    - "Feature not completed"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: NOT_COVERED
recommendation: RETURN_FOR_EXECUTION
```

---

## IVER-R1-T017 — Cancelled Implementation

### Input

```yaml
verification_input:
  plan_item:
    id: IP-017
    title: "Implement cancelled capability"
    approved_scope:
      - "Cancelled capability"
    traceability:
      implementation: [IMP-017]
      upstream: [FR-017]

  execution:
    state: CANCELLED
    result: NO_ACTION
    evidence: []

  observed_implementation: []

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence: []
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: NOT_COVERED
recommendation: RETURN_FOR_REVALIDATION
```

### Acceptance Criteria

Cancelled execution MUST NOT be interpreted as successful implementation.

---

## IVER-R1-T018 — Evidence From Another Plan Item

### Input

```yaml
verification_input:
  plan_item:
    id: IP-018
    title: "Implement customer profile"
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-018]
      upstream: [FR-018]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Evidence for IP-019"

  observed_implementation:
    - "Customer profile"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Evidence belongs to another plan item"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: FAIL
evidence: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

Finding:

```text
EXECUTION_EVIDENCE_SCOPE_MISMATCH
```

---

## IVER-R1-T019 — Verification Must Not Repair Missing Implementation

### Input

```yaml
verification_input:
  plan_item:
    id: IP-019
    title: "Implement profile viewing and update"
    approved_scope:
      - "Profile viewing"
      - "Profile update"
    traceability:
      implementation: [IMP-019]
      upstream: [FR-019]

  execution:
    state: IN_PROGRESS
    result: PARTIAL_EXECUTION
    evidence:
      - "Profile viewing implemented"

  observed_implementation:
    - "Profile viewing"

  dependencies: []
  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Profile update is missing"

```

### Expected Output

```yaml
status: PARTIALLY_VERIFIED
result: PASS_WITH_GAPS
remaining_scope:
  - "Profile update"
recommendation: RETURN_FOR_EXECUTION
```

### Acceptance Criteria

The verifier MUST report the missing scope.

It MUST NOT design or implement profile update.

---

## IVER-R1-T020 — Full Plan Item Coverage

### Input

```yaml
verification_input:
  plan:
    - id: IP-020
      status: COMPLETED
      verification: VERIFIED

    - id: IP-021
      status: COMPLETED
      verification: VERIFIED

    - id: IP-022
      status: IN_PROGRESS
      verification: PARTIALLY_VERIFIED

  verification_evidence:
    - "IP-020 fully verified"
    - "IP-021 fully verified"
    - "IP-022 partially verified"
```

### Expected Output

```yaml
result: PASS_WITH_GAPS
```

Summary:

```yaml
summary:
  total_plan_items: 3
  verified: 2
  partially_verified: 1
  not_verified: 0
  blocked: 0
  failed: 0
```

Recommendation:

```yaml
recommendation: RETURN_FOR_EXECUTION
```

### Acceptance Criteria

The overall result MUST NOT be `PASS` while an approved plan item remains only partially verified.

---

# 6. Round 1 Acceptance Gate

Round 1 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 unsupported scope accepted
0 missing approved scope falsely verified
0 invalid traceability accepted
0 cross-item evidence accepted
0 unsupported completion claims accepted
0 blocking OPEN items ignored
0 unresolved dependencies accepted
0 UNKNOWN values upgraded without evidence
0 cancelled executions treated as verified
0 verification repairs performed
0 plan redesigns performed
0 execution states confused with verification status
0 invalid verification results accepted
```

---

# 7. Round 1 Execution Record

| Test ID      | Expected Status    | Expected Result | Actual Status | Actual Result | Result | Finding               |
| ------------ | ------------------ | --------------- | ------------- | ------------- | ------ | --------------------- |
| IVER-R1-T001 | VERIFIED           | PASS            | —             | —             | —      | —                     |
| IVER-R1-T002 | VERIFIED           | PASS            | —             | —             | —      | —                     |
| IVER-R1-T003 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Completion evidence   |
| IVER-R1-T004 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | Partial scope         |
| IVER-R1-T005 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Not executed          |
| IVER-R1-T006 | FAIL               | FAIL            | —             | —             | —      | Unsupported scope     |
| IVER-R1-T007 | VERIFIED           | PASS            | —             | —             | —      | Traceability          |
| IVER-R1-T008 | FAIL               | FAIL            | —             | —             | —      | Missing traceability  |
| IVER-R1-T009 | FAIL               | FAIL            | —             | —             | —      | Traceability mismatch |
| IVER-R1-T010 | VERIFIED           | PASS            | —             | —             | —      | Dependency            |
| IVER-R1-T011 | BLOCKED            | BLOCKED         | —             | —             | —      | Dependency evidence   |
| IVER-R1-T012 | BLOCKED            | BLOCKED         | —             | —             | —      | Blocker               |
| IVER-R1-T013 | VERIFIED           | PASS            | —             | —             | —      | Non-blocking OPEN     |
| IVER-R1-T014 | BLOCKED            | BLOCKED         | —             | —             | —      | Blocking OPEN         |
| IVER-R1-T015 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | UNKNOWN               |
| IVER-R1-T016 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Execution failed      |
| IVER-R1-T017 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Cancelled             |
| IVER-R1-T018 | NOT_VERIFIED       | FAIL            | —             | —             | —      | Evidence mismatch     |
| IVER-R1-T019 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | No repair             |
| IVER-R1-T020 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | Plan coverage         |

````

---

# 8. Round 1 Gate

```text
ROUND 1

Required:
20/20 PASS

Status:
NOT EXECUTED

Promotion:
NOT YET

Next:
Round 2
````

A failed test MUST trigger a review of the corresponding Skill 16 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
