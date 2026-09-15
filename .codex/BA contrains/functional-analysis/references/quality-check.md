# Functional Analysis Quality Check

Use this reference only when validating or reviewing a functional-analysis
result.

## 1. Requirement Coverage

Check:

- Every functional capability maps to at least one original requirement.
- Every requirement is represented by one or more functions or explicitly
  marked as not function-defining.
- No requirement is silently dropped.
- No function exists without source evidence.

Reject unsupported functional capabilities.

## 2. Actor Accuracy

Check:

- Actor names match the source.
- Actor responsibilities are not expanded.
- Functions are assigned only to actors supported by the source.
- No new actor is invented.

Reject inferred ownership when the source does not support it.

## 3. Functional Boundary

Check that each function describes:

- an observable business capability;
- an actor interaction;
- a business-level system behavior.

Do not allow:

- API endpoints;
- database operations;
- frontend components;
- backend services;
- classes;
- jobs;
- queues;
- technical architecture;
- implementation technologies.

## 4. Functional Decomposition

Check:

- Broad requirements are decomposed only when useful.
- Distinct capabilities have separate function IDs when necessary.
- Decomposition does not automatically create CRUD operations.
- Decomposition does not introduce unsupported behavior.

Example:

Source:

`Facility Manager manages units.`

Valid:

`Facility Manager has a capability to manage units.`

Potentially invalid:

- Create unit
- Edit unit
- Delete unit
- Search unit
- Change unit status

unless the source explicitly supports those operations.

## 5. Ambiguity

Check ambiguous terms:

- manage
- monitor
- support
- handle
- track
- appropriate
- available
- suitable
- overdue

Verify that the analysis:

- preserves the original meaning;
- does not invent operational behavior;
- lowers confidence when necessary;
- creates an `OPEN_QUESTION` when ambiguity affects function behavior.

## 6. Input Accuracy

Check:

- Every functional input is explicitly stated or directly supported.
- Inputs are actual information used or provided by the function.
- Business categories are not automatically treated as inputs.
- No technical input mechanism is invented.

Reject invented:

- form fields;
- API parameters;
- database fields;
- authentication tokens;
- system-generated values.

## 7. Output Accuracy

Check:

- Outputs describe observable business-level results.
- Outputs are supported by source evidence.
- No technical artifacts are presented as outputs.

Reject invented:

- database records;
- API responses;
- generated IDs;
- emails;
- notifications;
- audit logs;
- files;
- system events.

## 8. Business Rules

Check:

- Ordinary facts are not incorrectly promoted to rules.
- Explicit constraints remain `SOURCE_STATED`.
- Reasonable deductions are `DERIVED`.
- Unresolved rules are `OPEN`.
- Every rule traces to an original requirement or source fact.

Important:

A generated `FN-*` or `BR-*` ID is never sufficient as the source.

## 9. Functional Dependencies

Check:
- Every dependency is between functional capabilities.
- The dependency target is another `FN-*` capability.
- Inputs are not classified as dependencies.
- Conditions are not classified as dependencies.
- Business objects are not classified as dependencies.
- Selection factors are not classified as dependencies.
- Prerequisites are not classified as dependencies.
- Actor information is not classified as dependencies.
- Configuration values are not classified as dependencies.
- Process context is not classified as dependencies.
- Process order alone does not establish dependency.
- Business plausibility does not establish dependency.
- One function using information from another does not automatically establish dependency.
- Technical dependencies are excluded.

If no explicit function-to-function dependency is supported, the result must
state that no explicit function-to-function dependencies are identified.
## 10. Traceability

Check:

`Function → Requirement`

and where process analysis exists:

`Function → Requirement → Business Process`

Every function must have a traceable source.

Every requirement must be:

- covered;
- intentionally represented by a broader function;
- or explicitly marked uncovered.

## 11. Open Questions

Check that questions:

- address unresolved functional behavior;
- can affect scope, behavior, responsibility, rules, inputs, outputs, or
  acceptance;
- are not generic discovery questions;
- are not duplicates.

Prefer merging several related unknowns into one higher-value question.

## 12. Quality Gate

### PASS

Use when:

- requirements are sufficiently supported;
- functions are traceable;
- no meaningful ambiguity remains;
- no unsupported behavior is introduced.

### PASS WITH QUESTIONS

Use when:

- core functionality is supported;
- unresolved behavior remains;
- ambiguity is explicitly documented;
- no material unsupported functionality has been invented.

### FAIL

Use when:

- functions cannot be traced to source;
- actors are invented or incorrectly assigned;
- unsupported workflow behavior is introduced;
- CRUD operations are invented from ambiguous language;
- technical implementation details are presented as functional requirements;
- significant source requirements are silently dropped.

## Final Review

Before accepting the result, ask:

1. Can every function be traced to an original requirement?
2. Is the actor supported by the source?
3. Did the analysis invent CRUD behavior?
4. Did it invent workflow or sequencing?
5. Did it invent validation, status, notification, or approval behavior?
6. Are inputs supported?
7. Are outputs business-level and supported?
8. Are business rules correctly classified?
9. Are dependencies evidence-based?
10. Are ambiguous behaviors explicitly unresolved?
11. Are open questions focused and non-duplicative?
12. Were API, database, UI, or implementation details introduced?

If any unsupported behavior is found, correct it before finalizing.