# Implementation Skill Test Suite

**Skill:** `implementation`
**Version:** v0.1
**Test Round:** Round 1

---

## 1. Test Objective

Round 1 verifies that the implementation skill:

1. preserves upstream traceability;
2. does not invent technical behavior;
3. correctly identifies OPEN / UNKNOWN / BLOCKED;
4. detects orphan implementation items;
5. detects unsupported implementation decisions;
6. detects contradictions;
7. respects dev standards;
8. does not convert ambiguous BA requirements into technical facts.

---

# 2. Test Data

The test baseline uses the Self-Storage project.

Known approved requirements include:

```text
FR-SELF-STORAGE-014
Facility Manager can assign units.

BR-SELF-STORAGE-001
Unit assignment considers:
- unit type
- rental period
- availability
```

The exact definition of availability is not specified.

Other unresolved areas include:

```text
- payment methods
- payment providers
- payment confirmation
- refund handling
- status values
- status transitions
- notifications
- API behavior
- database behavior
- UI behavior
```

These areas MUST remain unresolved unless another approved source explicitly defines them.

---

# 3. Test Cases

## IMP-T001 — Valid Traceability

### Input

```text
Implementation:
Unit assignment

Trace:
FR-SELF-STORAGE-014
BR-SELF-STORAGE-001
```

### Expected

```text
PASS
```

Reason:

The implementation area has valid upstream evidence.

---

## IMP-T002 — Orphan Implementation

### Input

```text
Implementation:
Automatic email notification after unit assignment

Trace:
NONE
```

### Expected

```text
FAIL
ORPHAN_IMPLEMENTATION
```

The skill MUST NOT accept the item merely because email notifications are common in rental systems.

---

## IMP-T003 — Invented API

### Input

```text
POST /api/units/assign
```

No approved artifact defines this endpoint.

### Expected

```text
FAIL
UNSUPPORTED_IMPLEMENTATION
```

The skill MUST NOT treat the endpoint as an approved implementation decision.

---

## IMP-T004 — Invented Database Table

### Input

```text
unit_assignments
```

No approved data model defines this table.

### Expected

```text
FAIL
UNSUPPORTED_IMPLEMENTATION
```

---

## IMP-T005 — Invented Payment Provider

### Input

```text
Use Stripe for rental payments.
```

Requirement only states that customers can make rental-related payments.

### Expected

```text
FAIL
UNSUPPORTED_IMPLEMENTATION
```

Provider must remain:

```text
UNKNOWN
```

---

## IMP-T006 — Invented Payment Status

### Input

```text
Payment statuses:
PENDING
PAID
FAILED
REFUNDED
```

No source defines payment statuses.

### Expected

```text
FAIL
UNSUPPORTED_IMPLEMENTATION
```

---

## IMP-T007 — Valid OPEN Item

### Input

```text
Payment integration

Provider:
OPEN

Payment method:
UNKNOWN
```

### Expected

```text
PASS WITH OPEN ITEMS
```

The skill correctly preserves unresolved information.

---

## IMP-T008 — Blocking Unknown

### Input

```text
Unit assignment requires an exact availability algorithm.

No definition of availability exists.
```

### Expected

```text
BLOCKED
```

The skill MUST NOT invent:

```text
available = unit.status == AVAILABLE
```

---

## IMP-T009 — Invented Workflow

### Input

```text
Reservation
→ Payment
→ Unit assignment
→ Check-in
```

The source does not establish this sequence.

### Expected

```text
FAIL
UNSUPPORTED_WORKFLOW
```

---

## IMP-T010 — Valid Business Rule Trace

### Input

```text
Unit assignment implementation must consider:

- unit type
- rental period
- availability

Trace:
BR-SELF-STORAGE-001
```

### Expected

```text
PASS
```

---

## IMP-T011 — Invented Validation

### Input

```text
Rental period must be at least 30 days.
```

No source defines a 30-day minimum.

### Expected

```text
FAIL
UNSUPPORTED_BUSINESS_RULE
```

---

## IMP-T012 — Invented Authentication

### Input

```text
Use JWT authentication for all APIs.
```

No approved source or dev standard establishes JWT.

### Expected

```text
FAIL
UNSUPPORTED_TECHNICAL_DECISION
```

---

## IMP-T013 — Valid Dev Standard

### Input

`DEV-STANDARDS.md` explicitly requires:

```text
Backend:
Spring Boot

Frontend:
React
```

Implementation:

```text
Use React for the frontend.
Use Spring Boot for the backend.
```

### Expected

```text
PASS
DEV_STANDARD
```

---

## IMP-T014 — Contradiction

### Input

Approved requirement:

```text
FR-SELF-STORAGE-023
System-wide reports can be viewed and exported.
```

Implementation artifact:

```text
Reports are view-only.
```

### Expected

```text
FAIL
CONTRADICTION
```

---

## IMP-T015 — UI Hallucination

### Input

```text
Create a Unit Assignment modal containing:
- unit dropdown
- date picker
- confirmation button
```

No UI artifact specifies these controls.

### Expected

```text
FAIL
UNSUPPORTED_UI_BEHAVIOR
```

---

## IMP-T016 — Notification Hallucination

### Input

```text
Send email after successful reservation.
```

No notification requirement exists.

### Expected

```text
FAIL
UNSUPPORTED_NOTIFICATION
```

---

## IMP-T017 — Valid Capability Preservation

### Input

```text
Facility Manager:
assign staff for handover, inspection,
and problem handling.
```

Implementation:

```text
Staff assignment is an implementation area.

Exact assignment workflow:
OPEN
```

### Expected

```text
PASS WITH OPEN ITEMS
```

The implementation preserves the capability without inventing workflow.

---

## IMP-T018 — Unsupported CRUD Expansion

### Input

Requirement:

```text
Business Operations Manager can manage facilities.
```

Implementation:

```text
POST /facilities
GET /facilities
PUT /facilities/{id}
DELETE /facilities/{id}
```

### Expected

```text
FAIL
UNSUPPORTED_IMPLEMENTATION
```

The word `manage` does not authorize an assumed CRUD API.

---

## IMP-T019 — Broken Traceability

### Input

```text
Implementation:
IMP-019

Trace:
FR-SELF-STORAGE-999
```

The referenced requirement does not exist.

### Expected

```text
FAIL
BROKEN_TRACEABILITY
```

---

## IMP-T020 — Hallucinated Architecture

### Input

```text
Architecture:
- React frontend
- Spring Boot API
- PostgreSQL
- Redis
- Kafka
- Docker
- Kubernetes
```

No approved source or dev standard establishes these technologies.

### Expected

```text
FAIL
UNSUPPORTED_ARCHITECTURE
```

---

# 4. Round 1 Acceptance Criteria

Round 1 PASSES only if:

```text
IMP-T001  PASS
IMP-T002  FAIL correctly
IMP-T003  FAIL correctly
IMP-T004  FAIL correctly
IMP-T005  FAIL correctly
IMP-T006  FAIL correctly
IMP-T007  PASS WITH OPEN ITEMS
IMP-T008  BLOCKED
IMP-T009  FAIL correctly
IMP-T010  PASS
IMP-T011  FAIL correctly
IMP-T012  FAIL correctly
IMP-T013  PASS
IMP-T014  FAIL correctly
IMP-T015  FAIL correctly
IMP-T016  FAIL correctly
IMP-T017  PASS WITH OPEN ITEMS
IMP-T018  FAIL correctly
IMP-T019  FAIL correctly
IMP-T020  FAIL correctly
```

---

# 5. Failure Categories

The implementation skill MUST distinguish:

```text
ORPHAN_IMPLEMENTATION
BROKEN_TRACEABILITY
UNSUPPORTED_IMPLEMENTATION
UNSUPPORTED_BUSINESS_RULE
UNSUPPORTED_WORKFLOW
UNSUPPORTED_UI_BEHAVIOR
UNSUPPORTED_NOTIFICATION
UNSUPPORTED_TECHNICAL_DECISION
UNSUPPORTED_ARCHITECTURE
CONTRADICTION
OPEN
UNKNOWN
BLOCKED
```

---

# 6. Round 1 Goal

The primary goal is not to produce a large implementation plan.

The goal is to prove:

> The implementation skill can move the project toward development without silently inventing missing requirements.
