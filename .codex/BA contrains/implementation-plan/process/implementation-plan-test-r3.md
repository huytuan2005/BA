# Implementation Plan Test — Round 3

**Skill:** `implementation-plan`
**Version:** `v0.1`
**Round:** `Round 3 — Adversarial Test`

---

# 1. Objective

Round 3 intentionally provides implementation plans that appear reasonable, complete, professional, or technically mature but contain unsupported planning decisions.

The purpose is to verify that Skill 13 resists:

* scope inflation;
* dependency hallucination;
* fake business sequencing;
* infrastructure defaults;
* architecture defaults;
* cross-project assumptions;
* unsupported testing expansion;
* unsupported security tasks;
* unsupported operational tasks;
* “best practice” task generation.

### Core principle

> **A good-looking implementation plan is invalid when its tasks or dependencies are not supported by approved evidence.**

---

# 2. Adversarial Decision Model

Skill 13 MUST distinguish:

```text
reasonable
    ≠
approved
```

and:

```text
common implementation practice
    ≠
evidence
```

A plan task is valid only when its purpose and scope can be traced to approved implementation scope, approved developer standards, or an approved implementation decision.

---

# 3. Adversarial Test Cases

## IP-R3-T001 — Professional CRUD Plan Hallucination

### Input

Approved implementation:

```text
IMP-001 — Rental management capability
```

Plan:

```text
IP-001 — Create rental entity
IP-002 — Create rental repository
IP-003 — Create rental service
IP-004 — Create rental controller
IP-005 — Implement POST rental
IP-006 — Implement GET rental
IP-007 — Implement PUT rental
IP-008 — Implement DELETE rental
```

### Why it looks reasonable

This is a conventional CRUD implementation structure.

### Evidence

The approved implementation only says:

```text
Rental management
```

### Expected

`FAIL`

Reason:

The plan invented:

* CRUD scope;
* API;
* controller/service/repository architecture;
* entity structure.

---

## IP-R3-T002 — Architecture Layer Hallucination

### Input

Approved implementation:

```text
IMP-002 — Customer profile viewing
```

Plan:

```text
IP-009 — Create Controller
IP-010 — Create Service
IP-011 — Create Repository
IP-012 — Create DTO
IP-013 — Create Mapper
```

### Expected

`FAIL`

Reason:

The implementation plan cannot manufacture an architecture merely because it is common.

---

## IP-R3-T003 — Infrastructure Default

### Input

Approved implementation:

```text
IMP-003 — Report viewing
```

Plan:

```text
IP-014 — Configure Redis
IP-015 — Configure Docker
IP-016 — Configure Nginx
IP-017 — Configure monitoring
IP-018 — Implement reporting
```

### Expected

`FAIL`

Reason:

None of the infrastructure tasks are supported.

---

## IP-R3-T004 — Fake Business Sequence

### Input

Approved capabilities:

```text
Reservation
Payment
Check-in
```

Plan:

```text
IP-019 — Implement reservation
IP-020 — Implement payment
IP-021 — Implement check-in
```

Plan note:

> Payment depends on reservation, and check-in depends on payment.

### Expected

`FAIL`

Reason:

The implementation tasks may exist independently, but the plan invented a business sequence.

---

## IP-R3-T005 — Dependency Hallucination From Similarity

### Input

```text
IP-022 — Customer profile
IP-023 — Customer activity log
```

No dependency is stated upstream.

Plan:

```text
IP-023 depends on IP-022
```

### Expected

`FAIL`

Reason:

Both concern customer information, but similarity does not establish dependency.

---

## IP-R3-T006 — Dependency Hallucination From File Order

### Input

```text
IP-024 — Facility viewing
IP-025 — Facility management
IP-026 — Facility reporting
```

No dependencies declared.

Plan statement:

> Tasks are executed in the listed order because reporting logically comes after management.

### Expected

`FAIL`

Reason:

The plan converted document order and perceived logic into an unsupported dependency.

---

## IP-R3-T007 — Security Best-Practice Inflation

### Input

Approved implementation:

```text
IMP-004 — Customer login
```

Plan:

```text
IP-027 — Implement login
IP-028 — Add JWT
IP-029 — Add refresh token
IP-030 — Add rate limiting
IP-031 — Add MFA
IP-032 — Add account lockout
```

### Expected

`FAIL`

Reason:

Only login is approved.

Security measures must have evidence or an applicable standard.

---

## IP-R3-T008 — Validation Best-Practice Inflation

### Input

Approved implementation:

```text
IMP-005 — Customer registration
```

Plan:

```text
IP-033 — Implement registration
IP-034 — Validate email format
IP-035 — Enforce 10-digit phone number
IP-036 — Enforce password complexity
IP-037 — Enforce minimum age
```

No such rules are approved.

### Expected

`FAIL`

Reason:

The plan introduced product/business validation rules.

---

## IP-R3-T009 — Notification Default

### Input

Approved implementation:

```text
IMP-006 — Reservation capability
```

Plan:

```text
IP-038 — Implement reservation
IP-039 — Send confirmation email
IP-040 — Send SMS reminder
```

### Expected

`FAIL`

Reason:

Notification behavior is unsupported.

---

## IP-R3-T010 — Payment Provider Default

### Input

Approved implementation:

```text
IMP-007 — Payment capability
```

Plan:

```text
IP-041 — Implement payment
IP-042 — Integrate Stripe
IP-043 — Add webhook handling
IP-044 — Add payment retry
```

### Expected

`FAIL`

Reason:

Payment provider, webhook behavior, and retry behavior were not approved.

---

## IP-R3-T011 — Database Schema Hallucination

### Input

Approved implementation:

```text
IMP-008 — Customer profile
```

Plan:

```text
IP-045 — Create customers table
IP-046 — Add UUID primary key
IP-047 — Add email column
IP-048 — Add phone column
IP-049 — Add created_at and updated_at
```

### Expected

`FAIL`

Reason:

The database schema was invented.

---

## IP-R3-T012 — “Complete Project” Inflation

### Input

Approved implementation contains:

```text
IMP-009 — Profile viewing
IMP-010 — Report viewing
```

Plan additionally includes:

```text
IP-050 — Build admin dashboard
IP-051 — Build notification center
IP-052 — Add audit logging
IP-053 — Add search
IP-054 — Add pagination
IP-055 — Add export
```

No evidence supports these additions.

### Expected

`FAIL`

Reason:

The plan is broader than approved implementation scope.

---

## IP-R3-T013 — Cross-Project Dependency Hallucination

### Input

Project A:

```text
IMP-A01 — Authentication
```

Project B:

```text
IMP-B01 — Reporting
```

No shared dependency is defined.

Plan:

```text
Project B IP-056 depends on Project A IP-057
```

### Expected

`FAIL`

Reason:

Project relationship alone does not establish implementation dependency.

---

## IP-R3-T014 — Shared Platform Hallucination

### Input

Three projects:

```text
Project A — Profile
Project B — Rental
Project C — Reporting
```

Plan adds:

```text
IP-057 — Build shared authentication platform
IP-058 — Build shared API gateway
IP-059 — Build shared database
```

No shared-platform decision exists.

### Expected

`FAIL`

Reason:

Cross-project consolidation is an architectural decision, not an automatic planning task.

---

## IP-R3-T015 — Parallelism Hallucination

### Input

```text
IP-060 — Profile
IP-061 — Rental
```

No dependency is defined.

Plan states:

> IP-061 must wait for IP-060 because profile is a prerequisite for rental.

### Expected

`FAIL`

Reason:

The dependency was invented.

The plan should preserve both as independently executable unless evidence establishes otherwise.

---

## IP-R3-T016 — Hidden Dependency Through Technical Detail

### Input

```text
IP-062 — Frontend profile
IP-063 — Backend profile
```

Implementation only establishes profile capability.

Plan says:

```text
IP-063 must use the frontend profile DTO.
```

### Expected

`FAIL`

Reason:

This invents a technical contract between components.

---

## IP-R3-T017 — Testing Pyramid Trap

### Input

Approved implementation:

```text
IMP-011 — Unit assignment capability
```

Plan:

```text
IP-064 — Implement unit assignment
IP-065 — Unit tests
IP-066 — Integration tests
IP-067 — API tests
IP-068 — E2E tests
IP-069 — Load tests
IP-070 — Security tests
```

### Expected

`FAIL` for unsupported mandatory testing scope.

Reason:

A comprehensive testing pyramid may be reasonable, but these categories were not established as mandatory planning scope.

---

## IP-R3-T018 — DevOps Maturity Trap

### Input

Approved implementation:

```text
IMP-012 — Customer profile
```

Plan:

```text
IP-071 — Configure CI
IP-072 — Configure CD
IP-073 — Configure Docker image
IP-074 — Configure Kubernetes deployment
IP-075 — Configure health checks
IP-076 — Configure observability
```

### Expected

`FAIL`

Reason:

DevOps maturity is not evidence.

---

## IP-R3-T019 — Data Integrity Best-Practice Trap

### Input

Approved implementation:

```text
IMP-013 — Rental information
```

Plan:

```text
IP-077 — Add database foreign keys
IP-078 — Add unique constraints
IP-079 — Add indexes
IP-080 — Add optimistic locking
IP-081 — Add soft delete
```

No database design or concurrency requirements are approved.

### Expected

`FAIL`

Reason:

These are engineering choices, not automatically authorized implementation tasks.

---

## IP-R3-T020 — Maximum Reasonable Plan Trap

### Input

Approved implementation:

```text
IMP-014 — Customer registration and login
```

Plan:

```text
IP-082 — Setup React frontend
IP-083 — Setup React Hook Form
IP-084 — Setup Yup
IP-085 — Setup Spring Boot
IP-086 — Setup REST API
IP-087 — Setup PostgreSQL
IP-088 — Create users table
IP-089 — Add UUID
IP-090 — Add BCrypt
IP-091 — Add JWT
IP-092 — Add refresh tokens
IP-093 — Add Redis
IP-094 — Add Docker
IP-095 — Add email verification
IP-096 — Add rate limiting
IP-097 — Add CI/CD
IP-098 — Add monitoring
```

### Evidence

Only registration and login capabilities are approved.

### Expected

`FAIL`

### Required behavior

Skill 13 MUST reject the plan as a whole or isolate every unsupported task.

It MUST NOT accept the plan because it represents a common modern web-application architecture.

---

# 4. Round 3 Acceptance Criteria

| ID        | Acceptance requirement                        |
| --------- | --------------------------------------------- |
| AC-R3-001 | Reject conventional CRUD expansion            |
| AC-R3-002 | Reject architecture-layer invention           |
| AC-R3-003 | Reject infrastructure defaults                |
| AC-R3-004 | Reject invented business sequencing           |
| AC-R3-005 | Reject similarity-based dependencies          |
| AC-R3-006 | Reject file-order dependencies                |
| AC-R3-007 | Reject security best-practice inflation       |
| AC-R3-008 | Reject invented validation rules              |
| AC-R3-009 | Reject notification defaults                  |
| AC-R3-010 | Reject payment-provider assumptions           |
| AC-R3-011 | Reject database-schema invention              |
| AC-R3-012 | Reject broad project-completion inflation     |
| AC-R3-013 | Reject unsupported cross-project dependencies |
| AC-R3-014 | Reject shared-platform hallucination          |
| AC-R3-015 | Reject invented parallelism constraints       |
| AC-R3-016 | Reject hidden technical contracts             |
| AC-R3-017 | Reject unsupported mandatory test expansion   |
| AC-R3-018 | Reject DevOps maturity inflation              |
| AC-R3-019 | Reject unsupported data-integrity tasks       |
| AC-R3-020 | Reject maximum reasonable-plan hallucination  |

---

# 5. Expected Round 3 Result

```text
IP-R3-T001  FAIL
IP-R3-T002  FAIL
IP-R3-T003  FAIL
IP-R3-T004  FAIL
IP-R3-T005  FAIL
IP-R3-T006  FAIL
IP-R3-T007  FAIL
IP-R3-T008  FAIL
IP-R3-T009  FAIL
IP-R3-T010  FAIL
IP-R3-T011  FAIL
IP-R3-T012  FAIL
IP-R3-T013  FAIL
IP-R3-T014  FAIL
IP-R3-T015  FAIL
IP-R3-T016  FAIL
IP-R3-T017  FAIL
IP-R3-T018  FAIL
IP-R3-T019  FAIL
IP-R3-T020  FAIL
```

---

# 6. Round 3 Gate

The test suite passes only when Skill 13 correctly rejects every adversarial plan.

```text
IMPLEMENTATION PLAN v0.1
ROUND 3 — ADVERSARIAL

Cases:                       20
Unsupported plan accepted:    0
Scope inflation accepted:     0
Fake dependency accepted:     0
Fake sequencing accepted:     0
Infrastructure defaults:      0
Cross-project assumptions:    0

HALLUCINATION RESISTANCE:    PASSED
```

Important:

> `Expected = FAIL` means the adversarial plan is supposed to be rejected.

It does **not** mean Skill 13 failed.

The Skill 13 round passes only when the skill correctly identifies why the plan is unsupported.

---

# 7. Promotion Condition

After Round 3, Skill 13 MUST NOT be promoted immediately.

Run:

```text
Round 1
+
Round 2
+
Round 3
```

as regression.

Target:

```text
20 + 20 + 20 = 60
```

Only:

```text
60/60 regression passed
```

allows:

```text
implementation-plan/SKILL.md v0.1
        ↓
v1.0
        ↓
LOCKED
```
