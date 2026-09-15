# Skill 15 — Implementation Executor

# `implementation-executor-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 3 — Final Adversarial / Regression`
**Total Test Cases:** `20`

---

# 1. Objective

Round 3 is the final validation round before promoting Skill 15.

It validates whether the executor preserves all previously established invariants under:

* repeated execution;
* execution after state transitions;
* partial completion;
* failure and recovery;
* dependency-chain changes;
* blocker resolution;
* scope changes;
* stale execution requests;
* contradictory evidence;
* mixed task queues;
* stop conditions;
* regression against Round 1 and Round 2 rules.

Round 3 MUST NOT weaken any rule established in previous rounds.

---

# 2. Final Invariants

The executor MUST preserve:

```text
Approved scope only
Explicit dependencies only
Explicit blockers only
OPEN remains OPEN
UNKNOWN remains UNKNOWN
No invented workaround
No invented architecture
No invented technical decision
Valid execution traceability only
Completion requires evidence
Partial execution ≠ completion
Skill 14 PASS ≠ implementation completion
State and result remain separate
Invalid state/result combinations are rejected
Cancelled scope is not reactivated
Failed scope is not retried without authorization
```

---

# 3. Normalized State Model

```text
NOT_STARTED
READY
IN_PROGRESS
BLOCKED
COMPLETED
FAILED
CANCELLED
```

---

# 4. Normalized Result Model

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

`PARTIALLY_COMPLETED` MUST NOT appear anywhere.

---

# 5. Round 3 Test Cases

## IEX-R3-T001 — Re-execution After Completion

### Input

```yaml id="0ks3do"
validation_gate:
  result: PASS

plan_item:
  id: IP-201
  title: "Implement approved customer profile"
  traceability: [IMP-201]
  evidence: IMPLEMENTATION
  dependencies: []
  status: COMPLETED

existing_state:
  previous_execution:
    status: COMPLETED
    evidence:
      - "Implementation verified"

requested_execution:
  - "Run the same implementation again."
```

### Expected Output

```yaml id="7k8aeo"
state: COMPLETED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

The executor MUST NOT duplicate completed work.

---

## IEX-R3-T002 — Partial Task Continues Only Remaining Scope

### Input

```yaml id="6lqj9e"
validation_gate:
  result: PASS

plan_item:
  id: IP-202
  title: "Implement approved profile capability"
  traceability: [IMP-202]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  completed_portion:
    - "Profile viewing"
  remaining_portion:
    - "Profile update"

requested_execution:
  - "Continue remaining approved work."
```

### Expected Output

```yaml id="jz6v3p"
state: IN_PROGRESS
result: CONTINUE
```

### Acceptance Criteria

The executor continues only the explicitly remaining approved scope.

---

## IEX-R3-T003 — Partial Task With New Scope

### Input

```yaml id="j4r2kn"
validation_gate:
  result: PASS

plan_item:
  id: IP-203
  title: "Implement approved profile capability"
  traceability: [IMP-203]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  remaining_portion:
    - "Profile update"

requested_execution:
  - "Profile update"
  - "Profile export"
```

### Expected Output

```yaml id="9j1s5b"
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

### Acceptance Criteria

Remaining approved work MUST NOT be used as justification for adding new work.

---

## IEX-R3-T004 — Blocker Resolved Without Scope Change

### Input

```yaml id="3yq9zi"
validation_gate:
  result: PASS

plan_item:
  id: IP-204
  title: "Implement approved payment capability"
  traceability: [IMP-204]
  evidence: IMPLEMENTATION
  dependencies: []
  status: BLOCKED

existing_state:
  blocker:
    status: RESOLVED
  approved_scope:
    - "Payment capability"
```

### Expected Output

```yaml id="5y6w7o"
state: READY
result: NO_ACTION
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

Resolution of a blocker makes the task eligible for execution; it does NOT imply completion.

---

## IEX-R3-T005 — Blocker Resolution With New Requirement

### Input

```yaml id="a1x8he"
validation_gate:
  result: PASS

plan_item:
  id: IP-205
  title: "Implement approved payment capability"
  traceability: [IMP-205]
  evidence: IMPLEMENTATION
  dependencies: []
  status: BLOCKED

existing_state:
  blocker:
    status: RESOLVED
  new_requirement:
    - "Add recurring billing"
```

### Expected Output

```yaml id="n6j2fs"
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

---

## IEX-R3-T006 — Dependency Completed After Task Was Blocked

### Input

```yaml id="x9w34m"
validation_gate:
  result: PASS

plan_item:
  id: IP-206
  title: "Implement dependent UI"
  traceability: [IMP-206]
  evidence: IMPLEMENTATION
  dependencies: [IP-205]
  status: BLOCKED

dependencies:
  - plan_item: IP-205
    state: COMPLETED
```

### Expected Output

```yaml id="5k78pf"
state: READY
result: NO_ACTION
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

The executor may reclassify the task as executable, but MUST NOT claim completion.

---

## IEX-R3-T007 — Dependency Completed Claim Without Evidence

### Input

```yaml id="1cfqte"
validation_gate:
  result: PASS

plan_item:
  id: IP-207
  title: "Implement dependent feature"
  traceability: [IMP-207]
  evidence: IMPLEMENTATION
  dependencies: [IP-206]
  status: READY

dependencies:
  - plan_item: IP-206
    state: COMPLETED

existing_state:
  dependency_evidence: []
```

### Expected Output

```yaml id="0u0zwg"
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

Finding:

```text id="01q9xh"
DEPENDENCY_COMPLETION_EVIDENCE_MISSING
```

---

## IEX-R3-T008 — Stale Execution Request After Scope Change

### Input

```yaml id="9d1j3s"
validation_gate:
  result: PASS

plan_item:
  id: IP-208
  title: "Implement approved dashboard"
  traceability: [IMP-208]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Dashboard"

existing_state:
  scope_version:
    approved: V2
    requested_execution: V1
```

### Expected Output

```yaml id="9izpov"
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

Finding:

```text id="3m7l0e"
STALE_EXECUTION_SCOPE
```

---

## IEX-R3-T009 — Contradictory Approval Evidence

### Input

```yaml id="bx7nqa"
validation_gate:
  result: PASS

plan_item:
  id: IP-209
  title: "Implement approved report"
  traceability: [IMP-209]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  approval_records:
    - "Approved"
    - "Approval revoked"
```

### Expected Output

```yaml id="4zj3r5"
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text id="m7f1ku"
APPROVAL_STATE_CONTRADICTION
```

---

## IEX-R3-T010 — Execution Evidence From Another Task

### Input

```yaml id="p8a6ww"
validation_gate:
  result: PASS

plan_item:
  id: IP-210
  title: "Implement customer profile"
  traceability: [IMP-210]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  execution_evidence:
    plan_item: IP-211
```

### Expected Output

```yaml
state: FAILED
result: FAILED
recommendation: STOP_EXECUTION
```

Finding:

```text
EXECUTION_EVIDENCE_SCOPE_MISMATCH
```

---

## IEX-R3-T011 — Completion Evidence Contradicts Current State

### Input

```yaml id="6x2xuy"
validation_gate:
  result: PASS

plan_item:
  id: IP-211
  title: "Implement approved capability"
  traceability: [IMP-211]
  evidence: IMPLEMENTATION
  dependencies: []
  status: COMPLETED

existing_state:
  execution_evidence:
    verification: "Feature remains incomplete."
```

### Expected Output

```yaml id="xcyv6k"
state: FAILED
result: FAILED
recommendation: STOP_EXECUTION
```

Finding:

```text
COMPLETION_STATE_CONTRADICTION
```

---

## IEX-R3-T012 — BLOCKED Task Hidden Inside Mixed Queue

### Input

```yaml id="y0b9af"
validation_gate:
  result: PASS

plan:
  - id: IP-212
    status: BLOCKED
  - id: IP-213
    status: READY
  - id: IP-214
    status: READY

dependencies:
  - plan_item: IP-212
    state: BLOCKED
  - plan_item: IP-213
    state: COMPLETED
  - plan_item: IP-214
    state: NOT_COMPLETED

requested_execution:
  - IP-212
  - IP-214
```

### Expected Output

```yaml id="q6d9m4"
selected_task: IP-214
state: COMPLETED
result: COMPLETED
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

The blocked task MUST NOT prevent an independent executable task from proceeding.

---

## IEX-R3-T013 — No Executable Task Available

### Input

```yaml id="f8ne44"
validation_gate:
  result: PASS

plan:
  - id: IP-215
    status: BLOCKED
  - id: IP-216
    status: BLOCKED
  - id: IP-217
    status: COMPLETED

requested_execution:
  - "Continue implementation."
```

### Expected Output

```yaml id="y9y8fl"
state: BLOCKED
result: NO_ACTION
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor MUST NOT invent a new task merely to keep execution moving.

---

## IEX-R3-T014 — Retry After Failure Without Recovery Authorization

### Input

```yaml id="j9kz47"
validation_gate:
  result: PASS

plan_item:
  id: IP-218
  title: "Implement approved capability"
  traceability: [IMP-218]
  evidence: IMPLEMENTATION
  dependencies: []
  status: FAILED

existing_state:
  recovery:
    authorization: NONE

requested_execution:
  - "Retry the failed task."
```

### Expected Output

```yaml id="f2pbk3"
state: BLOCKED
result: NO_ACTION
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

---

## IEX-R3-T015 — Retry Authorized Within Same Scope

### Input

```yaml id="bs1a5a"
validation_gate:
  result: PASS

plan_item:
  id: IP-219
  title: "Implement approved capability"
  traceability: [IMP-219]
  evidence: IMPLEMENTATION
  dependencies: []
  status: FAILED

existing_state:
  recovery:
    authorization: APPROVED
    scope_change: false
```

### Expected Output

```yaml id="42n9hc"
state: READY
result: NO_ACTION
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

Authorization may make retry eligible but MUST NOT claim execution has already happened.

---

## IEX-R3-T016 — Recovery Authorization Includes Scope Expansion

### Input

```yaml id="p2he6s"
validation_gate:
  result: PASS

plan_item:
  id: IP-220
  title: "Implement approved capability"
  traceability: [IMP-220]
  evidence: IMPLEMENTATION
  dependencies: []
  status: FAILED

existing_state:
  recovery:
    authorization: APPROVED
    scope_change: true
    new_scope:
      - "Add additional capability"
```

### Expected Output

```yaml id="hf8w0m"
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

---

## IEX-R3-T017 — CANCELLED Task Appears as Dependency

### Input

```yaml id="m6n0oe"
validation_gate:
  result: PASS

plan_item:
  id: IP-221
  title: "Implement dependent capability"
  traceability: [IMP-221]
  evidence: IMPLEMENTATION
  dependencies: [IP-220]
  status: READY

dependencies:
  - plan_item: IP-220
    state: CANCELLED
```

### Expected Output

```yaml id="a6m4pn"
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

`CANCELLED` MUST NOT satisfy a dependency.

---

## IEX-R3-T018 — OPEN Item Becomes Resolved With Explicit Evidence

### Input

```yaml id="4l9ew4"
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-222
  title: "Implement approved notification capability"
  traceability: [IMP-222]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-222
    item: "Notification channel"
    blocking: true

existing_state:
  decision:
    status: RESOLVED
    value: "Email"
    evidence: SOURCE_STATED
```

### Expected Output

```yaml id="q7tqg0"
state: COMPLETED
result: COMPLETED
open_items: NONE
```

### Acceptance Criteria

Execution may proceed because the formerly blocking OPEN item now has explicit evidence.

The executor MUST use the stated decision and MUST NOT replace it with another channel.

---

## IEX-R3-T019 — Regression: No `PARTIALLY_COMPLETED`

### Input

```yaml id="v0e5hy"
validation_gate:
  result: PASS

plan_item:
  id: IP-223
  title: "Implement approved capability"
  traceability: [IMP-223]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  completed_portion:
    - "Approved portion A"
  remaining_portion:
    - "Approved portion B"

requested_execution:
  - "Report partial progress."
```

### Expected Output

```yaml id="5j8u2z"
state: IN_PROGRESS
result: PARTIAL_EXECUTION
```

### Acceptance Criteria

The string:

```text
PARTIALLY_COMPLETED
```

MUST NOT appear in:

* state;
* result;
* recommendation;
* execution record.

---

## IEX-R3-T020 — Final Stop Condition

### Input

```yaml id="l8mm1u"
validation_gate:
  result: FAIL

plan_item:
  id: IP-224
  title: "Implement approved capability"
  traceability: [IMP-224]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

requested_execution:
  - "Continue anyway because most of the plan is already validated."
```

### Expected Output

```yaml id="3u6g1r"
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

The executor MUST stop immediately.

No partial execution, workaround, alternative task, or scope substitution is allowed.

---

# 6. Round 3 Acceptance Gate

Round 3 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 unauthorized re-executions
0 scope expansions
0 stale-scope executions
0 dependency bypasses
0 cancelled dependencies accepted
0 unsupported retries
0 unauthorized recovery executions
0 approval contradictions ignored
0 evidence-scope mismatches accepted
0 completion contradictions ignored
0 fabricated tasks
0 invented technical decisions
0 invalid state/result combinations
0 PARTIALLY_COMPLETED states
0 executions after a hard-stop condition
```

---

# 7. Regression Invariants

The following MUST remain true from Round 1 through Round 3:

```text
R1:
Blocking validation → no execution

R2:
Blocking OPEN → BLOCKED

R3:
Unsatisfied dependency → BLOCKED

R4:
Scope expansion → BLOCKED

R5:
Missing traceability → NO_ACTION

R6:
Completion without evidence → FAILED

R7:
Partial execution → IN_PROGRESS + PARTIAL_EXECUTION

R8:
Skill 14 PASS → execution eligibility only

R9:
Cancelled → never automatically reactivated

R10:
Failed → retry requires explicit recovery authorization

R11:
State and result remain separate

R12:
No invented workaround

R13:
No invented architecture

R14:
No invented requirement

R15:
No invalid state/result combination
```

---

# 8. Round 3 Execution Record

| Test ID     | Expected State | Expected Result   | Actual State | Actual Result | Result | Finding                     |
| ----------- | -------------- | ----------------- | ------------ | ------------- | ------ | --------------------------- |
| IEX-R3-T001 | COMPLETED      | NO_ACTION         | —            | —             | —      | Re-execution                |
| IEX-R3-T002 | IN_PROGRESS    | CONTINUE          | —            | —             | —      | Partial continuation        |
| IEX-R3-T003 | BLOCKED        | BLOCKED           | —            | —             | —      | Scope expansion             |
| IEX-R3-T004 | READY          | NO_ACTION         | —            | —             | —      | Blocker resolved            |
| IEX-R3-T005 | BLOCKED        | BLOCKED           | —            | —             | —      | New requirement             |
| IEX-R3-T006 | READY          | NO_ACTION         | —            | —             | —      | Dependency transition       |
| IEX-R3-T007 | BLOCKED        | BLOCKED           | —            | —             | —      | Missing dependency evidence |
| IEX-R3-T008 | BLOCKED        | BLOCKED           | —            | —             | —      | Stale scope                 |
| IEX-R3-T009 | BLOCKED        | NO_ACTION         | —            | —             | —      | Approval contradiction      |
| IEX-R3-T010 | FAILED         | FAILED            | —            | —             | —      | Evidence mismatch           |
| IEX-R3-T011 | FAILED         | FAILED            | —            | —             | —      | Completion contradiction    |
| IEX-R3-T012 | COMPLETED      | COMPLETED         | —            | —             | —      | Mixed queue                 |
| IEX-R3-T013 | BLOCKED        | NO_ACTION         | —            | —             | —      | No executable task          |
| IEX-R3-T014 | BLOCKED        | NO_ACTION         | —            | —             | —      | Unauthorized retry          |
| IEX-R3-T015 | READY          | NO_ACTION         | —            | —             | —      | Authorized retry            |
| IEX-R3-T016 | BLOCKED        | BLOCKED           | —            | —             | —      | Recovery scope change       |
| IEX-R3-T017 | BLOCKED        | BLOCKED           | —            | —             | —      | Cancelled dependency        |
| IEX-R3-T018 | COMPLETED      | COMPLETED         | —            | —             | —      | OPEN resolved               |
| IEX-R3-T019 | IN_PROGRESS    | PARTIAL_EXECUTION | —            | —             | —      | State normalization         |
| IEX-R3-T020 | BLOCKED        | NO_ACTION         | —            | —             | —      | Final stop                  |

---

# 9. Round 3 Gate

```text
ROUND 3

Required:
20/20 PASS

Status:
NOT EXECUTED

Promotion:
NOT YET
```

After Round 3 passes:

```text
Round 1 = 20/20
Round 2 = 20/20
Round 3 = 20/20

Total = 60/60
```

Only then may Skill 15 be promoted:

```text
v0.1 → v1.0
Status: LOCKED
```

A failed Round 3 test MUST trigger review of the relevant Skill 15 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
