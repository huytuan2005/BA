# Skill 14 — Implementation Plan Validator

# `implementation-plan-validator-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 1`
**Total Test Cases:** `20`

---

## 1. Objective

Validate that Skill 14 correctly validates an implementation plan against:

* approved implementation scope;
* traceability;
* dependency rules;
* dependency graph;
* blocker propagation;
* OPEN vs BLOCKED;
* planning status;
* technical decision boundaries;
* architecture boundaries;
* scope boundaries;
* validator non-interference;
* execution gate.

Round 1 focuses on baseline correctness.

It does not yet attempt maximum adversarial pressure. Those cases belong to Round 2 and Round 3.

---

## 2. Expected Decision Model

Skill 14 MUST:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

It MUST report problems rather than silently repair them.

For every test:

```text
Expected Result = validator decision
Actual Result   = observed validator decision
```

A test passes only when:

```text
Expected Result == Actual Result
```

---

# 3. Round 1 Test Cases

## IPV-R1-T001 — Valid Fully Traceable Plan

### Scenario

Approved implementation:

```text
IMP-001 — Implement customer profile capability
IMP-002 — Implement approved authentication capability
```

Plan:

```text
IP-001 — Implement customer profile capability
Traceability: IMP-001
Evidence: IMPLEMENTATION
Dependencies: None

IP-002 — Implement approved authentication capability
Traceability: IMP-002
Evidence: IMPLEMENTATION
Dependencies: None
```

### Expected

```text
PASS
```

### Acceptance Criteria

* every plan item has valid traceability;
* no unsupported scope;
* no invalid dependency;
* no blocker;
* no contradiction.

---

## IP- R1-T002 — Orphan Plan Item

### Scenario

Approved implementation:

```text
IMP-001 — Implement customer profile capability
```

Plan contains:

```text
IP-001 — Implement customer profile capability
Traceability: IMP-001

IP-002 — Add analytics dashboard
Traceability: None
```

### Expected

```text
FAIL
ORPHAN_PLAN_ITEM
```

### Acceptance Criteria

The validator detects `IP-002` as unsupported/orphaned.

---

## IPV-R1-T003 — Valid One-to-Many Traceability

### Scenario

Approved implementation:

```text
IMP-001 — Implement authentication capability
```

Plan:

```text
IP-001 — Prepare authentication boundary
Traceability: IMP-001

IP-002 — Implement authentication capability
Traceability: IMP-001

IP-003 — Validate approved authentication integration
Traceability: IMP-001
```

### Expected

```text
PASS
```

### Acceptance Criteria

One implementation item may map to multiple plan items when each task remains within approved scope.

---

## IPV-R1-T004 — Valid Many-to-One Traceability

### Scenario

Approved implementation:

```text
IMP-001 — Customer profile capability
IMP-002 — Customer account capability
```

Plan:

```text
IP-001 — Implement approved customer account/profile capability

Traceability:
IMP-001
IMP-002
```

### Expected

```text
PASS
```

### Acceptance Criteria

Many approved implementation items may map to one plan item when the mapping is explicit and supported.

---

## IPV-R1-T005 — Invalid Trace to Unsupported Source

### Scenario

Plan:

```text
IP-001 — Implement payment provider integration
Traceability: BR-001
```

But `BR-001` only says:

```text
Rental policies cover payments.
```

It does not approve a payment provider integration.

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

A syntactically valid trace is insufficient when the cited evidence does not support the actual task.

---

## IPV-R1-T006 — Valid Dependency

### Scenario

Plan:

```text
IP-001 — Prepare approved data access component

IP-002 — Implement approved service
Dependencies:
IP-001
```

Approved implementation explicitly requires the data access component before the service.

### Expected

```text
PASS
```

### Acceptance Criteria

The dependency represents a real implementation prerequisite.

---

## IPV-R1-T007 — Invented Dependency

### Scenario

Plan:

```text
IP-001 — Implement customer profile

IP-002 — Implement activity log

Dependencies:
IP-002 depends on IP-001
```

Approved scope establishes both capabilities but no prerequisite between them.

### Expected

```text
FAIL
INVENTED_DEPENDENCY
```

### Acceptance Criteria

Conceptual relationship alone does not justify dependency.

---

## IPV-R1-T008 — Valid Dependency Graph

### Scenario

```text
IP-001
   ↓
IP-002
   ↓
IP-003
```

No cycles or broken references exist.

### Expected

```text
PASS
```

### Acceptance Criteria

The graph is acyclic and every dependency references an existing plan item.

---

## IPV-R1-T009 — Dependency Cycle

### Scenario

```text
IP-001 → IP-002
IP-002 → IP-003
IP-003 → IP-001
```

### Expected

```text
FAIL
DEPENDENCY_CYCLE
```

### Acceptance Criteria

The validator detects the cycle globally.

---

## IPV-R1-T010 — Broken Dependency Reference

### Scenario

```text
IP-005 depends on IP-999
```

but `IP-999` does not exist.

### Expected

```text
FAIL
BROKEN_DEPENDENCY_REFERENCE
```

### Acceptance Criteria

The validator MUST NOT accept a dependency pointing to a nonexistent task.

---

## IPV-R1-T011 — Self Dependency

### Scenario

```text
IP-004 depends on IP-004
```

### Expected

```text
FAIL
INVALID_SELF_DEPENDENCY
```

### Acceptance Criteria

Self-dependency is always invalid.

---

## IPV-R1-T012 — Correct Blocker Propagation

### Scenario

```text
IP-001 = BLOCKED

IP-002 depends on IP-001

IP-003 is independent
```

### Expected

```text
IP-001 BLOCKED
IP-002 BLOCKED
IP-003 READY
```

### Acceptance Criteria

The blocker propagates only through dependency edges.

---

## IPV-R1-T013 — Invalid Blocker Propagation

### Scenario

```text
IP-001 = BLOCKED

IP-002 depends on IP-001

IP-003 independent
```

Plan declares:

```text
IP-003 = BLOCKED
```

### Expected

```text
FAIL
INVALID_BLOCKER_PROPAGATION
```

### Acceptance Criteria

The validator detects the unrelated blocker.

---

## IPV-R1-T014 — Valid READY WITH OPEN ITEMS

### Scenario

Plan:

```text
IP-005 — Prepare approved report integration boundary

Status:
READY WITH OPEN ITEMS

Open item:
Exact export format is not yet decided.
```

Approved scope allows preparation without defining the format.

### Expected

```text
PASS WITH OPEN ITEMS
```

### Acceptance Criteria

The unresolved detail is non-blocking.

---

## IPV-R1-T015 — OPEN Incorrectly Hiding a Blocker

### Scenario

Plan:

```text
IP-006 — Implement payment integration

Status:
READY WITH OPEN ITEMS

Open item:
Payment provider is not decided.

Implementation cannot proceed without the provider decision.
```

### Expected

```text
FAIL
```

or validation result identifying:

```text
INVALID_OPEN_BLOCKED_CLASSIFICATION
```

### Acceptance Criteria

The validator recognizes that the unresolved decision is blocking.

---

## IPV-R1-T016 — Valid Plan Status

### Scenario

A plan item has:

```text
Status:
READY
```

### Expected

```text
PASS
```

### Acceptance Criteria

`READY` is a valid implementation-task status.

---

## IPV-R1-T017 — Business Status Misused as Plan Status

### Scenario

Plan item:

```text
IP-003 — Implement rental capability

Status:
PENDING
```

No explicit definition says `PENDING` is a plan-task status.

### Expected

```text
FAIL
```

### Acceptance Criteria

The validator rejects unsupported business/domain status used as task state.

---

## IPV-R1-T018 — Unsupported Technology

### Scenario

Approved implementation only states:

```text
Customer profile capability
```

Plan says:

```text
IP-001 — Implement customer profile using Redis
```

No approved implementation, developer decision, or dev standard establishes Redis.

### Expected

```text
FAIL
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

Common technology is not accepted as evidence.

---

## IPV-R1-T019 — Unsupported Architecture

### Scenario

Approved implementation:

```text
Customer profile capability
```

Plan says:

```text
IP-001 — Implement CustomerController
IP-002 — Implement CustomerService
IP-003 — Implement CustomerRepository
```

No approved source establishes this architecture.

### Expected

```text
FAIL
INVENTED_ARCHITECTURE
```

### Acceptance Criteria

The validator detects architecture invention.

---

## IPV-R1-T020 — Validator Must Not Silently Repair

### Scenario

Plan contains:

```text
IP-001 — Implement customer profile
Traceability: None

IP-002 — Implement activity log
Dependencies:
IP-002 depends on IP-001
```

The validator could theoretically guess:

* missing trace for IP-001;
* whether IP-002 really depends on IP-001.

### Expected

```text
FAIL
```

with findings such as:

```text
ORPHAN_PLAN_ITEM
INVENTED_DEPENDENCY
```

The validator MUST NOT:

```text
add traceability
remove dependency
invent a replacement dependency
change status
rewrite the plan
```

### Acceptance Criteria

The validator reports the defects without modifying the supplied plan.

---

# 4. Round 1 Acceptance Gate

Round 1 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 silently repaired defects

0 false PASS for unsupported work

0 missed orphan plan items

0 missed invalid dependencies

0 missed dependency cycles

0 missed blocker propagation errors
```

AND:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

are correctly distinguished.

---

# 5. Round 1 Execution Record

To be completed after execution:

| Test ID     | Expected             | Actual | Result | Notes |
| ----------- | -------------------- | ------ | ------ | ----- |
| IPV-R1-T001 | PASS                 | —      | —      | —     |
| IPV-R1-T002 | FAIL                 | —      | —      | —     |
| IPV-R1-T003 | PASS                 | —      | —      | —     |
| IPV-R1-T004 | PASS                 | —      | —      | —     |
| IPV-R1-T005 | FAIL                 | —      | —      | —     |
| IPV-R1-T006 | PASS                 | —      | —      | —     |
| IPV-R1-T007 | FAIL                 | —      | —      | —     |
| IPV-R1-T008 | PASS                 | —      | —      | —     |
| IPV-R1-T009 | FAIL                 | —      | —      | —     |
| IPV-R1-T010 | FAIL                 | —      | —      | —     |
| IPV-R1-T011 | FAIL                 | —      | —      | —     |
| IPV-R1-T012 | PASS                 | —      | —      | —     |
| IPV-R1-T013 | FAIL                 | —      | —      | —     |
| IPV-R1-T014 | PASS WITH OPEN ITEMS | —      | —      | —     |
| IPV-R1-T015 | FAIL                 | —      | —      | —     |
| IPV-R1-T016 | PASS                 | —      | —      | —     |
| IPV-R1-T017 | FAIL                 | —      | —      | —     |
| IPV-R1-T018 | FAIL                 | —      | —      | —     |
| IPV-R1-T019 | FAIL                 | —      | —      | —     |
| IPV-R1-T020 | FAIL                 | —      | —      | —     |

---

# 6. Round 1 Gate

```text
ROUND 1

Required:
20/20 PASS

Promotion:
NOT YET

Next:
Round 2
```

A failed test MUST trigger:

```text
identify design gap
        ↓
revise implementation-plan-validator/SKILL.md
        ↓
rerun affected tests
        ↓
rerun regression before promotion
```

Test expectations MUST NOT be weakened merely to obtain PASS.
