# Implementation Plan Test — Round 2

**Skill:** `implementation-plan`
**Version:** `v0.1`
**Round:** `Round 2 — Advanced Planning Validation`

---

# 1. Objective

Round 2 validates whether Skill 13 correctly handles:

* complex implementation dependency graphs;
* blocker propagation;
* non-propagating blockers;
* development-standard precedence;
* inherited development standards;
* partial planning;
* cross-scope planning;
* split and merged implementation plans;
* valid parallel execution;
* reasonable implementation task hallucination;
* plan-level scope inflation;
* confusion between implementation order and business workflow;
* explicit dependency-cycle detection.

---

# 2. Expected Decision Model

```text
SUPPORTED
    ↓
READY

SUPPORTED + NON-BLOCKING OPEN
    ↓
READY WITH OPEN ITEMS

UNRESOLVED REQUIRED DEPENDENCY
    ↓
BLOCKED

UNSUPPORTED / INVENTED PLAN WORK
    ↓
FAIL

DEPENDENCY CYCLE
    ↓
FAIL

CONTRADICTORY STANDARD
    ↓
BLOCKED or FAIL
```

---

# 3. Advanced Test Cases

## IP-R2-T001 — Linear Dependency Chain

### Input

```text
IMP-001 — Approved authentication capability
IMP-002 — Approved authenticated profile capability
IMP-003 — Approved authenticated reporting capability
```

Plan:

```text
IP-001 depends on none
IP-002 depends on IP-001
IP-003 depends on IP-002
```

### Expected

`PASS`

Reason:

The implementation sequence is a valid dependency chain.

---

## IP-R2-T002 — Diamond Dependency

### Input

```text
IP-010 — Shared authentication foundation
IP-011 — Customer profile implementation
IP-012 — Staff profile implementation
IP-013 — Shared authenticated dashboard integration
```

Dependencies:

```text
          IP-010
          /    \
       IP-011  IP-012
          \    /
           IP-013
```

### Expected

`PASS`

Reason:

Both IP-011 and IP-012 depend independently on IP-010, while IP-013 depends on both.

Skill 13 MUST NOT incorrectly detect this as a cycle.

---

## IP-R2-T003 — Multiple Independent Branches

### Input

```text
IP-014 — Report viewing
IP-015 — Profile viewing
IP-016 — Unit assignment
```

No dependencies between them.

### Expected

`PASS`

All three may remain independently executable.

---

## IP-R2-T004 — Blocker Propagation Through Chain

### Input

```text
IP-020 = BLOCKED
IP-021 depends on IP-020
IP-022 depends on IP-021
IP-023 independent
```

### Expected

```text
IP-020 → BLOCKED
IP-021 → BLOCKED
IP-022 → BLOCKED
IP-023 → READY
```

Reason:

The block propagates only through dependent items.

---

## IP-R2-T005 — Blocker Does Not Propagate to Parallel Branch

### Input

```text
IP-024 = BLOCKED

IP-025 depends on IP-024
IP-026 depends on IP-024

IP-027 independent
```

### Expected

```text
IP-024 → BLOCKED
IP-025 → BLOCKED
IP-026 → BLOCKED
IP-027 → READY
```

### Requirement

The skill MUST NOT block unrelated work.

---

## IP-R2-T006 — Partial Blocker in a Combined Plan Item

### Input

Approved implementation:

```text
IMP-010 — Customer profile
IMP-011 — Customer rental history
```

Plan:

```text
IP-030 — Implement customer profile and rental history
```

`IMP-010` is ready.

`IMP-011` is blocked.

### Expected

`BLOCKED` for the combined plan item.

### Reason

The plan item cannot be safely completed while one of its required implementation scopes is blocked.

The skill MUST NOT silently mark the whole item READY merely because part of it is executable.

---

## IP-R2-T007 — Split Partial Planning

### Input

Approved implementation:

```text
IMP-012 — Rental management
```

Plan covers only:

```text
IP-031 — Rental viewing
IP-032 — Rental assignment
```

Other approved implementation scope remains unplanned.

### Expected

`PASS WITH OPEN ITEMS`

Reason:

Partial planning is allowed if the plan explicitly indicates incomplete coverage.

The skill MUST NOT claim that the entire `IMP-012` scope is planned.

---

## IP-R2-T008 — Partial Plan Misreported as Complete

### Input

Approved implementation:

```text
IMP-013 — Rental management
```

Plan:

```text
IP-033 — Rental viewing
```

Final statement:

```text
"All rental management implementation is planned."
```

### Expected

`FAIL`

Reason:

The artifact overclaims coverage.

---

## IP-R2-T009 — Dev Standard Inheritance

### Input

```text
Root standard:
Frontend = React
Backend = Spring Boot
```

Project standard:

```text
No override.
```

Plan:

```text
IP-034 — Implement approved frontend scope using React
IP-035 — Implement approved backend scope using Spring Boot
```

### Expected

`PASS / DEV_STANDARD`

---

## IP-R2-T010 — Project-Level Standard Override

### Input

Root:

```text
Backend = Spring Boot
```

Project:

```text
Backend = NestJS
```

Precedence policy:

```text
Project overrides Root.
```

Plan:

```text
IP-036 — Implement backend scope using NestJS
```

### Expected

`PASS / DEV_STANDARD`

---

## IP-R2-T011 — Conflicting Standards Without Precedence

### Input

Root:

```text
Backend = Spring Boot
```

Project:

```text
Backend = NestJS
```

No precedence rule.

Plan:

```text
IP-037 — Implement backend using NestJS
```

### Expected

`BLOCKED / CONTRADICTION`

Reason:

The plan cannot silently choose one standard.

---

## IP-R2-T012 — Standard Does Not Authorize Extra Tooling

### Input

Standard:

```text
Frontend = React
```

Plan:

```text
IP-038 — Implement React frontend
IP-039 — Add Redux
IP-040 — Add React Query
IP-041 — Add Tailwind
```

No approved implementation requires these tools.

### Expected

`FAIL`

Reason:

The standard establishes React, not every common React ecosystem tool.

---

## IP-R2-T013 — Cross-Scope Planning With Shared Dependency

### Input

```text
Project A:
IMP-A01 — Customer authentication

Project B:
IMP-B01 — Customer profile
```

Approved shared dependency:

```text
IMP-B01 depends on authentication capability.
```

Plan:

```text
Project A:
IP-050 — Authentication implementation

Project B:
IP-051 — Profile implementation
Depends on IP-050
```

### Expected

`PASS`

Reason:

Cross-scope dependency is valid when the upstream implementation dependency explicitly exists.

---

## IP-R2-T014 — Invalid Cross-Scope Dependency

### Input

```text
Project A:
IP-052 — Authentication implementation

Project B:
IP-053 — Report implementation
```

No upstream dependency exists.

Plan adds:

```text
IP-053 depends on IP-052
```

### Expected

`FAIL`

Reason:

Cross-project proximity is not evidence of dependency.

---

## IP-R2-T015 — Shared Infrastructure Hallucination

### Input

Two approved implementation areas:

```text
IMP-020 — Profile
IMP-021 — Reports
```

Plan adds:

```text
IP-054 — Build shared caching infrastructure
```

No cache requirement or standard exists.

### Expected

`FAIL`

Reason:

“Shared” infrastructure is a reasonable engineering idea, but not approved scope.

---

## IP-R2-T016 — Reasonable Testing Task Hallucination

### Input

Approved implementation:

```text
IMP-022 — Login capability
```

Plan adds:

```text
IP-055 — Implement login
IP-056 — Write unit tests
IP-057 — Add integration tests
IP-058 — Add end-to-end tests
IP-059 — Add load testing
```

No testing requirements or dev standard defines these layers.

### Expected

At minimum:

`FAIL` for unsupported testing scope.

The skill MAY allow generic verification planning where explicitly permitted, but MUST NOT silently introduce substantial test infrastructure or test categories as mandatory scope.

---

## IP-R2-T017 — Environment Setup Inflation

### Input

Approved implementation:

```text
IMP-023 — Profile viewing
```

Plan:

```text
IP-060 — Configure local environment
IP-061 — Configure Docker
IP-062 — Configure CI/CD
IP-063 — Configure monitoring
IP-064 — Implement profile viewing
```

No corresponding standard or approved implementation requirement exists.

### Expected

`FAIL`

Reason:

The plan inflated a small feature into unrelated infrastructure work.

---

## IP-R2-T018 — Dependency Based Only on File Order

### Input

Plan file lists:

```text
IP-065 — Profile
IP-066 — Reports
```

No dependency is declared.

### Expected

`PASS`

Reason:

Document order alone MUST NOT be interpreted as dependency.

---

## IP-R2-T019 — Technical Order Mistaken for Business Workflow

### Input

Plan:

```text
IP-067 — Prepare reservation implementation
IP-068 — Prepare payment implementation
IP-069 — Prepare check-in implementation
```

The tasks are ordered only for technical preparation.

### Expected

`PASS`

But the plan MUST NOT state:

```text
Reservation must happen before payment.
Payment must happen before check-in.
```

unless upstream evidence establishes that business sequence.

---

## IP-R2-T020 — Hidden Reasonable Default

### Input

Approved implementation:

```text
IMP-024 — Customer authentication capability
```

Plan:

```text
IP-070 — Implement authentication
IP-071 — Configure PostgreSQL user table
IP-072 — Add JWT token handling
IP-073 — Add Redis session storage
IP-074 — Configure Docker authentication environment
```

No technical decisions establish these technologies.

### Expected

`FAIL`

Reason:

The tasks look operationally reasonable but contain multiple unsupported technical assumptions.

---

## IP-R2-T021 — Explicit Dependency Cycle

### Input

Plan contains:

```text
IP-075 — Authentication integration
IP-076 — User profile integration
IP-077 — Permission integration
```

Dependencies:

```text
IP-075 depends on IP-077
IP-076 depends on IP-075
IP-077 depends on IP-076
```

Graph:

```text
IP-075
   ↓
IP-077
   ↓
IP-076
   ↓
IP-075
```

### Expected

`FAIL / DEPENDENCY_CYCLE`

### Required behavior

Skill 13 MUST explicitly identify that the dependency graph contains a cycle.

It MUST NOT:

* choose an arbitrary task order;
* break the cycle silently;
* mark all tasks `READY`;
* infer that the cycle represents a business workflow;
* remove a dependency without evidence.

The cycle must remain visible until the dependency is corrected.

---

# 4. Round 2 Acceptance Criteria

| ID        | Acceptance requirement                                 |
| --------- | ------------------------------------------------------ |
| AC-R2-001 | Correctly handle linear dependency chains              |
| AC-R2-002 | Correctly handle diamond dependency graphs             |
| AC-R2-003 | Preserve independent parallel work                     |
| AC-R2-004 | Propagate blockers through dependent chains            |
| AC-R2-005 | Do not propagate blockers to unrelated tasks           |
| AC-R2-006 | Detect partially blocked combined plan items           |
| AC-R2-007 | Permit partial planning without claiming full coverage |
| AC-R2-008 | Detect false complete-coverage claims                  |
| AC-R2-009 | Apply inherited dev standards                          |
| AC-R2-010 | Apply explicit project-over-root precedence            |
| AC-R2-011 | Block unresolved standard conflicts                    |
| AC-R2-012 | Prevent standard-driven tooling inflation              |
| AC-R2-013 | Allow evidence-supported cross-scope dependencies      |
| AC-R2-014 | Reject invented cross-scope dependencies               |
| AC-R2-015 | Reject unapproved shared infrastructure                |
| AC-R2-016 | Reject unsupported mandatory test-scope expansion      |
| AC-R2-017 | Reject environment/infrastructure inflation            |
| AC-R2-018 | Do not infer dependencies from file order              |
| AC-R2-019 | Separate technical order from business workflow        |
| AC-R2-020 | Reject reasonable-default technical tasks              |
| AC-R2-021 | Explicitly detect dependency cycles                    |

---

# 5. Expected Round 2 Result

```text
IP-R2-T001  PASS
IP-R2-T002  PASS
IP-R2-T003  PASS
IP-R2-T004  PASS
IP-R2-T005  PASS
IP-R2-T006  BLOCKED
IP-R2-T007  PASS WITH OPEN ITEMS
IP-R2-T008  FAIL
IP-R2-T009  PASS
IP-R2-T010  PASS
IP-R2-T011  BLOCKED
IP-R2-T012  FAIL
IP-R2-T013  PASS
IP-R2-T014  FAIL
IP-R2-T015  FAIL
IP-R2-T016  FAIL
IP-R2-T017  FAIL
IP-R2-T018  PASS
IP-R2-T019  PASS
IP-R2-T020  FAIL
IP-R2-T021  FAIL / DEPENDENCY_CYCLE
```

---

# 6. Round 2 Gate

Target:

```text
IMPLEMENTATION PLAN v0.1
ROUND 2

21/21 EXPECTED BEHAVIOR

DEPENDENCY GRAPH: PASSED
BLOCKER PROPAGATION: PASSED
DEPENDENCY CYCLE DETECTION: PASSED
DEV STANDARD PRECEDENCE: PASSED
PARTIAL PLANNING: PASSED
CROSS-SCOPE PLANNING: PASSED
REASONABLE-DEFAULT RESISTANCE: PASSED
```

A single unexpected acceptance of unsupported planning work MUST fail the round.
