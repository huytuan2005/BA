# Implementation Skill Test Suite

**Skill:** `implementation`
**Version:** v0.1
**Round:** Round 2

---

# 1. Objective

Round 2 kiểm tra các tình huống phức tạp hơn mà Round 1 chưa bao phủ:

```text
1. Partial traceability
2. Many requirements → one implementation item
3. One requirement → many implementation items
4. Inherited dev-standard
5. Conflicting dev-standards
6. Dependency chain
7. False-positive BLOCKED
8. Partial implementation coverage
9. Mixed supported + unsupported decisions
10. Dependency cycle
```

Mục tiêu:

> Skill phải biết phân biệt giữa implementation có đủ evidence, implementation chỉ được hỗ trợ một phần, và implementation thực sự bị block.

---

# 2. Test Cases

## IMP-R2-T001 — Partial Traceability

### Input

```text
Implementation:
Unit assignment validation

Trace:
FR-SELF-STORAGE-014
```

Known upstream:

```text
FR-SELF-STORAGE-014:
Facility Manager can assign units.

BR-SELF-STORAGE-001:
Unit assignment considers unit type,
rental period, and availability.
```

Implementation artifact:

```text
Validation:
- unit type
- rental period
- availability
- customer credit score
```

### Expected

```text
FAIL
```

Reason:

```text
unit type        → supported
rental period    → supported
availability     → supported
credit score     → unsupported
```

The valid portion MUST NOT hide the unsupported portion.

---

# 3. IMP-R2-T002 — Many Requirements → One Implementation Item

### Input

```text
Implementation:
Role-based facility data access

Trace:
FR-SELF-STORAGE-025
FR-SELF-STORAGE-026
```

Requirements:

```text
FR-025:
Administrator can assign roles.

FR-026:
Administrator can configure data access
permissions by role and assigned facility.
```

### Expected

```text
PASS
```

Reason:

One implementation area may legitimately satisfy multiple requirements.

The skill MUST preserve both trace links.

---

# 4. IMP-R2-T003 — One Requirement → Many Implementation Items

### Input

```text
FR-SELF-STORAGE-026
```

Implementation items:

```text
IMP-001 Role assignment handling
IMP-002 Facility access control
IMP-003 Permission configuration
```

### Expected

```text
PASS
```

Reason:

A single requirement may require multiple implementation areas.

The skill MUST NOT require a one-to-one relationship.

---

# 5. IMP-R2-T004 — Partial Coverage of One Requirement

### Input

Requirement:

```text
FR-SELF-STORAGE-023

System-wide reports can be viewed
and exported by facility, unit type,
revenue, and rental status.
```

Implementation:

```text
IMP-001:
View reports by facility.

IMP-002:
Export reports by facility.
```

Missing:

```text
unit type
revenue
rental status
```

### Expected

```text
PASS WITH OPEN ITEMS
```

The skill MUST identify incomplete coverage.

It MUST NOT report full implementation coverage.

---

# 6. IMP-R2-T005 — Inherited Dev Standard

### Input

Root standard:

```text
DEV-STANDARDS.md

Frontend:
React
```

Project-level file:

```text
projects/self-storage/dev-standards.md

No frontend override.
```

Implementation:

```text
Frontend implementation:
React
```

### Expected

```text
PASS
DEV_STANDARD
```

The implementation skill MUST inherit the applicable parent standard.

---

# 7. IMP-R2-T006 — Child Override of Dev Standard

### Input

Root:

```text
Frontend:
React
```

Project standard:

```text
Frontend:
React + TypeScript
```

Implementation:

```text
React + TypeScript
```

### Expected

```text
PASS
```

The more specific applicable standard overrides the inherited generic standard.

The inheritance chain MUST remain visible.

---

# 8. IMP-R2-T007 — Conflicting Dev Standards

### Input

Root:

```text
Backend:
Spring Boot
```

Project:

```text
Backend:
Node.js / NestJS
```

No precedence rule exists.

### Expected

```text
BLOCKED
```

Reason:

The skill cannot safely select one technology.

It MUST NOT silently choose:

```text
Spring Boot
```

or:

```text
NestJS
```

---

# 9. IMP-R2-T008 — Explicit Standard Precedence

### Input

Root:

```text
Backend:
Spring Boot
```

Project:

```text
Backend:
NestJS

Precedence:
Project standard overrides root standard.
```

Implementation:

```text
NestJS
```

### Expected

```text
PASS
```

The project-level standard is authoritative.

---

# 10. IMP-R2-T009 — Dependency Chain

### Input

```text
IMP-003 Unit assignment

depends on:
IMP-002 Unit availability definition

IMP-002 depends on:
IMP-001 Unit status definition
```

But:

```text
IMP-001 = OPEN
```

### Expected

```text
BLOCKED
```

Reason:

```text
IMP-001
   ↓
IMP-002
   ↓
IMP-003
```

The unresolved dependency propagates to the dependent implementation item.

---

# 11. IMP-R2-T010 — Dependency Does Not Propagate Unnecessarily

### Input

```text
IMP-003 Unit assignment
depends on:
IMP-002 Unit availability

IMP-010 User profile display
depends on:
FR-SELF-STORAGE-001
```

`IMP-002` is BLOCKED.

`IMP-010` has no dependency on `IMP-002`.

### Expected

```text
IMP-003 → BLOCKED
IMP-010 → NOT BLOCKED
```

The skill MUST NOT mark the entire implementation scope as blocked.

---

# 12. IMP-R2-T011 — False-Positive BLOCKED

### Input

Requirement:

```text
FR-SELF-STORAGE-027

System can track login history
and user activity logs.
```

Implementation:

```text
IMP-020 Activity logging
```

No exact storage technology has been selected.

### Expected

```text
PASS WITH OPEN ITEMS
```

NOT:

```text
BLOCKED
```

Reason:

The missing technical choice does not necessarily prevent implementation planning.

The skill must distinguish:

```text
OPEN technical decision
```

from:

```text
BLOCKING dependency
```

---

# 13. IMP-R2-T012 — Mixed Supported and Unsupported Decisions

### Input

```text
Implementation:
Authentication

Supported:
User login capability

Unsupported:
JWT
refresh token
OAuth
session timeout = 30 minutes
```

### Expected

```text
FAIL
```

The skill MUST isolate the unsupported decisions rather than accepting the entire implementation item.

---

# 14. IMP-R2-T013 — Valid Derived Decision

### Input

```text
Requirement:
System must allow users to log in.

Implementation:
Authentication component is required
to process the login capability.
```

### Expected

```text
PASS
DERIVED
```

Reason:

The existence of an implementation area is a reasonable implementation derivation.

No specific authentication technology has been invented.

---

# 15. IMP-R2-T014 — Invalid Derived Decision

### Input

```text
Requirement:
System must allow users to log in.

Implementation:
JWT authentication with refresh tokens
is required.
```

No source or dev standard defines JWT.

### Expected

```text
FAIL
UNSUPPORTED_TECHNICAL_DECISION
```

The skill MUST NOT classify this as merely `DERIVED`.

---

# 16. IMP-R2-T015 — Dependency Cycle

### Input

```text
IMP-001 depends on IMP-002
IMP-002 depends on IMP-003
IMP-003 depends on IMP-001
```

### Expected

```text
FAIL
DEPENDENCY_CYCLE
```

The skill MUST report the complete cycle.

---

# 17. IMP-R2-T016 — Valid Independent Implementation

### Input

```text
IMP-001 Login logging
IMP-002 Facility report viewing
IMP-003 Unit assignment
```

Dependencies:

```text
IMP-003 → IMP-002
IMP-001 → none
IMP-002 → none
```

### Expected

```text
PASS
```

The absence of a dependency does not make an item invalid.

---

# 18. IMP-R2-T017 — Requirement Split Without Lost Traceability

### Input

```text
FR-SELF-STORAGE-027
```

Implementation:

```text
IMP-001 Login history
IMP-002 User activity logging
```

### Expected

```text
PASS
```

Both implementation items retain:

```text
FR-SELF-STORAGE-027
```

as their trace source.

---

# 19. IMP-R2-T018 — Many-to-Many Traceability

### Input

Requirements:

```text
FR-025
FR-026
FR-027
```

Implementation:

```text
IMP-001 Authorization
IMP-002 Role management
IMP-003 Activity logging
```

Trace:

```text
IMP-001 → FR-025, FR-026
IMP-002 → FR-025, FR-026
IMP-003 → FR-027
```

### Expected

```text
PASS
```

The skill MUST support many-to-many traceability.

---

# 20. IMP-R2-T019 — Orphan Hidden Inside Valid Group

### Input

```text
IMP-001 Authorization
→ FR-025

IMP-002 Role management
→ FR-025

IMP-003 Email notification
→ FR-025
```

But `FR-025` does not mention email notifications.

### Expected

```text
FAIL
```

`IMP-003` is unsupported despite belonging to a group containing valid implementation items.

---

# 21. IMP-R2-T020 — Open Item Does Not Equal Failure

### Input

```text
Implementation:
Report export

Known:
Requirement explicitly allows reports to be exported.

Unknown:
Exact export file format.
```

### Expected

```text
PASS WITH OPEN ITEMS
```

The skill MUST NOT invent:

```text
CSV
Excel
PDF
```

and MUST NOT automatically mark the entire item as FAIL.

---

# 22. Round 2 Acceptance Criteria

Round 2 PASSES only if:

```text
IMP-R2-T001   FAIL correctly
IMP-R2-T002   PASS
IMP-R2-T003   PASS
IMP-R2-T004   PASS WITH OPEN ITEMS
IMP-R2-T005   PASS
IMP-R2-T006   PASS
IMP-R2-T007   BLOCKED
IMP-R2-T008   PASS
IMP-R2-T009   BLOCKED
IMP-R2-T010   PASS / scoped blocking
IMP-R2-T011   PASS WITH OPEN ITEMS
IMP-R2-T012   FAIL correctly
IMP-R2-T013   PASS / DERIVED
IMP-R2-T014   FAIL correctly
IMP-R2-T015   FAIL / DEPENDENCY_CYCLE
IMP-R2-T016   PASS
IMP-R2-T017   PASS
IMP-R2-T018   PASS
IMP-R2-T019   FAIL correctly
IMP-R2-T020   PASS WITH OPEN ITEMS
```

---

# 23. Round 2 Success Conditions

The skill is considered successful only if it can correctly distinguish:

```text
SUPPORTED
    ↓
PASS

SUPPORTED + NON-BLOCKING UNKNOWN
    ↓
PASS WITH OPEN ITEMS

UNRESOLVED REQUIRED DECISION
    ↓
BLOCKED

UNSUPPORTED / INVENTED
    ↓
FAIL

INVALID DEPENDENCY GRAPH
    ↓
FAIL
```

The most important rule for Round 2:

> `OPEN` does not automatically mean `BLOCKED`.

A missing decision becomes `BLOCKED` only when that decision prevents the dependent implementation from proceeding safely.
