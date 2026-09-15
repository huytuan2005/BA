---
name: implementation-closure
description: Decide whether verified implementation scope can be formally closed using approved closure criteria, verification evidence, traceability, blockers, open items, and remaining scope without implementing, repairing, redesigning, or inventing requirements.
---

# Skill 17 — Implementation Closure

**Version:** `v1.0`
**Status:** `LOCKED`

---

## 1. Purpose

The `implementation-closure` skill decides whether an approved implementation scope can be formally closed after execution and verification.

The skill consumes the validated implementation boundary and the current verification evidence produced by the preceding implementation skills.

The skill answers:

> Can the approved implementation scope be formally closed, closed with explicitly permitted gaps, reopened, blocked, or rejected based on the current evidence and approved closure criteria?

The skill MUST preserve evidence boundaries and MUST NOT convert incomplete, unresolved, unsupported, or contradictory information into closure merely because the implementation appears usable or complete.

### Core principle

> **Closure is an evidence-based acceptance decision over approved implementation scope; verification is necessary but is not automatically sufficient for closure.**

---

## 2. Pipeline Position

The implementation pipeline is:

```text
Skill 12 — implementation
        ↓
Skill 13 — implementation-plan
        ↓
Skill 14 — implementation-plan-validator
        ↓
Skill 15 — implementation-executor
        ↓
Skill 16 — implementation-verification
        ↓
Skill 17 — implementation-closure
```

Skill 17 is the final closure decision for the currently approved implementation scope.

Skill 17 MUST NOT silently bypass Skills 12–16.

---

## 3. Scope Boundary

Skill 17 MAY:

- determine closure status;
- determine closure result;
- evaluate approved closure criteria;
- compare approved scope with current verified scope;
- evaluate remaining scope;
- propagate relevant blockers;
- identify unresolved open items;
- identify material contradictions;
- validate closure traceability;
- report findings and recommendation.

Skill 17 MUST NOT:

- implement missing work;
- repair implementation defects;
- modify source code;
- redesign the implementation plan;
- create new implementation items;
- invent business requirements;
- invent product behavior;
- invent closure criteria;
- expand approved scope;
- resolve blockers by guessing;
- convert `OPEN` or `UNKNOWN` into a confirmed decision without evidence;
- treat developer convenience as closure authority;
- treat technical superiority as closure authority;
- accept unauthorized implementation scope;
- rewrite Skill 15 execution state/result;
- rewrite Skill 16 verification status/result;
- claim independent verification when only execution evidence exists.

A problem found by Skill 17 MUST be reported rather than silently repaired.

---

## 4. Closure Boundary

The closure decision operates over this evidence chain:

```text
Approved Implementation Scope
            ↓
Validated Implementation Plan
            ↓
Execution Records / Execution Evidence
            ↓
Verification Result / Verification Evidence
            ↓
Approved Closure Criteria / Closure Policy
            ↓
Closure Decision
```

Closure is valid only for the approved scope represented by this chain.

An implementation artifact cannot become closure-authorized merely because it exists.

---

## 5. Required Inputs

Primary inputs:

- approved implementation scope from Skill 12;
- validated implementation plan from Skills 13–14;
- current execution state/result from Skill 15;
- execution evidence from Skill 15;
- current verification status/result from Skill 16;
- verification evidence from Skill 16;
- approved closure criteria, when they exist;
- approved closure policy, when separate from the criteria;
- implementation traceability;
- blockers;
- open items;
- remaining scope;
- material contradictions;
- applicable development standards when they directly affect the closure decision.

Optional inputs:

- historical closure records;
- prior verification records;
- approved developer decisions;
- approved acceptance records;
- current implementation metadata;
- current project structure when explicitly provided as evidence.

A downstream claim is not automatically proof of upstream approval.

---

## 6. Evidence Classification

Skill 17 uses the following evidence classes:

| Classification | Meaning |
|---|---|
| `SOURCE_STATED` | Explicitly stated by an approved upstream source |
| `DERIVED` | Directly and safely derived from approved evidence |
| `DEV_STANDARD` | Explicitly established by an applicable development standard |
| `IMPLEMENTATION` | Approved implementation scope or implementation decision |
| `EXECUTION_EVIDENCE` | Evidence produced by Skill 15 execution |
| `VERIFICATION_EVIDENCE` | Evidence produced by Skill 16 verification |
| `OPEN` | Required information remains unresolved |
| `UNKNOWN` | Required information is unavailable or undefined |
| `BLOCKED` | Missing or conflicting information prevents safe closure |
| `CONTRADICTION` | Applicable evidence contains unresolved conflicting decisions |

Evidence class MUST reflect the source of the claim.

A closure claim MUST NOT be classified as `DERIVED` only because it appears reasonable.

---

## 7. Current Evidence Supersedes Stale Historical State

Skill 17 MUST prioritize current authoritative evidence over stale historical metadata.

Example:

```text
Historical closure:
CLOSED

Current verification:
NOT_VERIFIED
```

The current verification condition controls the present closure decision.

Historical state may be reported for audit/history, but it MUST NOT override current authoritative evidence.

Likewise:

```text
Historical verification:
PASS

Current verification:
FAIL
```

must be evaluated using the current `FAIL` condition.

A previous `CLOSED` or `PASS` state is not a permanent authorization for future closure.

---

## 8. Closure Unit

The closure unit consists of:

```text
Closure Scope
Plan Items
Verification Items
Verification Status
Verification Result
Verification Evidence
Remaining Scope
Blockers
Open Items
Closure Criteria
Closure Policy
Traceability
Closure Status
Closure Result
Findings
Recommendation
```

The closure unit MUST remain aligned with the approved implementation boundary.

---

## 9. Closure Status Model

Allowed closure statuses are:

```text
CLOSED
CLOSED_WITH_GAPS
REOPEN_REQUIRED
BLOCKED
REJECTED
```

### 9.1 CLOSED

`CLOSED` means the approved closure scope is sufficiently verified and every required closure criterion is satisfied.

### 9.2 CLOSED_WITH_GAPS

`CLOSED_WITH_GAPS` means:

- the required closure policy explicitly permits the remaining gap(s);
- the gap(s) are not disallowed by the approved closure criteria;
- the gap(s) do not invalidate the accepted scope;
- the remaining gap(s) are explicitly recorded.

A non-blocking gap MUST NOT be invented or assumed to be permitted.

### 9.3 REOPEN_REQUIRED

`REOPEN_REQUIRED` means the implementation scope cannot currently be accepted as closed and the outstanding condition is expected to be addressed through further execution or re-verification.

### 9.4 BLOCKED

`BLOCKED` means a required decision, evidence item, closure criterion, or other condition prevents a safe closure decision.

### 9.5 REJECTED

`REJECTED` means current authoritative evidence establishes a material failure, contradiction, unauthorized scope condition, or other condition that invalidates acceptance under the approved closure boundary.

---

## 10. Closure Result Model

Allowed closure results are:

```text
CLOSE
CLOSE_WITH_GAPS
REOPEN
BLOCKED
REJECT
```

### Status ↔ Result Mapping

| Result | Status |
|---|---|
| `CLOSE` | `CLOSED` |
| `CLOSE_WITH_GAPS` | `CLOSED_WITH_GAPS` |
| `REOPEN` | `REOPEN_REQUIRED` |
| `BLOCKED` | `BLOCKED` |
| `REJECT` | `REJECTED` |

`requested_closure.result` is input only and MUST NOT override the actual decision.

Likewise, a requested recommendation is input only and MUST NOT override the actual recommendation.

---

## 11. Closure Result Precedence

When multiple closure conditions apply, Skill 17 MUST use this precedence:

```text
REJECT
  > BLOCKED
  > REOPEN
  > CLOSE_WITH_GAPS
  > CLOSE
```

Therefore:

- a `REJECT` condition overrides `BLOCKED`, `REOPEN`, `CLOSE_WITH_GAPS`, and `CLOSE`;
- a `BLOCKED` condition overrides `REOPEN`, `CLOSE_WITH_GAPS`, and `CLOSE`;
- a `REOPEN` condition overrides `CLOSE_WITH_GAPS` and `CLOSE`;
- `CLOSE_WITH_GAPS` is allowed only when its policy conditions are explicitly satisfied.

A lower-priority requested result cannot force a higher-priority actual result.

---

## 12. Verification Is Not Automatically Closure

The following distinction is mandatory:

```text
VERIFIED ≠ automatically CLOSED
PASS ≠ automatically CLOSE
```

A verification result establishes what Skill 16 verified.

Closure additionally evaluates:

- approved closure criteria;
- closure policy;
- remaining required scope;
- blockers;
- open items;
- traceability;
- material contradictions;
- acceptance evidence;
- scope fidelity.

Therefore:

```text
VERIFIED
```
may still result in:

```text
BLOCKED
REOPEN
REJECT
```

when another approved closure condition requires it.

---

## 13. Verification-to-Closure Mapping

### 13.1 PASS

If Skill 16 reports:

```text
PASS
```

then Skill 17 MAY close only when all separately required closure conditions are also satisfied.

Expected baseline:

```text
PASS + all required closure criteria satisfied
→ CLOSED / CLOSE
```

If a required closure criterion is missing, unsatisfied, blocked, or unsupported, the final result MUST reflect that condition.

### 13.2 PASS_WITH_GAPS

If Skill 16 reports:

```text
PASS_WITH_GAPS
```

then:

- explicitly permitted gaps → `CLOSED_WITH_GAPS / CLOSE_WITH_GAPS`;
- required or blocking gaps → `REOPEN_REQUIRED / REOPEN` or `BLOCKED / BLOCKED` according to the nature of the missing decision/evidence.

### 13.3 NOT_VERIFIED

```text
NOT_VERIFIED
→ REOPEN_REQUIRED / REOPEN
```

unless a higher-priority `BLOCKED` or `REJECT` condition applies.

### 13.4 BLOCKED

```text
BLOCKED
→ BLOCKED / BLOCKED
```

unless a material contradiction or stronger `REJECT` condition independently applies.

### 13.5 FAIL

A `FAIL` result from Skill 16 means the implementation cannot be accepted as closed.

Skill 17 MAY map it to:

```text
REOPEN_REQUIRED / REOPEN
```

when the approved closure policy indicates the failure is recoverable.

Skill 17 MAY map it to:

```text
REJECTED / REJECT
```

when the current evidence establishes material invalidity, contradiction, or another policy-defined rejection condition.

Skill 17 MUST NOT invent the missing recovery policy.

---

## 14. Execution State and Result Must Not Be Rewritten

Skill 15 execution state and result remain separate from Skill 17 closure status/result.

Skill 17 MUST preserve the execution record as received.

Execution states may include:

```text
NOT_STARTED
READY
IN_PROGRESS
BLOCKED
COMPLETED
FAILED
CANCELLED
```

Execution results may include:

```text
STARTED
CONTINUE
COMPLETED
BLOCKED
FAILED
CANCELLED
PARTIAL_EXECUTION
NO_ACTION
```

Skill 17 MUST NOT rewrite these values merely to support closure.

Example:

```text
Execution:
CANCELLED

Closure:
REOPEN_REQUIRED / REOPEN
```

The cancellation remains part of execution history.

---

## 15. Scope Verification for Closure

Closure MUST compare:

```text
Approved Scope
vs
Executed Scope
vs
Verified Scope
vs
Observed Current Scope
```

The following must be detected:

- required approved item missing;
- required approved item incomplete;
- approved item executed but not verified;
- unauthorized extra scope;
- scope mismatch;
- implementation artifact not traceable to approved scope.

A system that appears functional does not automatically satisfy scope closure.

---

## 16. Required Scope Completion

Every required approved implementation item must satisfy the approved completion boundary before `CLOSE`.

The skill MUST NOT close required incomplete work because:

- the remaining work is small;
- the developer says it is harmless;
- the feature is technically optional in practice;
- the code compiles;
- the application runs;
- a user could work around it;
- it can be fixed later;
- the implementation is already considered “good enough.”

Only approved closure policy can authorize gap-tolerant closure.

---

## 17. Closure Criteria

Closure criteria are authoritative only when explicitly established by an approved source or closure policy.

Skill 17 MUST evaluate:

- each required closure criterion;
- evidence supporting satisfaction;
- whether the criterion applies to the current closure scope;
- whether the criterion is satisfied, unsatisfied, unresolved, or blocked.

### 17.1 No Closure-Criterion Invention

Skill 17 MUST NOT invent a closure criterion because it is:

- a common engineering practice;
- a preferred quality measure;
- technically desirable;
- easy to add;
- recommended by the developer;
- usually expected in similar projects;
- useful for future maintenance.

Example:

```text
All approved closure criteria = satisfied

New suggestion:
"Add performance documentation before closing."
```

If that requirement has no approved authority, it MUST NOT become a closure condition.

---

## 18. Closure Policy and Gap Handling

`CLOSED_WITH_GAPS` is permitted only when an approved policy explicitly allows the relevant gap type.

Skill 17 MUST distinguish:

```text
permitted non-blocking gap
```
from:

```text
required unresolved condition
```

A gap is not permitted merely because it is described as:

- minor;
- low priority;
- future work;
- nice to have;
- internal;
- technical;
- documentation-only.

Its closure eligibility must be supported by an approved policy or criterion.

---

## 19. OPEN Item Handling

`OPEN` means the relevant decision or evidence remains unresolved.

Skill 17 MUST NOT silently resolve `OPEN` items.

An OPEN item MAY coexist with closure only when the approved closure policy explicitly permits that kind of open item and it does not prevent required acceptance.

Otherwise the result MUST be `REOPEN` or `BLOCKED`, depending on the reason.

Examples:

```text
OPEN + approved non-blocking policy
→ CLOSE_WITH_GAPS
```

```text
OPEN + required closure criterion
→ BLOCKED or REOPEN
```

```text
OPEN + missing required decision
→ BLOCKED
```

---

## 20. UNKNOWN Handling

`UNKNOWN` means required information is unavailable or undefined.

Skill 17 MUST NOT convert `UNKNOWN` into:

```text
SATISFIED
VERIFIED
ACCEPTED
CLOSED
```

without supporting evidence.

If the UNKNOWN item is necessary for a safe closure decision, closure is blocked.

---

## 21. Blocker Handling

Any unresolved blocking condition that affects required closure criteria or required implementation scope MUST prevent closure.

A blocker MUST NOT be suppressed by:

- changing its wording;
- reducing its perceived severity without evidence;
- moving it into an open item;
- marking it as historical;
- stating that the developer can fix it later;
- treating it as outside the scope when the approved scope includes it.

### Blocker propagation

A blocker propagates only to closure items that actually depend on it.

Do not block unrelated closure scope.

Do not invent blocker relationships.

---

## 22. Material Contradiction Handling

If current authoritative evidence contains a material contradiction affecting the closure decision, Skill 17 MUST NOT silently choose one interpretation.

A material contradiction may include:

- approved scope says one behavior while current implementation claims another;
- current verification conflicts with current implementation evidence;
- closure criteria conflict with another approved closure rule and no precedence is established;
- current acceptance evidence conflicts with authoritative verification evidence.

Material contradiction MAY result in:

```text
REJECTED / REJECT
```

or:

```text
BLOCKED / BLOCKED
```

depending on whether the contradiction establishes invalidity or merely prevents safe closure.

---

## 23. Historical State Handling

Historical records are informational unless they are explicitly authoritative for the current closure decision.

The following MUST NOT override current evidence:

```text
previous CLOSED
previous CLOSE
previous PASS
previous ACCEPT_CLOSURE
```

The current authoritative evidence controls the current closure result.

Historical closure may be reported as audit context, but cannot be used to conceal a current gap or violation.

---

## 24. Requested Result and Recommendation Manipulation

The input may contain:

```text
requested_closure.result
requested_closure.status
requested_closure.recommendation
```

These fields are non-authoritative.

Examples:

```text
requested result = CLOSE
actual condition = BLOCKED
```

Expected:

```text
BLOCKED / BLOCKED
```

Likewise:

```text
requested result = REOPEN
actual condition = all approved criteria satisfied
```

Expected:

```text
CLOSED / CLOSE
```

Skill 17 MUST determine the actual decision from evidence, not caller preference.

---

## 25. Unauthorized Scope and Scope Laundering

Skill 17 MUST detect attempts to close work that contains unauthorized scope.

Examples include:

- an unapproved feature described as implementation detail;
- a new API hidden inside an approved capability;
- a new database structure treated as “necessary” without approval;
- an additional workflow presented as a technical convenience;
- extra UI behavior represented as default implementation;
- a new integration treated as implicit.

Phrases such as:

```text
included by default
needed internally
standard behavior
already part of the implementation
technically required
```

do not establish approval by themselves.

Unauthorized scope that materially affects closure MUST result in:

```text
REJECTED / REJECT
```

unless an applicable authoritative policy establishes a different resolution.

---

## 26. Developer Convenience Is Not Closure Authority

The following are not closure authority unless explicitly adopted by an approved policy:

- developer convenience;
- implementation speed;
- release pressure;
- reduced testing effort;
- easier maintenance;
- easier future repair;
- personal preference;
- technical elegance.

Example:

> “Closing now is faster and we can fix the remaining issue later.”

This is not a valid closure criterion.

---

## 27. Technical Superiority Is Not Closure Authority

A technically stronger implementation does not automatically authorize closure or scope expansion.

Example:

```text
Approved implementation = A
Developer implements A + technically superior B
```

If `B` is outside approved scope and materially changes the implementation boundary, Skill 17 MUST NOT accept B merely because it is better engineering.

Technical quality and scope authorization are separate questions.

---

## 28. Traceability Validation

Closure requires valid traceability.

Every closure-scoped implementation item MUST trace to:

- approved implementation scope;
- approved implementation-plan item;
- approved verification item/evidence;
- applicable approved upstream evidence where necessary.

A closure item MUST NOT become valid simply because another artifact references it.

### Required traceability properties

- reference exists;
- reference identifies a real artifact;
- reference is relevant to the current scope;
- mapping is not orphaned;
- mapping does not launder extra scope;
- verification evidence actually covers the referenced item.

Broken or unsupported closure traceability MAY produce:

```text
REJECTED / REJECT
```

when closure validity is materially affected.

---

## 29. Evidence Sufficiency

Evidence must be sufficient to support the closure claim being made.

Examples of insufficient evidence:

- “works on my machine”;
- “developer tested it” without required verification evidence;
- historical PASS from another run;
- an implementation claim with no verification evidence;
- a screenshot unrelated to the closure criterion;
- a plan item marked complete without execution evidence;
- a verification result with no supporting evidence where evidence is required.

Skill 17 MUST report evidence insufficiency rather than inventing proof.

---

## 30. Acceptance Evidence

Formal acceptance evidence is separate from implementation and verification evidence when the approved closure policy requires explicit acceptance.

If an approved closure criterion requires formal acceptance and that evidence is missing, Skill 17 MUST NOT assume that:

```text
PASS = ACCEPTANCE
```

unless the approved closure policy explicitly states that equivalence.

Missing required acceptance evidence may result in:

```text
BLOCKED / BLOCKED
```

---

## 31. Remaining Scope

Skill 17 MUST explicitly report remaining scope when closure is not complete.

Remaining scope may include:

- incomplete implementation items;
- unverified implementation items;
- unresolved blockers;
- required open decisions;
- permitted gaps;
- unsupported extra scope that must be removed or revalidated.

A remaining-scope item MUST preserve its source classification.

Do not relabel required work as “future enhancement” unless an approved policy or scope decision explicitly supports that classification.

---

## 32. Findings

Every non-CLOSE outcome SHOULD identify:

- finding ID;
- affected item;
- evidence class;
- source/reference;
- current condition;
- impact on closure;
- blocking or material status;
- required next boundary, without prescribing unapproved implementation.

Skill 17 MUST report findings rather than silently changing input artifacts.

---

## 33. Recommendation Model

Allowed recommendations are:

```text
ACCEPT_CLOSURE
ACCEPT_CLOSURE_WITH_GAPS
RETURN_FOR_EXECUTION
RETURN_FOR_REVALIDATION
WAIT_FOR_RESOLUTION
STOP
```

### Typical mappings

| Condition | Recommendation |
|---|---|
| `CLOSE` | `ACCEPT_CLOSURE` |
| `CLOSE_WITH_GAPS` | `ACCEPT_CLOSURE_WITH_GAPS` |
| `REOPEN` due incomplete implementation | `RETURN_FOR_EXECUTION` |
| `REOPEN` due insufficient verification | `RETURN_FOR_REVALIDATION` |
| `BLOCKED` by missing decision/evidence | `WAIT_FOR_RESOLUTION` |
| `REJECT` due material invalidity/contradiction | `STOP` |

The recommendation MUST follow the actual closure condition.

The skill MUST NOT force a recommendation merely because the caller requested it.

---

## 34. Closure Decision Workflow

Skill 17 SHOULD execute in this order:

```text
1. Validate required inputs
2. Confirm current implementation scope
3. Confirm current execution record
4. Confirm current verification result/evidence
5. Compare approved vs executed vs verified scope
6. Validate closure criteria
7. Validate closure policy
8. Validate remaining scope
9. Validate blockers
10. Validate OPEN / UNKNOWN items
11. Validate traceability
12. Detect unauthorized scope
13. Detect material contradictions
14. Ignore non-authoritative requested results
15. Apply closure-result precedence
16. Determine status
17. Determine remaining scope
18. Determine recommendation
19. Produce closure record
```

The workflow MUST NOT repair or redesign the implementation when a problem is found.

---

## 35. Closure Decision Matrix

| Current condition | Expected decision |
|---|---|
| PASS + all required criteria satisfied | `CLOSED / CLOSE` |
| PASS + required criterion missing | `BLOCKED / BLOCKED` |
| PASS_WITH_GAPS + approved permitted gap | `CLOSED_WITH_GAPS / CLOSE_WITH_GAPS` |
| PASS_WITH_GAPS + required gap | `REOPEN_REQUIRED / REOPEN` |
| NOT_VERIFIED | `REOPEN_REQUIRED / REOPEN` |
| BLOCKED | `BLOCKED / BLOCKED` |
| Material invalidity / contradiction | `REJECTED / REJECT` |
| Unauthorized material scope | `REJECTED / REJECT` |
| Valid scope + unsupported new closure criterion suggested | do not add criterion; evaluate existing criteria |
| Historical CLOSED but current condition fails | current condition wins |
| Requested CLOSE but actual condition blocks closure | actual condition wins |
| Requested REOPEN but actual conditions satisfy closure | actual condition wins |

When multiple conditions apply, apply precedence from Section 11.

---

## 36. Final Quality Gate

`CLOSE` requires all of the following:

```text
100% required approved implementation scope verified
AND
100% required approved closure criteria satisfied
AND
0 unresolved blocking conditions
AND
traceability valid
AND
actionable closure evidence sufficient
AND
0 material contradictions
AND
0 unauthorized material scope
```

`CLOSE_WITH_GAPS` requires:

```text
all required accepted scope verified
AND
all mandatory closure criteria satisfied
AND
remaining gaps explicitly permitted by approved policy
AND
no blocking condition caused by those gaps
AND
traceability valid
AND
gaps recorded explicitly
```

`CLOSE_WITH_GAPS` MUST NOT be used as a generic fallback for incomplete required scope.

---

## 37. No Silent Repair

When the closure input contains a defect, the skill MUST:

```text
identify
classify
report
```

It MUST NOT:

```text
repair
rewrite
invent
```

to make the closure result PASS or CLOSE.

Examples:

- missing evidence → report missing evidence;
- broken trace → report broken trace;
- contradictory criterion → report contradiction;
- extra scope → report scope violation;
- missing acceptance → report missing acceptance.

---

## 38. No Plan Redesign

Skill 17 does not redesign Skill 13 implementation plans.

If the approved implementation plan is insufficient, inconsistent, or incomplete, Skill 17 reports the issue and routes the work back through the appropriate upstream boundary.

It MUST NOT create or reorder plan items to force closure.

---

## 39. No Requirement Expansion

Closure is a decision over already approved implementation scope.

Skill 17 MUST NOT create new business requirements, new technical requirements, new workflows, new APIs, new data structures, new statuses, new permissions, or new integrations during closure.

Suggestions for future work remain suggestions unless separately approved.

---

## 40. Developer Boundary

Skill 17 may determine that implementation cannot be closed.

It MUST NOT determine unapproved implementation details such as:

- which code should be written;
- which framework should be adopted;
- which API should be added;
- which database structure should be created;
- which authentication mechanism should be chosen;
- which infrastructure should be deployed.

Those decisions belong to the appropriate upstream implementation/standards process.

---

## 41. Skill 16 / Skill 17 Separation

The distinction is mandatory:

```text
Skill 16 — implementation-verification

Question:
Does the executed implementation satisfy the approved implementation scope?
```

versus:

```text
Skill 17 — implementation-closure

Question:
Can the verified implementation scope be formally accepted as closed under the approved closure criteria and policy?
```

Skill 17 MUST NOT pretend to be Skill 16.

Skill 16 verification is an input to Skill 17, not a substitute for the closure decision.

---

## 42. Output Contract

The closure output MUST contain:

```yaml
run_id:
result:
status:
scope:
verification:
summary:
closure_criteria:
traceability:
evidence:
blockers:
open_items:
remaining_scope:
findings:
recommendation:
```

### Field requirements

#### `run_id`

Unique identifier for the closure evaluation.

#### `result`

One of:

```text
CLOSE
CLOSE_WITH_GAPS
REOPEN
BLOCKED
REJECT
```

#### `status`

One of:

```text
CLOSED
CLOSED_WITH_GAPS
REOPEN_REQUIRED
BLOCKED
REJECTED
```

#### `scope`

The approved implementation scope being evaluated.

#### `verification`

Must preserve the current Skill 16 verification status/result and relevant evidence references.

Skill 17 MUST NOT rewrite the underlying verification result.

#### `summary`

Concise explanation of the actual closure decision.

#### `closure_criteria`

Each approved criterion and its current satisfaction state.

#### `traceability`

Traceability covering closure scope and evidence.

#### `evidence`

Evidence supporting the decision.

#### `blockers`

Relevant unresolved blocking conditions.

#### `open_items`

Relevant unresolved OPEN items.

#### `remaining_scope`

Required incomplete/unverified work and permitted remaining gaps.

#### `findings`

Detailed closure findings.

#### `recommendation`

One allowed recommendation from Section 33.

---

## 43. Example — Valid CLOSE

```yaml
run_id: ICL-001
result: CLOSE
status: CLOSED
scope:
  - IMP-001
  - IMP-002
verification:
  result: PASS
  status: VERIFIED
closure_criteria:
  - criterion: all required scope verified
    status: SATISFIED
  - criterion: acceptance evidence present
    status: SATISFIED
traceability: VALID
evidence: SUFFICIENT
blockers: []
open_items: []
remaining_scope: []
findings: []
recommendation: ACCEPT_CLOSURE
```

---

## 44. Example — CLOSE_WITH_GAPS

```yaml
run_id: ICL-002
result: CLOSE_WITH_GAPS
status: CLOSED_WITH_GAPS
verification:
  result: PASS_WITH_GAPS
  status: PARTIALLY_VERIFIED
closure_criteria:
  status: SATISFIED
open_items:
  - id: OPEN-001
    policy: explicitly permitted non-blocking gap
remaining_scope:
  - OPEN-001
recommendation: ACCEPT_CLOSURE_WITH_GAPS
```

The specific gap type MUST be supported by approved policy.

---

## 45. Example — REOPEN

```yaml
run_id: ICL-003
result: REOPEN
status: REOPEN_REQUIRED
verification:
  result: NOT_VERIFIED
  status: NOT_VERIFIED
remaining_scope:
  - IMP-004
findings:
  - finding: required scope not verified
recommendation: RETURN_FOR_REVALIDATION
```

The implementation is not considered closed.

---

## 46. Example — BLOCKED

```yaml
run_id: ICL-004
result: BLOCKED
status: BLOCKED
verification:
  result: PASS
closure_criteria:
  status: BLOCKED
blockers:
  - formal acceptance evidence missing
recommendation: WAIT_FOR_RESOLUTION
```

PASS does not override a separately required closure condition.

---

## 47. Example — REJECT

```yaml
run_id: ICL-005
result: REJECT
status: REJECTED
verification:
  result: FAIL
findings:
  - material contradiction between approved scope and current implementation
recommendation: STOP
```

---

## 48. Contradiction With Requested Closure

Example:

```yaml
requested_closure:
  result: CLOSE
  recommendation: ACCEPT_CLOSURE

actual:
  blocker: unresolved required acceptance condition
```

Expected:

```yaml
result: BLOCKED
status: BLOCKED
recommendation: WAIT_FOR_RESOLUTION
```

The requested fields do not have authority over the actual decision.

---

## 49. Historical CLOSED With Current Gap

Example:

```yaml
historical:
  status: CLOSED
  result: CLOSE

current:
  required_scope:
    status: INCOMPLETE
```

Expected:

```text
REOPEN_REQUIRED / REOPEN
```

unless a stronger current `BLOCKED` or `REJECT` condition applies.

---

## 50. Historical PASS With Current Failure

Example:

```yaml
historical_verification: PASS
current_verification: FAIL
```

Current evidence controls.

The historical PASS MUST NOT be used to close the scope.

---

## 51. Multi-Condition Example

Current evidence may contain:

```text
one required scope gap
one unresolved blocker
one material contradiction
```

Apply precedence:

```text
REJECT > BLOCKED > REOPEN > CLOSE_WITH_GAPS > CLOSE
```

Therefore the actual result is:

```text
REJECT / REJECTED
```

when the contradiction is material and rejection-authoritative.

---

## 52. Closure Record Integrity

A closure record MUST be internally consistent.

Examples of invalid records:

```text
result: CLOSE
status: BLOCKED
```

or:

```text
result: REOPEN
status: CLOSED
```

or:

```text
result: CLOSE
remaining_scope:
  - required incomplete item
```

unless the item is explicitly permitted by approved closure policy and the output is instead `CLOSE_WITH_GAPS`.

The status/result combination MUST follow Section 10.

---

## 53. Minimality

Skill 17 MUST report only findings necessary to explain the closure decision and its evidence boundary.

It MUST NOT generate:

- speculative implementation tasks;
- unrelated quality improvements;
- future feature proposals as closure conditions;
- technical redesigns;
- unapproved remediation plans.

A closure record is an acceptance decision, not a backlog generator.

---

## 54. Determinism

Given the same authoritative inputs, Skill 17 SHOULD produce the same closure result and status.

The result MUST NOT change merely because:

- the caller asks for a different result;
- the developer prefers closure;
- a historical record says CLOSED;
- an unsupported best practice is suggested;
- the implementation appears subjectively good.

---

## 55. Golden Rules

```text
1. Closure is not implementation.
2. Closure is not verification.
3. VERIFIED does not automatically mean CLOSED.
4. PASS does not automatically mean CLOSE.
5. Current authoritative evidence beats stale historical state.
6. Requested result does not override actual evidence.
7. Required incomplete scope cannot be closed.
8. Required missing evidence cannot be invented.
9. Closure criteria cannot be invented.
10. Developer convenience is not closure authority.
11. Technical superiority is not scope authority.
12. Unauthorized scope cannot be laundered into closure.
13. OPEN remains OPEN until supported by evidence or an approved policy explicitly permits closure with that OPEN item.
14. UNKNOWN remains UNKNOWN until supported.
15. Blockers cannot be silently suppressed.
16. Material contradictions cannot be silently ignored.
17. Skill 17 does not repair code.
18. Skill 17 does not redesign plans.
19. Skill 17 does not expand requirements.
20. Closure traceability must remain valid.
21. Closure evidence must be sufficient for the claim.
22. Result precedence is REJECT > BLOCKED > REOPEN > CLOSE_WITH_GAPS > CLOSE.
```

---

## 56. Final Contract

Skill 17 is successful when it can reliably determine the following:

```text
CLOSED
```
when all required approved closure conditions are satisfied;

```text
CLOSED_WITH_GAPS
```
when gaps are explicitly permitted by approved policy;

```text
REOPEN_REQUIRED
```
when required implementation or verification remains incomplete;

```text
BLOCKED
```
when a required unresolved decision/evidence prevents safe closure;

```text
REJECTED
```
when current authoritative evidence establishes material invalidity, contradiction, or unauthorized scope.

The skill MUST preserve the separation:

```text
Implementation
    ↓
Plan
    ↓
Validation
    ↓
Execution
    ↓
Verification
    ↓
Closure
```

The skill MUST NOT move information upward through this chain by invention.

### Final quality gate

```text
IMPLEMENTATION CLOSURE v1.0
STATUS: LOCKED

Round 1 = 20/20 PASS
Round 2 = 20/20 PASS
Round 3 = 20/20 PASS

TOTAL = 60/60 PASS

PROMOTION GATE: PASSED
```

Changes to a locked Skill 17 MUST be versioned and regression-tested before any future unlock or replacement.
