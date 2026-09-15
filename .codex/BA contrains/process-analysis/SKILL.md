---
name: process-analysis
description: Analyze supported business processes from discovered requirements. Use when requirements need to be organized into business processes, actor interactions, triggers, outcomes, constraints, and unresolved workflow questions.
---

# Process Analysis

## Goal

Turn discovered requirements into a compact, traceable business-process baseline.

## Input

Primary input:
- `projects/<project>/discovered-requirements.md`

The input should contain discovered requirements, actors, business rules,
assumptions, open questions, and traceability where available.

## Load only what is needed

1. Read the discovered requirements first.
2. Use the process-analysis quality check only when validating or reviewing the result.
3. Do not load unrelated skills or project files unless required.
4. Do not treat previous generated output as source evidence unless explicitly provided as input.

## Rules

1. Derive processes only from supported requirements.
2. Preserve the source actor and capability.
3. Group related requirements into business processes when useful.
4. Do not invent workflow steps.
5. Do not invent statuses, transitions, policies, calculations, notifications, integrations, APIs, databases, or UI behavior.
6. Do not assume that one requirement equals one process.
7. Do not assume that one process has a complete end-to-end workflow.
8. Keep process analysis at the business/process level.
9. Preserve ambiguity instead of resolving it through invention.
10. Every derived process must be traceable to one or more requirements.
11. If a process cannot be defined completely, describe only the supported part.
12. Record missing workflow information as `OPEN_QUESTION`.

## Ambiguity handling

Do not operationalize ambiguous terms such as:

`manage`, `monitor`, `support`, `handle`,
`appropriate`, `available`, `suitable`, `overdue`.

When an ambiguous capability is used:

- preserve the original capability;
- do not convert it into CRUD operations;
- do not invent workflow steps;
- do not invent status transitions;
- do not invent responsibilities beyond the stated actor;
- lower confidence when meaningful interpretation is required;
- create an `OPEN_QUESTION` when the ambiguity can change process behavior or scope.

## Process identification

Create a process only when the source supports a meaningful business capability or interaction.

Prefer concise process names such as:

- Facility and Unit Discovery
- Unit Reservation
- Rental Payment
- Check-In and Handover
- Unit Return and Condition Check

Do not create artificial processes such as:

- Login Process

unless authentication/login is explicitly part of the source requirements.

## Process ID

Use:

`BP-<PROJECT>-<NNN>`

Example:

`BP-SELF-STORAGE-001`

Number sequentially within the project.

## Traceability

Every business process must reference one or more source requirement IDs.

Use:

`FR-<PROJECT>-<NNN>`

Business rules may also be referenced when they constrain the process.

### Traceability source rule

The `Source` column must point to the original source evidence,
normally a requirement ID such as `FR-<PROJECT>-<NNN>`.

Do NOT use the newly generated business-process ID or business-rule ID
as the sole source of a derived item.

Correct:

`BP-SELF-STORAGE-002 → FR-SELF-STORAGE-002`

Correct:

`BR-SELF-STORAGE-001 → FR-SELF-STORAGE-014`

Incorrect:

`BR-SELF-STORAGE-001 → BR-SELF-STORAGE-001`

A generated ID identifies the analysis artifact.
It is not source evidence.

If the original source cannot be identified, mark the item
as `OPEN_QUESTION` instead of inventing a source reference.

## Process confidence

Use only:

- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH

The process is directly supported by one or more requirements
and its supported scope is clear.

### MEDIUM

The process is supported, but some sequencing, responsibility,
or operational meaning remains ambiguous.

### LOW

Meaningful interpretation is required to describe the process.
Create an `OPEN_QUESTION`.

## Triggers and inputs

Record only triggers or inputs explicitly supported by the source.

Examples:

- customer arrival;
- facility;
- unit type;
- start date;
- rental period;
- scheduled appointment;
- assigned unit.

### Input classification rule

Do not automatically classify every noun or business value
mentioned in a requirement as a process input.

Distinguish between:

- `TRIGGER`: an event or condition that starts or prompts the process;
- `INPUT`: information or value explicitly supplied or used by the process;
- `BUSINESS_VALUE`: a fee, policy, price, status, or other domain value mentioned by the source.

Only label something as `TRIGGER` or `INPUT` when the source supports
that role.

For example:

If the requirement says:

`Customer pays deposits, rental fees, renewal fees, or extra charges.`

Do not automatically output:

`Input: deposit, rental fee, renewal fee, extra charge.`

Unless the source explicitly describes these as process inputs,
use a conservative description such as:

`Rental-related charge specified by the requirement`

or:

`Not specified`

Do not invent payment data fields, payment methods,
payment states, or payment workflow.

Do not invent:

- automatic triggers;
- system events;
- scheduled jobs;
- validation rules;
- payment callbacks;
- notifications.

If the trigger is unknown, write `Not specified`.

## Outcomes

Record only outcomes supported by the requirements.

Do not infer technical outputs.

For example:

Supported:
- customer reservation is submitted;
- customer receives an assigned unit;
- report can be viewed.

Not supported unless explicitly stated:
- reservation ID is generated;
- invoice is created;
- email is sent;
- database record is updated.

### Outcome wording rule

Do not strengthen a source capability into a completed business outcome.

Prefer:

`The capability to support X is identified.`

when the source only states that X can be managed, supported,
monitored, or handled.

For ambiguous capabilities, preserve the source wording and
avoid implying a defined lifecycle or completion state.

## Process constraints

Include only:

- explicit business rules;
- source-supported conditions;
- source-supported constraints.

Do not turn ordinary facts into business rules.

Use status:

- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

`DERIVED` should be used sparingly.

If a possible rule requires unresolved interpretation, use `OPEN`
and explain the missing information.

## Open-question deduplication

Prefer fewer, higher-value open questions.

Merge questions when they address the same unresolved process area.

Do not repeat the same uncertainty across multiple sections.

Prioritize questions that can change:
- process scope;
- actor responsibility;
- workflow behavior;
- business rules;
- permissions;
- acceptance behavior.

When several unknowns belong to the same area, combine them into one question.

## Output contract

The section names, order, and numbering are fixed.

Do not rename, merge, split, remove, or add top-level sections.

Return exactly:

1. Project Context
2. Supported Business Processes
3. Actor Interactions
4. Process Triggers and Inputs
5. Process Outcomes
6. Process Constraints and Business Rules
7. Unsupported or Ambiguous Process Steps
8. Process Traceability
9. Open Questions
10. Quality Gate
## Business rule traceability

For every business rule included in the process analysis:

1. Identify the original requirement or source evidence.
2. Put that original source ID in the `Source` column.
3. Never use the generated business-rule ID as its own source.
4. If the rule is directly stated by the requirement, use `SOURCE_STATED`.
5. If the rule is inferred from multiple supported requirements, use `DERIVED`
   and cite the supporting requirement IDs.
6. If the rule cannot be established without interpretation, use `OPEN`.

Example:

```text
ID: BR-SELF-STORAGE-001
Rule: Unit assignment considers unit type, rental period, and availability.
Source: FR-SELF-STORAGE-014
Status: SOURCE_STATED


