# Skill: implementation-plan-validator

**Version:** `v1.0`
**Status:** `LOCKED`

## 1. Purpose

Validate an existing implementation plan produced from approved implementation scope.

The skill determines whether the implementation plan is safe to proceed to implementation execution without:

* unsupported scope;
* broken traceability;
* invalid dependencies;
* dependency cycles;
* incorrect blocker propagation;
* incorrect `OPEN` / `BLOCKED` classification;
* technical hallucination;
* architecture invention;
* business workflow disguised as implementation dependency;
* accidental scope inflation.

The skill validates the plan.

It does **not** redesign the plan, invent missing implementation work, or write application code.

### Core principle

> **Validate the plan against approved evidence; do not improve the plan by inventing missing decisions.**

---

## 2. Scope Boundary

Skill 14 validates:

```text
implementation-plan
        ↓
validation
        ↓
PASS / PASS WITH OPEN ITEMS / BLOCKED / FAIL
```

It MUST NOT:

* create new implementation scope;
* silently repair unsupported tasks;
* infer missing technical decisions;
* infer missing business workflows;
* add dependencies;
* add architecture;
* add infrastructure;
* add testing requirements;
* convert `OPEN` into a concrete decision;
* convert `UNKNOWN` into a concrete decision.

A validator finding a problem MUST report the problem rather than silently fixing it.

---

## 3. Inputs

Primary inputs:

* `implementation-plan.md`;
* `implementation-plan-dependencies.md`;
* `implementation-plan-blockers.md`;
* approved `implementation/SKILL.md`;
* approved implementation outputs from Skill 12;
* `implementation-readiness` result;
* approved blueprint;
* functional requirements;
* business rules;
* NFRs;
* applicable `dev-standards/DEV-STANDARDS.md`.

Optional inputs:

* `implementation-plan-open-items.md`;
* `implementation-plan-progress.md`;
* approved developer decisions;
* existing project structure;
* existing implementation status.

The validator MUST distinguish between:

```text
available evidence
```

and:

```text
information merely present in the plan
```

A plan claiming a decision does not prove that the decision is supported.

---

## 4. Outputs

The skill may produce:

```text
implementation-plan-validation.md
```

Optional:

```text
implementation-plan-validation-traceability.md
implementation-plan-validation-dependencies.md
implementation-plan-validation-blockers.md
implementation-plan-validation-findings.md
```

The validator output MUST identify:

* validation result;
* detected issues;
* evidence used;
* affected plan items;
* severity;
* blocking impact;
* unresolved questions where relevant.

---

## 5. Evidence Classification

Validation findings SHOULD use:

| Classification   | Meaning                                                               |
| ---------------- | --------------------------------------------------------------------- |
| `SOURCE_STATED`  | Explicitly supported by upstream evidence                             |
| `DERIVED`        | Directly and safely derived from evidence                             |
| `DEV_STANDARD`   | Supported by an applicable development standard                       |
| `IMPLEMENTATION` | Supported by approved implementation scope or decision                |
| `OPEN`           | Required information remains unresolved                               |
| `UNKNOWN`        | Required information is unavailable                                   |
| `BLOCKED`        | Missing/conflicting information prevents safe validation or execution |
| `CONTRADICTION`  | Relevant sources contain conflicting decisions                        |

The validator MUST NOT classify an unsupported plan detail as `DERIVED` merely because it appears reasonable.

---

## 6. Validation Order

Validation SHOULD follow this order:

```text
1. Input integrity
2. Traceability
3. Scope compliance
4. Dependency validity
5. Dependency cycle detection
6. Blocker propagation
7. OPEN / BLOCKED classification
8. Technical decision compliance
9. Architecture / infrastructure compliance
10. Business workflow boundary
11. Scope inflation
12. Final quality gate
```

A failure at one stage MUST NOT cause the validator to invent corrections for later stages.

---

## 7. Input Integrity

Before validating content, confirm that required validation inputs are available.

If a required validation source is unavailable:

```text
BLOCKED
```

The validator MUST NOT assume missing evidence.

A missing optional artifact does not automatically block validation.

---

## 8. Traceability Validation

Every plan item MUST trace to:

* an approved implementation item;
* an applicable development standard;
* an approved developer decision;
* or another explicitly supporting upstream artifact.

A trace is valid only if the cited upstream artifact actually supports the work claimed by the plan item.

Missing trace:

```text
ORPHAN_PLAN_ITEM
```

Result:

```text
FAIL
```

A valid trace is necessary but not sufficient.

---

## 9. Scope Validation

For every plan item, verify:

```text
planned work
        ↓
supported by approved scope?
```

The validator MUST reject:

* unsupported feature additions;
* unsupported validation rules;
* unsupported notifications;
* unsupported integrations;
* unsupported reports;
* unsupported security controls;
* unsupported infrastructure;
* unsupported operational tasks.

A plan item that is professionally reasonable but unsupported remains invalid.

---

## 10. CRUD Validation

The validator MUST detect unjustified CRUD expansion.

`manage X` does not automatically authorize:

```text
Create
Read
Update
Delete
```

unless CRUD was explicitly approved.

Finding:

```text
INVENTED_CRUD
```

---

## 11. Dependency Validation

Every dependency MUST have an implementation prerequisite basis.

Dependencies MUST NOT be accepted solely because:

* tasks are related;
* one appears more fundamental;
* one appears earlier in a file;
* one sounds like a parent task;
* one is a common business sequence;
* one is a common architecture sequence.

Invalid dependency:

```text
INVENTED_DEPENDENCY
```

---

## 12. Business Workflow Detection

Implementation dependency and product workflow MUST remain separate.

Example:

```text
Reservation
    ↓
Payment
    ↓
Check-in
```

does not automatically establish implementation dependencies.

Finding:

```text
BUSINESS_WORKFLOW_AS_DEPENDENCY
```

---

## 13. Dependency Graph Validation

The validator MUST check the dependency graph globally.

It MUST detect:

```text
DEPENDENCY_CYCLE
INVALID_SELF_DEPENDENCY
BROKEN_DEPENDENCY_REFERENCE
```

A valid diamond graph MUST NOT be falsely classified as a cycle.

---

## 14. Dependency Consistency

All dependency artifacts MUST agree.

For example:

```text
implementation-plan.md
IP-003 depends on IP-002
```

must not conflict with:

```text
implementation-plan-dependencies.md
IP-003 has no dependencies
```

Conflict:

```text
FAIL
DEPENDENCY_CONTRADICTION
```

The validator MUST NOT choose one silently.

---

## 15. Blocker Validation

The validator MUST verify blocker propagation through dependency edges only.

Example:

```text
IP-001 BLOCKED
IP-002 depends on IP-001
IP-003 independent
```

must result in:

```text
IP-001 BLOCKED
IP-002 BLOCKED
IP-003 READY
```

Incorrect propagation:

```text
INVALID_BLOCKER_PROPAGATION
```

---

## 16. Partial Blocker Validation

If a plan item combines supported and blocked work, the validator MUST determine whether the blocked portion prevents safe execution of the whole item.

If it does:

```text
BLOCKED
```

If safe separation is possible, report:

```text
PLAN_SPLIT_RECOMMENDED
```

The validator MUST NOT silently split the plan.

---

## 17. OPEN vs BLOCKED Validation

The validator MUST verify that `OPEN` does not hide a true blocker.

Example:

```text
Required payment provider = OPEN
Payment implementation cannot proceed without it
```

Correct result:

```text
BLOCKED
```

Conversely, a non-blocking open item may remain:

```text
PASS WITH OPEN ITEMS
```

The validator MUST NOT force every `OPEN` item into `BLOCKED`.

---

## 18. Status Validation

Allowed plan/task statuses:

```text
READY
READY WITH OPEN ITEMS
BLOCKED
IN PROGRESS
COMPLETED
```

Business statuses MUST NOT be treated as plan statuses unless explicitly defined as such.

---

## 19. Technology Validation

Unsupported technologies MUST be detected.

Examples:

```text
PostgreSQL
MySQL
Redis
Docker
Kubernetes
JWT
OAuth2
REST
GraphQL
```

require support from:

* approved implementation;
* applicable dev standard;
* approved developer decision.

Finding:

```text
INVENTED_TECHNOLOGY
```

---

## 20. Architecture Validation

Unsupported architecture decisions MUST be detected.

Examples:

```text
Controller
Service
Repository
DTO
Mapper
microservice
API gateway
event bus
message queue
caching layer
```

Finding:

```text
INVENTED_ARCHITECTURE
```

---

## 21. Database Validation

Unsupported database structure MUST be detected.

Examples:

```text
table
column
primary key
foreign key
index
unique constraint
UUID
soft delete
optimistic locking
```

Finding:

```text
INVENTED_DATABASE_DETAIL
```

---

## 22. Security Validation

Unsupported security expansion MUST be detected.

Examples:

```text
JWT
refresh token
MFA
rate limiting
account lockout
password policy
security headers
```

Finding:

```text
INVENTED_SECURITY_SCOPE
```

---

## 23. Testing Validation

Testing work requires evidence.

Unsupported testing scope includes:

```text
unit testing
integration testing
API testing
E2E testing
load testing
security testing
performance testing
```

Finding:

```text
INVENTED_TESTING_SCOPE
```

---

## 24. DevOps / Operational Validation

Unsupported operational scope includes:

```text
CI/CD
Docker
Kubernetes
monitoring
observability
health checks
logging platform
deployment pipeline
```

Finding:

```text
INVENTED_OPERATIONAL_SCOPE
```

---

## 25. Notification and Integration Validation

The validator MUST detect unsupported:

```text
email
SMS
push notification
webhook
third-party integration
payment provider
external service
```

unless explicitly approved.

---

## 26. Cross-Project Validation

Project similarity does not establish dependency.

The validator MUST reject unsupported:

```text
cross-project dependency
shared auth platform
shared database
API gateway
shared infrastructure
```

Finding:

```text
UNSUPPORTED_CROSS_PROJECT_DEPENDENCY
```

---

## 27. Scope Inflation Validation

The validator MUST compare the entire plan against approved scope.

A technically coherent ecosystem surrounding a small approved capability is still invalid when unsupported.

Finding:

```text
SCOPE_INFLATION
```

---

## 28. Technical Chain Validation

The validator MUST inspect the root evidence of technical chains.

Example:

```text
React
↓
React Hook Form
↓
Yup
↓
Axios
↓
REST API
↓
JWT
↓
Redis
```

Compatibility is not evidence.

---

## 29. Minimality Check

The validator SHOULD detect tasks added only to make the plan appear complete.

It MUST distinguish:

```text
missing necessary task
```

from:

```text
invented task
```

It MUST NOT automatically add the missing task.

---

## 30. Plan Completeness Boundary

Completeness means:

```text
all approved implementation scope is adequately planned
+
all planned work is evidence-supported
+
dependencies are valid
+
blockers are correctly represented
```

It does not mean:

```text
every possible engineering task exists
```

---

## 31. Validation Findings

Each finding SHOULD contain:

```text
Finding ID
Severity
Affected Plan Item
Rule
Evidence
Observed Condition
Expected Condition
Result
Blocking Impact
```

Example:

```text
VAL-001

Severity: HIGH

Affected Item:
IP-007

Rule:
Technology Validation

Evidence:
No approved source establishes Redis.

Observed:
IP-007 requires Redis.

Expected:
No unsupported technology should be introduced.

Result:
FAIL
INVENTED_TECHNOLOGY

Blocking Impact:
Blocks plan validation.
```

---

## 32. Severity

Suggested severity levels:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Severity MUST reflect actual impact and MUST NOT override evidence classification.

---

## 33. Contradiction Handling

When relevant sources conflict and no precedence or resolution exists:

```text
BLOCKED
CONTRADICTION
```

The validator MUST NOT choose based on:

* popularity;
* convenience;
* assumed recency;
* personal preference;
* filename;
* framework familiarity.

---

## 34. Validator Non-Interference Rule

Skill 14 MUST NOT silently modify:

```text
plan item
dependency
status
scope
technical choice
blocker
open item
```

When a problem exists, report the problem.

The validator MUST NOT:

```text
add traceability
remove dependencies
invent replacement dependencies
change statuses
rewrite the plan
insert missing implementation tasks
```

---

## 35. Validation Result

Possible overall results:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

### PASS

All required validations pass.

### PASS WITH OPEN ITEMS

The plan is safe for supported work while non-blocking questions remain.

### BLOCKED

Required evidence is unavailable or unresolved contradiction prevents safe validation.

### FAIL

The plan contains one or more invalid conditions.

---

## 36. Quality Gate

The validator passes only when:

```text
100% plan items traceable

AND

100% dependencies valid

AND

0 dependency cycles

AND

0 broken dependency references

AND

0 unsupported scope additions

AND

0 unsupported technical decisions

AND

0 invalid blocker propagation

AND

OPEN / BLOCKED classifications are valid

AND

no unresolved planning contradiction exists
```

---

## 37. Final Decision Contract

The final validator result MUST explicitly contain:

```text
Validation Result
Blocking Findings
Non-Blocking Findings
Traceability Result
Dependency Result
Blocker Result
Scope Result
Technical Decision Result
Open Item Result
Recommendation
```

Example:

```text
Validation Result:
PASS

Blocking Findings:
0

Non-Blocking Findings:
2

Traceability:
PASS

Dependencies:
PASS

Blockers:
PASS

Scope:
PASS

Technical Decisions:
PASS

Open Items:
PASS WITH OPEN ITEMS

Recommendation:
ALLOW IMPLEMENTATION EXECUTION
```

For a failed plan:

```text
Validation Result:
FAIL

Blocking Findings:
3

Recommendation:
DO NOT ALLOW IMPLEMENTATION EXECUTION
```

---

## 38. Execution Gate

```text
PASS
        ↓
IMPLEMENTATION EXECUTION: ALLOWED
```

```text
PASS WITH OPEN ITEMS
        ↓
IMPLEMENTATION EXECUTION: ALLOWED
FOR SUPPORTED / NON-BLOCKED WORK
```

```text
BLOCKED
        ↓
IMPLEMENTATION EXECUTION: NOT ALLOWED
FOR BLOCKED SCOPE
```

```text
FAIL
        ↓
IMPLEMENTATION EXECUTION: NOT ALLOWED
```

---

## 39. Golden Rules

> Validate the plan; do not redesign it.

> Evidence validates a plan; plausibility does not.

> Traceability is necessary but not sufficient.

> A valid trace does not authorize unrelated work.

> Dependency is an implementation prerequisite, not a business workflow.

> Open remains OPEN.

> Blocked remains BLOCKED.

> Unsupported technical choices remain unsupported.

> Reasonable defaults are not evidence.

> Do not repair hallucinations by inventing replacements.

> Do not add missing implementation scope.

> Do not silently modify the plan.

> No application code is generated by this skill.

---

# Skill 14 — Implementation Plan Validator

## Regression Result

**Skill Version:** `v1.0`

**Status:** `LOCKED`

**Regression Scope:** Round 1 + Round 2 + Round 3

**Total Test Cases:** `60`

### Result

| Round                 |  Cases | Result         |
| --------------------- | -----: | -------------- |
| Round 1               |     20 | **20/20 PASS** |
| Round 2               |     20 | **20/20 PASS** |
| Round 3 — Adversarial |     20 | **20/20 PASS** |
| **Total**             | **60** | **60/60 PASS** |

### Regression Quality Gate

* Traceability validation: **PASS**
* Semantic trace validation: **PASS**
* Orphan detection: **PASS**
* Unsupported scope detection: **PASS**
* CRUD expansion detection: **PASS**
* Dependency validation: **PASS**
* Dependency cycle detection: **PASS**
* Broken dependency detection: **PASS**
* Blocker propagation: **PASS**
* `OPEN` vs `BLOCKED`: **PASS**
* Dev Standard scope/inheritance: **PASS**
* Technology invention detection: **PASS**
* Architecture invention detection: **PASS**
* Database invention detection: **PASS**
* Security scope detection: **PASS**
* Testing scope detection: **PASS**
* Operational/DevOps scope detection: **PASS**
* Business workflow dependency detection: **PASS**
* Cross-project assumption detection: **PASS**
* Scope inflation detection: **PASS**
* Contradiction detection: **PASS**
* Validator non-interference: **PASS**
* Execution gate: **PASS**

### Final Verdict

**REGRESSION: 60/60 PASS**

**Skill 14 v1.0 satisfies the complete regression suite.**

**Promotion: `v0.1 → v1.0`**

**Status: `LOCKED`**

No behavioral changes should be made directly to `v1.0`. Any future change MUST open a new version and repeat the required validation and regression process.
