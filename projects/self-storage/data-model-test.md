# Data Model Generator — Self-Storage Test

## Test Input

Use the existing Self-Storage project evidence together with the outputs of:
- requirement-discovery;
- process-analysis;
- functional-analysis;
- use-case-generator;
- user-story-generator.

## Expected Safety Checks

1. Do not invent `id` fields.
2. Do not invent email/phone/address/password fields.
3. Do not invent payment entities or invoice entities unless supported by the
   Self-Storage source being tested.
4. Do not invent reservation/contract/payment status values.
5. Do not create FK fields automatically.
6. Do not infer relationships merely from process sequence.
7. Preserve `one or more rented storage units` as the only explicit quantity
   evidence relevant to that relationship.
8. Keep physical database design out of the result.
9. Flag unresolved identifiers, relationship cardinalities, and lifecycle
   details where source evidence is insufficient.

## Source-Supported Candidate Concepts

The source supports concepts including:
- Storage Customer;
- Facility;
- Storage Unit;
- Reservation;
- Rental Contract;
- Facility Staff;
- Facility Manager;
- Business Operations Manager;
- System Administrator.

Actors are not automatically entities. The model must distinguish an actor
from business information about that actor.

The source explicitly mentions unit properties such as type, size, location,
rental price, and status. It also explicitly provides reservation information:
facility, unit type, start date, and rental period.

The source mentions rental contracts and payment status, but does not define
complete contract/payment structures, identifiers, statuses, or payment
methods.

## Test Result

Quality target: `PASS WITH QUESTIONS`.

The result should be considered ready for lock only if the quality check
confirms that no unsupported entity, attribute, key, relationship,
cardinality, status, or database implementation detail was introduced.

## Executed Baseline Result

### Candidate entities
- `ENT-SELF-STORAGE-001` — Customer — supported by customer-facing rental,
  payment, check-in, support, and manager monitoring capabilities — HIGH.
- `ENT-SELF-STORAGE-002` — Facility — explicitly managed and reported by
  multiple actors — HIGH.
- `ENT-SELF-STORAGE-003` — Storage Unit — explicitly managed, assigned,
  handed over, returned, inspected, and reported — HIGH.
- `ENT-SELF-STORAGE-004` — Reservation — explicitly reserved and checked by
  staff — HIGH.
- `ENT-SELF-STORAGE-005` — Rental Contract — explicitly monitored by the
  Facility Manager — HIGH.
- `ENT-SELF-STORAGE-006` — Payment — supported as a business information
  concept by payment status and payment activities, but its exact structure
  is unresolved — MEDIUM.
- `ENT-SELF-STORAGE-007` — Staff Assignment — NOT generated as an entity;
  assignment is treated as an unresolved relationship/behavior until the
  source establishes a persistent business concept.

### Supported attributes
- Storage Unit: Type, Size, Location, Rental Price, Status — HIGH.
- Reservation: Facility, Unit Type, Start Date, Rental Period — HIGH.
- Rental Contract: Rental Period, Payment Status — MEDIUM, because the source
  associates these monitored values with rental contracts but does not define
  a full contract structure.

No generic `id`, name, email, phone, address, password, created date, or
updated date fields are generated.

### Keys
`No explicit identifier/key is identified from the source.`

### Relationships
- Customer → reserves → Reservation — supported, cardinality unspecified.
- Reservation → concerns → Facility — supported, cardinality unspecified.
- Customer → has/manages → rented Storage Unit — supported by the explicit
  `one or more` wording; use `1..*` only on the customer-to-rented-unit
  quantity where the source wording is applied.

No FK fields are generated.

### Status/lifecycle
- Storage Unit has a `Status` attribute — HIGH.
- Exact status values and transitions are unresolved.
- Reservation, Rental Contract, Payment, return, renewal, and overdue
  statuses/transitions are not invented.

### Quality gate
`PASS WITH QUESTIONS`

Reasons:
1. Core business concepts and explicitly stated attributes are traceable.
2. Keys and technical database structures are not invented.
3. Relationships are limited to source-supported associations.
4. Status values and lifecycle transitions remain unresolved.
5. Payment and contract structure require clarification before physical design.
