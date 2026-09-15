---
name: api-generator
description: Analyze source-supported API requirements from functional requirements, functional capabilities, use cases, and data-model evidence. Use when business requirements need an API baseline without inventing endpoints, HTTP methods, parameters, payload fields, status codes, authentication, or implementation details.
---

# API Generator

## Goal

Turn supported functional and data requirements into a compact, traceable API
baseline only when the source explicitly supports an API or API-like contract.

API design is an implementation-facing artifact. It must not be fabricated
from business requirements merely because an API would be useful.

## Input

Use:
- discovered functional requirements;
- functional capabilities;
- use cases;
- supported business rules;
- supported functional inputs and outputs;
- data-model evidence;
- explicit API/interface evidence, if present;
- open questions.

Do not treat assumptions or open questions as confirmed API behavior.

## Load only what is needed

1. Read relevant project evidence first.
2. Use `references/quality-check.md` only when validating/reviewing.
3. Do not load unrelated skills unless the task requires them.

## Core Rules

1. Generate an API only when the source explicitly identifies an API,
   endpoint, web service, HTTP operation, integration contract, or equivalent
   interface requirement.
2. A FR, FN, UC, actor, entity, business object, or use-case name alone is not
   evidence that an API exists.
3. Never automatically convert:
   - FR → endpoint;
   - FN → endpoint;
   - UC → endpoint;
   - entity → CRUD API;
   - business object → resource;
   - input → request parameter;
   - output → response field.
4. Preserve source terminology.
5. Do not invent HTTP methods.
6. Do not invent URL paths, path parameters, query parameters, headers, request
   bodies, response bodies, status codes, authentication, authorization,
   pagination, filtering, sorting, versioning, rate limits, or error schemas.
7. Do not infer REST merely because an HTTP API is plausible.
8. Do not infer CRUD from words such as `manage`.
9. Do not infer an API from a frontend/backend architecture assumption.
10. Do not turn technical implementation choices into requirements.
11. Keep business requirements separate from interface design decisions.
12. If the source supports an API concept but omits contract details, preserve
    the API capability and mark the missing contract details as open questions.
13. If no API evidence exists, explicitly state that no API contracts are
    identified from the source.

## API Boundary

An API artifact represents an externally consumable interface contract only
when supported by source evidence.

Valid source examples:
- `POST /reservations` is explicitly specified.
- `The system exposes an API for reservation creation.`
- `Mobile clients call the reservation service.`
- `The integration consumes a payment API.`

Invalid evidence for automatically creating an API:
- `Customer can reserve a unit.`
- `Manager manages units.`
- `Customer views facilities.`
- `Reservation has a start date.`

The latter are business/functional evidence, not API contracts.

## API ID

Use:

`API-<PROJECT>-<NNN>`

Number sequentially within the project.

## Naming

If an API operation is explicitly named by the source, preserve it.

If the source only supports an interface capability without a technical
operation name, use a business-level name such as:

`Reservation Interface`

Do not manufacture names such as:
- `POST /api/reservations`
- `GET /api/customers/{id}`
- `updateUnitStatus()`

unless explicitly supported.

## HTTP Method and Path

Only include HTTP method or path when explicitly supported.

If absent:

`Not specified in source.`

Do not select GET/POST/PUT/PATCH/DELETE based on common REST practice.

## Parameters and Payloads

Only identify parameters or request/response fields when the source explicitly
supports them as part of the interface contract.

A functional input is not automatically an API parameter.

For example:

`facility, unit type, start date, rental period`

may be functional inputs for reservation, but must not become:

`POST /reservations { facilityId, unitTypeId, startDate, rentalPeriod }`

unless the API contract explicitly supports that mapping.

Do not invent:
- IDs;
- field names;
- JSON structure;
- data types;
- required/optional markers;
- enum values;
- headers;
- tokens.

## Responses

Only document response data when explicitly supported.

Do not invent:
- `200 OK`;
- `201 Created`;
- response DTOs;
- generated IDs;
- confirmation messages;
- timestamps;
- database records.

If the source only states that an interface supports a capability:

`Response contract not specified in source.`

## Authentication and Authorization

Do not infer authentication or authorization mechanisms.

Do not invent:
- JWT;
- OAuth;
- API keys;
- sessions;
- bearer tokens;
- role-based endpoint guards.

Even when actors and roles exist, actor role ≠ API authentication contract.

If security is explicitly specified, preserve only the stated mechanism and
scope.

## API Relationships and Dependencies

Do not infer endpoint dependencies from:
- process order;
- use-case order;
- business objects;
- shared entities;
- request/response data;
- actor roles;
- functional dependencies;
- business plausibility.

A relationship may be recorded only when the source explicitly establishes
that one interface requires, calls, extends, or depends on another interface.

Every dependency must connect actual `API-*` identifiers:

`API-A → API-B`

If none exists:

`No explicit API-to-API relationships are identified from the source.`

Do not create a relationship table when none exists.

## Data Model Boundary

Data-model evidence can support an API field only when the source explicitly
links the field to the API contract.

Do not convert:
- entity → API resource;
- attribute → JSON property;
- PK → path parameter;
- FK → request field;
- relationship → nested response.

Conceptual data model and API contract remain separate artifacts.

## Business Rules

Include only rules that are explicitly relevant to the supported API contract.

Do not transform ordinary API fields or endpoint names into business rules.

If a business rule constrains an API operation, preserve its source meaning and
trace it to the original FR/source evidence.

## Confidence

Use only:

- `HIGH`
- `MEDIUM`
- `LOW`

### HIGH

API contract detail is directly specified by the source.

### MEDIUM

An API/interface is explicitly supported, but some contract details are
missing or require limited interpretation.

### LOW

Significant interpretation is required to represent the interface. Create an
open question when the unresolved detail affects the API contract.

## Traceability

Every API artifact must trace to original source evidence.

Prefer:

`API → FR`

Where useful:

`API → FR → FN → UC`

If explicit interface evidence has its own source identifier, preserve it.

Do not use generated API IDs as the source of another API requirement.

## Output Contract

Return exactly these sections, in this order:

### 1. Project Context
1–3 bullets.

### 2. API Evidence
Table:
`Source | API Evidence | Scope | Confidence`

If no API evidence exists:
`No explicit API/interface evidence is identified from the source.`

### 3. API Inventory
Table:
`ID | API / Interface | Purpose | Source | Confidence`

If none:
`No API contracts are identified from the source.`

### 4. API Operations
Table:
`API | Operation | HTTP Method | Path | Source | Confidence`

Use `Not specified in source.` for unsupported method/path details.
If no supported operations exist:
`No explicit API operations are identified from the source.`

### 5. Request Inputs
Table:
`API / Operation | Input | Source | Confidence`

Only include interface-level inputs explicitly supported by the source.
Do not convert functional inputs automatically.

### 6. Response Outputs
Table:
`API / Operation | Output | Source | Confidence`

Only include interface-level outputs explicitly supported by the source.

### 7. API Rules and Constraints
Table:
`ID | API / Operation | Rule | Source | Status`

Status:
- `SOURCE_STATED`
- `DERIVED`
- `OPEN`

### 8. Authentication and Authorization
Table:
`API / Operation | Security Requirement | Source | Confidence`

If none:
`No explicit API authentication or authorization requirements are identified from the source.`

### 9. API Relationships
Only create this table when explicit API-to-API relationships exist.
Table:
`Source API | Relationship | Target API | Source | Confidence`

Allowed relationships:
- `INCLUDE`
- `EXTEND`
- `GENERALIZATION`
- `DEPENDENCY`

If none:
`No explicit API-to-API relationships are identified from the source.`

### 10. Unsupported or Ambiguous API Behavior
List only unresolved details affecting:
- API existence;
- operation scope;
- method/path;
- inputs/outputs;
- security;
- rules;
- relationships.

### 11. API Traceability
Table:
`API / Operation | Requirement | Functional Capability | Use Case`

Flag requirements that are not API-defining.

### 12. Open Questions
Only high-value questions that can change the API contract or determine
whether an API is required.

### 13. Quality Gate
Use one:
- `PASS`
- `PASS WITH QUESTIONS`
- `FAIL`

Add at most 5 short reasons.

## Output Consistency Checks

Before finalizing:
- Every API has a stable `API-*` ID.
- Every API has explicit source evidence.
- No FR/FN/UC is converted into an API automatically.
- No entity is converted into a resource automatically.
- No CRUD is inferred from `manage`.
- No HTTP method is invented.
- No path is invented.
- No request/response fields are invented.
- No status codes are invented.
- No authentication mechanism is invented.
- No authorization mechanism is invented.
- No API relationship is inferred from process/use-case order.
- Every relationship target is another `API-*`.
- Functional inputs are not automatically API inputs.
- Data-model fields are not automatically API fields.
- All supported API artifacts trace to original source evidence.
- Requirements that are not API-defining are explicitly identified.
- Open questions are focused and nonduplicate.

## Anti-Bloat

- Do not explain API design theory.
- Do not produce OpenAPI/Swagger YAML unless explicitly requested.
- Do not generate endpoint catalogs from requirements alone.
- Do not generate CRUD mechanically.
- Do not invent technical contract details to make the API look complete.
- Prefer a small evidence-backed interface baseline over a complete-looking
  fabricated API specification.

## Completion

If explicit API evidence is absent, complete the analysis by stating that no
API contracts are identified and explain the relevant gap through open
questions. Do not ask the user for confirmation before producing the baseline.
