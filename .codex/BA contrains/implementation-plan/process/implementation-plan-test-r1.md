# Implementation Plan Test — Round 1

**Skill:** `implementation-plan`
**Version:** `v0.1`
**Round:** `Round 1`

## Objective

Validate:

* plan traceability;
* task decomposition;
* implementation dependency handling;
* blocker propagation;
* open-item handling;
* scope preservation;
* no business-workflow invention;
* no technical hallucination;
* no architecture inflation.

---

## IP-T001 — Valid Plan Item

Implementation:

```text
IMP-001 — Authentication capability
```

Plan:

```text
IP-001 — Implement approved authentication capability
Trace: IMP-001
```

Expected:

`PASS`

---

## IP-T002 — Orphan Plan Item

Plan:

```text
IP-002 — Add dashboard analytics
```

No implementation or upstream artifact supports analytics.

Expected:

`FAIL / ORPHAN_PLAN_ITEM`

---

## IP-T003 — One Implementation → Multiple Plan Items

```text
IMP-002 — Rental management
```

Plan:

```text
IP-003 — Prepare rental management component
IP-004 — Integrate approved rental management capability
```

Both trace to `IMP-002`.

Expected:

`PASS`

---

## IP-T004 — Multiple Implementation → One Plan Item

```text
IMP-003 — Role management
IMP-004 — Facility access configuration
```

Plan:

```text
IP-005 — Implement approved access-management scope
```

Both traces are retained.

Expected:

`PASS`

---

## IP-T005 — Invented CRUD

Implementation:

```text
IMP-005 — Manage rental information
```

Plan:

```text
IP-006 — Create rental API
IP-007 — Read rental API
IP-008 — Update rental API
IP-009 — Delete rental API
```

Expected:

`FAIL`

Reason:

The plan expanded ambiguous scope into CRUD/API work.

---

## IP-T006 — Valid Implementation Dependency

```text
IP-010 — Implement approved service
IP-011 — Integrate approved UI with service
```

`IP-011 depends on IP-010`.

Expected:

`PASS`

---

## IP-T007 — False Dependency

```text
IP-012 — Implement report viewing
IP-013 — Implement profile display
```

No dependency exists.

Expected:

`PASS`

Both remain independently executable.

---

## IP-T008 — Dependency Cycle

```text
IP-014 → IP-015
IP-015 → IP-016
IP-016 → IP-014
```

Expected:

`FAIL / DEPENDENCY_CYCLE`

---

## IP-T009 — Blocker Propagation

```text
IP-017 = BLOCKED
IP-018 depends on IP-017
IP-019 independent
```

Expected:

```text
IP-017 = BLOCKED
IP-018 = BLOCKED
IP-019 = READY
```

---

## IP-T010 — Non-Blocking Open Item

```text
Requirement:
Report export is supported.

Unknown:
Exact export format.
```

Plan:

```text
IP-020 — Prepare report export capability
```

Expected:

`READY WITH OPEN ITEMS`

Do not invent CSV, Excel, or PDF.

---

## IP-T011 — Blocking Unknown

```text
IP-021 — Implement unit assignment

Dependency:
Unit availability definition is unresolved and required.
```

Expected:

`BLOCKED`

---

## IP-T012 — Business Workflow Disguised as Plan

```text
IP-022 Reservation
   ↓
IP-023 Payment
   ↓
IP-024 Check-in
```

No approved product sequence exists.

Expected:

`FAIL`

Reason:

Implementation order is incorrectly being used to create a business workflow.

---

## IP-T013 — Valid Technical Ordering

```text
IP-025 Prepare approved backend component
   ↓
IP-026 Integrate approved frontend component
```

The dependency is technical and supported.

Expected:

`PASS`

---

## IP-T014 — JWT Hallucination

Requirement:

```text
Customer can log in.
```

Plan:

```text
IP-027 Implement JWT authentication
```

No approved technical decision exists.

Expected:

`FAIL`

---

## IP-T015 — Dev Standard Technology

Dev standard:

```text
Frontend = React
```

Plan:

```text
IP-028 Implement approved frontend scope using React
```

Expected:

`PASS / DEV_STANDARD`

---

## IP-T016 — Standard Scope Inflation

Dev standard:

```text
Frontend = React
```

Plan:

```text
IP-029 Setup Redux
IP-030 Setup React Query
IP-031 Setup Tailwind
```

None are explicitly required.

Expected:

`FAIL`

---

## IP-T017 — Valid Split Without Lost Traceability

Implementation:

```text
IMP-006 — Login history and activity logging
```

Plan:

```text
IP-032 Implement login-history capability
IP-033 Implement activity-log capability
```

Both retain `IMP-006`.

Expected:

`PASS`

---

## IP-T018 — Invented Infrastructure

Approved implementation:

```text
Authentication capability only.
```

Plan:

```text
IP-034 Configure Docker
IP-035 Configure Kubernetes
IP-036 Configure CI/CD
```

No infrastructure requirement or standard exists.

Expected:

`FAIL`

---

## IP-T019 — Minimal Plan

Approved implementation contains only:

```text
Profile viewing
```

Plan:

```text
IP-037 Implement approved profile viewing
```

No unnecessary supporting tasks.

Expected:

`PASS`

---

## IP-T020 — Plan Status vs Business Status

Plan:

```text
IP-038 status = IN PROGRESS
```

This is task state.

Expected:

`PASS`

But:

```text
Rental.status = IN PROGRESS
```

would require business evidence and MUST NOT be inferred from plan status.

Expected:

`FAIL`

---

# Round 1 Acceptance Criteria

| Criterion                   | Required |
| --------------------------- | -------- |
| Traceable plan items        | 100%     |
| Unsupported plan items      | 0        |
| Broken dependencies         | 0        |
| Dependency cycles           | 0        |
| Invented business workflow  | 0        |
| Invented technology         | 0        |
| Invented architecture       | 0        |
| Scope inflation             | 0        |
| Correct blocker propagation | 100%     |
| Open ≠ automatic blocker    | 100%     |

Target:

```text
IMPLEMENTATION PLAN v0.1
ROUND 1
20/20 PASSED
```
