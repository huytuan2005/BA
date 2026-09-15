---
name: use-case-generator
description: Generate source-supported use cases from discovered functional requirements and functional capabilities. Use when functional analysis needs to be represented as actor-system interactions without inventing workflows, rules, dependencies, or implementation details.
---

# Use Case Generator

## Goal

Turn supported functional requirements and functional capabilities into a
compact, traceable use-case baseline.

Use cases describe meaningful actor-system interactions.
They do not define technical implementation.

## Input

Use:
- discovered functional requirements;
- functional capability inventory;
- functional rules and constraints;
- functional inputs and outputs;
- unsupported or ambiguous behavior;
- open questions.

Do not treat assumptions or open questions as confirmed behavior.

## Load only what is needed

1. Read the relevant project evidence first.
2. Use `references/quality-check.md` only when validating/reviewing.
3. Do not load unrelated skills unless the task requires them.

## Core Rules

1. Every use case must trace to one or more original `FR-*` requirements.
2. Preserve the source actor.
3. Describe an observable actor-system interaction.
4. Generate use cases only from supported functional capabilities.
5. Do not invent actors, goals, workflows, business rules, statuses,
   validations, notifications, integrations, or implementation details.
6. Do not turn every function into a separate use case automatically.
7. Group functions only when they represent one coherent actor goal.
8. Keep distinct actor goals as separate use cases when combining them would
   reduce clarity or traceability.
9. Preserve ambiguous source capabilities instead of operationalizing them.
10. Do not convert business context, inputs, conditions, prerequisites,
    selection factors, configuration values, or process order into
    use-case relationships unless the source explicitly supports the
    relationship.
11. Do not infer `include`, `extend`, generalization, or dependency
    relationships from process order or business plausibility.
12. Do not create detailed main flows or alternative flows unless explicitly
    requested and sufficiently supported by the source.
13. Do not define APIs, database structures, UI components, classes,
    technologies, or architecture.
14. Do not create NFRs unless explicitly supported.

## Use Case Boundary

A use case represents a meaningful actor goal or actor-system interaction.

Prefer:

`<Actor> <goal/action>`

Examples:
- Customer reserves a storage unit.
- Customer makes a payment.
- Staff checks a reservation.
- Manager views facility reports.

Avoid technical or implementation-oriented names such as:
- Submit reservation API.
- Update reservation database.
- Validate payment endpoint.
- Render customer dashboard.

## Use Case ID

Use:

`UC-<PROJECT>-<NNN>`

Number sequentially within the project.

## Naming

Prefer concise verb + business object/goal.

Good:
- Reserve Storage Unit
- Make Payment
- Check Reservation
- Assign Unit
- View Facility Reports

Avoid:
- Manage Storage Unit

when the source does not define what "manage" means.

If an ambiguous capability must be represented, preserve the ambiguity:

`Manage Rented Storage Units`

and document the unresolved behavior.

## Functional Capability Mapping

A use case may map to:
- one functional capability;
- multiple closely related functional capabilities supporting one actor goal.

Do not force a one-to-one mapping.

Example:

`FN-A: view facility information`
`FN-B: view available units`

may become one use case only if the source supports them as one coherent
actor goal.

Do not combine unrelated capabilities merely to reduce the number of
use cases.

## Actor

Use the actor exactly as defined by the source.

Do not:
- create new actors;
- merge actors without evidence;
- assign responsibilities to another actor;
- infer system actors or external services.

## Goal

The goal must represent what the actor wants to accomplish through the
system.

Do not strengthen the source.

For example:

Source:
`manage rented units`

Do not generate:
`Create, update, delete, transfer, and terminate rented units`

unless those operations are explicitly supported.

## Preconditions

A precondition may be included only when explicitly supported by the source.

Do not infer preconditions from:
- process order;
- common business practice;
- technical requirements;
- assumptions.

Do not automatically treat another use case as a precondition.

Example:

Do NOT infer:

`Reserve Unit` must be completed before `Check In`

unless the source explicitly establishes that relationship.

If no supported precondition exists, write:

`None explicitly identified from the source.`

## Postconditions

A postcondition describes an observable business result or resulting state
after the use case, but only when explicitly supported by the source.

Do not reinterpret the functional capability itself as a postcondition.

Do not invent:
- records created;
- reservation status changes;
- contract creation;
- payment confirmation;
- unit assignment;
- notifications;
- invoices;
- generated identifiers;
- database updates.

If the source only states that the actor can perform a capability and does
not define a resulting business state, write:

`None explicitly identified from the source.`

## Alternative / Exception Flows

Do not create alternative or exception flows unless:
- the source explicitly supports the variation; or
- the user explicitly requests analysis of the known ambiguity.

Never invent:
- payment failure;
- invalid data;
- unavailable unit;
- expired reservation;
- permission denial;
- notification failure;
- system error

unless supported by the source.

## Use Case Relationships

Supported relationships are limited to relationships explicitly established
by the source.

### Include

Use `include` only when the source explicitly establishes that one use case
always requires another use case.

### Extend

Use `extend` only when the source explicitly establishes optional or
conditional behavior extending another use case.

### Generalization

Use actor or use-case generalization only when explicitly supported.

### Dependency

Do not infer use-case dependency from:
- input;
- business object;
- condition;
- prerequisite;
- selection factor;
- actor information;
- configuration;
- process context;
- process order;
- business plausibility.

A relationship must connect actual use cases:

`UC-* → UC-*`

If the source does not explicitly support a use-case relationship, do not
create one.

If no explicit relationships exist, write:

`No explicit use-case relationships are identified from the source.`

Do not create a relationship table when none exists.

## Business Rules

Include only rules supported by the source.

Preserve the original rule meaning.

Do not transform selection factors or context into additional use cases.

Example:

`Unit assignment considers unit type, rental period, and availability.`

This is a business rule for the relevant use case, not:

`UC → Unit Type`

or:

`UC → Availability`

## Inputs and Outputs

Use functional inputs and outputs only when relevant to the use case.

Inputs must be source-supported.

Outputs must remain business-level and observable.

Do not convert:
- input → use case;
- output → use case;
- business object → use case;
- field → use case.

## Ambiguity

Check ambiguous terms including:

- manage;
- monitor;
- track;
- support;
- handle;
- appropriate;
- available;
- suitable;
- overdue.

If behavior is undefined:
1. preserve the source wording;
2. do not invent operations;
3. lower confidence;
4. record an open question when it can affect the use case scope or behavior.

## Confidence

Use only:

- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH
Directly supported with little interpretation.

### MEDIUM
Supported but requires meaningful interpretation of the actor goal or
use-case boundary.

### LOW
Significant interpretation is required.

LOW-confidence use cases should normally have a corresponding open question
when the unresolved behavior affects scope or execution.

## Traceability

Every use case must trace to the original requirement:

`UC → FR`

Where useful:

`UC → FR → FN`

Do not use a generated UC ID or FN ID as a substitute for source evidence.

Every source requirement must be:
- represented by at least one use case;
- intentionally covered by another broader use case; or
- explicitly marked as not use-case-defining.

## Output Contract

Return exactly these sections, in this order:

### 1. Project Context

1–3 bullets.

### 2. Actors

Table:

`ID | Actor | Use-Case Goal Summary`

### 3. Use Case Inventory

Table:

`ID | Actor | Use Case | Goal | Source | Confidence`

### 4. Use Case Preconditions

Table:

`Use Case | Preconditions | Source | Confidence`

If none:

`None explicitly identified from the source.`

### 5. Use Case Postconditions

Table:

`Use Case | Observable Postcondition | Source | Confidence`

If none:

`None explicitly identified from the source.`

### 6. Use Case Inputs and Outputs

Table:

`Use Case | Inputs | Outputs | Source`

Only include source-supported information.

### 7. Use Case Rules and Constraints

Table:

`ID | Use Case | Rule | Source | Status`

Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

Do not create rules from ordinary context.

### 8. Use Case Relationships

Only create this table when explicit relationships exist.

Table:

`Source Use Case | Relationship | Target Use Case | Source | Confidence`

Allowed relationships:
- `INCLUDE`
- `EXTEND`
- `GENERALIZATION`
- `DEPENDENCY`

If none:

`No explicit use-case relationships are identified from the source.`

Do not create a table when none exist.

### 9. Unsupported or Ambiguous Behavior

List only unresolved behavior that affects:
- use-case scope;
- actor responsibility;
- preconditions;
- postconditions;
- rules;
- flows;
- relationships.

### 10. Use Case Traceability

Table:

`Use Case | Requirement | Functional Capability`

Flag uncovered requirements.

### 11. Open Questions

Only high-value questions that can change:
- use-case scope;
- actor responsibility;
- behavior;
- rules;
- preconditions;
- postconditions;
- relationships.

Deduplicate related questions.

### 12. Quality Gate

Use one:

- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Output Consistency Checks

Before finalizing:

- Every UC has a stable `UC-*` ID.
- Every UC has a supported actor.
- Every UC traces to an original `FR-*`.
- No unsupported actor is introduced.
- No ambiguous capability is silently expanded.
- No automatic CRUD is invented.
- No workflow is invented.
- No unsupported precondition is inferred.
- No unsupported postcondition is inferred.
- No unsupported alternative flow is invented.
- No business object/input/condition is converted into a use case.
- No process order is converted into a relationship.
- No `include`/`extend`/generalization/dependency is inferred.
- Every relationship is explicitly supported by source evidence.
- Inputs and outputs remain business-level.
- No API/DB/UI/technology details appear.
- Open questions are focused and nonduplicate.
- All source requirements are covered or explicitly marked.
- Postconditions describe resulting business outcomes/states, not a restatement of the use-case capability.
## Anti-Bloat

- Do not explain BA theory.
- Do not restate the full requirements.
- Do not generate detailed flows unless requested.
- Do not create artificial use cases for every input or business object.
- Do not create relationship diagrams unless requested.
- Prefer a small number of meaningful use cases over mechanical decomposition.

## Completion

If the source is sufficient, complete the use-case baseline without asking
for confirmation.

If behavior is unresolved, record it as an open question instead of asking
the user to clarify before producing the baseline.