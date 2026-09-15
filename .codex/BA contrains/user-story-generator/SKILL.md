---
name: user-story-generator
description: Generate source-supported user stories and acceptance criteria from functional requirements and use cases. Use when actor goals need to be expressed in concise agile form without inventing behavior, rules, workflows, or implementation details.
---

# User Story Generator

## Goal

Turn supported functional requirements and use cases into a compact,
traceable user-story baseline.

User stories express actor goals in a concise business-facing form.
Acceptance criteria define observable behavior only when the source supports it.

## Input

Use:
- discovered functional requirements;
- functional capability inventory;
- use-case inventory;
- functional/use-case rules and constraints;
- supported inputs and outputs;
- unsupported or ambiguous behavior;
- open questions.

Do not treat assumptions or open questions as confirmed behavior.

## Load only what is needed

1. Read relevant project evidence first.
2. Use `references/quality-check.md` only when validating/reviewing.
3. Do not load unrelated skills unless the task requires them.

## Core Rules

1. Every user story must trace to one or more original `FR-*` requirements.
2. Where a use case exists, preserve `US → UC → FR` traceability.
3. Preserve the source actor and actor goal.
4. Generate stories only from supported functional capabilities/use cases.
5. Do not invent actors, goals, workflows, rules, validations, statuses,
   notifications, integrations, permissions, or implementation details.
6. Do not create one story for every function mechanically when multiple
   functions clearly support one coherent actor goal.
7. Do not combine unrelated actor goals merely to reduce story count.
8. Preserve ambiguous source capabilities instead of operationalizing them.
9. Do not infer business value beyond what the source supports.
10. Do not invent acceptance criteria to make a story look complete.
11. Do not convert technical details, fields, APIs, database structures, UI
    components, classes, or technologies into stories or criteria.
12. Do not create NFR stories unless explicitly requested and supported.

## User Story Boundary

A user story represents a meaningful actor goal or actor-visible capability.

Prefer:

`As a <Actor>, I want to <source-supported goal>, so that I can <source-supported business purpose>.`

If the source does not explicitly support a distinct business purpose,
use the actor goal without inventing a benefit. In that case, write:

`As a <Actor>, I want to <source-supported goal>.`

Do not add generic benefits such as:
- save time;
- improve efficiency;
- increase security;
- improve user experience;
- reduce errors;

unless the source explicitly supports them.

## Story ID

Use:

`US-<PROJECT>-<NNN>`

Number sequentially within the project.

## Story Sizing and Grouping

Group multiple closely related capabilities into one story only when they
represent one coherent actor goal and traceability remains clear.

Keep separate stories when:
- actors differ;
- goals differ;
- acceptance behavior differs materially;
- combining them would hide scope or ambiguity.

Do not split merely because a capability contains several business nouns.
Do not automatically split `manage` into CRUD stories.

## Acceptance Criteria

Acceptance criteria are allowed only when the source provides enough
observable behavior to state them without invention.

A criterion should describe:
- an actor-visible capability;
- a source-supported input or output;
- a source-supported rule or constraint;
- a source-supported condition.

Prefer concise criteria such as:

`- Customer can specify facility, unit type, start date, and rental period when reserving a unit.`

Do not invent:
- Given/When/Then steps that require unsupported behavior;
- validation messages;
- default values;
- status changes;
- notifications;
- confirmations;
- records created;
- payment success/failure behavior;
- authorization outcomes;
- calculations;
- error handling.

If the source is insufficient, write:

`None explicitly identified from the source.`

Do not treat the user story itself as an acceptance criterion.

## Acceptance Criteria and Ambiguity

For ambiguous capabilities such as:
- manage;
- monitor;
- track;
- support;
- handle;
- appropriate;
- available;
- suitable;
- overdue;

preserve the ambiguity.

Do not manufacture detailed criteria for the undefined behavior.
Lower confidence when interpretation is required and record an open question
when the unresolved behavior affects scope or acceptance.

## Business Rules

Attach only rules explicitly supported by the source or directly inherited
from the analyzed requirement/use case.

A rule may constrain a story, but a rule is not automatically a criterion if
its observable acceptance behavior is not fully specified.

Do not create rules from:
- ordinary business nouns;
- process order;
- common practice;
- technical assumptions.

## Inputs and Outputs

Use source-supported inputs and outputs only when relevant to the story.

Inputs must remain business-level.
Outputs must remain observable and business-level.

Do not turn:
- fields into stories;
- API parameters into criteria;
- database records into outputs;
- generated IDs into acceptance criteria;
- tokens/authentication mechanisms into stories.

## Traceability

Every story must trace to the original requirement:

`US → FR`

Where a use case exists:

`US → UC → FR`

Where useful:

`US → UC → FR → FN`

Do not use generated IDs as a substitute for source evidence.

Every source requirement must be:
- represented by at least one story;
- intentionally covered by another broader story; or
- explicitly marked as not suitable for a user story.

## Confidence

Use only:
- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH
Directly supported by the source with little interpretation.

### MEDIUM
Supported but requires meaningful interpretation of the story boundary or
actor goal.

### LOW
Significant interpretation is required, especially for ambiguous behavior.

LOW-confidence stories should normally have a corresponding open question
when the unresolved behavior affects scope or acceptance.

## Output Contract

Return exactly these sections, in this order:

### 1. Project Context
1–3 bullets.

### 2. Actors
Table:
`ID | Actor | Story Goal Summary`

### 3. User Story Inventory
Table:
`ID | Actor | User Story | Source | Confidence`

### 4. Acceptance Criteria
Table:
`User Story | Acceptance Criteria | Source | Confidence`
If none are source-supported:
`None explicitly identified from the source.`

### 5. Story Inputs and Outputs
Table:
`User Story | Inputs | Outputs | Source`
Only include source-supported information.

### 6. Story Rules and Constraints
Table:
`ID | User Story | Rule | Source | Status`
Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

### 7. Unsupported or Ambiguous Behavior
List only unresolved behavior that affects:
- story scope;
- actor responsibility;
- acceptance criteria;
- rules;
- inputs/outputs.

### 8. Story Traceability
Table:
`User Story | Use Case | Requirement | Functional Capability`
Flag uncovered requirements.

### 9. Open Questions
Only high-value questions that can change:
- story scope;
- actor responsibility;
- acceptance criteria;
- rules;
- inputs/outputs.
Deduplicate related questions.

### 10. Quality Gate
Use one:
- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`
Add at most 5 short reasons.

## Output Consistency Checks

Before finalizing:
- Every US has a stable `US-*` ID.
- Every US has a supported actor.
- Every US traces to an original `FR-*`.
- Use-case traceability is preserved where applicable.
- No unsupported business value is invented.
- No ambiguous capability is silently expanded.
- No automatic CRUD is invented.
- No workflow is invented.
- No unsupported acceptance criterion is invented.
- No user story is created from an input, business object, condition, or field alone.
- Inputs and outputs remain business-level.
- Rules trace to original evidence.
- Technical details are excluded.
- Open questions are focused and nonduplicate.
- All source requirements are covered or explicitly marked.

## Anti-Bloat

- Do not explain Agile theory or BA theory.
- Do not restate the full requirements.
- Do not force Given/When/Then formatting.
- Do not generate detailed test cases unless explicitly requested.
- Do not create artificial stories for every input or business object.
- Prefer a small number of meaningful stories over mechanical decomposition.

## Completion

If the source is sufficient, complete the story baseline without asking for
confirmation.

If behavior is unresolved, record it as an open question instead of asking
the user to clarify before producing the baseline.
