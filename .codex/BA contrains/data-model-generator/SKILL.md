---
name: data-model-generator
description: Derive a compact, traceable conceptual data model from supported requirements, functional analysis, use cases, and user stories without inventing entities, fields, keys, relationships, or database implementation details.
---

# Data Model Generator

## Goal

Turn supported business requirements and functional behavior into a compact,
traceable conceptual data-model baseline.

The model describes business information needed by the system. It does not
assume a database design.

## Input

Use, when available:
- discovered functional requirements;
- functional capability inventory;
- functional inputs and outputs;
- business rules and constraints;
- use-case inventory;
- user stories and supported acceptance criteria;
- project source facts;
- open questions.

Do not treat assumptions, inferred implementation details, or open questions
as confirmed data-model facts.

## Load only what is needed

1. Read the relevant project evidence first.
2. Use `references/quality-check.md` only when validating/reviewing.
3. Do not load unrelated skills unless the task requires them.

## Core Rules

1. Source evidence is authoritative.
2. Derive data concepts only from supported source evidence.
3. Preserve source terminology where practical.
4. Every entity, attribute, relationship, key, and constraint must be traceable
   to source evidence or explicitly labeled as derived.
5. Do not invent entities merely because a noun appears in the source.
6. Do not invent attributes from common database design practice.
7. Do not invent primary keys, foreign keys, unique keys, indexes, or generated
   identifiers unless explicitly supported by the source.
8. Do not infer relationships from business plausibility alone.
9. Do not infer cardinality from ordinary wording unless the source explicitly
   establishes quantity or multiplicity.
10. Do not infer normalization, table splitting, join tables, inheritance,
    audit tables, soft-delete fields, timestamps, or technical metadata.
11. Do not define SQL tables, column types, ORM entities, migrations, schemas,
    indexes, database technologies, or implementation architecture unless
    explicitly requested and supported.
12. Do not convert every use-case input into a persistent attribute.
13. Do not convert every output, rule, actor, status, or process into an entity.
14. Preserve ambiguity instead of filling missing data structure.
15. Do not create data required only by an assumed workflow.

## Conceptual Data Boundary

A candidate entity represents a meaningful business information concept that
must be represented or referenced by the system.

Prefer business concepts such as:
- Facility
- Storage Unit
- Reservation
- Rental Contract
- Customer

Only include an entity when source evidence supports it.

Do not create technical entities such as:
- UserSession
- AuditLog
- NotificationQueue
- APIRequest
- DatabaseRecord

unless the source explicitly requires the corresponding business information.

## Entity Identification

An entity may be:
- directly named as information managed, monitored, viewed, assigned, or
  referenced by the source;
- directly required to represent a supported business capability;
- carefully derived when several supported capabilities clearly require the
  same business information concept.

A derived entity must be marked `DERIVED` and must cite the original source.

Do not create an entity solely because:
- it is common in similar systems;
- it would make the model more normalized;
- it would be useful for implementation;
- a process step seems to require it;
- a use case name contains the noun.

## Entity ID

Use:

`ENT-<PROJECT>-<NNN>`

Number sequentially within the project.

## Attribute Identification

An attribute is a business property of an entity explicitly stated or
strongly and directly supported by source evidence.

Examples supported by the Self-Storage source include:
- Facility: facility identity/details only when actually stated;
- Storage Unit: type, size, location, rental price, status;
- Reservation: facility, unit type, start date, rental period;
- Customer: customer information only where the source explicitly requires it.

Do not invent typical fields such as:
- id;
- createdAt;
- updatedAt;
- email;
- phone;
- address;
- password;
- status;
- name;
- code;

unless the source supports them for that entity.

Use:

`ATT-<PROJECT>-<NNN>`

for attribute IDs.

## Attribute Type

Do not invent implementation data types.

If the source only says `start date`, record the business concept as
`Start Date`, not `DATE`.

If a type is explicitly stated, preserve it at business level.

Avoid:
- VARCHAR(255);
- UUID;
- INT;
- DECIMAL(10,2);
- enum definitions;
- SQL-specific types.

## Identifiers and Keys

Keys require special protection against hallucination.

Only identify a primary key, business identifier, unique key, or foreign key
when the source explicitly provides or requires it.

Do NOT assume:
- every entity has an `id` primary key;
- names/codes are unique;
- one entity references another through an ID;
- foreign keys exist because entities are related.

If no key is explicitly supported, write:

`No explicit identifier/key is identified from the source.`

A relationship does not automatically create a foreign key.

## Relationships

A relationship must connect two supported entities.

Use:

`REL-<PROJECT>-<NNN>`

A relationship is valid only when the source explicitly indicates that two
business information concepts are associated, assigned, contained, used,
referenced, or otherwise related.

Do not infer a relationship from:
- process order;
- common business practice;
- a shared attribute name;
- a use-case sequence;
- technical implementation;
- business plausibility alone.

### Relationship Cardinality

Record cardinality only when explicitly supported.

Allowed conceptual notation:
- `1`
- `0..1`
- `1..*`
- `0..*`
- `UNSPECIFIED`

Do not infer `1..*` merely because a relationship sounds plural.

If the source says a customer can manage **one or more** rented storage units,
that supports the quantity on the customer side of that specific relationship.
Otherwise use `UNSPECIFIED`.

## Foreign Keys

Foreign keys are implementation-oriented unless explicitly required by the
source.

Therefore:
- do not create FK fields automatically from relationships;
- do not name an FK column unless the source explicitly identifies it;
- represent the conceptual relationship separately.

## Business Rules and Data Constraints

Include only source-supported data constraints such as:
- allowed values explicitly stated;
- required relationships explicitly stated;
- quantity limits explicitly stated;
- policy constraints that directly govern stored business information.

Do not turn every business rule into a database constraint.

For each rule use:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

A derived constraint must remain clearly marked as derived.

## Statuses and Lifecycle

A status belongs in the model only when the source explicitly identifies the
status concept.

Do not invent status values or transitions.

If the source says `unit status` but does not define its values, record the
attribute `Status` and an open question about allowed values/lifecycle.

Do not invent:
- ACTIVE;
- AVAILABLE;
- RESERVED;
- EXPIRED;
- RETURNED;
- DELETED;

unless source-supported.

## Traceability

Trace all model elements to original evidence.

Preferred relationships:

`ENT → FR`
`ATT → FR/FN/UC`
`REL → FR/FN/UC`
`RULE → FR`

Where useful:

`ENT → FR → FN → UC → US`

Do not use generated entity/attribute/relationship IDs as a substitute for
source evidence.

## Confidence

Use only:
- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH
Directly supported by source with little interpretation.

### MEDIUM
Supported but requires meaningful interpretation of the business concept or
model boundary.

### LOW
Significant interpretation is required.

LOW-confidence elements should normally have a corresponding open question
when the uncertainty affects scope or model structure.

## Unsupported or Ambiguous Data

Record gaps when the missing information can affect:
- entity scope;
- attribute scope;
- identifiers/keys;
- relationships;
- cardinality;
- status/lifecycle;
- data ownership;
- business constraints.

Do not fill these gaps using standard database conventions.

## Output Contract

Return exactly these sections, in this order:

### 1. Project Context
1–3 bullets.

### 2. Candidate Entity Inventory
Table:
`ID | Entity | Business Purpose | Source | Confidence`

### 3. Candidate Attribute Inventory
Table:
`ID | Entity | Attribute | Source | Confidence`

### 4. Identifiers and Keys
Table:
`Entity | Identifier/Key | Type | Source | Confidence`

If none:
`No explicit identifier/key is identified from the source.`

Allowed `Type` values:
- `PRIMARY_KEY`
- `BUSINESS_IDENTIFIER`
- `UNIQUE_KEY`
- `FOREIGN_KEY`

Do not infer keys.

### 5. Candidate Relationships
Only create this table when explicit relationships are supported.

Table:
`ID | Entity A | Relationship | Entity B | Cardinality | Source | Confidence`

If none:
`No explicit entity relationships are identified from the source.`

### 6. Data Rules and Constraints
Table:
`ID | Entity/Relationship | Rule or Constraint | Source | Status`

Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

### 7. Status and Lifecycle Information
Table:
`Entity | Status/Lifecycle Information | Source | Confidence`

If none:
`No explicit status/lifecycle information is identified from the source.`

### 8. Unsupported or Ambiguous Data Behavior
List only unresolved data-model issues affecting structure or meaning.

### 9. Data Model Traceability
Table:
`Model Element | Source Requirement | Functional Capability | Use Case | User Story`

Use only levels that are actually available.
Flag uncovered source requirements.

### 10. Open Questions
Only high-value questions that can change:
- entity scope;
- attributes;
- keys;
- relationships/cardinality;
- lifecycle/status;
- constraints.

Deduplicate related questions.

### 11. Quality Gate
Use one:
- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Output Consistency Checks

Before finalizing:
- Every entity has source evidence.
- Every attribute has source evidence.
- No automatic `id` field.
- No invented primary key.
- No invented foreign key.
- No invented unique key.
- No relationship without evidence.
- No inferred cardinality.
- No CRUD-derived entities.
- No technical metadata.
- No SQL data types.
- No ORM/database implementation.
- No invented statuses or transitions.
- Ambiguity is preserved.
- Every model element is traceable.
- Every requirement is covered or explicitly marked.
- Open questions are focused and nonduplicate.

## Anti-Bloat

- Do not explain database theory.
- Do not produce physical schema unless explicitly requested.
- Do not add generic audit fields.
- Do not add authentication fields unless source-supported.
- Do not normalize or denormalize without evidence.
- Do not create entities for every noun.
- Prefer a small conceptual model over a complete imagined database.

## Completion

If the source is sufficient, complete the conceptual data-model baseline
without asking for confirmation.

If structure is unresolved, record it as an open question instead of inventing
an answer.
