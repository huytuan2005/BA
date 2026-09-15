# Skill 15 — Implementation Executor

**File:** `implementation-executor/SKILL.md`
**Version:** `v1.0`
**Status:** `LOCKED`

---

# 1. Purpose

The `implementation-executor` skill executes an approved implementation plan after the plan has passed the required implementation-plan validation gate.

The executor translates approved implementation-plan items into controlled execution activity.

The executor MUST:

* execute only approved scope;
* preserve upstream traceability;
* respect dependencies and blockers;
* distinguish OPEN from resolved information;
* distinguish execution state from execution result;
* preserve explicit evidence;
* stop when execution boundaries are violated;
* avoid introducing new requirements or technical decisions.

The executor MUST NOT:

* redesign the implementation plan;
* reinterpret unresolved decisions as facts;
* add unapproved scope;
* invent technical solutions;
* bypass validation gates;
* bypass dependencies or blockers;
* claim completion without evidence.

---

# 2. Execution Boundary

The execution chain is:

```text
Approved Requirements / Upstream Evidence
                ↓
Implementation Artifacts
                ↓
Implementation Plan
                ↓
Skill 14 — Implementation Plan Validator
                ↓
Execution Gate
                ↓
Skill 15 — Implementation Executor
                ↓
Execution Evidence
                ↓
Updated Execution State
```

Skill 15 operates only after the implementation plan has been validated by Skill 14.

Skill 15 MUST NOT move backward into planning or validation in order to justify execution.

---

# 3. Required Inputs

The executor MUST receive, or be able to resolve from authoritative project artifacts:

```text
1. Validated implementation plan
2. Skill 14 validation result
3. Approved implementation items
4. Upstream traceability
5. Approved decisions
6. Dev Standards
7. Dependencies
8. Blockers
9. OPEN items
10. Current implementation state
```

Optional inputs include:

```text
- current source code
- current project structure
- previous execution records
- current execution progress
- developer execution decisions
- test evidence
- build/deployment evidence
- rollback or recovery information
```

Optional inputs MUST NOT override authoritative inputs.

---

# 4. Execution Preconditions

Execution may begin only when all required preconditions are satisfied.

Minimum gate:

```text
Skill 14 = PASS
```

or:

```text
Skill 14 = PASS_WITH_OPEN_ITEMS
```

provided that the selected execution item has no blocking OPEN condition.

Execution MUST NOT begin when:

```text
Skill 14 = FAIL
Skill 14 = BLOCKED
blocking OPEN item exists
required dependency is unsatisfied
explicit blocker exists
scope has changed
required traceability is missing or invalid
approval is contradictory
required execution evidence is unavailable
```

A Skill 14 PASS establishes:

```text
Execution Eligibility
```

It does NOT establish:

```text
Implementation Completion
```

---

# 5. Execution Unit

The basic execution unit is one validated implementation-plan item.

Every execution unit MUST be independently identifiable.

At minimum:

```text
Plan Item ID
Plan Item Title
Implementation Item
Traceability
Evidence
Dependencies
Current Status
Requested Execution
Approved Scope
Execution State
Execution Result
Execution Evidence
```

Execution MUST NOT be based only on:

* filename;
* folder position;
* task naming;
* perceived importance;
* convenience;
* urgency;
* developer preference.

---

# 6. Task Selection

A candidate task may be selected only when:

```text
1. It belongs to approved scope.
2. Its execution gate allows execution.
3. Its current state is executable.
4. All required dependencies are satisfied.
5. No blocking condition remains.
6. Required traceability exists.
7. Scope has not changed.
8. No blocking OPEN item remains.
```

Priority MUST be determined only by explicitly approved priority rules.

The executor MUST NOT infer priority from:

```text
task naming
file order
business importance
urgency
developer convenience
implementation difficulty
personal preference
```

When multiple executable tasks exist, selection MUST follow explicitly defined execution priority.

---

# 7. Dependency Preconditions

A dependency is satisfied only when completion is explicitly established.

Valid dependency completion requires:

```text
Dependency ID
+
Explicit completion state
+
Valid completion evidence
```

The following MUST NOT satisfy a dependency:

```text
"almost complete"
"should be finished"
"probably complete"
"expected to finish"
"developer is working on it"
"looks done"
```

A dependency with contradictory evidence MUST be treated as unresolved.

Example:

```text
dependency record = COMPLETED
current evidence = BLOCKED
```

Result:

```text
dependency check = FAIL
execution state = BLOCKED
```

A `CANCELLED` dependency does NOT satisfy a required dependency.

---

# 8. Blocker Handling

Explicit blockers MUST prevent execution of affected work.

A blocked task MUST NOT be executed.

The executor MUST NOT bypass a blocker through:

```text
temporary substitution
alternative technology
alternative architecture
scope reduction
scope substitution
unapproved workaround
assumed approval
assumed dependency completion
unapproved parallel implementation
```

A blocker may be considered resolved only when explicit evidence resolves the blocking condition.

Blocker resolution means:

```text
eligible for re-evaluation
```

It does NOT mean:

```text
automatically completed
```

---

# 9. OPEN Item Handling

OPEN information is not equivalent to confirmed information.

The executor MUST preserve:

```text
OPEN
UNKNOWN
BLOCKED
```

until explicit evidence resolves them.

A blocking OPEN item causes:

```yaml
state: BLOCKED
result: BLOCKED
```

A non-blocking OPEN item may allow execution to proceed only when the execution can be performed without deciding the unresolved matter.

The executor MUST NOT convert an OPEN item into:

```text
ASSUMED
DEFAULT
PROBABLY
COMMON PRACTICE
MOST LIKELY
CONVENIENT CHOICE
```

Examples of prohibited inference:

```text
provider unresolved
→ choose Stripe

notification channel unresolved
→ choose email

architecture unresolved
→ choose microservices

database field unresolved
→ add the field

authentication behavior unresolved
→ implement JWT
```

---

# 10. Scope Fidelity

The executor MUST execute the exact validated implementation scope.

Approved scope is authoritative.

Execution MUST NOT add:

```text
features
enhancements
UI improvements
API behavior
database behavior
security behavior
notifications
integrations
deployment work
logging behavior
monitoring behavior
performance optimization
extra validation
extra business rules
```

unless those items are explicitly included in approved scope.

A broader request MUST NOT be silently reduced to a safe subset while continuing under the original execution request.

When requested execution exceeds approved scope:

```yaml
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

---

# 11. No New Requirements During Execution

Execution may reveal useful ideas, missing capabilities, or possible improvements.

These discoveries MUST NOT automatically become implementation scope.

Example:

```text
Discovery:
"Users may also need profile export."
```

Allowed:

```text
record discovery
```

Not allowed:

```text
implement profile export
```

unless it becomes explicitly approved through the upstream process.

Execution is not a requirements-discovery authority.

---

# 12. No Technical Invention

The executor MUST NOT invent or silently choose:

```text
API endpoints
request/response contracts
database tables
database columns
database relations
authentication mechanisms
authorization rules
business workflows
status values
notification channels
integration providers
architectural patterns
infrastructure
deployment topology
caching
message brokers
external services
calculations
technical workarounds
recovery strategies
```

When required technical information is unresolved:

```text
retain the unresolved state
```

Do not fill the gap.

---

# 13. Dev Standards Inheritance

Execution MUST inherit approved Dev Standards where applicable.

Dev Standards may govern:

```text
naming
coding conventions
directory structure
testing conventions
logging
error handling
security standards
deployment conventions
branching
documentation
tooling
```

Dev Standards MUST NOT be used to create product requirements that are not otherwise approved.

Precedence remains:

```text
Explicit project decision
        ↓
Validated implementation plan
        ↓
Approved implementation artifacts
        ↓
Dev Standards
        ↓
Existing convention
```

Lower-level conventions MUST NOT override explicit project decisions.

---

# 14. Execution Traceability

Every execution MUST preserve the chain:

```text
Execution
   ↓
Implementation Plan Item
   ↓
Implementation Item
   ↓
Approved Upstream Evidence
```

A valid traceability record must be:

```text
present
identifiable
scope-consistent
authoritative
```

The executor MUST reject:

```text
fabricated IDs
unknown IDs presented as valid
references to unrelated implementation items
stale references
scope-mismatched references
missing references
```

Missing or invalid execution traceability prevents execution.

---

# 15. Normalized Execution State Model

Skill 15 uses exactly the following execution states:

```text
NOT_STARTED
READY
IN_PROGRESS
BLOCKED
COMPLETED
FAILED
CANCELLED
```

These are execution **states**.

`PARTIALLY_COMPLETED` MUST NOT be used.

---

# 16. Normalized Execution Result Model

Skill 15 uses exactly the following execution results:

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

These are execution **results**.

`PARTIAL_EXECUTION` is a result, not a state.

---

# 17. State / Result Separation

The executor MUST maintain a strict separation:

```text
STATE
=
current execution condition
```

```text
RESULT
=
outcome of the current execution action
```

They MUST NOT be merged.

Valid combinations include:

```text
NOT_STARTED + NO_ACTION
READY       + STARTED
IN_PROGRESS + CONTINUE
IN_PROGRESS + PARTIAL_EXECUTION
COMPLETED   + COMPLETED
BLOCKED     + BLOCKED
FAILED      + FAILED
CANCELLED   + CANCELLED
```

The following combinations are invalid:

```text
COMPLETED + BLOCKED
COMPLETED + FAILED
COMPLETED + PARTIAL_EXECUTION
FAILED + COMPLETED
BLOCKED + CONTINUE
BLOCKED + COMPLETED
CANCELLED + CONTINUE
CANCELLED + COMPLETED
```

Invalid combinations MUST be rejected.

---

# 18. Partial Execution

Partial execution is represented only as:

```yaml
state: IN_PROGRESS
result: PARTIAL_EXECUTION
```

The executor MUST record:

```text
completed_portion
remaining_portion
execution_evidence
```

Example:

```yaml
state: IN_PROGRESS
result: PARTIAL_EXECUTION

completed_portion:
  - "Profile viewing"

remaining_portion:
  - "Approved profile update"
```

The executor MUST NOT use:

```text
PARTIALLY_COMPLETED
```

as a state or result.

Partial progress MUST NOT be reported as completion.

---

# 19. Completion Criteria

A task may be marked:

```text
state: COMPLETED
result: COMPLETED
```

only when all approved completion criteria are satisfied.

Completion requires sufficient execution evidence.

The following are insufficient by themselves:

```text
claim
appearance
intention
partial implementation
stale evidence
unverified developer statement
evidence from another task
```

A completion claim without sufficient evidence MUST NOT become `COMPLETED`.

---

# 20. Execution Evidence

Execution evidence must be tied to the executed plan item.

Evidence may include approved project evidence such as:

```text
source changes
test results
build results
verification results
approved deployment evidence
approved environment evidence
other explicit execution evidence
```

Evidence belonging to another plan item MUST NOT be reused.

Contradictory evidence MUST be surfaced.

Example:

```text
plan state = COMPLETED

verification:
"feature remains incomplete"
```

The executor MUST NOT preserve the unsupported completion claim.

---

# 21. Failure Handling

When execution fails:

```yaml
state: FAILED
result: FAILED
```

The executor MUST record:

```text
failure reason
execution evidence
affected portion
current state
```

Failure MUST NOT trigger an invented workaround.

The executor MUST NOT automatically:

```text
switch technology
switch architecture
switch provider
change database design
change API design
expand scope
```

---

# 22. Recovery Handling

A failed task may become eligible for retry only after the applicable recovery authorization is explicit.

Required condition:

```text
recovery authorization = explicit
```

and, where applicable:

```text
scope change = false
```

If recovery changes scope:

```yaml
state: BLOCKED
result: BLOCKED
recommendation: REVALIDATE_CHANGED_SCOPE
```

Recovery MUST NOT become a hidden mechanism for introducing new implementation scope.

---

# 23. Cancelled Tasks

A cancelled implementation-plan item MUST NOT be automatically reactivated.

The executor MUST NOT infer:

```text
"this feature is still useful"
```

as authorization to resume it.

Without explicit authorization:

```yaml
state: CANCELLED
result: NO_ACTION
```

---

# 24. Execution Independence and Ordering

A blocked task MUST NOT automatically block unrelated executable work.

Example:

```text
IP-101 = BLOCKED
IP-102 = READY
IP-102 has no dependency on IP-101
```

The executor may execute:

```text
IP-102
```

provided all other preconditions are satisfied.

However, the executor MUST follow explicit dependency chains.

A dependent task MUST NOT bypass a blocked prerequisite.

---

# 25. Execution Workflow

The executor MUST follow this workflow:

```text
1. Select Candidate Task
        ↓
2. Validate Execution Gate
        ↓
3. Validate Task Status
        ↓
4. Validate Dependencies
        ↓
5. Validate Blockers
        ↓
6. Validate Scope
        ↓
7. Validate OPEN Items
        ↓
8. Validate Traceability
        ↓
9. Capture Pre-Execution State
        ↓
10. Execute Approved Work
        ↓
11. Capture Execution Evidence
        ↓
12. Validate Result
        ↓
13. Update Execution State
        ↓
14. Determine Next Executable Task
```

The executor MUST stop at any step where a blocking condition is detected.

---

# 26. Step 1 — Select Candidate Task

Candidate selection MUST consider:

```text
approved scope
current status
dependency readiness
blocker state
OPEN item state
explicit priority
traceability
```

No candidate may be selected merely because it appears first in a list.

---

# 27. Step 2 — Validate Execution Gate

Check:

```text
Skill 14 result
```

Decision:

```text
PASS
→ continue validation

PASS_WITH_OPEN_ITEMS
→ continue only if OPEN is non-blocking

FAIL
→ BLOCKED + NO_ACTION

BLOCKED
→ BLOCKED + NO_ACTION
```

---

# 28. Step 3 — Validate Task Status

Recommended executable entry:

```text
READY
```

`IN_PROGRESS` may continue an already active task when the requested execution is explicitly within its remaining approved scope.

Existing terminal states require special handling:

```text
COMPLETED
→ no re-execution

FAILED
→ recovery authorization required

CANCELLED
→ explicit reactivation required
```

---

# 29. Step 4 — Validate Dependencies

For every dependency:

```text
dependency exists
dependency state is explicitly known
dependency is COMPLETED where completion is required
dependency evidence is sufficient
no contradiction exists
```

Failure results in:

```yaml
state: BLOCKED
result: BLOCKED
```

---

# 30. Step 5 — Validate Blockers

Check for:

```text
direct blocker
indirect dependency blocker
approval blocker
architecture blocker
provider blocker
technical decision blocker
environment blocker
execution evidence blocker
```

A blocker may not be silently bypassed.

---

# 31. Step 6 — Validate Scope

Compare:

```text
approved scope
vs
requested execution
```

Allowed:

```text
requested execution ⊆ approved scope
```

Not allowed:

```text
requested execution > approved scope
```

Changed scope requires:

```text
REVALIDATE_CHANGED_SCOPE
```

---

# 32. Step 7 — Validate OPEN Items

Classify:

```text
NONE
NON_BLOCKING
BLOCKING
```

Rules:

```text
NONE
→ continue

NON_BLOCKING
→ continue without guessing

BLOCKING
→ BLOCKED
```

---

# 33. Step 8 — Validate Traceability

Confirm:

```text
Execution
→ Plan Item
→ Implementation Item
→ Approved Evidence
```

Traceability must match the executed scope.

Failure:

```yaml
state: BLOCKED
result: NO_ACTION
recommendation: STOP_EXECUTION
```

---

# 34. Step 9 — Capture Pre-Execution State

Before executing, capture relevant baseline information:

```text
current task state
dependency state
blocker state
OPEN item state
approved scope
existing implementation state
relevant execution evidence
```

This prevents unsupported claims about what changed during execution.

---

# 35. Step 10 — Execute Approved Work

Only the approved execution work may be performed.

During execution:

```text
Do not redesign.
Do not add requirements.
Do not invent missing decisions.
Do not create unapproved scope.
Do not silently change architecture.
```

---

# 36. Step 11 — Capture Execution Evidence

After execution, capture evidence sufficient to determine:

```text
completed
partially completed
failed
blocked
```

Evidence must correspond to the actual plan item.

---

# 37. Step 12 — Validate Result

Determine whether execution actually achieved the approved completion criteria.

Possible outcomes:

```text
COMPLETED
PARTIAL_EXECUTION
FAILED
BLOCKED
NO_ACTION
```

The executor MUST NOT claim completion merely because execution was attempted.

---

# 38. Step 13 — Update Execution State

Examples:

```text
READY
 ↓
IN_PROGRESS
 ↓
COMPLETED
```

```text
READY
 ↓
BLOCKED
```

```text
IN_PROGRESS
 ↓
PARTIAL_EXECUTION
 ↓
IN_PROGRESS
```

```text
IN_PROGRESS
 ↓
FAILED
```

Invalid transitions MUST be rejected.

---

# 39. Step 14 — Determine Next Executable Task

After an execution result, the executor determines whether another task may proceed.

Selection MUST use:

```text
explicit priority
dependency readiness
blocker state
scope approval
execution eligibility
```

The executor MUST NOT remain blocked on one branch when an unrelated executable task exists.

When no executable task exists, execution MUST stop or wait according to blocker conditions.

---

# 40. Decision Matrix

| Condition                                        | State                  | Result             | Action            |
| ------------------------------------------------ | ---------------------- | ------------------ | ----------------- |
| Skill 14 PASS, task ready                        | READY / IN_PROGRESS    | STARTED / CONTINUE | Execute           |
| Skill 14 PASS_WITH_OPEN_ITEMS, non-blocking OPEN | READY                  | STARTED            | Execute           |
| Skill 14 FAIL                                    | BLOCKED                | NO_ACTION          | Stop              |
| Skill 14 BLOCKED                                 | BLOCKED                | NO_ACTION          | Stop              |
| Dependency unsatisfied                           | BLOCKED                | BLOCKED            | Wait              |
| Blocking OPEN                                    | BLOCKED                | BLOCKED            | Wait              |
| Scope changed                                    | BLOCKED                | BLOCKED            | Revalidate        |
| Missing traceability                             | BLOCKED                | NO_ACTION          | Stop              |
| Task already completed                           | COMPLETED              | NO_ACTION          | Do not execute    |
| Execution partially succeeds                     | IN_PROGRESS            | PARTIAL_EXECUTION  | Continue later    |
| Execution succeeds                               | COMPLETED              | COMPLETED          | Continue queue    |
| Execution fails                                  | FAILED                 | FAILED             | Stop / recover    |
| Task cancelled                                   | CANCELLED              | NO_ACTION          | Do not reactivate |
| No executable tasks remain                       | BLOCKED or NOT_STARTED | NO_ACTION          | Stop / wait       |

---

# 41. Execution Loop

The execution loop is:

```text
Find candidate
    ↓
Check execution gate
    ↓
Check readiness
    ↓
Check dependency
    ↓
Check blocker
    ↓
Check scope
    ↓
Check OPEN items
    ↓
Check traceability
    ↓
Execute
    ↓
Collect evidence
    ↓
Validate result
    ↓
Update state
    ↓
Select next task
```

The loop MUST terminate when:

```text
no executable task remains
hard blocker exists
execution gate fails
scope changes
required authorization is missing
execution evidence is insufficient
a contradiction prevents safe continuation
```

---

# 42. Stop Conditions

Execution MUST stop immediately when:

```text
Skill 14 = FAIL
Skill 14 = BLOCKED
blocking OPEN discovered
dependency becomes unsatisfied
scope changes
approval becomes contradictory
traceability becomes invalid
required authorization is missing
execution violates approved scope
unsupported technical decision becomes necessary
completion evidence is insufficient
hard execution contradiction is discovered
```

The executor MUST NOT continue merely to avoid an incomplete queue.

---

# 43. Change Control

Any change affecting:

```text
scope
requirements
architecture
API
database
security
workflow
integration
deployment
dependency
approval
```

MUST be treated as a change to the approved execution boundary.

The executor MUST NOT silently absorb the change.

Required response:

```text
pause affected execution
record change
identify impact
request upstream revalidation
```

---

# 44. Discovered Information

Execution may reveal:

```text
missing requirement
inconsistent artifact
technical limitation
implementation conflict
dependency issue
environment issue
new feature opportunity
```

The executor MUST record the discovery when relevant.

The executor MUST NOT transform discovery into approved implementation scope automatically.

---

# 45. Contradiction Handling

Contradictions include:

```text
approval = approved + revoked
dependency = completed + blocked
task = completed + incomplete evidence
scope = V1 + V2
traceability = one item + unrelated evidence
```

When contradiction materially affects safe execution:

```text
state: BLOCKED
```

or:

```text
state: FAILED
```

depending on whether the contradiction prevents starting or invalidates an execution/completion claim.

The executor MUST NOT choose whichever source is more convenient.

---

# 46. Rollback / Recovery

Rollback or recovery MUST follow approved project mechanisms.

The executor MUST NOT invent a rollback architecture or recovery strategy.

Where rollback is required but the approved procedure is unknown:

```text
state: BLOCKED
result: BLOCKED
```

The executor records the condition and stops affected execution.

---

# 47. Execution Reporting

Every execution MUST produce an explicit execution record.

Minimum structure:

```yaml
execution:
  run_id: EXEC-xxx
  validation_gate: PASS | PASS_WITH_OPEN_ITEMS | BLOCKED | FAIL
  plan_item: IP-xxx

  preconditions:
    result: PASS | FAIL

  dependencies:
    result: PASS | FAIL

  blockers:
    result: NONE | BLOCKED

  open_items:
    result: NONE | NON_BLOCKING | BLOCKING

  scope_check:
    result: PASS | FAIL

  state: NOT_STARTED | READY | IN_PROGRESS | BLOCKED | COMPLETED | FAILED | CANCELLED

  result: STARTED | CONTINUE | COMPLETED | BLOCKED | FAILED | CANCELLED | PARTIAL_EXECUTION | NO_ACTION

  evidence:
    - <execution evidence>

  open_items_remaining:
    - <remaining item>

  recommendation:
    CONTINUE_NEXT_READY_ITEM
    | WAIT_FOR_BLOCKER_RESOLUTION
    | REVALIDATE_CHANGED_SCOPE
    | STOP_EXECUTION
```

---

# 48. Findings

The executor SHOULD record explicit findings where execution cannot safely proceed.

Examples:

```text
EXECUTION_TRACEABILITY_MISSING
TRACEABILITY_REFERENCE_INVALID
TRACEABILITY_SCOPE_MISMATCH
DEPENDENCY_STATE_CONTRADICTION
DEPENDENCY_COMPLETION_EVIDENCE_MISSING
UNRESOLVED_PROVIDER_DECISION
ARCHITECTURE_DECISION_OPEN
RECOVERY_DECISION_OPEN
COMPLETION_EVIDENCE_INSUFFICIENT
EXECUTION_EVIDENCE_SCOPE_MISMATCH
COMPLETION_STATE_CONTRADICTION
STALE_EXECUTION_SCOPE
APPROVAL_STATE_CONTRADICTION
INVALID_STATE_RESULT_COMBINATION
```

Findings MUST describe the execution problem.

They MUST NOT silently create a solution.

---

# 49. Quality Gate

Execution is considered successful only when:

```text
scope respected
dependencies satisfied
blockers resolved
OPEN items handled correctly
traceability valid
approved work executed
execution evidence captured
completion criteria satisfied
state/result combination valid
```

A successful build alone does not prove completion unless build evidence is itself the approved completion criterion.

---

# 50. Skill 14 / Skill 15 Separation

Skill 14:

```text
validates the implementation plan
```

Skill 15:

```text
executes the validated implementation plan
```

The distinction is:

```text
Skill 14
→ "May this plan be executed?"

Skill 15
→ "Execute the approved plan."
```

Skill 15 MUST NOT redesign the plan in order to make it executable.

When the plan is not executable:

```text
return blocked / no-action
```

not:

```text
invent missing design
```

---

# 51. Execution Status Invariants

The following invariants MUST always hold:

```text
1. BLOCKED means execution is not currently permitted.
2. COMPLETED requires evidence.
3. FAILED means execution did not complete successfully.
4. CANCELLED means execution is not automatically resumed.
5. IN_PROGRESS may represent partial execution.
6. PARTIAL_EXECUTION is a result, not a state.
7. READY means eligible to begin execution.
8. PASS from Skill 14 does not imply completion.
9. OPEN is never silently converted into an assumption.
10. Dependency completion must be explicit.
11. Scope expansion requires revalidation.
12. Traceability must remain valid.
```

---

# 52. Golden Rules

```text
1. Execute only validated scope.
2. Never guess unresolved information.
3. Never bypass a dependency.
4. Never bypass a blocker.
5. Never invent technical decisions.
6. Never expand approved scope.
7. Preserve complete execution traceability.
8. Require completion evidence.
9. Represent partial execution as IN_PROGRESS + PARTIAL_EXECUTION.
10. Keep state and result separate.
11. Treat Skill 14 PASS as execution eligibility, not completion.
12. Never reactivate cancelled work without explicit authorization.
13. Never retry failed work without applicable recovery authorization.
14. Never convert discovery into new scope.
15. Never accept fabricated or mismatched evidence.
16. Reject invalid state/result combinations.
17. Stop when a hard execution boundary is violated.
18. Do not weaken a rule merely to keep execution moving.
19. Do not invent a workaround for an unresolved decision.
20. Preserve upstream traceability through execution.
```

---

# 53. Final Execution Contract

```text
implementation-executor

INPUT:
validated implementation plan

GATE:
Skill 14 PASS
or Skill 14 PASS_WITH_OPEN_ITEMS with non-blocking OPEN

EXECUTION:
approved scope only

BLOCK:
FAIL / BLOCKED / blocking OPEN / unsatisfied dependency /
scope change / invalid traceability / hard contradiction

COMPLETION:
state = COMPLETED
result = COMPLETED
+
sufficient execution evidence

PARTIAL:
state = IN_PROGRESS
result = PARTIAL_EXECUTION

FAILURE:
state = FAILED
result = FAILED

CANCELLED:
state = CANCELLED
result = NO_ACTION

UNKNOWN / OPEN:
remain unresolved

NO INVENTION:
mandatory

TRACEABILITY:
Execution → Plan Item → Implementation Item → Approved Evidence
```

---

# 54. Regression Result

Skill 15 was validated through three execution-test rounds.

```text
Round 1:
20/20 PASS

Round 2:
20/20 PASS

Round 3:
20/20 PASS
```

Total:

```text
60/60 PASS
```

Regression verification:

```text
0 executions against FAIL validation
0 executions against BLOCKED validation
0 unsatisfied dependency bypasses
0 blocking OPEN bypasses
0 scope bypasses
0 silent scope expansions
0 invented workarounds
0 invented architecture
0 fabricated traceability
0 traceability mismatches accepted
0 unsupported completion claims
0 invalid state/result combinations
0 unauthorized retries
0 unauthorized recovery executions
0 cancelled-scope reactivations
0 PARTIALLY_COMPLETED states
0 hard-stop violations
```

---

# 55. Promotion Status

```text
Previous Version:
v0.1 — DRAFT

Validated:
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

# 56. Lock Rule

`implementation-executor` is now:

```text
v1.0 — LOCKED
```

The validated execution rules MUST NOT be weakened or silently altered.

Any material rule change requires:

```text
new version
+
updated test coverage
+
appropriate regression
```

A locked Skill MUST NOT be modified merely to make a failing implementation or test appear to pass.
