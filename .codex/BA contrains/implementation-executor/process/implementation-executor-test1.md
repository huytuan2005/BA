# Skill 15 — Implementation Executor

# `implementation-executor-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 1`
**Total Test Cases:** `20`

---

## 1. Objective

Validate that Skill 15 can execute only validated and executable implementation-plan items while preserving:

* Skill 14 execution gate;
* task readiness;
* dependency satisfaction;
* blocker handling;
* OPEN vs BLOCKED;
* scope fidelity;
* execution traceability;
* execution evidence;
* normalized execution state;
* execution result;
* completion criteria;
* stop conditions;
* separation between execution and design.

Round 1 focuses on baseline execution correctness.

It does not yet stress sophisticated scope bypass, hidden technical invention, recovery manipulation, or adversarial execution plans. Those belong to later rounds.

---

# 2. Explicit Test Input Format

Each test case MUST provide a self-contained execution input:

```yaml
validation_gate:
  result: PASS | PASS_WITH_OPEN_ITEMS | BLOCKED | FAIL

plan_item:
  id: IP-xxx
  title: <task>
  traceability:
    - IMP-xxx
  evidence: IMPLEMENTATION | DEV_STANDARD | SOURCE_STATED | DERIVED
  dependencies: []
  status: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED

dependencies:
  - plan_item: IP-xxx
    state: COMPLETED | NOT_COMPLETED | BLOCKED

blockers:
  - plan_item: IP-xxx
    status: BLOCKED
    reason: <reason>

open_items:
  - plan_item: IP-xxx
    item: <question>
    blocking: true | false

approved_scope:
  - <approved scope>

requested_execution:
  - <requested work>

existing_state:
  <relevant current implementation state>
```

`READY_WITH_OPEN_ITEMS` is NOT a normalized execution state.

When a task has non-blocking OPEN items, the task MUST use:

```yaml
status: READY
open_items:
  - blocking: false
```

---

# 3. Explicit Expected Output Format

Every execution result MUST contain at least:

```yaml
execution:
  run_id: EXEC-xxx
  validation_gate: PASS | PASS_WITH_OPEN_ITEMS | BLOCKED | FAIL
  plan_item: IP-xxx

  preconditions:
    result: PASS | FAIL

  dependencies:
    result: PASS | FAIL

  blockers:
    result: NONE | BLOCKED

  open_items:
    result: NONE | NON_BLOCKING | BLOCKING

  scope_check:
    result: PASS | FAIL

  state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED

  result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION

  evidence:
    - <execution evidence>

  open_items_remaining:
    - <remaining item>

  recommendation:
    CONTINUE_NEXT_READY_ITEM
    | WAIT_FOR_BLOCKER_RESOLUTION
    | REVALIDATE_CHANGED_SCOPE
    | STOP_EXECUTION
```

The executor MUST maintain a strict separation between:

```text
state
```

and:

```text
result
```

`PARTIAL_EXECUTION` is a result, NOT a state.

A partial execution MUST be represented as:

```yaml
state: IN_PROGRESS
result: PARTIAL_EXECUTION
```

The output MUST NOT silently modify the supplied plan.

---

# 4. State / Result Combination Rules

The following combinations are valid:

| State       | Result            |
| ----------- | ----------------- |
| NOT_STARTED | NO_ACTION         |
| READY       | STARTED           |
| IN_PROGRESS | CONTINUE          |
| IN_PROGRESS | PARTIAL_EXECUTION |
| COMPLETED   | COMPLETED         |
| BLOCKED     | BLOCKED           |
| FAILED      | FAILED            |
| CANCELLED   | CANCELLED         |

The following combinations are invalid:

```text
COMPLETED + BLOCKED
COMPLETED + FAILED
FAILED + COMPLETED
BLOCKED + CONTINUE
BLOCKED + COMPLETED
CANCELLED + CONTINUE
CANCELLED + COMPLETED
```

`PARTIALLY_COMPLETED` MUST NOT appear anywhere in Skill 15 output.

---

# 5. Round 1 Test Cases

## IEX-R1-T001 — Valid Ready Task

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-001
  title: "Implement approved customer profile capability"
  traceability: [IMP-001]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

dependencies: []
blockers: []
open_items: []

approved_scope:
  - "Customer profile capability"

requested_execution:
  - "Implement customer profile capability"
```

### Expected Output

```yaml
state: IN_PROGRESS → COMPLETED
result: COMPLETED
scope_check: PASS
dependencies: PASS
blockers: NONE
```

### Acceptance Criteria

The executor performs the approved task and records execution evidence.

---

## IEX-R1-T002 — Skill 14 PASS WITH OPEN ITEMS, Non-Blocking

### Input

```yaml
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-002
  title: "Prepare approved report export boundary"
  traceability: [IMP-002]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-002
    item: "Exact export format unresolved"
    blocking: false
```

### Expected Output

```yaml
state: COMPLETED
result: COMPLETED
open_items: NON_BLOCKING
```

### Acceptance Criteria

The executor proceeds without inventing the export format.

---

## IEX-R1-T003 — Skill 14 FAIL

### Input

```yaml
validation_gate:
  result: FAIL

plan_item:
  id: IP-003
  title: "Implement approved customer profile"
  traceability: [IMP-003]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

Execution does not begin.

---

## IEX-R1-T004 — Skill 14 BLOCKED

### Input

```yaml
validation_gate:
  result: BLOCKED

plan_item:
  id: IP-004
  title: "Implement approved payment capability"
  traceability: [IMP-004]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

Blocked validation prevents execution of affected scope.

---

## IEX-R1-T005 — Task Already COMPLETED

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-005
  title: "Implement customer profile"
  traceability: [IMP-005]
  evidence: IMPLEMENTATION
  dependencies: []
  status: COMPLETED
```

### Expected Output

```yaml
state: COMPLETED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

The executor MUST NOT execute already completed work again merely because it is present in the plan.

---

## IEX-R1-T006 — Unsatisfied Dependency

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-006
  title: "Implement approved UI integration"
  traceability: [IMP-006]
  evidence: IMPLEMENTATION
  dependencies: [IP-005]
  status: READY

dependencies:
  - plan_item: IP-005
    state: NOT_COMPLETED
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor does not bypass the unsatisfied dependency.

---

## IEX-R1-T007 — Satisfied Dependency

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-007
  title: "Implement approved UI integration"
  traceability: [IMP-007]
  evidence: IMPLEMENTATION
  dependencies: [IP-006]
  status: READY

dependencies:
  - plan_item: IP-006
    state: COMPLETED
```

### Expected Output

```yaml
dependencies: PASS
state: COMPLETED
result: COMPLETED
```

### Acceptance Criteria

The task is executable because its required prerequisite is explicitly completed.

---

## IEX-R1-T008 — Direct Blocker

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-008
  title: "Implement payment provider integration"
  traceability: [IMP-008]
  evidence: IMPLEMENTATION
  dependencies: []
  status: BLOCKED

blockers:
  - plan_item: IP-008
    status: BLOCKED
    reason: "Required provider decision unresolved"
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor does not invent a payment provider.

---

## IEX-R1-T009 — Non-Blocking Open Item

### Input

```yaml
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-009
  title: "Prepare approved report boundary"
  traceability: [IMP-009]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-009
    item: "Exact display label unresolved"
    blocking: false
```

### Expected Output

```yaml
open_items: NON_BLOCKING
state: COMPLETED
result: COMPLETED
```

### Acceptance Criteria

Execution proceeds without guessing the unresolved label.

---

## IEX-R1-T010 — Blocking Open Item

### Input

```yaml
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-010
  title: "Implement provider-specific payment integration"
  traceability: [IMP-010]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-010
    item: "Payment provider unresolved"
    blocking: true
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor does not convert the open item into an assumed provider.

---

## IEX-R1-T011 — Scope Matches Exactly

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-011
  title: "Implement customer profile viewing"
  traceability: [IMP-011]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Customer profile viewing"

requested_execution:
  - "Customer profile viewing"
```

### Expected Output

```yaml
scope_check: PASS
state: COMPLETED
result: COMPLETED
```

---

## IEX-R1-T012 — Requested Scope Broader Than Plan

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-012
  title: "Implement customer profile viewing"
  traceability: [IMP-012]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Customer profile viewing"

requested_execution:
  - "Customer profile viewing"
  - "Customer profile deletion"
```

### Expected Output

```yaml
scope_check: FAIL
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

### Acceptance Criteria

The executor MUST NOT silently execute only the allowed subset.

---

## IEX-R1-T013 — Unsupported New Requirement Discovered

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-013
  title: "Implement approved login capability"
  traceability: [IMP-013]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Login capability"

existing_state:
  discovery: "Password reset appears useful but is not approved."

requested_execution:
  - "Login"
  - "Password reset"
```

### Expected Output

```yaml
scope_check: FAIL
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

### Acceptance Criteria

The executor does not implement the new requirement.

---

## IEX-R1-T014 — Valid Execution Traceability

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-014
  title: "Implement approved customer profile"
  traceability: [IMP-014]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY
```

### Expected Output

```yaml
traceability:
  plan: IP-014
  implementation: IMP-014

state: COMPLETED
result: COMPLETED
```

### Acceptance Criteria

Execution evidence remains connected to the plan and implementation item.

---

## IEX-R1-T015 — Missing Execution Traceability

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-015
  title: "Implement customer profile"
  traceability: []
  evidence: UNKNOWN
  dependencies: []
  status: READY
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text
EXECUTION_TRACEABILITY_MISSING
```

### Acceptance Criteria

No execution occurs without traceability.

---

## IEX-R1-T016 — Independent Task Can Proceed

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-016
  title: "Implement independent report capability"
  traceability: [IMP-016]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

blockers:
  - plan_item: IP-015
    status: BLOCKED
    reason: "Unresolved dependency"
```

### Expected Output

```yaml
state: COMPLETED
result: COMPLETED
```

### Acceptance Criteria

A blocked unrelated task does not prevent independent execution.

---

## IEX-R1-T017 — Execution Failure Does Not Expand Scope

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-017
  title: "Implement approved customer profile"
  traceability: [IMP-017]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  execution_error: "Approved implementation cannot currently complete."
```

### Expected Output

```yaml
state: FAILED
result: FAILED
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

The executor records the failure and does not introduce alternative technology or architecture.

---

## IEX-R1-T018 — Partial Execution

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-018
  title: "Implement approved profile capability"
  traceability: [IMP-018]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  completed_portion:
    - "Profile viewing"
  remaining_portion:
    - "Approved profile update"
```

### Expected Output

```yaml
state: IN_PROGRESS
result: PARTIAL_EXECUTION

completed_portion:
  - "Profile viewing"

remaining_portion:
  - "Approved profile update"
```

### Acceptance Criteria

The executor MUST NOT claim `COMPLETED`.

`PARTIAL_EXECUTION` MUST appear only as the execution result and MUST NOT be used as the execution state.

---

## IEX-R1-T019 — Completion Requires Evidence

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-019
  title: "Implement approved customer profile"
  traceability: [IMP-019]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  claim: "Code appears to exist."
  execution_evidence: []
```

### Expected Output

```yaml
state: FAILED
result: FAILED
```

Finding:

```text
COMPLETION_EVIDENCE_INSUFFICIENT
```

### Acceptance Criteria

The executor MUST NOT mark the task `COMPLETED` based only on an unsupported completion claim.

---

## IEX-R1-T020 — Next Ready Task Selection

### Input

```yaml
validation_gate:
  result: PASS

plan:
  - id: IP-020
    status: COMPLETED
  - id: IP-021
    status: BLOCKED
  - id: IP-022
    status: READY

dependencies:
  - plan_item: IP-021
    state: BLOCKED
  - plan_item: IP-022
    state: COMPLETED

blockers:
  - plan_item: IP-021
    status: BLOCKED
    reason: "Required decision unresolved"

requested_execution:
  - IP-022
```

### Expected Output

```yaml
selected_task: IP-022
state: COMPLETED
result: COMPLETED
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

The executor selects executable work rather than remaining stuck on the blocked branch.

---

# 6. Round 1 Acceptance Gate

Round 1 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 executions against FAIL validation
0 executions against BLOCKED validation
0 executions with unsatisfied dependency
0 executions with blocking open item
0 unsupported scope executions
0 executions without traceability
0 false COMPLETED claims
0 silent scope expansions
0 invented workarounds
0 PARTIALLY_COMPLETED states
```

---

# 7. Round 1 Execution Record

| Test ID     | Expected State | Expected Result   | Actual State | Actual Result | Result | Notes |
| ----------- | -------------- | ----------------- | ------------ | ------------- | ------ | ----- |
| IEX-R1-T001 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T002 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T003 | BLOCKED        | NO_ACTION         | —            | —             | —      | —     |
| IEX-R1-T004 | BLOCKED        | NO_ACTION         | —            | —             | —      | —     |
| IEX-R1-T005 | COMPLETED      | NO_ACTION         | —            | —             | —      | —     |
| IEX-R1-T006 | BLOCKED        | BLOCKED           | —            | —             | —      | —     |
| IEX-R1-T007 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T008 | BLOCKED        | BLOCKED           | —            | —             | —      | —     |
| IEX-R1-T009 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T010 | BLOCKED        | BLOCKED           | —            | —             | —      | —     |
| IEX-R1-T011 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T012 | BLOCKED        | BLOCKED           | —            | —             | —      | —     |
| IEX-R1-T013 | BLOCKED        | BLOCKED           | —            | —             | —      | —     |
| IEX-R1-T014 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T015 | BLOCKED        | NO_ACTION         | —            | —             | —      | —     |
| IEX-R1-T016 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |
| IEX-R1-T017 | FAILED         | FAILED            | —            | —             | —      | —     |
| IEX-R1-T018 | IN_PROGRESS    | PARTIAL_EXECUTION | —            | —             | —      | —     |
| IEX-R1-T019 | FAILED         | FAILED            | —            | —             | —      | —     |
| IEX-R1-T020 | COMPLETED      | COMPLETED         | —            | —             | —      | —     |

---

# 8. Round 1 Gate

```text
ROUND 1

Required:
20/20 PASS

Promotion:
NOT YET

Next:
Round 2
```

A failed test MUST trigger a review of the corresponding Skill 15 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
