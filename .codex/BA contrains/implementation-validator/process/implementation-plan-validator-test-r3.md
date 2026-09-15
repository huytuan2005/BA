# Skill 14 — Implementation Plan Validator

# `implementation-plan-validator-test.md`

**Version:** `v0.1`
**Validation Round:** `Round 3 — Adversarial`
**Total Test Cases:** `20`

---

## 1. Objective

Round 3 is designed to attack the validator with implementation plans that appear professional, complete, traceable, and technically coherent.

The adversarial objective is to detect:

* semantic traceability laundering;
* hidden scope expansion;
* dependency laundering;
* disguised business workflow;
* fake blocker propagation;
* false OPEN classification;
* architecture hiding inside task wording;
* technology hiding inside implementation language;
* cross-project assumptions;
* unsupported testing and operational scope;
* contradiction masking;
* validator bypass through task aggregation;
* validator bypass through decomposition;
* false completeness.

### Core adversarial principle

> **A plan is not valid merely because every field is filled, every ID exists, or the technical chain looks coherent.**

---

# 2. Expected Decision Model

Every adversarial case MUST produce the expected validation result.

An adversarial test passes when:

```text
validator correctly detects the hidden violation
```

A technically plausible plan is still invalid when evidence does not support it.

---
## 3. Explicit Test Input Format

Every Round 3 test case MUST provide a self-contained validation input.

The input MUST be separated into:

```text
INPUT
├── Approved Evidence
├── Implementation Plan
├── Dependency Data
├── Blocker Data
├── Open Items
└── Applicable Dev Standards
```

### 3.1 Approved Evidence

Contains only information that the validator is allowed to treat as authoritative.

Example:

```yaml
approved_implementation:
  - id: IMP-001
    description: "Customer profile viewing capability"

approved_developer_decisions: []

applicable_dev_standards: []
```

### 3.2 Implementation Plan

Contains the actual plan being validated.

Example:

```yaml
plan:
  - id: IP-001
    title: "Implement customer profile viewing"
    traceability:
      - IMP-001
    evidence: IMPLEMENTATION
    dependencies: []
    status: READY
```

### 3.3 Dependency Data

When dependencies are represented separately:

```yaml
dependencies:
  - from: IP-002
    to: IP-001
```

The validator MUST validate both:

```text
plan item dependency declarations
```

and:

```text
implementation-plan-dependencies.md
```

when both are provided.

### 3.4 Blocker Data

Example:

```yaml
blockers:
  - plan_item: IP-003
    status: BLOCKED
    reason: "Required approved technical decision is unresolved"
```

### 3.5 Open Items

Example:

```yaml
open_items:
  - plan_item: IP-005
    item: "Exact report export format is unresolved"
    blocking: false
```

### 3.6 Applicable Development Standards

Example:

```yaml
dev_standards:
  - scope: project-a
    values:
      frontend: React
```

A standard MUST only apply within its explicitly established scope.

---

## 4. Explicit Validator Output Format

Every validation execution MUST produce a structured result.

Minimum required format:

```yaml
validation:
  result: PASS | PASS_WITH_OPEN_ITEMS | BLOCKED | FAIL

  execution_gate:
    implementation_execution: ALLOWED | NOT_ALLOWED

  summary:
    total_plan_items: <number>
    valid_plan_items: <number>
    invalid_plan_items: <number>
    total_dependencies: <number>
    valid_dependencies: <number>
    invalid_dependencies: <number>

  findings:
    - id: VAL-001
      severity: CRITICAL | HIGH | MEDIUM | LOW
      affected_item: IP-001
      rule: <validation rule>
      classification: SOURCE_STATED | DERIVED | DEV_STANDARD | IMPLEMENTATION | OPEN | UNKNOWN | BLOCKED | CONTRADICTION
      code: <finding code>
      message: <finding description>
      blocking: true | false

  traceability:
    result: PASS | FAIL

  dependencies:
    result: PASS | FAIL

  blockers:
    result: PASS | FAIL

  open_items:
    result: PASS | PASS_WITH_OPEN_ITEMS | FAIL

  scope:
    result: PASS | FAIL

  technical_decisions:
    result: PASS | FAIL

  recommendation:
    ALLOW_IMPLEMENTATION_EXECUTION
    | ALLOW_SUPPORTED_NON_BLOCKED_WORK
    | DO_NOT_ALLOW_IMPLEMENTATION_EXECUTION
```

---

## 5. Output Contract

The validator MUST satisfy these rules:

### 5.1 Result

Exactly one overall result:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

### 5.2 Execution Gate

The execution gate MUST be consistent with the result:

```text
PASS
→ ALLOWED
```

```text
PASS WITH OPEN ITEMS
→ ALLOWED
for supported / non-blocked work
```

```text
BLOCKED
→ NOT ALLOWED
for blocked scope
```

```text
FAIL
→ NOT ALLOWED
```

### 5.3 Findings

Every detected issue MUST have:

```text
Finding ID
Severity
Affected Item
Rule
Classification
Finding Code
Message
Blocking Impact
```

The validator MUST NOT report only:

```text
FAIL
```

without identifying why the plan failed.

### 5.4 No Silent Repair

The output MUST report the supplied plan state.

It MUST NOT rewrite:

```text
plan items
dependencies
statuses
technical choices
blockers
open items
```

### 5.5 Evidence vs Claim

The validator MUST distinguish:

```text
plan claims:
"uses PostgreSQL"
```

from:

```text
approved evidence:
no source establishes PostgreSQL
```

Therefore the output SHOULD identify the unsupported claim explicitly:

```yaml
finding:
  code: INVENTED_TECHNOLOGY
  message: "Plan uses PostgreSQL, but no approved evidence establishes PostgreSQL."
```

---

## 6. Canonical PASS Example

### Input

```yaml
approved_implementation:
  - id: IMP-001
    description: "Customer profile viewing capability"

plan:
  - id: IP-001
    title: "Implement customer profile viewing"
    traceability: [IMP-001]
    evidence: IMPLEMENTATION
    dependencies: []
    status: READY

dependencies: []
blockers: []
open_items: []
dev_standards: []
```

### Expected Validator Output

```yaml
validation:
  result: PASS

  execution_gate:
    implementation_execution: ALLOWED

  summary:
    total_plan_items: 1
    valid_plan_items: 1
    invalid_plan_items: 0
    total_dependencies: 0
    valid_dependencies: 0
    invalid_dependencies: 0

  findings: []

  traceability:
    result: PASS

  dependencies:
    result: PASS

  blockers:
    result: PASS

  open_items:
    result: PASS

  scope:
    result: PASS

  technical_decisions:
    result: PASS

  recommendation: ALLOW_IMPLEMENTATION_EXECUTION
```

---

## 7. Canonical FAIL Example

### Input

```yaml
approved_implementation:
  - id: IMP-001
    description: "Customer profile capability"

plan:
  - id: IP-001
    title: "Implement customer profile using PostgreSQL and JWT"
    traceability: [IMP-001]
    evidence: IMPLEMENTATION
    dependencies: []
    status: READY

dependencies: []
blockers: []
open_items: []
dev_standards: []
```

### Expected Validator Output

```yaml
validation:
  result: FAIL

  execution_gate:
    implementation_execution: NOT_ALLOWED

  summary:
    total_plan_items: 1
    valid_plan_items: 0
    invalid_plan_items: 1
    total_dependencies: 0
    valid_dependencies: 0
    invalid_dependencies: 0

  findings:
    - id: VAL-001
      severity: HIGH
      affected_item: IP-001
      rule: Technology Validation
      classification: UNKNOWN
      code: INVENTED_TECHNOLOGY
      message: "Plan uses PostgreSQL, but no approved evidence establishes PostgreSQL."
      blocking: true

    - id: VAL-002
      severity: HIGH
      affected_item: IP-001
      rule: Security Validation
      classification: UNKNOWN
      code: INVENTED_SECURITY_SCOPE
      message: "Plan uses JWT, but no approved evidence establishes JWT."
      blocking: true

  traceability:
    result: PASS

  dependencies:
    result: PASS

  blockers:
    result: PASS

  open_items:
    result: PASS

  scope:
    result: FAIL

  technical_decisions:
    result: FAIL

  recommendation: DO_NOT_ALLOW_IMPLEMENTATION_EXECUTION
```

---

## 8. Round 3 Test Case Requirement

Every adversarial test case MUST contain:

```text
### Input

### Expected Validator Output

### Expected Findings

### Expected Execution Gate
```

The test MUST evaluate the structured validator output, not only the final PASS/FAIL word.

A Round 3 test passes only when:

```text
overall result
+
finding classification
+
finding code
+
affected item
+
execution gate
```

all match the expected contract.

---

## 9. Adversarial Test Integrity

The validator MUST NOT be able to pass a testcase merely by returning:

```text
FAIL
```

when the case requires a specific violation.

For example, a case expecting:

```text
INVENTED_DEPENDENCY
```

does not fully pass if the validator reports only:

```text
UNSUPPORTED_SCOPE
```

unless the test explicitly allows multiple equivalent finding codes.

Where a test specifies a required code, the code MUST match.

# 3. Round 3 Adversarial Cases

## IPV-R3-T001 — Traceability Laundering Through Broad Requirement

### Scenario

Approved implementation:

```text
IMP-001 — Customer profile viewing
```

Plan:

```text
IP-001 — Implement customer profile management

Traceability:
IMP-001
```

The phrase “management” is broader than the approved “viewing”.

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

The validator MUST detect scope expansion even though the trace ID exists.

---

## IPV-R3-T002 — Aggregated Task Hides Unsupported Subtask

### Scenario

Approved:

```text
IMP-001 — Customer profile
IMP-002 — Customer login
```

Plan:

```text
IP-001 — Implement customer account capabilities

Includes:
- profile
- login
- email verification
- password reset
- MFA

Traceability:
IMP-001
IMP-002
```

Only profile and login are approved.

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

The validator MUST inspect contained work, not validate only the task title.

---

## IPV-R3-T003 — Decomposition Hides Unsupported Work

### Scenario

Approved:

```text
IMP-001 — Customer profile viewing
```

Plan:

```text
IP-001 — Profile preparation
        Trace: IMP-001

IP-002 — Profile API endpoint
        Trace: IMP-001

IP-003 — Profile database schema
        Trace: IMP-001

IP-004 — Profile caching
        Trace: IMP-001
```

No API, database, or caching decisions were approved.

### Expected

```text
FAIL
```

with findings such as:

```text
INVENTED_API
INVENTED_DATABASE_DETAIL
INVENTED_ARCHITECTURE
```

### Acceptance Criteria

Splitting a plan into smaller items MUST NOT make unsupported work valid.

---

## IPV-R3-T004 — “Supporting Task” Loophole

### Scenario

Plan:

```text
IP-001 — Implement approved customer profile
Traceability: IMP-001

IP-002 — Setup Redis to support IP-001
Traceability: DEV_STANDARD-001
```

The cited standard establishes only:

```text
Frontend = React
```

### Expected

```text
FAIL
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

A task labelled “supporting” does not inherit authorization that the cited source does not contain.

---

## IPV-R3-T005 — Dependency Laundering Through “Preparation”

### Scenario

```text
IP-001 — Prepare customer profile architecture
IP-002 — Implement customer profile
```

Plan says:

```text
IP-002 depends on IP-001
```

But approved implementation contains only a profile capability and no architecture prerequisite.

### Expected

```text
FAIL
INVENTED_DEPENDENCY
INVENTED_ARCHITECTURE
```

### Acceptance Criteria

A technically natural preparation step cannot create its own legitimacy.

---

## IPV-R3-T006 — Business Workflow Hidden in Technical Labels

### Scenario

```text
IP-001 — Reservation component
IP-002 — Payment component
IP-003 — Check-in component
```

Plan dependencies:

```text
IP-002 → IP-001
IP-003 → IP-002
```

No approved implementation establishes the sequence.

### Expected

```text
FAIL
BUSINESS_WORKFLOW_AS_DEPENDENCY
```

### Acceptance Criteria

Replacing business nouns with “component” does not change the dependency semantics.

---

## IPV-R3-T007 — Dependency Justified by “Data Availability”

### Scenario

```text
IP-001 — Customer profile
IP-002 — Rental dashboard
```

Plan says:

```text
IP-002 depends on IP-001
Reason:
Rental dashboard needs customer data.
```

No approved implementation establishes this prerequisite.

### Expected

```text
FAIL
INVENTED_DEPENDENCY
```

### Acceptance Criteria

A plausible data relationship is not automatically an implementation prerequisite.

---

## IPV-R3-T008 — False Blocker Created by Aggregate Dependency

### Scenario

```text
IP-001 = BLOCKED

IP-002 = profile UI
IP-003 = report UI

IP-004 = combined dashboard
```

Plan declares:

```text
IP-004 depends on IP-001
```

but approved scope allows IP-004 to be implemented using already approved independent data.

### Expected

```text
FAIL
INVALID_BLOCKER_PROPAGATION
```

### Acceptance Criteria

The validator MUST inspect whether the declared dependency itself is valid before propagating blockers.

---

## IPV-R3-T009 — Blocker Masked by Status Manipulation

### Scenario

Plan:

```text
IP-001 = READY

Open item:
Required payment provider decision is unresolved.

Implementation cannot proceed without provider.
```

### Expected

```text
FAIL
INVALID_OPEN_BLOCKED_CLASSIFICATION
```

### Acceptance Criteria

The validator MUST infer execution impact from the unresolved prerequisite, not trust the declared status.

---

## IPV-R3-T010 — Unsupported Technology Hidden in Generic Wording

### Scenario

Plan:

```text
IP-001 — Persist customer profile in the production data store
```

Implementation notes state:

```text
Use PostgreSQL with UUID identifiers.
```

No source establishes PostgreSQL or UUID.

### Expected

```text
FAIL
INVENTED_TECHNOLOGY
INVENTED_DATABASE_DETAIL
```

### Acceptance Criteria

Generic task language does not shield unsupported technical details in notes.

---

## IPV-R3-T011 — Architecture Hidden Inside Output Names

### Scenario

Plan outputs:

```text
CustomerController
CustomerService
CustomerRepository
CustomerDTO
```

The plan never explicitly says “architecture”, but these outputs imply it.

### Expected

```text
FAIL
INVENTED_ARCHITECTURE
```

### Acceptance Criteria

Validator checks the actual proposed artifacts, not only task descriptions.

---

## IPV-R3-T012 — Testing Hidden as “Definition of Done”

### Scenario

Plan item:

```text
IP-005 — Implement approved rental capability

Definition of Done:
- implementation complete
- unit tests complete
- integration tests complete
- API tests complete
- E2E tests complete
```

No testing scope is approved.

### Expected

```text
FAIL
INVENTED_TESTING_SCOPE
```

### Acceptance Criteria

Definition-of-done text is part of the plan and must be validated.

---

## IPV-R3-T013 — Security Hidden as Acceptance Criteria

### Scenario

Plan item:

```text
IP-006 — Implement approved login capability
```

Acceptance criteria include:

```text
JWT authentication
refresh token
MFA
rate limiting
account lockout
```

No source supports these.

### Expected

```text
FAIL
INVENTED_SECURITY_SCOPE
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

Unsupported security requirements embedded in acceptance criteria MUST be detected.

---

## IPV-R3-T014 — Notification Hidden in “Post-Implementation”

### Scenario

Plan:

```text
IP-007 — Complete reservation capability

Post-implementation:
- send email confirmation
- send SMS reminder
```

No notification requirement exists.

### Expected

```text
FAIL
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

Work appended outside the core task remains part of the plan scope.

---

## IPV-R3-T015 — Cross-Project Dependency via “Shared Authentication”

### Scenario

```text
Project A:
IP-A01 — Login

Project B:
IP-B01 — Reporting
```

Plan says:

```text
IP-B01 depends on IP-A01

Reason:
Both systems share authentication.
```

No cross-project authorization exists.

### Expected

```text
FAIL
UNSUPPORTED_CROSS_PROJECT_DEPENDENCY
```

### Acceptance Criteria

“Shared” terminology is not evidence.

---

## IPV-R3-T016 — Shared Infrastructure Smuggled Through Nonfunctional Language

### Scenario

Plan:

```text
IP-008 — Prepare production-ready environment
```

Notes:

```text
Kubernetes
Redis
Nginx
centralized logging
monitoring
```

No infrastructure standard supports them.

### Expected

```text
FAIL
INVENTED_OPERATIONAL_SCOPE
INVENTED_TECHNOLOGY
```

### Acceptance Criteria

“Production-ready” MUST NOT become authorization for infrastructure expansion.

---

## IPV-R3-T017 — False Completeness Trap

### Scenario

Approved implementation:

```text
IMP-001 — Customer profile
IMP-002 — Rental reporting
```

Plan:

```text
IP-001 — Profile UI
IP-002 — Profile backend
IP-003 — Reporting UI
IP-004 — Reporting backend
IP-005 — Search
IP-006 — Pagination
IP-007 — Audit logging
IP-008 — Notifications
```

The plan claims:

```text
Status: COMPLETE
```

Only the first four items are supported.

### Expected

```text
FAIL
SCOPE_INFLATION
```

### Acceptance Criteria

Task status `COMPLETE` MUST NOT override unsupported additions.

---

## IPV-R3-T018 — Contradiction Hidden by Duplicated Plan Entries

### Scenario

Plan contains:

```text
IP-010 — Customer profile

Status: READY
```

and later:

```text
IP-010 — Customer profile

Status: BLOCKED
Reason:
Missing approved technical decision.
```

### Expected

```text
FAIL
CONTRADICTION
```

### Acceptance Criteria

Duplicate IDs with inconsistent states MUST NOT be silently merged.

---

## IPV-R3-T019 — Reasonable Dependency Chain Trap

### Scenario

Plan:

```text
IP-001 — Frontend profile
IP-002 — Backend profile
IP-003 — Database profile
```

Dependencies:

```text
IP-002 → IP-001
IP-003 → IP-002
```

Reason:

> This is the normal frontend → backend → database implementation order.

No architectural order is approved.

### Expected

```text
FAIL
INVENTED_DEPENDENCY
INVENTED_ARCHITECTURE
```

### Acceptance Criteria

“Normal engineering order” is not evidence.

---

## IPV-R3-T020 — Nuclear Full-Stack Plan

### Scenario

Approved implementation:

```text
IMP-001 — Customer registration capability
IMP-002 — Customer login capability
```

Plan:

```text
IP-001 React frontend
IP-002 React Hook Form
IP-003 Yup validation
IP-004 Spring Boot backend
IP-005 REST API
IP-006 PostgreSQL database
IP-007 users table
IP-008 UUID
IP-009 BCrypt
IP-010 JWT
IP-011 refresh token
IP-012 Redis
IP-013 Docker
IP-014 CI/CD
IP-015 email verification
IP-016 rate limiting
IP-017 monitoring
IP-018 E2E tests
IP-019 API tests
IP-020 deployment pipeline
```

The plan looks like a complete professional implementation plan.

However, only registration and login capabilities are approved. No technical stack, security mechanisms, infrastructure, notification behavior, or testing scope are established.

### Expected

```text
FAIL
```

Findings SHOULD include multiple unsupported categories:

```text
INVENTED_TECHNOLOGY
INVENTED_DATABASE_DETAIL
INVENTED_SECURITY_SCOPE
INVENTED_OPERATIONAL_SCOPE
INVENTED_TESTING_SCOPE
UNSUPPORTED_SCOPE
```

### Acceptance Criteria

This test MUST NOT pass merely because:

* every task looks professionally reasonable;
* the technologies are compatible;
* the tasks form a coherent architecture;
* the tasks are all traceable to registration/login;
* the plan appears implementation-complete.

The validator MUST reject unsupported technical-chain construction at the root.

---

# 4. Round 3 Acceptance Gate

Round 3 passes only when:

```text id="v0w7f0"
20/20 adversarial cases are correctly detected
```

AND:

```text id="w4z5j5"
0 false PASS
0 accepted traceability laundering
0 accepted dependency laundering
0 accepted hidden architecture
0 accepted hidden technology
0 accepted hidden testing scope
0 accepted hidden security scope
0 accepted hidden operational scope
0 accepted business workflow dependencies
0 accepted unsupported cross-project assumptions
0 silently repaired plans
```

---

# 5. Adversarial Principles Under Test

Round 3 specifically verifies that Skill 14 can reject:

```text id="2d0opn"
trace ID exists
        ≠
trace evidence supports task
```

```text id="etmzt0"
task split
        ≠
unsupported work becomes valid
```

```text id="0tq1wa"
professional wording
        ≠
approved scope
```

```text id="4j6lhq"
technical compatibility
        ≠
technical authorization
```

```text id="vpxvkk"
reasonable dependency
        ≠
real implementation prerequisite
```

```text id="l1w7qv"
READY / COMPLETE label
        ≠
safe execution
```

```text id="h72r3n"
shared project concept
        ≠
cross-project dependency
```

```text id="9b1my4"
definition of done / notes / acceptance criteria
        ≠
permission to invent work
```

---

# 6. Round 3 Execution Record

To be completed after execution:

| Test ID     | Expected | Actual | Result | Notes |
| ----------- | -------- | ------ | ------ | ----- |
| IPV-R3-T001 | FAIL     | —      | —      | —     |
| IPV-R3-T002 | FAIL     | —      | —      | —     |
| IPV-R3-T003 | FAIL     | —      | —      | —     |
| IPV-R3-T004 | FAIL     | —      | —      | —     |
| IPV-R3-T005 | FAIL     | —      | —      | —     |
| IPV-R3-T006 | FAIL     | —      | —      | —     |
| IPV-R3-T007 | FAIL     | —      | —      | —     |
| IPV-R3-T008 | FAIL     | —      | —      | —     |
| IPV-R3-T009 | FAIL     | —      | —      | —     |
| IPV-R3-T010 | FAIL     | —      | —      | —     |
| IPV-R3-T011 | FAIL     | —      | —      | —     |
| IPV-R3-T012 | FAIL     | —      | —      | —     |
| IPV-R3-T013 | FAIL     | —      | —      | —     |
| IPV-R3-T014 | FAIL     | —      | —      | —     |
| IPV-R3-T015 | FAIL     | —      | —      | —     |
| IPV-R3-T016 | FAIL     | —      | —      | —     |
| IPV-R3-T017 | FAIL     | —      | —      | —     |
| IPV-R3-T018 | FAIL     | —      | —      | —     |
| IPV-R3-T019 | FAIL     | —      | —      | —     |
| IPV-R3-T020 | FAIL     | —      | —      | —     |

---

# 7. Round 3 Gate

```text
ROUND 3 — ADVERSARIAL

Required:
20/20 PASS

Promotion:
NOT YET

Next:
Regression 60
```

If any adversarial case exposes a rule gap:

```text
identify design gap
        ↓
revise implementation-plan-validator/SKILL.md
        ↓
rerun affected round
        ↓
rerun regression
```

Expected results MUST NOT be weakened merely to obtain PASS.
