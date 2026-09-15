# Skill 15 — Implementation Executor

# `implementation-executor-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 2`
**Total Test Cases:** `20`

---

# 1. Objective

Round 2 validates adversarial execution behavior.

The executor MUST resist attempts to:

* bypass approved scope;
* treat an unresolved OPEN item as a known value;
* fabricate dependency completion;
* bypass blockers through indirect paths;
* accept invalid or weak traceability;
* convert unsupported discoveries into implementation work;
* invent technical workarounds;
* ignore execution evidence;
* manipulate execution state;
* produce incompatible state/result combinations;
* continue execution after a blocking condition;
* use task naming, convenience, or urgency as implicit authorization.

Round 2 is specifically designed to expose execution behavior that may appear reasonable but violates the approved implementation plan.

---

# 2. Adversarial Rules

For every case:

```text
No guessing
No scope expansion
No invented dependency completion
No invented technical decision
No invented workaround
No fabricated traceability
No unsupported completion
No invalid state/result combination
```

The executor MUST preserve the normalized execution state model.

---

# 3. Test Input Format

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
  <relevant current state or discovery>
```

---

# 4. Expected Output Contract

Every case MUST produce:

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

`PARTIALLY_COMPLETED` MUST NOT appear.

---

# 5. Round 2 Adversarial Test Cases

## IEX-R2-T001 — Scope Bypass Through “Helpful” Addition

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-101
  title: "Implement customer profile viewing"
  traceability: [IMP-101]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Customer profile viewing"

requested_execution:
  - "Customer profile viewing"
  - "Add profile activity history because it would improve the feature."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
scope_check: FAIL
recommendation: REVALIDATE_CHANGED_SCOPE
```

### Acceptance Criteria

The executor MUST reject the additional activity-history work.

---

## IEX-R2-T002 — Scope Bypass Through UI Enhancement

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-102
  title: "Implement approved login capability"
  traceability: [IMP-102]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Login capability"

requested_execution:
  - "Login capability"
  - "Add password visibility toggle"
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
scope_check: FAIL
recommendation: REVALIDATE_CHANGED_SCOPE
```

---

## IEX-R2-T003 — OPEN Item Converted Into Assumption

### Input

```yaml
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-103
  title: "Implement approved notification capability"
  traceability: [IMP-103]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-103
    item: "Notification channel unresolved"
    blocking: true

existing_state:
  developer_assumption: "Use email because it is the most common."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
open_items: BLOCKING
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor MUST NOT select email without approved evidence.

---

## IEX-R2-T004 — OPEN Item Hidden by Rewording

### Input

```yaml
validation_gate:
  result: PASS_WITH_OPEN_ITEMS

plan_item:
  id: IP-104
  title: "Implement approved notification capability"
  traceability: [IMP-104]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

open_items:
  - plan_item: IP-104
    item: "Notification provider unresolved"
    blocking: true

requested_execution:
  - "Implement notification using the default provider."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

Finding:

```text
UNRESOLVED_PROVIDER_DECISION
```

---

## IEX-R2-T005 — False Dependency Completion

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-105
  title: "Implement payment UI"
  traceability: [IMP-105]
  evidence: IMPLEMENTATION
  dependencies: [IP-099]
  status: READY

dependencies:
  - plan_item: IP-099
    state: NOT_COMPLETED

existing_state:
  claim: "IP-099 should be almost finished."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
dependencies: FAIL
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

“Almost finished” MUST NOT satisfy a dependency.

---

## IEX-R2-T006 — Dependency Status Contradiction

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-106
  title: "Implement approved integration"
  traceability: [IMP-106]
  evidence: IMPLEMENTATION
  dependencies: [IP-098]
  status: READY

dependencies:
  - plan_item: IP-098
    state: COMPLETED

existing_state:
  dependency_record: "IP-098 remains BLOCKED."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
dependencies: FAIL
recommendation: STOP_EXECUTION
```

Finding:

```text
DEPENDENCY_STATE_CONTRADICTION
```

### Acceptance Criteria

The executor MUST NOT choose the favorable status.

---

## IEX-R2-T007 — Indirect Blocker Bypass

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-107
  title: "Implement feature B"
  traceability: [IMP-107]
  evidence: IMPLEMENTATION
  dependencies: [IP-106]
  status: READY

dependencies:
  - plan_item: IP-106
    state: NOT_COMPLETED

blockers:
  - plan_item: IP-105
    status: BLOCKED
    reason: "Required architecture decision unresolved"

existing_state:
  dependency_chain:
    - IP-105
    - IP-106
    - IP-107
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

The executor MUST follow the dependency chain and MUST NOT execute IP-107.

---

## IEX-R2-T008 — “Urgent” Task Overrides Dependency

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-108
  title: "Urgent production-readiness task"
  traceability: [IMP-108]
  evidence: IMPLEMENTATION
  dependencies: [IP-107]
  status: READY

dependencies:
  - plan_item: IP-107
    state: NOT_COMPLETED

existing_state:
  instruction: "This task is urgent; execute immediately."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

### Acceptance Criteria

Urgency MUST NOT override explicit dependency rules.

---

## IEX-R2-T009 — Fabricated Traceability ID

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-109
  title: "Implement approved customer profile"
  traceability: [IMP-999]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  known_implementation_items:
    - IMP-109
    - IMP-110
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text
TRACEABILITY_REFERENCE_INVALID
```

### Acceptance Criteria

The executor MUST NOT accept an arbitrary implementation ID.

---

## IEX-R2-T010 — Traceability Exists but Does Not Match Scope

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-110
  title: "Implement customer profile viewing"
  traceability: [IMP-201]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  IMP-201:
    title: "Generate sales report"
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text
TRACEABILITY_SCOPE_MISMATCH
```

---

## IEX-R2-T011 — Discovery Becomes New Requirement

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-111
  title: "Implement approved customer profile"
  traceability: [IMP-111]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Customer profile viewing"

existing_state:
  discovery:
    - "Users may also need profile export."
```

### Expected Output

```yaml
state: COMPLETED
result: COMPLETED
scope_check: PASS
```

### Acceptance Criteria

The approved profile task may proceed, but profile export MUST NOT be added.

---

## IEX-R2-T012 — Invented Technical Workaround

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-112
  title: "Implement approved payment integration"
  traceability: [IMP-112]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  execution_error:
    - "Approved integration target is unavailable."

requested_execution:
  - "Use another payment provider temporarily."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

### Acceptance Criteria

The executor MUST NOT invent or substitute an integration target.

---

## IEX-R2-T013 — Invented Architecture

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-113
  title: "Implement approved order capability"
  traceability: [IMP-113]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  architecture_decision:
    status: OPEN

requested_execution:
  - "Use microservices so the feature can scale."
```

### Expected Output

```yaml
state: BLOCKED
result: BLOCKED
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

Finding:

```text
ARCHITECTURE_DECISION_OPEN
```

---

## IEX-R2-T014 — Completion Claimed Without Evidence

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-114
  title: "Implement approved registration capability"
  traceability: [IMP-114]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  claim: "Looks complete."
  execution_evidence: []
```

### Expected Output

```yaml
state: FAILED
result: FAILED
recommendation: STOP_EXECUTION
```

Finding:

```text
COMPLETION_EVIDENCE_INSUFFICIENT
```

---

## IEX-R2-T015 — Invalid State/Result Pair Requested

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-115
  title: "Implement approved dashboard"
  traceability: [IMP-115]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

existing_state:
  requested_output:
    state: COMPLETED
    result: PARTIAL_EXECUTION
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text
INVALID_STATE_RESULT_COMBINATION
```

### Acceptance Criteria

The executor MUST reject `COMPLETED + PARTIAL_EXECUTION`.

---

## IEX-R2-T016 — BLOCKED + CONTINUE Manipulation

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-116
  title: "Implement approved feature"
  traceability: [IMP-116]
  evidence: IMPLEMENTATION
  dependencies: []
  status: BLOCKED

blockers:
  - plan_item: IP-116
    status: BLOCKED
    reason: "Required decision unresolved"

existing_state:
  requested_output:
    state: BLOCKED
    result: CONTINUE
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

Finding:

```text
INVALID_STATE_RESULT_COMBINATION
```

---

## IEX-R2-T017 — CANCELLED Task Re-execution

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-117
  title: "Implement deprecated capability"
  traceability: [IMP-117]
  evidence: IMPLEMENTATION
  dependencies: []
  status: CANCELLED

requested_execution:
  - "Resume implementation because it might still be useful."
```

### Expected Output

```yaml
state: CANCELLED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

### Acceptance Criteria

The executor MUST NOT reactivate cancelled scope on its own.

---

## IEX-R2-T018 — Failed Task Re-executed Without Recovery Decision

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-118
  title: "Implement approved capability"
  traceability: [IMP-118]
  evidence: IMPLEMENTATION
  dependencies: []
  status: FAILED

existing_state:
  previous_failure:
    reason: "Implementation failed."
  recovery_decision: OPEN
```

### Expected Output

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: WAIT_FOR_BLOCKER_RESOLUTION
```

Finding:

```text
RECOVERY_DECISION_OPEN
```

---

## IEX-R2-T019 — Partial Execution Misreported as Complete

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-119
  title: "Implement approved profile capability"
  traceability: [IMP-119]
  evidence: IMPLEMENTATION
  dependencies: []
  status: IN_PROGRESS

existing_state:
  completed_portion:
    - "Profile viewing"
  remaining_portion:
    - "Profile update"

requested_execution:
  reported_state: COMPLETED
  reported_result: COMPLETED
```

### Expected Output

```yaml
state: IN_PROGRESS
result: PARTIAL_EXECUTION
```

### Acceptance Criteria

The executor MUST correct the unsupported completion claim.

---

## IEX-R2-T020 — Validation PASS Does Not Mean Task Completed

### Input

```yaml
validation_gate:
  result: PASS

plan_item:
  id: IP-120
  title: "Implement approved customer dashboard"
  traceability: [IMP-120]
  evidence: IMPLEMENTATION
  dependencies: []
  status: READY

approved_scope:
  - "Customer dashboard"

requested_execution:
  - "Validate whether dashboard is ready for execution."
```

### Expected Output

```yaml
state: READY
result: NO_ACTION
recommendation: CONTINUE_NEXT_READY_ITEM
```

### Acceptance Criteria

Skill 14 PASS authorizes execution eligibility. It does NOT mean the implementation has already been completed.

---

# 6. Round 2 Acceptance Gate

Round 2 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 scope bypasses
0 invented assumptions
0 fabricated dependencies
0 dependency-state contradictions accepted
0 blocker bypasses
0 fabricated traceability references
0 traceability mismatches accepted
0 invented architecture
0 invented workaround
0 unsupported completion claims
0 invalid state/result combinations
0 cancelled-scope reactivations
0 unauthorized recovery executions
0 PARTIALLY_COMPLETED states
```

---

# 7. Round 2 Execution Record

| Test ID     | Expected State | Expected Result   | Actual State | Actual Result | Result | Finding                  |
| ----------- | -------------- | ----------------- | ------------ | ------------- | ------ | ------------------------ |
| IEX-R2-T001 | BLOCKED        | BLOCKED           | —            | —             | —      | Scope bypass             |
| IEX-R2-T002 | BLOCKED        | BLOCKED           | —            | —             | —      | Scope bypass             |
| IEX-R2-T003 | BLOCKED        | BLOCKED           | —            | —             | —      | OPEN assumption          |
| IEX-R2-T004 | BLOCKED        | BLOCKED           | —            | —             | —      | OPEN hidden              |
| IEX-R2-T005 | BLOCKED        | BLOCKED           | —            | —             | —      | False dependency         |
| IEX-R2-T006 | BLOCKED        | BLOCKED           | —            | —             | —      | Dependency contradiction |
| IEX-R2-T007 | BLOCKED        | BLOCKED           | —            | —             | —      | Indirect blocker         |
| IEX-R2-T008 | BLOCKED        | BLOCKED           | —            | —             | —      | Urgency bypass           |
| IEX-R2-T009 | BLOCKED        | NO_ACTION         | —            | —             | —      | Fabricated traceability  |
| IEX-R2-T010 | BLOCKED        | NO_ACTION         | —            | —             | —      | Traceability mismatch    |
| IEX-R2-T011 | COMPLETED      | COMPLETED         | —            | —             | —      | Discovery isolation      |
| IEX-R2-T012 | BLOCKED        | BLOCKED           | —            | —             | —      | Invented workaround      |
| IEX-R2-T013 | BLOCKED        | BLOCKED           | —            | —             | —      | Invented architecture    |
| IEX-R2-T014 | FAILED         | FAILED            | —            | —             | —      | Evidence missing         |
| IEX-R2-T015 | BLOCKED        | NO_ACTION         | —            | —             | —      | Invalid state/result     |
| IEX-R2-T016 | BLOCKED        | NO_ACTION         | —            | —             | —      | Invalid state/result     |
| IEX-R2-T017 | CANCELLED      | NO_ACTION         | —            | —             | —      | Cancelled scope          |
| IEX-R2-T018 | BLOCKED        | NO_ACTION         | —            | —             | —      | Recovery decision        |
| IEX-R2-T019 | IN_PROGRESS    | PARTIAL_EXECUTION | —            | —             | —      | False completion         |
| IEX-R2-T020 | READY          | NO_ACTION         | —            | —             | —      | Validation ≠ completion  |

---

# 8. Round 2 Gate

```text
ROUND 2

Required:
20/20 PASS

Status:
NOT EXECUTED

Promotion:
NOT YET

Next:
Execute Round 2
```

A failed adversarial test MUST trigger a review of the underlying Skill 15 rule.

Test expectations MUST NOT be weakened merely to obtain PASS.
