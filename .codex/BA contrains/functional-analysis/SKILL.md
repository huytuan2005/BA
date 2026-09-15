---
name: functional-analysis
description: Analyze functional behavior from discovered requirements and business processes. Use when requirements need to be decomposed into observable system functions, inputs, outputs, rules, actors, and unresolved behavior without defining technical implementation.
---

# Functional Analysis

## Goal

Turn supported requirements and business processes into a compact,
traceable functional baseline.

## Input

Use:
- discovered functional requirements;
- supported business processes;
- source facts;
- business rules;
- open questions.

Do not treat assumptions or open questions as confirmed functionality.

## Load only what is needed

1. Read the relevant project evidence first.
2. Use `references/quality-check.md` only when validating or reviewing the result.
3. Do not load unrelated skills unless the task requires them.

## Rules

1. Derive functions only from supported requirements and process analysis.
2. Preserve the source actor.
3. Preserve traceability to the original requirement.
4. Decompose broad requirements into smaller functional capabilities only when this improves clarity.
5. Do not invent functionality to complete an assumed workflow.
6. Do not convert business nouns into system functions without evidence.
7. Preserve ambiguous source wording.
8. Do not invent statuses, transitions, validations, calculations, notifications, integrations, or approval flows.
9. Do not define APIs, database structures, UI screens, components, classes, or implementation technologies.
10. Do not create NFRs unless explicitly supported.
11. Distinguish confirmed functionality from unresolved behavior.
12. If a functional interpretation requires significant inference, mark it `OPEN_QUESTION` and lower confidence.

## Functional capability

A functional capability describes what the system supports for an actor.

Prefer:

`The system shall allow <actor> to <observable capability>.`

A capability may contain:
- actor;
- action;
- business object;
- relevant business context;
- source requirement.

Do not add implementation mechanisms.

## Functional decomposition

Decompose a requirement when:
- it contains multiple distinct actor-visible capabilities;
- separating capabilities improves traceability;
- each resulting capability can stand independently.

Do not decompose merely to create CRUD operations.

For example:

`manage units`

must not automatically become:

- create unit;
- view unit;
- update unit;
- delete unit.

If the source does not specify these operations, preserve the broader capability and record the ambiguity.

## Ambiguity handling

Do not operationalize ambiguous terms such as:

`manage`, `monitor`, `support`, `handle`, `track`,
`appropriate`, `available`, `suitable`, `overdue`.

When ambiguity affects behavior:

- preserve the source meaning;
- do not invent missing operations;
- lower confidence;
- create an `OPEN_QUESTION`.

## Inputs

Only identify an input when the source explicitly states or directly supports
that information being provided or used by the function.

Do not treat:
- business values;
- configuration categories;
- fee types;
- report categories;
- actor names

as functional inputs unless the source supports that interpretation.

## Outputs

Describe observable business-level results only.

Examples:
- information is made available to the actor;
- a requested capability is supported;
- a business decision can be made based on specified information.

Do not invent:
- database records;
- API responses;
- generated IDs;
- emails;
- notifications;
- audit entries;
- technical files.

## Business rules

Only identify a business rule when it expresses:
- a constraint;
- a condition;
- a policy;
- a decision rule;
- a required relationship.

Every derived rule must trace to an original requirement or source fact.

Use:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

Never use a generated functional ID as the sole source of a business rule.

## Confidence

Use only:

- `HIGH`: directly supported with little interpretation.
- `MEDIUM`: supported but requires meaningful interpretation or decomposition.
- `LOW`: significant ambiguity or inference remains.

If confidence is `LOW` because behavior is unresolved, create an
`OPEN_QUESTION`.

## Functional ID

Use:

`FN-<PROJECT>-<NNN>`

Number sequentially within the project.

Example:

`FN-SELF-STORAGE-001`

## Traceability

Every functional capability must trace to one or more original requirements.

Use the original requirement ID as the primary source.

Example:

`FN-SELF-STORAGE-001 → FR-SELF-STORAGE-001`

Do not use:
- BP ID;
- FN ID;
- BR ID

as a replacement for the original requirement source.

## Output contract

The section names, order, and numbering are fixed.

Return exactly:

### 1. Project Context

1–3 concise bullets.

### 2. Functional Capability Inventory

Table:

`ID | Actor | Functional Capability | Source | Confidence`

### 3. Functional Inputs

Table:

`Function | Input | Source | Confidence`

If none are supported:

`None identified from source.`

### 4. Functional Outputs

Table:

`Function | Observable Output | Source | Confidence`

### 5. Functional Rules and Constraints

Table:

`ID | Rule | Source | Status`

Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

## Functional Dependencies

A functional dependency is a relationship between two or more
functional capabilities.

A dependency is valid only when the source explicitly indicates that
one functional capability requires, enables, or relies on another
functional capability.

The dependency target MUST be another functional capability identified
by an `FN-*` identifier.

Valid example:
`FN-A → FN-B`

The source must explicitly support the relationship.

Do NOT classify the following as functional dependencies:
- function inputs;
- business objects;
- selection factors;
- conditions;
- prerequisites;
- actor information;
- configuration values;
- process context.

Invalid examples:
- `FN-A → scheduled appointment`
- `FN-A → input`
- `FN-A → condition`
- `FN-A → business object`
- `FN-A → selection factor`
- `FN-A → prerequisite`
- `FN-A → actor information`
- `FN-A → configuration`
- `FN-A → process context`

Do NOT infer dependencies from:
- process ordering;
- business plausibility;
- common system design;
- one function using information produced by another function.

Process order alone does not establish a functional dependency.

If no explicit function-to-function dependency is supported by the
source, write:

`No explicit function-to-function dependencies are identified from the source.`

When no explicit dependency exists, do NOT create a dependency table.
### 7. Unsupported or Ambiguous Behavior

List behavior that cannot safely be defined from the source.

### 8. Functional Traceability

Show:

`Function → Requirement → Business Process`

If a business process is not available, use:

`Function → Requirement`

Flag uncovered requirements.

### 9. Open Questions

Only include questions that can change:
- functional scope;
- actor responsibility;
- function behavior;
- business rules;
- inputs or outputs;
- acceptance behavior.

Prefer fewer, higher-value questions.

Merge questions addressing the same unresolved functional area.
nput classification
### 10. Quality Gate

Use exactly one:

- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Output consistency checks

Before finalizing, verify:

- Every function has an `FN-*` ID.
- Every function traces to an original `FR-*`.
- Every function has an actor.
- No unsupported CRUD operations were invented.
- Inputs are supported by source evidence.
- Outputs remain business-level.
- No API, database, UI, code, or implementation details were introduced.
- Business rules trace to original source requirements.
- Ambiguous behavior remains unresolved.
- `LOW` confidence items have appropriate open questions.
- Every source requirement is represented or explicitly marked uncovered.
- Functional dependencies are evidence-based.
- Open questions are not unnecessarily duplicated.

## Anti-bloat

- Do not restate the full requirements.
- Do not explain BA theory.
- Do not generate use cases unless explicitly requested.
- Do not generate user stories unless explicitly requested.
- Do not generate acceptance criteria unless explicitly requested.
- Do not generate APIs, data models, UI designs, or implementation details.
- Prefer one clear functional capability over several artificial sub-functions.

## Input classification

Classify information as a functional input only when the source indicates
that the actor provides or the function explicitly uses that information.

If information merely describes a condition, context, or prerequisite,
do not automatically classify it as an input.

When useful, describe it as contextual information instead.

Do not invent:
- form fields;
- parameters;
- database fields;
- API payloads;
- technical request data.

## Open-question deduplication

Prefer fewer, higher-value open questions.

Merge questions when they address the same unresolved functional area.

Do not repeat the same uncertainty across multiple questions.

Prioritize questions that can change:
- functional scope;
- actor responsibility;
- function behavior;
- business rules;
- inputs or outputs;
- acceptance behavior.

## Completion rule

If the evidence is sufficient, complete the analysis without asking the user
for confirmation.

Record unresolved behavior as `OPEN_QUESTION`.

