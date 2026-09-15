# Skill 14 — Implementation Plan Validator

# `implementation-plan-validator-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 2`
**Total Test Cases:** `20`

---

## 1. Objective

Round 2 stress-tests Skill 14 beyond basic validation.

The focus is:

* misleading but syntactically valid traceability;
* partial traceability;
* dependency graph edge cases;
* blocker propagation chains;
* conflicting plan artifacts;
* development-standard inheritance and scope;
* unsupported technical details hidden inside valid tasks;
* unsupported cross-project assumptions;
* execution-gate correctness;
* validator non-interference under ambiguous conditions.

Round 2 MUST test whether Skill 14 validates the **evidence relationship**, not merely the presence of IDs or technically plausible task descriptions.

---

# 2. Test Cases

## IPV-R2-T001 — Trace Exists but Supports Only Part of the Task

### Scenario

Approved implementation:

```text
IMP-001 — Customer profile viewing capability
```

Plan:

```text
IP-001 — Implement customer profile viewing
        + profile creation
        + profile update
        + profile deletion

Traceability:
IMP-001
```

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

The validator MUST recognize that the trace supports only viewing, not the added CRUD operations.

---

## IPV-R2-T002 — Valid Trace but Wrong Implementation Item

### Scenario

Approved:

```text
IMP-001 — Customer profile
IMP-002 — Rental reporting
```

Plan:

```text
IP-001 — Implement rental reporting

Traceability:
IMP-001
```

### Expected

```text
FAIL
INVALID_TRACEABILITY
```

### Acceptance Criteria

The validator MUST verify semantic support, not merely whether the referenced implementation ID exists.

---

## IPV-R2-T003 — Partial Traceability After Scope Split

### Scenario

Approved:

```text
IMP-001 — Authentication capability
```

Plan:

```text
IP-001 — Prepare authentication boundary
Traceability: IMP-001

IP-002 — Implement login capability
Traceability: IMP-001

IP-003 — Implement password reset capability
Traceability: None
```

### Expected

```text
FAIL
ORPHAN_PLAN_ITEM
```

### Acceptance Criteria

Splitting approved scope does not remove the traceability requirement from individual plan items.

---

## IPV-R2-T004 — Many-to-Many Traceability with One Unsupported Relationship

### Scenario

Approved:

```text
IMP-001 — Customer profile
IMP-002 — Customer account
```

Plan:

```text
IP-001 — Implement approved customer profile/account capability

Traceability:
IMP-001
IMP-002

IP-002 — Add SMS account recovery

Traceability:
IMP-001
IMP-002
```

No source supports SMS recovery.

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

Valid many-to-many traceability cannot legitimize unrelated work.

---

## IPV-R2-T005 — Transitive Dependency Validity

### Scenario

```text
IP-001
   ↓
IP-002
   ↓
IP-003
```

`IP-003` requires the output of `IP-002`, and `IP-002` requires `IP-001`.

### Expected

```text
PASS
```

### Acceptance Criteria

The validator accepts a valid transitive dependency chain without requiring every upstream node to be declared as a direct dependency.

---

## IPV-R2-T006 — Diamond Dependency Graph

### Scenario

```text
         IP-002
        ↗       ↘
IP-001             IP-004
        ↘       ↗
         IP-003
```

There is no cycle.

### Expected

```text
PASS
```

### Acceptance Criteria

The validator does not falsely classify a diamond graph as a cycle.

---

## IPV-R2-T007 — Mixed Valid and Invalid Dependencies

### Scenario

```text
IP-001
   ↓
IP-002
   ↓
IP-003
```

and additionally:

```text
IP-003 depends on IP-010
```

but `IP-010` does not exist.

### Expected

```text
FAIL
BROKEN_DEPENDENCY_REFERENCE
```

### Acceptance Criteria

One valid dependency does not hide one invalid dependency.

---

## IPV-R2-T008 — Blocker Propagation Through Multiple Levels

### Scenario

```text
IP-001 = BLOCKED

IP-002 depends on IP-001
IP-003 depends on IP-002
IP-004 independent
```

### Expected

```text
IP-001 BLOCKED
IP-002 BLOCKED
IP-003 BLOCKED
IP-004 READY
```

### Acceptance Criteria

The validator propagates the blocker transitively.

---

## IPV-R2-T009 — Blocker Stops at Dependency Boundary

### Scenario

```text
IP-001 = BLOCKED

IP-002 depends on IP-001
IP-003 depends on IP-002
IP-004 depends only on IP-005
IP-005 READY
```

### Expected

```text
IP-001 BLOCKED
IP-002 BLOCKED
IP-003 BLOCKED
IP-004 READY
IP-005 READY
```

### Acceptance Criteria

The validator does not propagate a blocker into a separate dependency branch.

---

## IPV-R2-T010 — Contradictory Plan Artifacts

### Scenario

`implementation-plan.md` says:

```text
IP-003 depends on IP-002
```

`implementation-plan-dependencies.md` says:

```text
IP-003 has no dependencies
```

### Expected

```text
FAIL
DEPENDENCY_CONTRADICTION
```

### Acceptance Criteria

The validator MUST NOT silently select one artifact as authoritative.

---

## IPV-R2-T011 — Blocker Artifact Contradiction

### Scenario

`implementation-plan.md`:

```text
IP-005 = READY
```

`implementation-plan-blockers.md`:

```text
IP-005 = BLOCKED
Reason: unresolved required decision
```

### Expected

```text
FAIL
CONTRADICTION
```

### Acceptance Criteria

Conflicting blocker state must be reported.

---

## IPV-R2-T012 — Dev Standard Applies Within Scope

### Scenario

Development standard:

```text
Project A:
Frontend = React
```

Plan:

```text
Project A
IP-001 — Implement approved frontend capability using React
```

### Expected

```text
PASS
```

Evidence:

```text
DEV_STANDARD
```

### Acceptance Criteria

The validator recognizes a technical choice explicitly established by an applicable standard.

---

## IPV-R2-T013 — Dev Standard Outside Applicable Scope

### Scenario

Development standard:

```text
Project A:
Frontend = React
```

Plan:

```text
Project B
IP-001 — Implement approved frontend capability using React
```

No Project B standard or cross-project inheritance is defined.

### Expected

```text
FAIL
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

The validator does not apply a standard outside its declared scope.

---

## IPV-R2-T014 — Inherited Standard with Unspecified Child Value

### Scenario

Standard hierarchy:

```text
Root:
Frontend = React
Backend = Spring Boot

Project:
Backend is not specified
```

Plan:

```text
IP-001 — Implement approved frontend capability using React
IP-002 — Implement approved backend capability using Spring Boot
```

### Expected

```text
PASS
```

### Acceptance Criteria

Unspecified child values inherit applicable parent values.

---

## IPV-R2-T015 — Child Standard Explicitly Overrides Parent

### Scenario

Standard hierarchy:

```text
Root:
Backend = Spring Boot

Project:
Backend = NestJS
```

The standard system explicitly establishes project-over-root precedence.

Plan:

```text
IP-001 — Implement approved backend capability using NestJS
```

### Expected

```text
PASS
```

Evidence:

```text
DEV_STANDARD
```

### Acceptance Criteria

The validator uses explicit precedence rather than assuming parent precedence.

---

## IPV-R2-T016 — Conflicting Standards Without Precedence

### Scenario

Two applicable standards state:

```text
Standard A:
Backend = Spring Boot

Standard B:
Backend = NestJS
```

No precedence rule exists.

Plan:

```text
IP-001 — Implement backend using Spring Boot
```

### Expected

```text
BLOCKED
CONTRADICTION
```

### Acceptance Criteria

The validator does not choose Spring Boot or NestJS based on popularity, recency, or preference.

---

## IPV-R2-T017 — Hidden Unsupported Technology Inside Valid Capability

### Scenario

Approved:

```text
IMP-001 — Implement approved customer profile capability
```

Plan:

```text
IP-001 — Implement customer profile with PostgreSQL persistence.
```

No source establishes PostgreSQL.

### Expected

```text
FAIL
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

A valid capability trace does not authorize unsupported technical details embedded in the task.

---

## IPV-R2-T018 — Cross-Project Dependency with No Evidence

### Scenario

```text
Project A:
IP-A01 — Authentication

Project B:
IP-B01 — Reporting
Depends on IP-A01
```

No approved cross-project dependency exists.

### Expected

```text
FAIL
UNSUPPORTED_CROSS_PROJECT_DEPENDENCY
```

### Acceptance Criteria

Project relationship alone does not justify implementation dependency.

---

## IPV-R2-T019 — Safe Partial Plan with Open Item

### Scenario

Approved scope:

```text
IMP-001 — Report export capability
```

Plan:

```text
IP-001 — Prepare approved report export boundary

Status:
READY WITH OPEN ITEMS

Open:
Exact export format remains undecided.
```

The task does not require the format decision yet.

### Expected

```text
PASS WITH OPEN ITEMS
```

### Acceptance Criteria

The validator recognizes a legitimate non-blocking open item.

---

## IPV-R2-T020 — Fail Must Block Execution

### Scenario

Plan contains:

```text
IP-001 — Customer profile using JWT
```

No source establishes JWT.

Validator detects:

```text
INVENTED_TECHNOLOGY
```

### Expected

```text
FAIL
```

Execution gate:

```text
IMPLEMENTATION EXECUTION: NOT ALLOWED
```

### Acceptance Criteria

A failed validation MUST NOT produce:

```text
IMPLEMENTATION EXECUTION: ALLOWED
```

The validator must preserve the execution boundary.

---

# 3. Round 2 Acceptance Gate

Round 2 passes only when:

```text
20/20 test cases behave as expected
```

AND:

```text
0 false PASS
0 false execution approvals
0 silently repaired contradictions
0 accepted unsupported trace relationships
0 missed blocker propagation errors
0 missed dependency graph errors
0 invalid standard-scope inheritances
```

The validator MUST verify evidence semantics, not merely identifiers.

---

# 4. Round 2 Execution Record

To be completed after execution:

| Test ID     | Expected                | Actual | Result | Notes |
| ----------- | ----------------------- | ------ | ------ | ----- |
| IPV-R2-T001 | FAIL                    | —      | —      | —     |
| IPV-R2-T002 | FAIL                    | —      | —      | —     |
| IPV-R2-T003 | FAIL                    | —      | —      | —     |
| IPV-R2-T004 | FAIL                    | —      | —      | —     |
| IPV-R2-T005 | PASS                    | —      | —      | —     |
| IPV-R2-T006 | PASS                    | —      | —      | —     |
| IPV-R2-T007 | FAIL                    | —      | —      | —     |
| IPV-R2-T008 | PASS                    | —      | —      | —     |
| IPV-R2-T009 | PASS                    | —      | —      | —     |
| IPV-R2-T010 | FAIL                    | —      | —      | —     |
| IPV-R2-T011 | FAIL                    | —      | —      | —     |
| IPV-R2-T012 | PASS                    | —      | —      | —     |
| IPV-R2-T013 | FAIL                    | —      | —      | —     |
| IPV-R2-T014 | PASS                    | —      | —      | —     |
| IPV-R2-T015 | PASS                    | —      | —      | —     |
| IPV-R2-T016 | BLOCKED / CONTRADICTION | —      | —      | —     |
| IPV-R2-T017 | FAIL                    | —      | —      | —     |
| IPV-R2-T018 | FAIL                    | —      | —      | —     |
| IPV-R2-T019 | PASS WITH OPEN ITEMS    | —      | —      | —     |
| IPV-R2-T020 | FAIL                    | —      | —      | —     |

---

# 5. Round 2 Gate

```text
ROUND 2

Required:
20/20 PASS

Promotion:
NOT YET

Next:
Round 3 Adversarial
```

A failed validation case MUST NOT trigger an automatic rewrite of the supplied plan.

If a true rule gap is discovered:

```text
identify design gap
        ↓
revise implementation-plan-validator/SKILL.md
        ↓
rerun affected round
        ↓
continue validation
```

Test expectations MUST NOT be weakened merely to obtain PASS.
