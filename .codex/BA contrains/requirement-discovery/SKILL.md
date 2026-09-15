---
name: requirement-discovery
description: Extract supported business and functional requirements from project evidence. Use when requirements are incomplete, unstructured, or supplied as notes, screenshots, documents, actor/capability lists, or existing requirements.
---

# Requirement Discovery

## Goal
Turn source evidence into a compact, traceable discovery baseline.

## Load only what is needed
1. Read the project evidence first.
2. Use `references/quality-check.md` only when validating or reviewing the result.
3. Do not load unrelated skills or project files unless the task requires them.

## Rules
1. Extract facts before interpreting them.
2. Never turn an inference into a fact.
3. Label every non-source conclusion as `CANDIDATE_REQUIREMENT`, `ASSUMPTION`, or `OPEN_QUESTION`.
4. Derive requirements conservatively; do not add implementation details.
5. Split distinct user-visible capabilities into separate requirements when useful.
6. Preserve the source actor and source wording needed for traceability.
7. Do not create NFRs unless the source supports them.
8. Do not generate use cases, user stories, APIs, database models, or UI designs unless explicitly requested.
## Ambiguity handling

Do not operationalize ambiguous terms such as:
`manage`, `monitor`, `support`, `handle`, `appropriate`,
`available`, `overdue`.

If the source does not define the operation:
- preserve the original capability;
- lower confidence when interpretation is required;
- create an OPEN_QUESTION;
- do not invent CRUD operations, workflows, statuses, or policies.
## Requirement ID
Use `FR-<PROJECT>-<NNN>` with sequential numbering within the project.

## Requirement wording
Prefer:
`The system shall allow <actor> to <observable capability>.`

## Confidence

Use only: `HIGH`, `MEDIUM`, `LOW`.

- HIGH: directly supported by the source with little or no interpretation.
- MEDIUM: supported by the source but the capability contains meaningful ambiguity.
- LOW: significant interpretation is required; create an open question.

## Output
Return exactly these sections, in this order:

### 1. Project Context
1–3 bullets.

### 2. Actors
Table: `ID | Actor | Source capability summary`

### 3. Source Facts
Only facts needed to explain the derived requirements. Keep concise.

### 5. Candidate Business Rules
Table:
`ID | Rule | Source | Status`

Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

Do not turn ordinary source facts into business rules unless they define
a constraint, policy, condition, or decision rule.

### 5. Candidate Business Rules
Only rules explicitly supported or directly implied by source. Mark inferred rules as `OPEN_QUESTION` instead of silently creating them.

### 6. Candidate NFRs
Only if explicitly supported. Otherwise write `None identified from source`.

### 7. Assumptions
Only assumptions necessary to interpret the source.

### 8. Open Questions
Only questions that could change scope, behavior, rules, permissions, or acceptance.

### 9. Traceability
Summarize source-to-requirement coverage. Flag uncovered source capabilities.

### 10. Quality Gate
Use one of:
- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Anti-bloat
- Do not restate the full source.
- Do not explain BA theory.
- Do not add generic best practices.
- Do not invent acceptance criteria.
- Do not produce more than 5 open questions per major capability area unless the user asks for exhaustive analysis.

## Completion rule
If the source is sufficient, finish the discovery output without asking the user for confirmation. Record missing information as open questions.
