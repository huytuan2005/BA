# Skill: implementation-plan

**Version:** `v1.0`
**Status:** `LOCKED`

---

## 1. Purpose

Convert approved implementation scope into an actionable implementation plan.

The plan defines:

* implementation work items;
* implementation order;
* dependencies between work items;
* blockers;
* open items;
* implementation readiness boundaries;
* traceability back to approved implementation and upstream artifacts.

The skill does **not** write application code.

### Core principle

> **Plan the implementation work without inventing product behavior, business workflow, technical architecture, or requirements.**

---

## 2. Inputs

Primary inputs:

* approved `implementation/SKILL.md`;
* implementation outputs approved by Skill 12;
* implementation decisions;
* implementation blockers;
* implementation readiness result;
* approved blueprint;
* functional requirements;
* business rules;
* NFRs;
* applicable `dev-standards/DEV-STANDARDS.md`.

Optional inputs:

* approved developer decisions;
* existing project structure;
* existing implementation status.

Unsupported information MUST NOT become a planning assumption.

---

## 3. Outputs

The skill may produce:

```text
implementation-plan.md

implementation-plan-dependencies.md

implementation-plan-blockers.md
```

Optional:

```text
implementation-plan-open-items.md

implementation-plan-progress.md
```

---

## 4. Evidence Classification

Each plan item MUST retain its source classification where relevant:

| Classification   | Meaning                                        |
| ---------------- | ---------------------------------------------- |
| `SOURCE_STATED`  | Explicit upstream requirement                  |
| `DERIVED`        | Safely derived implementation work             |
| `DEV_STANDARD`   | Required by an applicable development standard |
| `IMPLEMENTATION` | Approved by Skill 12                           |
| `OPEN`           | Decision remains unresolved                    |
| `UNKNOWN`        | Information unavailable                        |
| `BLOCKED`        | Work cannot safely proceed                     |
| `CONTRADICTION`  | Relevant sources conflict                      |

---

## 5. Planning Boundary

Skill 13 plans **implementation work**, not product behavior.

Valid:

```text
IP-001 — Prepare approved frontend project structure

IP-002 — Implement approved authentication capability

IP-003 — Integrate approved implementation boundary
```

Invalid:

```text
Customer registers
    ↓
Email verification
    ↓
Login
    ↓
JWT issuance
```

unless that workflow is explicitly supported upstream.

---

## 6. Planning Order Is Not Business Workflow

Technical task ordering may be required for implementation dependency.

Example:

```text
IP-001 — Define approved data access component
        ↓
IP-002 — Implement approved service
        ↓
IP-003 — Implement approved UI integration
```

This means:

> `IP-003` depends on `IP-002`.

It MUST NOT be interpreted as a product workflow.

Skill 13 MUST clearly distinguish:

```text
implementation dependency
```

from:

```text
business/process sequence
```

---

## 7. Work Item Structure

Every implementation-plan item SHOULD contain:

```text
ID

Title

Purpose

Traceability

Evidence

Dependencies

Outputs

Status

Blockers

Open items
```

Example:

```text
IP-001

Title: Implement approved authentication capability

Traceability:
- FR-xxx
- IMP-xxx

Evidence:
IMPLEMENTATION

Dependencies:
None

Status:
READY
```

---

## 8. Traceability

Every plan item MUST trace to:

* an approved implementation item;
* an approved development standard;
* or a directly supporting upstream artifact.

Orphan plan item:

```text
ORPHAN_PLAN_ITEM
```

Result:

```text
FAIL
```

A valid implementation trace does not authorize unrelated planning work.

---

## 9. One-to-Many and Many-to-One

Supported mappings:

```text
one implementation item
    ↓
many plan items
```

and:

```text
many implementation items
    ↓
one plan item
```

Many-to-many mappings are also allowed when each relationship is explicit.

Traceability MUST NOT be lost when implementation scope is split into tasks.

---

## 10. Dependency Rules

Dependencies MUST describe implementation prerequisites.

Example:

```text
IP-003 depends on IP-002
```

The dependency is valid only when IP-002 provides something IP-003 requires.

Skill 13 MUST NOT create dependency solely because the tasks appear conceptually related.

---

## 11. Dependency Cycle

Cycles are invalid:

```text
IP-001 → IP-002

IP-002 → IP-003

IP-003 → IP-001
```

Result:

```text
FAIL

DEPENDENCY_CYCLE
```

---

## 12. Blocker Propagation

If:

```text
IP-002 = BLOCKED
```

and:

```text
IP-003 depends on IP-002
```

then IP-003 MAY become:

```text
BLOCKED
```

However, unrelated items MUST remain independently executable.

Example:

```text
IP-002 BLOCKED

IP-003 depends on IP-002

IP-010 independent
```

Result:

```text
IP-002 BLOCKED

IP-003 BLOCKED

IP-010 READY
```

---

## 13. Open Items

An unresolved item does not automatically block planning.

Example:

```text
Exact export format = OPEN

IP-005:
Prepare report export integration boundary
```

may remain:

```text
READY WITH OPEN ITEMS
```

provided implementation can proceed safely without inventing the format.

---

## 14. Required Blocking Decision

If a required technical or behavioral decision is unresolved and implementation cannot safely proceed, mark the task:

```text
BLOCKED
```

Do not manufacture a decision to remove the blocker.

---

## 15. Planning Status

Allowed plan-item statuses:

```text
READY

READY WITH OPEN ITEMS

BLOCKED

IN PROGRESS

COMPLETED
```

These status values describe **plan/task state**, not business-domain entity state.

Skill 13 MUST NOT introduce product statuses such as:

```text
PENDING

ACTIVE

CANCELLED

COMPLETED
```

unless those are explicitly upstream business statuses.

---

## 16. No CRUD Expansion

Skill 13 MUST NOT expand:

```text
manage X
```

into:

```text
create X
read X
update X
delete X
```

unless Skill 12 already approved those implementation units.

The plan follows approved implementation scope.

---

## 17. No Technology Invention

Skill 13 MUST NOT introduce technology merely to make the plan concrete.

Do not invent:

```text
PostgreSQL

JWT

REST

Redis

Docker

Kubernetes

OAuth2
```

unless inherited from:

* approved implementation;
* applicable development standard;
* approved developer decision.

---

## 18. No Architecture Invention

A plan MUST NOT create unapproved architecture work such as:

```text
microservice migration

event bus

repository layer

caching layer

message queue

API gateway
```

merely because they are common engineering patterns.

---

## 19. No Scope Inflation

Do not add:

```text
extra feature

extra validation

extra notification

extra report

extra integration

extra security control

extra infrastructure
```

unless supported by approved scope.

---

## 20. Minimal Planning Principle

The implementation plan should contain the minimum work needed to implement approved scope safely.

Do not create tasks merely to make the plan look complete.

Example:

Invalid:

```text
IP-001 Setup Redis

IP-002 Setup Kafka

IP-003 Setup Docker

IP-004 Setup Kubernetes
```

when none is required by approved implementation scope.

---

## 21. Developer Boundary

Skill 13 determines:

* what work needs to be done;
* which approved implementation item each task addresses;
* implementation dependencies;
* blockers;
* open items;
* readiness state.

The developer remains responsible for detailed coding decisions unless already established by approved implementation artifacts or dev standards.

---

## 22. Plan Item Readiness

### `READY`

The task has sufficient evidence and dependencies.

### `READY WITH OPEN ITEMS`

The task can proceed safely while non-blocking questions remain.

### `BLOCKED`

A required unresolved dependency or decision prevents safe implementation.

---

## 23. Plan Validation Result

The overall implementation plan may produce:

```text
PASS

PASS WITH OPEN ITEMS

BLOCKED

FAIL
```

`FAIL` applies when the plan contains:

* unsupported scope;
* orphan tasks;
* invented technical decisions;
* invented product behavior;
* broken dependencies;
* dependency cycles;
* contradictory planning decisions.

These are **plan-level validation results**, not plan-item readiness states.

---

## 24. Quality Gate

The plan passes only when:

```text
100% plan items traceable

AND

100% dependency relationships valid

AND

0 dependency cycles

AND

0 unsupported scope additions

AND

0 hallucinated technical decisions

AND

all blockers explicitly identified
```

Gate result:

```text
PASS

PASS WITH OPEN ITEMS

BLOCKED

FAIL
```

---

## 25. Golden Rules

> Plan implementation, not product behavior.

> Implementation dependency is not business workflow.

> Follow approved implementation scope.

> Do not turn ambiguity into tasks that assume an answer.

> Do not use common engineering practice as evidence.

> Open remains OPEN.

> Blocked remains BLOCKED.

> Unknown remains UNKNOWN.

> No code is generated by this skill.

---

# Skill 13 — Implementation Plan

## Regression Result

**Skill Version:** `v1.0`

**Status:** `LOCKED`

**Regression Scope:** Round 1 + Round 2 + Round 3

**Total Test Cases:** `60`

### Result

* Round 1: **20/20 PASS**
* Round 2: **20/20 PASS**
* Round 3: **20/20 PASS**
* Overall: **60/60 PASS**

### Quality Gate

* Traceability: **PASS**
* Unsupported plan items: **0 detected**
* Hallucinated dependencies: **0 undetected**
* Broken dependency relationships: **0**
* Dependency cycles: **0 undetected**
* Blocker propagation: **PASS**
* Dev Standard inheritance/precedence: **PASS**
* Open vs Blocked distinction: **PASS**
* Business workflow disguised as implementation dependency: **REJECTED**
* Technical/architecture/infrastructure defaults: **REJECTED**
* Security/testing/DevOps best-practice inflation: **REJECTED**
* Cross-project/shared-platform assumptions: **REJECTED**
* “Reasonable” but unsupported implementation details: **REJECTED**

## Verdict

**REGRESSION: 60/60 PASS**

**Skill 13 v1.0 satisfies the regression suite.**

The adversarial suite confirms that the skill can resist:

* CRUD hallucination
* architecture invention
* infrastructure invention
* dependency invention
* business-sequence invention
* security/testing/DevOps scope inflation
* database-schema invention
* cross-project assumptions
* “complete project” expansion
* maximum-reasonable-plan hallucination

## Promotion

**Promotion result: `v0.1 → v1.0`**

**Status: `LOCKED`**

No behavioral changes should be made directly to `v1.0`. Any future change MUST open a new version and repeat the required validation/regression process.
