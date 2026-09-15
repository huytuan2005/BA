# Skill 16 — Implementation Verification

**File:** `implementation-verification/SKILL.md`
**Version:** `v1.0`
**Status:** `LOCKED`

---

# 1. Purpose

The `implementation-verification` skill verifies whether executed implementation work satisfies the approved implementation plan and its supporting evidence.

The skill determines:

* what was actually implemented;
* whether approved scope was implemented;
* whether implementation results are supported by evidence;
* whether traceability remains intact;
* whether completion claims are justified;
* what approved scope remains incomplete;
* what remains blocked or unresolved;
* whether the implementation can be considered verified.

The skill does NOT implement missing work.

The skill does NOT repair implementation problems.

The skill does NOT redesign the implementation plan.

### Core principle

> **Verify what was approved and executed; never invent what should have been implemented.**

---

# 2. Position in the Pipeline

Skill 16 operates after Skill 15.

```text id="5rm6ab"
Skill 12
Implementation
    ↓
Skill 13
Implementation Plan
    ↓
Skill 14
Implementation Plan Validator
    ↓
Skill 15
Implementation Executor
    ↓
Skill 16
Implementation Verification
```

The distinction is:

```text id="hkrcvk"
Skill 14
=
Can the plan be executed?

Skill 15
=
Execute the approved plan.

Skill 16
=
Verify whether the execution actually satisfies the approved plan.
```

Skill 16 MUST NOT perform the role of Skill 14 or Skill 15.

---

# 3. Verification Boundary

Skill 16 verifies only:

```text id="xffmla"
approved implementation plan
        ↓
approved implementation scope
        ↓
execution record
        ↓
execution evidence
        ↓
current implementation state
```

It MUST NOT expand the verification boundary through unsupported assumptions.

The verifier MUST NOT ask:

```text id="ztrfwm"
"What would a complete system normally contain?"
```

Instead it MUST ask:

```text id="ou44sg"
"Does the available evidence demonstrate the approved implementation?"
```

---

# 4. Required Inputs

Primary inputs:

* validated implementation plan from Skill 14 / Skill 13;
* Skill 15 execution records;
* execution states;
* execution results;
* execution evidence;
* implementation traceability;
* approved implementation artifacts;
* applicable Dev Standards where they form part of the approved implementation boundary.

Optional inputs:

* current source code;
* current project structure;
* build results;
* test results;
* deployment evidence;
* verification evidence;
* previous verification records;
* approved recovery records.

Missing optional information MUST NOT automatically be treated as implementation failure.

---

# 5. Evidence Classification

Verification evidence MUST preserve source classification.

Supported classifications:

| Classification       | Meaning                                              |
| -------------------- | ---------------------------------------------------- |
| `SOURCE_STATED`      | Explicit upstream evidence                           |
| `DERIVED`            | Safely derived verification conclusion               |
| `DEV_STANDARD`       | Evidence established by applicable Dev Standard      |
| `IMPLEMENTATION`     | Approved implementation evidence                     |
| `EXECUTION_EVIDENCE` | Evidence produced during Skill 15 execution          |
| `OPEN`               | Verification-relevant information remains unresolved |
| `UNKNOWN`            | Required information is unavailable                  |
| `BLOCKED`            | Verification cannot safely proceed                   |
| `CONTRADICTION`      | Relevant evidence conflicts                          |

Verification MUST NOT upgrade:

```text id="1iia7d"
OPEN → VERIFIED
UNKNOWN → VERIFIED
```

without supporting evidence.

---

# 6. Verification Unit

The basic verification unit is a validated implementation-plan item.

Every verification unit SHOULD identify:

```text id="flyr0f"
Plan Item ID
Implementation Item
Approved Scope
Execution Record
Execution State
Execution Result
Execution Evidence
Verification Evidence
Verification Status
Findings
Remaining Scope
```

Verification MUST remain item-level where possible.

A project-level PASS MUST NOT hide an unverified plan item.

---

# 7. Verification Status Model

Skill 16 uses the following verification statuses:

```text id="nj49nd"
VERIFIED
PARTIALLY_VERIFIED
NOT_VERIFIED
BLOCKED
FAIL
```

These statuses describe verification state only.

They are NOT execution states.

They MUST NOT replace Skill 15 execution states.

---

# 8. Verification Result Model

Each verification run SHOULD produce:

```text id="kgxist"
PASS
PASS_WITH_GAPS
NOT_VERIFIED
BLOCKED
FAIL
```

The distinction is:

```text id="3djuix"
Verification Status
=
state of an individual verification item

Verification Result
=
outcome of the verification run
```

---

# 9. Verification Status Meaning

### `VERIFIED`

The approved implementation scope for the item is supported by sufficient evidence.

### `PARTIALLY_VERIFIED`

Some approved scope is supported, but some approved scope remains incomplete or insufficiently evidenced.

### `NOT_VERIFIED`

The available evidence does not establish that the approved implementation exists or satisfies the required execution evidence.

### `BLOCKED`

Verification cannot safely continue because a required verification input, decision, dependency, or authoritative evidence is unavailable or unresolved.

### `FAIL`

Verification identifies a material contradiction, unsupported implementation, scope violation, invalid evidence, or other condition that makes the implementation unacceptable against the approved boundary.

---

# 10. Plan-to-Execution Verification

Skill 16 MUST verify:

```text id="y92ycl"
Plan Item
    ↓
Execution Record
    ↓
Execution Evidence
```

Every approved implementation-plan item MUST be accounted for.

Possible conditions:

```text id="wilz1k"
PLAN ITEM EXECUTED
PLAN ITEM PARTIALLY EXECUTED
PLAN ITEM NOT EXECUTED
PLAN ITEM BLOCKED
PLAN ITEM CANCELLED
```

The verifier MUST NOT treat:

```text id="iykkix"
NOT EXECUTED
```

as:

```text id="4i46ze"
VERIFIED
```

---

# 11. Scope Verification

The verifier MUST compare:

```text id="t1lvlp"
approved implementation scope
        vs
executed implementation scope
        vs
observed implementation scope
```

The following must be detected:

```text id="18cx4s"
missing approved scope
extra unapproved scope
scope substitution
scope reduction
scope expansion
```

An implementation may be technically functional and still fail verification if it implements unapproved scope.

---

# 12. Scope Coverage

For each plan item, classify approved scope as:

```text id="pol1hj"
FULLY COVERED
PARTIALLY COVERED
NOT COVERED
UNKNOWN
```

Example:

```text id="7zt1xj"
Approved:
Profile viewing
Profile update

Implemented:
Profile viewing

Result:
PARTIALLY COVERED
```

Verification result:

```text id="d8s4cz"
PARTIALLY_VERIFIED
```

The verifier MUST NOT invent the missing profile-update behavior.

---

# 13. Extra Scope Detection

If implementation evidence shows unapproved scope:

```text id="on0gsm"
Approved:
Customer profile viewing

Observed:
Customer profile viewing
+
Customer profile export
```

The export capability is not automatically accepted because it is useful or technically harmless.

Expected finding:

```text id="3hpeyf"
UNSUPPORTED_IMPLEMENTATION_SCOPE
```

The verifier MUST distinguish:

```text id="1s9z9a"
approved implementation
```

from:

```text id="rqf4bw"
observed additional implementation
```

---

# 14. Traceability Verification

Every verified implementation item MUST preserve:

```text id="li5yne"
Verification
    ↓
Execution
    ↓
Plan Item
    ↓
Implementation Item
    ↓
Approved Upstream Evidence
```

Traceability MUST be:

```text id="yafffa"
present
valid
scope-consistent
evidence-consistent
```

Invalid traceability produces:

```text id="4fwrp7"
INVALID_EXECUTION_TRACEABILITY
```

A technically working feature MUST NOT be considered verified when its approved traceability cannot be established.

---

# 15. Execution-State Consistency

Skill 16 MUST verify that the Skill 15 execution record is internally consistent.

Example:

```text id="z67lyj"
Skill 15:

state = IN_PROGRESS
result = PARTIAL_EXECUTION
```

Skill 16 MUST NOT treat the item as fully completed.

Example:

```text id="vsm081"
Skill 15:

state = COMPLETED
result = COMPLETED
```

This is evidence of claimed completion.

It is NOT by itself sufficient verification.

---

# 16. Completion Claim Verification

Completion requires evidence.

The verifier MUST check:

```text id="s5co6v"
claimed completion
        ↓
approved completion criteria
        ↓
execution evidence
        ↓
verification evidence
```

A completion claim without sufficient supporting evidence MUST NOT become:

```text id="ce9a0u"
VERIFIED
```

Possible result:

```text id="4fe6dw"
NOT_VERIFIED
```

or:

```text id="f1s5ag"
FAIL
```

depending on severity and contradiction.

---

# 17. Partial Execution Verification

When Skill 15 reports:

```yaml id="4k6edk"
state: IN_PROGRESS
result: PARTIAL_EXECUTION
```

Skill 16 MUST inspect:

```text id="9zy79o"
completed_portion
remaining_portion
execution_evidence
```

Expected behavior:

```text id="hb1p8z"
completed portion with sufficient evidence
→ may be VERIFIED

remaining portion
→ NOT_VERIFIED
```

Overall item:

```text id="tzekmk"
PARTIALLY_VERIFIED
```

The verifier MUST NOT convert partial execution into completion.

---

# 18. Completion Criteria

Verification MUST use the completion criteria established by:

* approved implementation plan;
* approved implementation item;
* approved upstream evidence;
* applicable Dev Standards where relevant.

The verifier MUST NOT invent new completion criteria merely because they seem useful.

Example:

Approved:

```text id="gyphwh"
Profile viewing implemented.
```

Verifier MUST NOT add:

```text id="arkubr"
performance benchmark
load test
caching
analytics
extra UI states
```

unless those criteria are explicitly part of the approved boundary.

---

# 19. Dependency Verification

Skill 16 MUST verify whether required implementation dependencies were actually satisfied.

For each dependency:

```text id="8uhuhk"
dependency exists
dependency completion is evidenced
dependency relation matches plan
dependent implementation did not bypass it
```

A dependency that was merely assumed complete MUST NOT be accepted.

If the dependency remained unresolved:

```text id="1qx4oi"
verification status = BLOCKED
```

or:

```text id="cymiq8"
NOT_VERIFIED
```

depending on whether verification itself is prevented.

---

# 20. Blocker Verification

The verifier MUST determine whether blockers identified during planning/execution:

```text id="ugzo3t"
resolved
remaining
incorrectly bypassed
```

If a blocker remains:

```text id="3u0fhb"
affected scope
→ NOT_VERIFIED or BLOCKED
```

An unrelated blocker MUST NOT invalidate unrelated verified scope.

---

# 21. OPEN / UNKNOWN Verification

OPEN and UNKNOWN information remain unresolved unless supported by new explicit evidence.

The verifier MUST NOT convert:

```text id="dlj0db"
OPEN
```

into:

```text id="926krd"
PASS
```

just because the implementation happens to work under one assumption.

The verifier MUST NOT convert:

```text id="vzw6mr"
UNKNOWN
```

into:

```text id="jzajow"
VERIFIED
```

without evidence.

---

# 22. Contradiction Verification

The verifier MUST detect contradictions such as:

```text id="d2ln7o"
execution = COMPLETED
verification evidence = incomplete

plan scope = A
implementation scope = A + B

traceability = IMP-001
observed implementation = unrelated item

dependency = COMPLETED
dependency evidence = BLOCKED
```

A material contradiction MUST prevent verification.

Finding example:

```text id="7sgf33"
VERIFICATION_CONTRADICTION
```

---

# 23. Unsupported Implementation Detection

Skill 16 MUST detect implementation that exceeds approved evidence.

Examples:

```text id="hhidhi"
extra endpoint
extra database behavior
extra authentication mechanism
extra notification
extra business rule
extra workflow
extra UI behavior
extra infrastructure
extra integration
```

The verifier MUST NOT approve unsupported implementation merely because it is technically correct.

Finding:

```text id="erpo8s"
UNSUPPORTED_IMPLEMENTATION_SCOPE
```

---

# 24. Regression Against Implementation Plan

Verification MUST compare final implementation against the complete approved plan.

For every plan item:

```text id="9obq2y"
planned
executed
evidenced
verified
```

A project MUST NOT receive a full verification PASS while approved plan items remain unverified.

---

# 25. No Implementation Repair

When verification discovers a missing implementation:

```text id="i5qms0"
Approved:
Profile update

Observed:
Profile viewing only
```

Skill 16 MUST report:

```text id="98bcfw"
MISSING_APPROVED_IMPLEMENTATION
```

It MUST NOT:

```text id="vtw9fz"
implement profile update
```

It MUST NOT:

```text id="gsr13x"
rewrite the implementation plan
```

It MUST NOT:

```text id="fcjhcd"
invent an implementation solution
```

---

# 26. No Plan Redesign

If verification reveals that the implementation plan was incomplete or unclear, Skill 16 MUST report the condition.

It MUST NOT silently modify:

```text id="x7ienx"
plan item
dependency
scope
priority
architecture
technical decision
```

Upstream revision belongs to the appropriate previous Skill.

---

# 27. No Technology Invention During Verification

Verification MUST NOT introduce:

```text id="d8hpvu"
new framework
new database
new API pattern
new architecture
new security mechanism
new infrastructure
new testing requirement
```

merely because verification would be easier.

Verification is evidence-based, not architecture-based.

---

# 28. Verification Evidence

Verification evidence SHOULD identify:

```text id="ilqk4o"
what was checked
how it was checked
which approved item it verifies
what evidence supports the conclusion
what remains unverified
```

Example:

```text id="0j74d4"
Plan Item:
IP-018

Approved:
Profile viewing + profile update

Observed:
Profile viewing verified.
Profile update not evidenced.

Verification:
PARTIALLY_VERIFIED
```

---

# 29. Verification Finding Model

Findings SHOULD use explicit identifiers.

Examples:

```text id="b0u9k6"
MISSING_APPROVED_IMPLEMENTATION
UNSUPPORTED_IMPLEMENTATION_SCOPE
INVALID_EXECUTION_TRACEABILITY
COMPLETION_EVIDENCE_INSUFFICIENT
VERIFICATION_CONTRADICTION
DEPENDENCY_VERIFICATION_FAILED
BLOCKER_REMAINS
OPEN_VERIFICATION_ITEM
UNKNOWN_VERIFICATION_ITEM
```

A finding describes the verification problem.

It MUST NOT silently prescribe an invented technical solution.

---

# 30. Verification Workflow

Skill 16 MUST follow:

```text id="bkvp6i"
1. Load Approved Implementation Plan
        ↓
2. Load Skill 15 Execution Records
        ↓
3. Load Execution Evidence
        ↓
4. Map Plan Items to Execution Items
        ↓
5. Verify Traceability
        ↓
6. Verify Scope
        ↓
7. Verify Dependencies
        ↓
8. Verify Blockers
        ↓
9. Verify OPEN / UNKNOWN Items
        ↓
10. Verify Completion Criteria
        ↓
11. Verify Execution Evidence
        ↓
12. Compare Observed Implementation
        ↓
13. Detect Contradictions
        ↓
14. Determine Item Verification Status
        ↓
15. Determine Overall Verification Result
        ↓
16. Produce Verification Report
```

---

# 31. Verification Decision Matrix

| Condition                              | Verification Status           | Result                 |
| -------------------------------------- | ----------------------------- | ---------------------- |
| Full approved scope evidenced          | VERIFIED                      | PASS                   |
| Partial approved scope evidenced       | PARTIALLY_VERIFIED            | PASS_WITH_GAPS         |
| Required evidence missing              | NOT_VERIFIED                  | NOT_VERIFIED           |
| Required verification input unresolved | BLOCKED                       | BLOCKED                |
| Unsupported scope detected             | FAIL                          | FAIL                   |
| Invalid traceability                   | FAIL                          | FAIL                   |
| Material contradiction                 | FAIL                          | FAIL                   |
| Dependency not evidenced               | BLOCKED / NOT_VERIFIED        | BLOCKED / NOT_VERIFIED |
| Blocker remains                        | BLOCKED                       | BLOCKED                |
| Non-blocking OPEN remains              | VERIFIED / PARTIALLY_VERIFIED | PASS / PASS_WITH_GAPS  |
| No approved task executed              | NOT_VERIFIED                  | NOT_VERIFIED           |

---

# 32. Overall Verification Result

The overall result MUST be based on verified plan-item coverage.

### `PASS`

All required approved implementation scope is sufficiently evidenced.

### `PASS_WITH_GAPS`

Some plan items are only partially verified, while the remaining gaps are non-fatal to the current verification boundary.

### `NOT_VERIFIED`

Evidence is insufficient to establish the required implementation.

### `BLOCKED`

Verification cannot safely complete because required information or evidence is unresolved.

### `FAIL`

The implementation materially violates approved scope, traceability, evidence, or other validated boundaries.

---

# 33. Verification Report

Minimum report:

```yaml id="stgzuj"
verification:
  run_id: VERIFY-xxx
  result: PASS | PASS_WITH_GAPS | NOT_VERIFIED | BLOCKED | FAIL

  summary:
    total_plan_items: <n>
    verified: <n>
    partially_verified: <n>
    not_verified: <n>
    blocked: <n>
    failed: <n>

  items:
    - plan_item: IP-xxx
      status: VERIFIED | PARTIALLY_VERIFIED | NOT_VERIFIED | BLOCKED | FAIL
      execution_state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED
      execution_result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION
      scope_coverage: FULLY_COVERED | PARTIALLY_COVERED | NOT_COVERED | UNKNOWN
      traceability: PASS | FAIL
      evidence: PASS | FAIL
      dependencies: PASS | FAIL | NOT_APPLICABLE
      blockers: NONE | PRESENT
      findings:
        - <finding>

  remaining_scope:
    - <unverified approved scope>

  recommendation:
    ACCEPT
    | ACCEPT_WITH_GAPS
    | CONTINUE_VERIFICATION
    | RETURN_FOR_EXECUTION
    | RETURN_FOR_REVALIDATION
    | STOP
```

---

# 34. Recommendation Boundary

Skill 16 may recommend:

```text id="k7smlg"
ACCEPT
ACCEPT_WITH_GAPS
CONTINUE_VERIFICATION
RETURN_FOR_EXECUTION
RETURN_FOR_REVALIDATION
STOP
```

These recommendations MUST reflect verification findings.

The skill MUST NOT directly perform the recommended action.

---

# 35. Verification vs Execution

Skill 15:

```text id="7c2rwn"
Does the approved work get executed?
```

Skill 16:

```text id="ownixs"
Does the evidence demonstrate that the approved work was actually completed?
```

Example:

```text id="8b4lb2"
Skill 15:
COMPLETED + COMPLETED

Skill 16:
NOT_VERIFIED
```

This is valid when execution completion was claimed without sufficient verification evidence.

---

# 36. Verification vs Planning

Skill 13:

```text id="a6c8uq"
What implementation work should be done?
```

Skill 16:

```text id="w1txkc"
Was that approved work actually implemented?
```

Skill 16 MUST NOT create new plan items from missing implementation.

---

# 37. Verification vs Validation

Skill 14 validates the implementation plan before execution.

Skill 16 verifies the outcome after execution.

```text id="32gyd2"
Skill 14
Plan Validation

Skill 15
Execution

Skill 16
Execution Verification
```

These roles MUST remain separate.

---

# 38. Quality Gate

A verification run may PASS only when:

```text id="eq9ets"
100% required approved scope accounted for

AND

100% required plan items traceable

AND

completion claims sufficiently evidenced

AND

no unsupported scope remains accepted

AND

no material contradiction remains unresolved

AND

required dependencies verified

AND

blocking conditions resolved
```

`PASS_WITH_GAPS` may be used only for explicitly non-blocking gaps.

---

# 39. Golden Rules

> Verify, do not implement.

> Verify approved scope, not ideal scope.

> Execution completion is not verification completion.

> Evidence is required for verification.

> Partial execution remains partial.

> OPEN remains OPEN until supported by evidence.

> UNKNOWN remains UNKNOWN until supported by evidence.

> Do not approve invented scope.

> Do not repair missing implementation.

> Do not redesign the plan.

> Do not invent technical decisions during verification.

> Preserve end-to-end traceability.

---

# 40. Regression Result

Skill 16 was validated through three execution-test rounds.

```text id="x7q9lr"
Round 1:
20/20 PASS

Round 2:
20/20 PASS

Round 3:
20/20 PASS
```

Total:

```text id="d5q3kp"
60/60 PASS
```

Regression verification:

```text id="v8k2mr"
0 unsupported scope accepted
0 missing approved scope falsely verified
0 invalid traceability accepted
0 cross-item evidence accepted
0 unsupported completion claims accepted
0 blocking OPEN items ignored
0 unresolved dependencies accepted
0 UNKNOWN values upgraded without evidence
0 cancelled executions treated as verified
0 verification repairs performed
0 plan redesigns performed
0 stale evidence accepted without qualification
0 false completion claims accepted
0 partial coverage promoted to full verification
0 blocker bypasses accepted
0 ambiguous evidence silently reused
0 scope-version mismatches accepted
0 execution-state / verification-status confusion
0 invalid verification result / recommendation combinations
0 false PASS aggregations
0 historical results overriding current evidence
0 current failures hidden by historical PASS
0 recommendation overrides verification findings
```

---

# 41. Promotion Status

```text id="f1xq5r"
Previous Version:
v0.1 — DRAFT

Validation:
Round 1 = 20/20 PASS
Round 2 = 20/20 PASS
Round 3 = 20/20 PASS

Regression:
60/60 PASS

Promotion:
APPROVED

Current Version:
v1.0

Status:
LOCKED
```

---

# 42. Lock Rule

`implementation-verification` is now:

```text id="w8r1ce"
v1.0 — LOCKED
```

The validated verification rules MUST NOT be weakened or silently altered.

Any material rule change requires:

```text id="x9m3zu"
new version
+
updated test coverage
+
appropriate regression
```

A locked Skill MUST NOT be modified merely to make a failing implementation, evidence set, or verification test appear to pass.
