# Skill: implementation

**Version:** `v1.0`
**Status:** `LOCKED`
**Purpose:** Convert approved BA artifacts into implementation-oriented outputs without inventing unsupported product behavior, business rules, or technical decisions.

---

## 1. Purpose

This skill transforms approved upstream artifacts into implementation-oriented guidance while preserving evidence boundaries.

The skill answers:

> What is approved to implement, what is still open, what is blocked, and what implementation decisions are supported?

It does not automatically decide technical details merely because they are common, convenient, or industry-standard.

### Core principle

> **Implementation may choose HOW only when upstream artifacts establish WHAT, or an applicable development standard explicitly establishes HOW.**

---

## 2. Inputs

The skill may consume:

- approved functional requirements;
- business rules;
- NFRs;
- process models;
- actors and permissions;
- approved blueprint;
- implementation-readiness result;
- applicable `dev-standards/DEV-STANDARDS.md`;
- approved implementation decisions.

Implementation MUST NOT treat unsupported information as an implicit input.

---

## 3. Evidence Classification

Every implementation decision MUST have an evidence classification.

| Classification | Meaning |
|---|---|
| `SOURCE_STATED` | Explicitly stated by an approved upstream artifact |
| `DERIVED` | Directly and safely derived from approved evidence |
| `DEV_STANDARD` | Explicitly established by an applicable development standard |
| `OPEN` | Required information is not yet decided |
| `UNKNOWN` | Information is unavailable or undefined |
| `BLOCKED` | Missing or conflicting information prevents safe implementation |
| `CONTRADICTION` | Applicable sources contain unresolved conflicting decisions |

---

## 4. Evidence-First Rule

A technical decision MUST NOT be accepted only because it is:

- common;
- recommended;
- conventional;
- widely used;
- easier to implement;
- preferred by the developer;
- a common AI-generated default.

Examples that MUST NOT be invented without evidence:

```text
JWT
OAuth2
REST
GraphQL
PostgreSQL
MySQL
Redis
Docker
Kubernetes
UUID
CRUD
soft delete
audit logging
pagination
status enums
email notification
SMS notification
refresh tokens
session timeout
```

A reasonable technical default is still an unsupported decision unless established by evidence or an applicable development standard.

---

## 5. Dev Standards

`dev-standards/DEV-STANDARDS.md` may establish technical implementation choices.

A development standard is authoritative only within its applicable scope.

A standard establishes **what it explicitly states**, not unrelated technical details.

Example:

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
Docker
```

---

## 6. Dev Standards Inheritance and Precedence

 Skill 12 MUST resolve applicability and precedence explicitly.

### 6.1 Standard scopes

Supported scopes are:

```text
Global / Default
    ↓
Root / Organization
    ↓
Project
    ↓
Project-specific implementation scope
```

A more specific scope MAY override a less specific scope **only when that precedence rule is explicitly established by the development-standard system**.

The skill MUST NOT invent precedence merely from file location, naming, or perceived specificity.

### 6.2 Inheritance

When a child scope does not define a value, the applicable parent value is inherited.

Example:

```text
Root:
Frontend = React
Backend = Spring Boot

Project:
Backend = NestJS
```

Effective values:

```text
Frontend = React
Backend = NestJS
```

### 6.3 Explicit override

A project-level standard can override a root-level standard only when project scope is defined as higher precedence by the governing standard policy.

Example:

```text
Root:
Backend = Spring Boot

Project:
Backend = NestJS

Precedence:
Project overrides Root
```

Result:

```text
Backend = NestJS
```

Evidence classification:

```text
DEV_STANDARD
```

### 6.4 Conflicting standards without precedence

If applicable standards conflict and no precedence rule exists, Skill 12 MUST NOT silently select either technology.

Expected result:

```text
BLOCKED
```

or:

```text
CONTRADICTION
```

depending on whether the conflict prevents implementation.

### 6.5 Standard scope does not expand automatically

Even when a standard resolves a technology, it MUST NOT create additional application behavior.

Example:

```text
Backend = Spring Boot
```

does not automatically imply:

```text
REST API
JPA
JWT
Controller-Service-Repository
PostgreSQL
```

Each additional decision requires its own evidence.

---

## 7. Implementation Rule

Implementation areas are categories, not requirements.

Examples:

```text
Authentication
Authorization
Data persistence
API layer
UI layer
Logging
Validation
Deployment
Notifications
```

Mentioning an implementation area does not authorize invention of its concrete technology or behavior.

---

## 8. Technical Decision Rule

A technical decision is valid only when at least one of the following is true:

### A. Explicit upstream evidence

Example:

```text
Database = MySQL
```

Result:

```text
DEV_STANDARD
```

### B. Safe derivation

Example:

```text
Requirement:
Customer can log in.

Derived:
Authentication capability is required.
```

Result:

```text
DERIVED
```

But:

```text
Customer can log in
→ JWT required
```

is NOT a valid derivation unless separately supported.

### C. Approved implementation decision

An already-approved implementation decision may be reused without re-inventing it.

---

## 9. Unsupported Decisions

If implementation introduces behavior or technology without evidence, mark it as unsupported.

Examples:

```text
UNSUPPORTED_TECHNICAL_DECISION
UNSUPPORTED_BUSINESS_RULE
UNSUPPORTED_WORKFLOW
UNSUPPORTED_STATUS
UNSUPPORTED_API
UNSUPPORTED_SCHEMA
UNSUPPORTED_NOTIFICATION
UNSUPPORTED_SECURITY
UNSUPPORTED_UI_BEHAVIOR
UNSUPPORTED_ARCHITECTURE
```

Unsupported implementation content causes `FAIL` for the affected implementation item.

---

## 10. Partial Implementation

One implementation item may contain both supported and unsupported content.

Example:

```text
Unit assignment:
- unit type        ← supported
- rental period    ← supported
- availability     ← supported
- customer score   ← unsupported
```

Expected behavior:

```text
Supported content → preserve
Unsupported content → reject
Overall item → FAIL
```

Valid evidence MUST NOT hide unsupported additions.

---

## 11. Open vs Blocked

`OPEN` does not automatically mean `BLOCKED`.

### `PASS WITH OPEN ITEMS`

Use when the unresolved decision does not prevent safe implementation of the current item.

Example:

```text
Report export is required.
Exact export format is unknown.
```

Result:

```text
PASS WITH OPEN ITEMS
```

### `BLOCKED`

Use when implementation depends on an unresolved decision and proceeding would require invention.

Example:

```text
Unit assignment depends on an undefined unit-status model.
```

Result:

```text
BLOCKED
```

---

## 12. Dependency Rules

Implementation dependencies MUST be explicit.

If:

```text
IMP-003
   ↓ depends on
IMP-002
   ↓ depends on
IMP-001
```

and `IMP-001` is blocked, dependent implementation may also become blocked.

Unrelated implementation items MUST NOT inherit the block.

Dependency cycles are invalid:

```text
IMP-001 → IMP-002 → IMP-003 → IMP-001
```

Result:

```text
FAIL
DEPENDENCY_CYCLE
```

---

## 13. Traceability

Every implementation item MUST trace to one or more approved upstream artifacts or applicable development standards.

Valid patterns include:

```text
one requirement → many implementation items
many requirements → one implementation item
many requirements ↔ many implementation items
```

Missing trace:

```text
ORPHAN_IMPLEMENTATION
```

Result:

```text
FAIL
```

A trace to a valid requirement does not legitimize unrelated invented behavior.

---

## 14. Prohibited Inference

Skill 12 MUST NOT infer:

### API

```text
endpoint
HTTP method
request schema
response schema
status code
```

### Database

```text
table
column
primary key
foreign key
index
database engine
```

### Authentication / Security

```text
JWT
OAuth2
refresh token
session timeout
MFA
password policy
```

### Workflow

```text
A → B → C
```

unless the ordering is established.

### Status

```text
PENDING
ACTIVE
COMPLETED
CANCELLED
```

unless established.

### Product behavior

```text
CRUD
soft delete
pagination
automatic assignment
automatic notification
```

unless established.

### Architecture

```text
Controller
Service
Repository
Entity
microservice
event-driven architecture
```

unless supported by an applicable standard or approved decision.

---

## 15. Business Rule Boundary

A business rule may constrain implementation but MUST NOT be silently expanded.

Example:

```text
Unit assignment considers:
- unit type
- rental period
- availability
```

does not authorize:

```text
cheapest unit
nearest unit
customer credit score
priority customer
```

unless separately supported.

---

## 16. Hallucination Detection

The skill MUST detect:

```text
invented endpoint
invented database
invented field
invented API response
invented status
invented workflow
invented payment provider
invented notification channel
invented authentication mechanism
invented UI behavior
invented deployment architecture
invented business calculation
```

A coherent technical chain is still invalid if its root decision lacks evidence.

---

## 17. Minimal Implementation Principle

Prefer the smallest implementation that satisfies approved evidence.

Do not introduce:

```text
microservices
extra abstractions
speculative integrations
unnecessary database normalization
extra CRUD operations
extra notifications
extra infrastructure
extra security mechanisms
```

merely because they are considered best practice.

---

## 18. Quality Gate

Possible results:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

### PASS

All implementation decisions are evidence-supported.

### PASS WITH OPEN ITEMS

Supported implementation can proceed, but non-blocking decisions remain open.

### BLOCKED

Required unresolved information prevents safe implementation.

### FAIL

Implementation contains unsupported, invented, contradictory, or orphan decisions.

---

## 19. Developer Boundary

Skill 12 defines:

- what is approved;
- what is supported;
- what may safely be implemented;
- what remains open;
- what blocks implementation.

The developer decides HOW unless:

- upstream evidence explicitly specifies the technical choice;
- `DEV-STANDARDS.md` explicitly specifies the technical choice;
- an approved implementation decision already establishes it.

---

## 20. Validation Contract

Skill 12 MUST pass all validation rounds before promotion.

```text
Round 1
Structural + traceability validation
        ↓
Round 2
Dependency + standards + partial-coverage validation
        ↓
Round 3
Adversarial hallucination validation
        ↓
Regression
All previous cases rerun
        ↓
Promotion to v1.0
```

Promotion requires:

```text
Round 1 = PASSED
Round 2 = PASSED
Round 3 = PASSED
Regression = PASSED
```

A regression failure prevents promotion.

---

## 21. Golden Rule

> **Unknown remains UNKNOWN.**
>
> **Open remains OPEN.**
>
> **Blocked remains BLOCKED.**
>
> **Reasonable does not mean supported.**
>
> **A development default is not evidence.**
>
> **A technical decision requires evidence.**

---

## 22. Lock Record

```text
SKILL: implementation
VERSION: v1.0
STATUS: LOCKED

ROUND 1: PASSED (20/20)
ROUND 2: PASSED (20/20)
ROUND 3: PASSED (20/20)
REGRESSION: PASSED (60/60)

HALLUCINATION RESISTANCE: PASSED
DEV-STANDARD PRECEDENCE: DEFINED
IMPLEMENTATION GATE: PASSED
```
