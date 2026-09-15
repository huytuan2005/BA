# Skill 16 — Implementation Verification

# `implementation-verification-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 3 — Final Adversarial / Regression`
**Total Test Cases:** `20`

---

# 1. Objective

Round 3 is the final validation round before promotion of Skill 16.

It validates whether the verifier preserves all rules established by Round 1 and Round 2 under:

* multi-item verification;
* changing execution states;
* post-execution scope changes;
* evidence drift;
* dependency changes;
* blocker resolution;
* contradictory evidence;
* mixed verification outcomes;
* incomplete plan coverage;
* aggregation of item results into overall verification result;
* recommendation consistency;
* regression against previously validated invariants.

Round 3 MUST NOT weaken any rule from Round 1 or Round 2.

---

# 2. Final Verification Invariants

The following MUST remain true:

```text
Verify, do not implement.

Approved scope is the verification boundary.

Execution completion does not equal verification completion.

Partial execution does not equal full verification.

OPEN is not resolved by assumption.

UNKNOWN is not VERIFIED without evidence.

Traceability must remain valid.

Evidence must belong to the correct verification item.

Current authoritative evidence takes precedence over stale execution metadata.

Unsupported extra implementation scope is not accepted.

Missing approved scope is not silently ignored.

Contradictions must be surfaced.

Verification does not repair implementation.

Verification does not redesign the implementation plan.

Verification status and execution state/result remain separate.

Overall verification result follows deterministic precedence.

Recommendation must remain consistent with the overall result.
```

---

# 3. Normalized Models

## Execution State

```text
NOT_STARTED
READY
IN_PROGRESS
BLOCKED
COMPLETED
FAILED
CANCELLED
```

## Execution Result

```text
STARTED
CONTINUE
COMPLETED
BLOCKED
FAILED
CANCELLED
PARTIAL_EXECUTION
NO_ACTION
```

## Verification Status

```text
VERIFIED
PARTIALLY_VERIFIED
NOT_VERIFIED
BLOCKED
FAIL
```

## Overall Verification Result

```text
PASS
PASS_WITH_GAPS
NOT_VERIFIED
BLOCKED
FAIL
```

---

# 4. Overall Result Precedence

The verifier MUST use:

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

If no FAIL exists:

```text
any BLOCKED
→ overall BLOCKED
```

If no FAIL or BLOCKED exists:

```text
any required NOT_VERIFIED
→ overall NOT_VERIFIED
```

If only partial/non-blocking gaps exist:

```text
PASS_WITH_GAPS
```

Only fully verified required scope produces:

```text
PASS
```

---

# 5. Test Input Format

Each case MUST provide:

```yaml
verification_input:
  plan:
    - plan_item:
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
        - <observed implementation>

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

# 6. Expected Output Contract

Every verification run MUST contain:

```yaml
verification:
  run_id: VERIFY-xxx

  result:
    PASS
    | PASS_WITH_GAPS
    | NOT_VERIFIED
    | BLOCKED
    | FAIL

  summary:
    total_plan_items: <n>
    verified: <n>
    partially_verified: <n>
    not_verified: <n>
    blocked: <n>
    failed: <n>

  items:
    - plan_item: IP-xxx

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

---

# 7. Round 3 Test Cases

## IVER-R3-T001 — Fully Verified Multi-Item Plan

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-201
        title: "Implement customer profile"
        approved_scope:
          - "Customer profile"
        traceability:
          implementation: [IMP-201]
          upstream: [FR-201]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Profile implementation completed"

      observed_implementation:
        - "Customer profile"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Profile fully verified"

    - plan_item:
        id: IP-202
        title: "Implement customer report"
        approved_scope:
          - "Customer report"
        traceability:
          implementation: [IMP-202]
          upstream: [FR-202]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Report implementation completed"

      observed_implementation:
        - "Customer report"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Report fully verified"
```

### Expected Output

```yaml
summary:
  total_plan_items: 2
  verified: 2
  partially_verified: 0
  not_verified: 0
  blocked: 0
  failed: 0

result: PASS
recommendation: ACCEPT
```

---

## IVER-R3-T002 — One Partial Item Prevents PASS

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-203
        approved_scope:
          - "Profile viewing"
        traceability:
          implementation: [IMP-203]
          upstream: [FR-203]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Viewing implemented"

      observed_implementation:
        - "Profile viewing"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Viewing verified"

    - plan_item:
        id: IP-204
        approved_scope:
          - "Profile update"
        traceability:
          implementation: [IMP-204]
          upstream: [FR-204]

      execution:
        state: IN_PROGRESS
        result: PARTIAL_EXECUTION
        evidence:
          - "Update partially implemented"

      observed_implementation:
        - "Profile update partially implemented"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Partial evidence only"
```

### Expected Output

```yaml
result: PASS_WITH_GAPS
```

Summary:

```yaml
summary:
  total_plan_items: 2
  verified: 1
  partially_verified: 1
  not_verified: 0
  blocked: 0
  failed: 0
```

Recommendation:

```yaml
recommendation: RETURN_FOR_EXECUTION
```

---

## IVER-R3-T003 — One NOT_VERIFIED Item

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-205
        approved_scope:
          - "Approved capability A"
        traceability:
          implementation: [IMP-205]
          upstream: [FR-205]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Completion claimed"

      observed_implementation:
        - "Capability A"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "No authoritative verification evidence"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: UNKNOWN
recommendation: CONTINUE_VERIFICATION
```

---

## IVER-R3-T004 — One BLOCKED Item

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-206
        approved_scope:
          - "Approved capability"

        traceability:
          implementation: [IMP-206]
          upstream: [FR-206]

      execution:
        state: BLOCKED
        result: BLOCKED
        evidence: []

      observed_implementation: []

      dependencies: []
      blockers:
        - status: PRESENT
          reason: "Required decision unresolved"

      open_items: []

      verification_evidence: []
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
recommendation: STOP
```

---

## IVER-R3-T005 — FAIL Takes Precedence Over Partial Gap

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-207
        approved_scope:
          - "Profile viewing"
        traceability:
          implementation: [IMP-207]
          upstream: [FR-207]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Profile viewing completed"

      observed_implementation:
        - "Profile viewing"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Profile verified"

    - plan_item:
        id: IP-208
        approved_scope:
          - "Profile update"
        traceability:
          implementation: [IMP-208]
          upstream: [FR-208]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Feature implemented"

      observed_implementation:
        - "Profile update"
        - "Unapproved scoring behavior"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Extra scoring behavior observed"
```

### Expected Output

```yaml
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

### Acceptance Criteria

The partial/verified item MUST NOT hide the material FAIL.

---

## IVER-R3-T006 — BLOCKED Takes Precedence Over NOT_VERIFIED

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-209
        approved_scope:
          - "Capability A"
        traceability:
          implementation: [IMP-209]
          upstream: [FR-209]

      execution:
        state: BLOCKED
        result: BLOCKED
        evidence: []

      observed_implementation: []

      dependencies: []
      blockers:
        - status: PRESENT
          reason: "Required dependency unresolved"

      open_items: []

      verification_evidence: []

    - plan_item:
        id: IP-210
        approved_scope:
          - "Capability B"
        traceability:
          implementation: [IMP-210]
          upstream: [FR-210]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence: []

      observed_implementation:
        - "Capability B"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence: []
```

### Expected Output

```yaml
result: BLOCKED
recommendation: STOP
```

---

## IVER-R3-T007 — Dependency Becomes Invalid After Execution

### Input

```yaml
verification_input:
  plan_item:
    id: IP-211
    approved_scope:
      - "Dependent capability"
    traceability:
      implementation: [IMP-211]
      upstream: [FR-211]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dependent capability completed"

  observed_implementation:
    - "Dependent capability"

  dependencies:
    - plan_item: IP-210
      state: COMPLETED
      evidence:
        - "Old dependency completion evidence"

  blockers:
    - status: PRESENT
      reason: "Dependency IP-210 is currently invalid"

  open_items: []

  verification_evidence:
    - "Current dependency no longer satisfies required boundary"
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
dependencies: FAIL
recommendation: STOP
```

Finding:

```text
DEPENDENCY_VERIFICATION_FAILED
```

---

## IVER-R3-T008 — Scope Changes After Successful Execution

### Input

```yaml
verification_input:
  plan_item:
    id: IP-212
    approved_scope:
      - "Dashboard V1"

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dashboard V1 completed"

  observed_implementation:
    - "Dashboard V2"

  blockers:
    - status: NONE

  open_items: []

  verification_evidence:
    - "Current implementation is V2"
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

## IVER-R3-T009 — Execution Evidence Valid, Verification Evidence Contradictory

### Input

```yaml
verification_input:
  plan_item:
    id: IP-213
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-213]
      upstream: [FR-213]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Execution completed"

  observed_implementation:
    - "Capability present"

  blockers:
    - status: NONE

  open_items: []

  verification_evidence:
    - "Required behavior missing"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_EXECUTION
```

Finding:

```text
VERIFICATION_CONTRADICTION
```

---

## IVER-R3-T010 — Non-Blocking OPEN Across Verified Item

### Input

```yaml
verification_input:
  plan_item:
    id: IP-214
    approved_scope:
      - "Approved report"
    traceability:
      implementation: [IMP-214]
      upstream: [FR-214]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Report completed"

  observed_implementation:
    - "Approved report"

  blockers:
    - status: NONE

  open_items:
    - item: "Future export label"
      blocking: false

  verification_evidence:
    - "Report fully verified"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
recommendation: ACCEPT
```

### Acceptance Criteria

A non-blocking OPEN item that is outside the current approved completion boundary MUST NOT prevent verification.

---

## IVER-R3-T011 — Blocking OPEN Appears During Verification

### Input

```yaml
verification_input:
  plan_item:
    id: IP-215
    approved_scope:
      - "Provider-specific notification"
    traceability:
      implementation: [IMP-215]
      upstream: [FR-215]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Notification implemented"

  observed_implementation:
    - "Email notification"

  blockers:
    - status: NONE

  open_items:
    - item: "Notification channel was never approved"
      blocking: true

  verification_evidence:
    - "Email implementation exists"
```

### Expected Output

```yaml
status: BLOCKED
result: BLOCKED
recommendation: RETURN_FOR_REVALIDATION
```

---

## IVER-R3-T012 — Evidence Belongs to Another Version

### Input

```yaml
verification_input:
  plan_item:
    id: IP-216
    approved_scope:
      - "Dashboard V2"
    traceability:
      implementation: [IMP-216]
      upstream: [FR-216]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dashboard V2 implemented"

  observed_implementation:
    - "Dashboard V2"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Dashboard V1 test suite passed"
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

## IVER-R3-T013 — Cancellation After Partial Progress

### Input

```yaml
verification_input:
  plan_item:
    id: IP-217
    approved_scope:
      - "Capability A"
      - "Capability B"
    traceability:
      implementation: [IMP-217]
      upstream: [FR-217]

  execution:
    state: CANCELLED
    result: NO_ACTION
    evidence:
      - "Execution cancelled after capability A"

  observed_implementation:
    - "Capability A"
    - "Capability B missing"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Capability A exists"
```

### Expected Output

```yaml
status: NOT_VERIFIED
result: NOT_VERIFIED
scope_coverage: PARTIALLY_COVERED
recommendation: RETURN_FOR_REVALIDATION
```

### Acceptance Criteria

Cancellation does not erase the remaining approved scope.

---

## IVER-R3-T014 — Revalidation Result Must Not Become PASS Automatically

### Input

```yaml
verification_input:
  plan_item:
    id: IP-218
    approved_scope:
      - "Dashboard"
    traceability:
      implementation: [IMP-218]
      upstream: [FR-218]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Dashboard implemented"

  observed_implementation:
    - "Dashboard"

  blockers:
    - status: NONE

  open_items: []

  verification_evidence:
    - "Implementation is complete"

  previous_verification:
    result: FAIL
    finding:
      - "Unsupported extra widget"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
recommendation: ACCEPT
```

### Acceptance Criteria

The current evidence determines current verification. A historical FAIL MUST NOT permanently poison a corrected current implementation when the current approved scope is fully satisfied.

---

## IVER-R3-T015 — Historical PASS Must Not Override Current Failure

### Input

```yaml
verification_input:
  plan_item:
    id: IP-219
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-219]
      upstream: [FR-219]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile previously verified"

  observed_implementation:
    - "New unapproved profile scoring behavior"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Current implementation includes unsupported behavior"

  previous_verification:
    result: PASS
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

## IVER-R3-T016 — Mixed Independent Items

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-220
        approved_scope:
          - "Customer profile"
        traceability:
          implementation: [IMP-220]
          upstream: [FR-220]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Profile verified"

      observed_implementation:
        - "Customer profile"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []
      verification_evidence:
        - "Profile verified"

    - plan_item:
        id: IP-221
        approved_scope:
          - "Customer report"
        traceability:
          implementation: [IMP-221]
          upstream: [FR-221]

      execution:
        state: BLOCKED
        result: BLOCKED
        evidence: []

      observed_implementation: []

      dependencies: []
      blockers:
        - status: PRESENT
          reason: "Report data source unresolved"
      open_items: []
      verification_evidence: []
```

### Expected Output

```yaml
result: BLOCKED
recommendation: STOP
```

### Acceptance Criteria

The verified independent item remains `VERIFIED`; only the blocked branch is affected.

---

## IVER-R3-T017 — No Remaining Scope After Repeated Verification

### Input

```yaml
verification_input:
  plan_item:
    id: IP-222
    approved_scope:
      - "Profile viewing"
    traceability:
      implementation: [IMP-222]
      upstream: [FR-222]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile viewing completed"

  observed_implementation:
    - "Profile viewing"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Profile viewing verified"

  previous_verification:
    status: PARTIALLY_VERIFIED
    remaining_scope:
      - "Profile viewing"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
scope_coverage: FULLY_COVERED
remaining_scope: []
recommendation: ACCEPT
```

### Acceptance Criteria

Current sufficient evidence may upgrade a previous partial verification.

---

## IVER-R3-T018 — Recommendation Cannot Override FAIL

### Input

```yaml
verification_input:
  plan_item:
    id: IP-223
    approved_scope:
      - "Customer profile"
    traceability:
      implementation: [IMP-223]
      upstream: [FR-223]

  execution:
    state: COMPLETED
    result: COMPLETED
    evidence:
      - "Profile implemented"

  observed_implementation:
    - "Profile"
    - "Unapproved automatic scoring"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Everything works correctly"

  requested_recommendation:
    - "ACCEPT"
```

### Expected Output

```yaml
status: FAIL
result: FAIL
recommendation: RETURN_FOR_REVALIDATION
```

### Acceptance Criteria

A requested recommendation MUST NOT override verification findings.

---

## IVER-R3-T019 — Full Current Verification Overrides Stale Execution State

### Input

```yaml
verification_input:
  plan_item:
    id: IP-224
    approved_scope:
      - "Approved capability"
    traceability:
      implementation: [IMP-224]
      upstream: [FR-224]

  execution:
    state: IN_PROGRESS
    result: CONTINUE
    evidence:
      - "Old execution record"

  observed_implementation:
    - "Approved capability fully implemented"

  blockers:
    - status: NONE
  open_items: []

  verification_evidence:
    - "Current authoritative implementation evidence"
    - "Current verification confirms full approved scope"
```

### Expected Output

```yaml
status: VERIFIED
result: PASS
scope_coverage: FULLY_COVERED
recommendation: ACCEPT
```

### Acceptance Criteria

Stale execution metadata MUST NOT override current authoritative verification evidence.

---

## IVER-R3-T020 — Final Regression Boundary

### Input

```yaml
verification_input:
  plan:
    - plan_item:
        id: IP-225
        approved_scope:
          - "Customer profile"
        traceability:
          implementation: [IMP-225]
          upstream: [FR-225]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Profile implementation completed"

      observed_implementation:
        - "Customer profile"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Profile fully verified"

    - plan_item:
        id: IP-226
        approved_scope:
          - "Profile update"
        traceability:
          implementation: [IMP-226]
          upstream: [FR-226]

      execution:
        state: IN_PROGRESS
        result: PARTIAL_EXECUTION
        evidence:
          - "Profile update partially implemented"

      observed_implementation:
        - "Profile update partially implemented"

      dependencies: []
      blockers:
        - status: NONE
      open_items: []

      verification_evidence:
        - "Only partial update evidence"

    - plan_item:
        id: IP-227
        approved_scope:
          - "Profile export"
        traceability:
          implementation: [IMP-227]
          upstream: [FR-227]

      execution:
        state: COMPLETED
        result: COMPLETED
        evidence:
          - "Export implemented"

      observed_implementation:
        - "Profile export"

      dependencies: []
      blockers:
        - status: NONE
      open_items:
        - item: "Export format"
          blocking: true

      verification_evidence:
        - "Export exists but format remains unresolved"
```

### Expected Output

```yaml
summary:
  total_plan_items: 3
  verified: 1
  partially_verified: 1
  not_verified: 0
  blocked: 1
  failed: 0

result: BLOCKED
recommendation: STOP
```

### Acceptance Criteria

The overall result MUST be `BLOCKED`.

`PARTIALLY_VERIFIED` and `VERIFIED` items MUST NOT hide the blocking third item.

---

# 8. Round 3 Acceptance Gate

Round 3 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 false PASS aggregations
0 false PASS_WITH_GAPS aggregations
0 ignored BLOCKED items
0 ignored FAIL items
0 stale evidence accepted without qualification
0 historical results incorrectly overriding current evidence
0 current failures hidden by historical PASS
0 partial scope promoted to full verification
0 scope version mismatches accepted
0 dependency verification bypasses
0 OPEN assumptions accepted
0 UNKNOWN values upgraded without evidence
0 ambiguous evidence silently reused
0 recommendation overrides findings
0 verification repairs performed
0 plan redesigns performed
0 execution state/result confusion
```

---

# 9. Regression Invariants

The following Round 1 and Round 2 rules MUST remain unchanged:

```text
R1:
Execution completion ≠ verification completion

R2:
Partial execution ≠ full verification

R3:
Missing evidence ≠ VERIFIED

R4:
Invalid traceability ≠ VERIFIED

R5:
Unsupported scope → FAIL

R6:
Blocking OPEN → BLOCKED

R7:
Unverified dependency → BLOCKED

R8:
UNKNOWN → NOT_VERIFIED unless new evidence exists

R9:
Current authoritative evidence may supersede stale execution metadata

R10:
Historical PASS does not override current failure

R11:
Verification does not repair implementation

R12:
Verification does not redesign the plan

R13:
FAIL has highest overall-result precedence

R14:
BLOCKED has precedence over NOT_VERIFIED

R15:
NOT_VERIFIED has precedence over PASS_WITH_GAPS

R16:
Recommendation cannot override verification result

R17:
Independent verified items remain verified when another branch is blocked

R18:
Current evidence may upgrade previous partial verification

R19:
Scope remains bounded by approved implementation

R20:
State/result and verification status/result remain separate
```

---

# 10. Round 3 Execution Record

| Test ID      | Expected Status    | Expected Result | Actual Status | Actual Result | Result | Finding                  |
| ------------ | ------------------ | --------------- | ------------- | ------------- | ------ | ------------------------ |
| IVER-R3-T001 | VERIFIED           | PASS            | —             | —             | —      | Multi-item PASS          |
| IVER-R3-T002 | PARTIALLY_VERIFIED | PASS_WITH_GAPS  | —             | —             | —      | Partial aggregation      |
| IVER-R3-T003 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Missing evidence         |
| IVER-R3-T004 | BLOCKED            | BLOCKED         | —             | —             | —      | Blocking execution       |
| IVER-R3-T005 | FAIL               | FAIL            | —             | —             | —      | FAIL precedence          |
| IVER-R3-T006 | BLOCKED            | BLOCKED         | —             | —             | —      | BLOCKED precedence       |
| IVER-R3-T007 | BLOCKED            | BLOCKED         | —             | —             | —      | Dependency invalidation  |
| IVER-R3-T008 | FAIL               | FAIL            | —             | —             | —      | Scope version            |
| IVER-R3-T009 | FAIL               | FAIL            | —             | —             | —      | Evidence contradiction   |
| IVER-R3-T010 | VERIFIED           | PASS            | —             | —             | —      | Non-blocking OPEN        |
| IVER-R3-T011 | BLOCKED            | BLOCKED         | —             | —             | —      | Blocking OPEN            |
| IVER-R3-T012 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Stale evidence           |
| IVER-R3-T013 | NOT_VERIFIED       | NOT_VERIFIED    | —             | —             | —      | Cancellation             |
| IVER-R3-T014 | VERIFIED           | PASS            | —             | —             | —      | Current revalidation     |
| IVER-R3-T015 | FAIL               | FAIL            | —             | —             | —      | Current failure          |
| IVER-R3-T016 | BLOCKED            | BLOCKED         | —             | —             | —      | Mixed branches           |
| IVER-R3-T017 | VERIFIED           | PASS            | —             | —             | —      | Upgrade previous partial |
| IVER-R3-T018 | FAIL               | FAIL            | —             | —             | —      | Recommendation boundary  |
| IVER-R3-T019 | VERIFIED           | PASS            | —             | —             | —      | Stale execution state    |
| IVER-R3-T020 | BLOCKED            | BLOCKED         | —             | —             | —      | Final aggregation        |

---

# 11. Round 3 Gate

```text
ROUND 3

Required:
20/20 PASS

Status:
NOT EXECUTED

Promotion:
NOT YET

Next:
Regression
```

A failed test MUST trigger review of the relevant Skill 16 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
