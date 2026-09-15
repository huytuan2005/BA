---
name: nfr-generator
description: Identify source-supported non-functional requirements and quality constraints from project evidence. Use when functional analysis, use cases, or source material may contain explicit quality, security, performance, reliability, usability, compliance, or operational constraints.
---

# NFR Generator

## Goal

Turn explicit quality-related evidence into a compact, traceable NFR baseline.

NFRs describe qualities, constraints, or conditions on the system or its
operation. They do not invent technical solutions.

## Input

Use:
- project source evidence;
- discovered functional requirements;
- business processes;
- functional capabilities;
- use cases;
- user stories;
- explicit business rules or constraints.

Treat `ASSUMPTION` and `OPEN_QUESTION` as unresolved, not confirmed NFRs.

## Load only what is needed

1. Read relevant project evidence first.
2. Use `references/quality-check.md` only when validating/reviewing.
3. Do not load unrelated skills unless the task requires them.

## Core Rules

1. Create an NFR only when source evidence explicitly supports a quality,
   constraint, or operational requirement.
2. Never invent a numeric target, threshold, SLA, capacity, availability,
   recovery target, security control, compliance requirement, or usability
   target.
3. Do not convert ordinary functional requirements into NFRs.
4. Do not convert business rules into NFRs unless the rule explicitly defines
   a quality or operational constraint.
5. Preserve the source meaning and terminology.
6. Separate `SOURCE_STATED`, `DERIVED`, and `OPEN`.
7. Significant interpretation must lower confidence and normally create an
   open question.
8. Do not prescribe implementation unless the source explicitly does so.
9. Do not create architecture, APIs, database structures, UI designs, code,
   infrastructure, technologies, or vendor choices.
10. Do not create NFRs merely because they are common best practices.
11. Do not treat a security-sensitive domain as evidence of a specific
    security requirement.
12. Do not treat a word such as `secure`, `fast`, `reliable`, `easy`, or
    `available` as a measurable NFR unless the source gives enough meaning
    to support it.
13. Do not manufacture acceptance criteria or test metrics.

## NFR Boundary

An NFR is appropriate when the source constrains how well, under what quality
condition, or under what operational constraint the system must behave.

Examples of evidence that may support NFRs:
- explicit response-time target;
- explicit availability target;
- explicit capacity/concurrency target;
- explicit accessibility requirement;
- explicit security/privacy requirement;
- explicit retention or audit requirement;
- explicit recovery objective;
- explicit compatibility requirement;
- explicit regulatory/compliance requirement.

Examples that do NOT by themselves support NFRs:
- customer pays;
- manager monitors revenue;
- system has user accounts;
- payment exists;
- data is stored;
- the domain involves money;
- the system is web-based;
- a common practice would normally be desirable.

## Quality Categories

Use only categories supported by source evidence. Allowed labels:

- `PERFORMANCE`
- `SECURITY`
- `USABILITY`
- `ACCESSIBILITY`
- `RELIABILITY`
- `AVAILABILITY`
- `SCALABILITY`
- `COMPATIBILITY`
- `MAINTAINABILITY`
- `PORTABILITY`
- `PRIVACY`
- `COMPLIANCE`
- `OPERABILITY`
- `AUDITABILITY`
- `DATA_QUALITY`
- `OTHER`

Do not create an NFR merely to populate a category.

## Measurability

A measurable NFR should preserve the source's target, unit, scope, and
condition.

Do not invent values such as:
- `< 2 seconds`;
- `99.9%`;
- `1,000 concurrent users`;
- `RPO 15 minutes`;
- `RTO 1 hour`;
- `WCAG AA`;
unless the source explicitly supports them.

If the source expresses only a qualitative constraint, preserve it as
qualitative and do not manufacture a metric.

If the source says a quality is required but does not define its level,
record the gap as an `OPEN_QUESTION`.

## Security and Privacy

Do not infer security mechanisms from sensitive operations.

For example, these do NOT automatically justify:
- JWT;
- OAuth;
- MFA;
- encryption at rest;
- TLS;
- RBAC;
- password policy;
- session timeout;
- audit logging.

Create such an NFR only when the source explicitly requires the relevant
security/privacy behavior.

## Derived NFRs

`DERIVED` is allowed only when the conclusion follows directly from explicit
source evidence without adding a new target or implementation mechanism.

Example:
Source explicitly requires a particular data-retention period.
A derived NFR may preserve that retention constraint.

Do not use `DERIVED` to introduce common best practice.

## NFR ID

Use:

`NFR-<PROJECT>-<NNN>`

Number sequentially within the project.

## Requirement Wording

Prefer:

`The system shall <quality/constraint>.`

For qualitative constraints, preserve source wording where necessary.

Examples:
- `The system shall support the explicitly specified response-time target.`
- `The system shall retain activity logs for the explicitly specified period.`

Do not weaken a source-stated target or strengthen an ambiguous statement.

## Evidence and Traceability

Every NFR must trace to original source evidence.

Preferred:
`NFR → Source`

Where the NFR is clearly related to a functional requirement:
`NFR → FR → Source`

Do not use generated FR/FN/UC/US IDs as a substitute for actual source
evidence.

If no explicit source evidence supports an NFR category, state that no NFR
is identified for that category.

## Confidence

Use only:

- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH
Explicitly stated with clear quality/constraint meaning.

### MEDIUM
Supported but requires limited interpretation.

### LOW
Meaningful interpretation is required.

LOW-confidence NFRs should normally have an open question when the unresolved
meaning affects the NFR target, scope, or applicability.

## Open Questions

Create questions only when they can change:
- whether an NFR exists;
- NFR scope;
- target/threshold;
- condition;
- applicability;
- actor or operational responsibility;
- compliance/security/privacy interpretation.

Do not create generic questions such as "What are the NFRs?"

## Output Contract

Return exactly these sections, in this order:

### 1. Project Context
1–3 bullets.

### 2. NFR Inventory
Table:
`ID | Category | NFR | Source | Confidence`

If no NFRs are supported:
`No explicit NFRs identified from the source.`

### 3. NFR Targets and Conditions
Table:
`NFR | Target / Constraint | Condition / Scope | Source`
Do not invent missing targets or conditions.
If none are explicit:
`None explicitly identified from the source.`

### 4. NFR Security, Privacy, and Compliance
Table:
`NFR | Type | Requirement / Constraint | Source | Confidence`
Include only explicit evidence.
If none:
`None explicitly identified from the source.`

### 5. NFR Dependencies and Constraints
Only include relationships explicitly supported by source evidence.
Table:
`NFR | Depends On / Constrains | Source | Confidence`
The target must be an actual `NFR-*` when describing an NFR-to-NFR
dependency.
Do not infer dependency from implementation, architecture, or domain
plausibility.
If none:
`No explicit NFR-to-NFR dependencies are identified from the source.`

### 6. Unsupported or Ambiguous Quality Requirements
List only unresolved quality-related behavior, targets, scope, or constraints.

### 7. NFR Traceability
Table:
`NFR | Source Requirement (if applicable) | Source Evidence`
Flag NFRs without direct evidence.

### 8. Open Questions
Only high-value questions affecting NFR existence, scope, target, condition,
or interpretation.

### 9. Quality Gate
Use one:
- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Output Consistency Checks

Before finalizing:
- Every NFR has a stable `NFR-*` ID.
- Every NFR has explicit source evidence.
- No functional requirement was merely relabeled as an NFR.
- No numeric target was invented.
- No SLA/availability/capacity/recovery target was invented.
- No security control was inferred from domain sensitivity.
- No privacy/compliance requirement was invented.
- No implementation technology was introduced.
- No acceptance criteria or test metric was invented.
- Qualitative source wording remains qualitative when necessary.
- Derived NFRs do not add unsupported targets or mechanisms.
- Every NFR is traceable to source evidence.
- Open questions are focused and nonduplicate.
- NFR-to-NFR dependencies are evidence-based and target another `NFR-*`.

## Anti-Bloat

- Do not explain NFR theory.
- Do not populate every quality category.
- Do not add generic security, performance, accessibility, or reliability
  recommendations.
- Do not create technical solutions.
- Prefer no NFR over an invented NFR.

## Completion

If the source supports no explicit NFRs, complete the analysis and state that
clearly. Do not ask the user to supply NFRs before producing the baseline.
