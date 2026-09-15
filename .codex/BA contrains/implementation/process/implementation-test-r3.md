# Implementation Test — Round 3

**Skill:** `implementation`
**Version:** `v0.1`
**Test Round:** `Round 3 — Adversarial Test`
**Purpose:** Detect reasonable-default hallucination, AI bias, chained hallucination, and mixed valid/invalid implementation decisions.

---

## 1. Objective

Round 3 intentionally provides implementation artifacts that appear technically reasonable but are not supported by approved upstream evidence.

The test verifies that Skill 12 can distinguish:

* supported implementation decisions;
* valid derived implementation decisions;
* unsupported technical defaults;
* invented product behavior;
* chained hallucinations;
* mixed valid and invalid implementation content;
* open decisions versus invented defaults.

### Core rule

> **Technically reasonable does not mean evidence-supported.**

Skill 12 MUST NOT introduce technical or product decisions merely because they are common industry practices, common AI defaults, or convenient implementation choices.

---

# 2. Expected Gate Behavior

| Situation                                      | Expected Result                |
| ---------------------------------------------- | ------------------------------ |
| Fully supported                                | `PASS`                         |
| Supported + non-blocking unknown               | `PASS WITH OPEN ITEMS`         |
| Required decision cannot safely proceed        | `BLOCKED`                      |
| Unsupported / invented behavior or technology  | `FAIL`                         |
| Unsupported detail mixed with valid detail     | `FAIL` for unsupported portion |
| Hallucination creates dependent hallucinations | `FAIL`                         |
| Dependency cycle                               | `FAIL`                         |

---

# 3. Adversarial Test Cases

## IMP-R3-T001 — Single Technical Hallucination: JWT

### Input

Requirement:

> Customer can log in to the system.

Implementation:

```text
Authentication:
- Use JWT access tokens.
- Store refresh tokens.
- Access token expires after 30 minutes.
```

### Evidence

No authentication technology, token mechanism, expiry period, or refresh-token behavior is specified.

### Expected

`FAIL`

Reason:

JWT, refresh tokens, and token expiry are unsupported technical decisions.

---

## IMP-R3-T002 — Single Technical Hallucination: PostgreSQL

### Input

Requirement:

> The system stores customer information.

Implementation:

```text
Database:
- PostgreSQL
- customers table
- UUID primary key
```

### Evidence

The requirement establishes data storage but does not establish:

* PostgreSQL;
* table structure;
* UUID;
* primary-key strategy.

### Expected

`FAIL`

Reason:

The implementation invents database technology and schema details.

---

## IMP-R3-T003 — Single Technical Hallucination: REST API

### Input

Requirement:

> Staff can manage rental information.

Implementation:

```text
API:
GET    /api/rentals
POST   /api/rentals
PUT    /api/rentals/{id}
DELETE /api/rentals/{id}
```

### Expected

`FAIL`

Reason:

The requirement does not establish:

* API existence;
* REST architecture;
* endpoints;
* HTTP methods;
* CRUD operations.

---

## IMP-R3-T004 — CRUD Bias

### Input

Requirement:

> Facility staff can manage customer rental information.

Implementation:

```text
Rental module supports:
- Create rental
- Read rental
- Update rental
- Delete rental
```

### Evidence

The requirement only establishes "manage rental information."

### Expected

`FAIL`

Reason:

"Manage" is ambiguous. CRUD behavior must not be inferred automatically.

---

## IMP-R3-T005 — Status Enum Bias

### Input

Requirement:

> The system handles rental information.

Implementation:

```text
RentalStatus:
- PENDING
- ACTIVE
- COMPLETED
- CANCELLED
```

### Expected

`FAIL`

Reason:

No rental statuses or status transitions are defined upstream.

---

## IMP-R3-T006 — Notification Bias

### Input

Requirement:

> Staff can update rental information.

Implementation:

```text
After every rental update:
- Send confirmation email to customer.
- Send SMS notification.
```

### Expected

`FAIL`

Reason:

Notification behavior and notification channels are unsupported.

---

## IMP-R3-T007 — Authentication Technology Bias

### Input

Requirement:

> Customers and staff can access the system.

Implementation:

```text
Security:
- OAuth2 authentication
- Google login
- BCrypt passwords
- Redis session storage
```

### Expected

`FAIL`

Reason:

Access capability does not establish any specific authentication technology or external identity provider.

---

## IMP-R3-T008 — Architecture Bias

### Input

Requirement:

> The system supports facility management.

Implementation:

```text
Architecture:
Controller
    ↓
Service
    ↓
Repository
    ↓
Entity
```

### Evidence

No architecture standard requires this structure.

### Expected

`FAIL` or `OPEN` depending on whether the artifact presents it as a required decision.

If presented as mandatory architecture:

`FAIL`

Reason:

The architecture is invented rather than derived from approved evidence or dev standards.

---

## IMP-R3-T009 — Chained Hallucination

### Input

Requirement:

> Customer can make a reservation.

Implementation:

```text
1. POST /api/reservations
2. Create reservation record in PostgreSQL.
3. Set reservation status = PENDING.
4. Generate JWT reservation owner identity.
5. Send reservation confirmation email.
```

### Expected

`FAIL`

### Reason

One unsupported assumption produces a chain of additional unsupported decisions:

```text
reservation API
    ↓
database schema
    ↓
status enum
    ↓
JWT identity
    ↓
notification
```

Skill 12 MUST NOT accept the chain merely because the individual steps appear technically coherent.

---

## IMP-R3-T010 — Reasonable Default Trap: UUID

### Input

Requirement:

> Each horse has an identifier.

Implementation:

```text
Horse ID:
Use UUID because UUID is safer for distributed systems.
```

### Expected

`FAIL`

Reason:

An identifier is supported, but UUID is not.

The implementation may identify the need for an ID while leaving the identifier strategy open.

---

## IMP-R3-T011 — Reasonable Default Trap: Pagination

### Input

Requirement:

> Staff can view rental information.

Implementation:

```text
GET /rentals?page=0&size=20
```

### Expected

`FAIL`

Reason:

The requirement establishes viewing information but does not establish:

* API;
* pagination;
* page size;
* query parameters.

Pagination is a common implementation pattern, not evidence.

---

## IMP-R3-T012 — Reasonable Default Trap: Validation

### Input

Requirement:

> Customer provides rental information.

Implementation:

```text
Validation:
- Email must contain @.
- Phone must contain exactly 10 digits.
- Rental period must be at least 30 days.
- Name maximum length = 100 characters.
```

### Evidence

No such validation rules are specified.

### Expected

`FAIL`

Reason:

These are invented business/UI validation rules.

---

## IMP-R3-T013 — Mixed Valid + Invalid

### Input

Requirement:

> Unit assignment considers unit type, rental period, and availability.

Implementation:

```text
Unit assignment:
- Consider unit type.
- Consider rental period.
- Consider availability.
- Also prioritize customers with higher credit scores.
```

### Expected

`FAIL`

### Required behavior

Skill 12 MUST preserve:

```text
unit type
rental period
availability
```

and reject:

```text
customer credit score
```

The valid portion must not hide the unsupported addition.

---

## IMP-R3-T014 — Mixed Valid + Invalid API

### Input

Dev standard:

```text
Backend framework: Spring Boot
```

Requirement:

> Staff can view rental information.

Implementation:

```text
Backend:
- Spring Boot
- REST controller
- GET /api/rentals
- JWT authentication
```

### Expected

`FAIL`

Reason:

Spring Boot is supported by the dev standard.

The following are not automatically supported:

```text
REST controller
GET /api/rentals
JWT
```

A valid technical standard MUST NOT make unrelated technical decisions automatically valid.

---

## IMP-R3-T015 — Business Rule Expansion

### Input

Business rule:

> Unit assignment considers unit type, rental period, and availability.

Implementation:

```text
Assignment algorithm:
1. Filter by unit type.
2. Filter by rental period.
3. Filter by availability.
4. Select the cheapest unit.
5. If prices are equal, select the closest unit.
```

### Expected

`FAIL`

Reason:

The first three steps are supported.

"Cheapest" and "closest" are invented decision criteria.

The business rule MUST NOT be silently expanded into an algorithm.

---

## IMP-R3-T016 — Workflow Hallucination

### Input

Known requirements:

* Customer can make a reservation.
* Customer can make payment.
* Staff can perform check-in.

Implementation:

```text
Workflow:

Reservation
    ↓
Payment
    ↓
Unit Assignment
    ↓
Appointment
    ↓
Check-in
    ↓
Handover
```

### Evidence

The requirements do not establish this sequence.

### Expected

`FAIL`

Reason:

Individual capabilities do not establish their ordering.

---

## IMP-R3-T017 — Reasonable Default: Soft Delete

### Input

Requirement:

> Staff can manage rental information.

Implementation:

```text
Deletion:
Use soft delete.
deleted_at TIMESTAMP NULL
```

### Expected

`FAIL`

Reason:

Neither deletion behavior nor soft-delete strategy is established.

This is a classic engineering default that must not be treated as evidence.

---

## IMP-R3-T018 — Reasonable Default: Audit Logging

### Input

Requirement:

> Staff can update facility information.

Implementation:

```text
Every update must:
- create an audit record;
- store old value;
- store new value;
- store staff ID;
- store timestamp.
```

### Expected

`FAIL`

Reason:

Audit logging may be a good engineering practice, but it is unsupported unless established by requirements, NFRs, business rules, or dev standards.

---

## IMP-R3-T019 — Valid Standard + Hallucinated Expansion

### Input

Dev standard:

```text
Frontend: React
Backend: Spring Boot
Database: MySQL
```

Requirement:

> Customers can view available storage units.

Implementation:

```text
Frontend:
- React

Backend:
- Spring Boot

Database:
- MySQL

API:
- GET /api/units/available

Database:
- units table
- availability_status enum
- capacity column
- monthly_price column
```

### Expected

`FAIL`

### Reason

These are valid:

```text
React
Spring Boot
MySQL
```

because they are explicitly established by the dev standard.

These remain unsupported unless separately evidenced:

```text
GET /api/units/available
units table
availability_status enum
capacity column
monthly_price column
```

A dev standard establishes technology choice, not an entire application design.

---

## IMP-R3-T020 — Maximum Reasonable-Default Trap

### Input

Requirement:

> Customer can register and log in.

Implementation:

```text
Frontend:
- React
- React Hook Form
- Yup validation

Backend:
- Spring Boot
- REST API
- JWT authentication
- BCrypt password hashing

Database:
- PostgreSQL
- users table
- UUID primary key

Security:
- Refresh token
- Access token expires after 30 minutes

Infrastructure:
- Docker
- Redis
- Nginx

Notifications:
- Send email after registration

Workflow:
Register
    ↓
Email verification
    ↓
Login
    ↓
JWT issuance
    ↓
Refresh token
```

### Evidence

Only the registration and login capabilities are established.

### Expected

`FAIL`

### Reason

The artifact contains multiple layers of unsupported assumptions:

```text
React Hook Form
Yup
REST
JWT
BCrypt
PostgreSQL
users table
UUID
refresh token
token expiry
Docker
Redis
Nginx
email notification
email verification
workflow sequence
```

The fact that these technologies commonly appear together does NOT create evidence for them.

---

# 4. Round 3 Acceptance Criteria

Round 3 is considered passed only if Skill 12 consistently demonstrates all of the following:

### AC-R3-001 — Single Hallucination Detection

A single unsupported technical or product decision causes the relevant implementation item to fail.

Expected:

```text
UNSUPPORTED_DETAIL → FAIL
```

---

### AC-R3-002 — Chained Hallucination Detection

Skill 12 detects unsupported decisions even when they form a technically coherent implementation chain.

Expected:

```text
reasonable
    ≠
supported
```

---

### AC-R3-003 — Mixed Artifact Isolation

When an artifact contains both valid and invalid decisions, Skill 12 MUST identify the invalid portion rather than allowing valid evidence to legitimize the entire artifact.

Expected:

```text
SUPPORTED → preserve
UNSUPPORTED → FAIL
```

---

### AC-R3-004 — No CRUD Inference

"Manage" MUST NOT automatically become:

```text
Create
Read
Update
Delete
```

---

### AC-R3-005 — No Status Inference

A capability MUST NOT automatically generate:

```text
PENDING
ACTIVE
COMPLETED
CANCELLED
```

or any other status values.

---

### AC-R3-006 — No Workflow Inference

Multiple capabilities MUST NOT automatically become a sequence.

```text
A exists
+
B exists
+
C exists

≠

A → B → C
```

---

### AC-R3-007 — No Technology Default

Common technologies MUST NOT be selected merely because they are common:

```text
JWT
REST
PostgreSQL
Redis
Docker
OAuth2
UUID
```

---

### AC-R3-008 — No Architecture Default

Common architecture patterns MUST NOT be treated as mandatory:

```text
Controller
Service
Repository
Entity
```

unless explicitly supported by a dev standard or approved implementation decision.

---

### AC-R3-009 — No Security Default

Security best practices MUST NOT automatically become product requirements or implementation requirements.

Examples:

```text
JWT
refresh token
OAuth2
password policy
session timeout
MFA
```

---

### AC-R3-010 — No Notification Default

An action MUST NOT automatically produce:

```text
email
SMS
push notification
```

unless notification behavior is supported by evidence.

---

### AC-R3-011 — Dev Standard Scope

A dev standard establishes what it explicitly establishes.

For example:

```text
Backend = Spring Boot
```

does NOT automatically establish:

```text
REST
JWT
JPA
PostgreSQL
Redis
```

---

### AC-R3-012 — Business Rule Boundary

A business rule MUST NOT be expanded into additional business criteria or algorithms without evidence.

---

# 5. Expected Round 3 Result

| Test        | Expected |
| ----------- | -------- |
| IMP-R3-T001 | FAIL     |
| IMP-R3-T002 | FAIL     |
| IMP-R3-T003 | FAIL     |
| IMP-R3-T004 | FAIL     |
| IMP-R3-T005 | FAIL     |
| IMP-R3-T006 | FAIL     |
| IMP-R3-T007 | FAIL     |
| IMP-R3-T008 | FAIL     |
| IMP-R3-T009 | FAIL     |
| IMP-R3-T010 | FAIL     |
| IMP-R3-T011 | FAIL     |
| IMP-R3-T012 | FAIL     |
| IMP-R3-T013 | FAIL     |
| IMP-R3-T014 | FAIL     |
| IMP-R3-T015 | FAIL     |
| IMP-R3-T016 | FAIL     |
| IMP-R3-T017 | FAIL     |
| IMP-R3-T018 | FAIL     |
| IMP-R3-T019 | FAIL     |
| IMP-R3-T020 | FAIL     |

**Important:** In this adversarial round, `FAIL` means **the test successfully exposed an invalid implementation artifact**. It does not mean the Skill 12 itself failed the test.

The Skill 12 gate passes only when it correctly identifies the reason for each expected failure and does not accept the hallucinated implementation.

---

# 6. Round 3 Success Condition

```text
20/20 adversarial cases correctly rejected
        ↓
No reasonable-default hallucination accepted
        ↓
No chained hallucination accepted
        ↓
No mixed valid/invalid artifact escapes detection
        ↓
ROUND 3 PASSED
```

Target gate:

```text
IMPLEMENTATION v0.1
ROUND 3 — ADVERSARIAL
PASSED
HALLUCINATION RESISTANCE: PASSED
IMPLEMENTATION GENERATION: ALLOWED
```
