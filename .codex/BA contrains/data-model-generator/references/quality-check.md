# Data Model Generator Quality Check

Use this reference only when validating or reviewing a result.

## 1. Entity Coverage
- Every entity maps to source evidence.
- No entity exists only because its noun appears in a use case.
- No technical entity is invented.
- Every relevant source information concept is represented or explicitly
  marked as not data-model-defining.

## 2. Attribute Accuracy
- Every attribute is explicitly stated or strongly/directly supported.
- No generic `id` field is invented.
- No generic timestamps are invented.
- No email/phone/address/name/status fields are invented without evidence.
- No attribute is created merely because it is common database practice.

## 3. Keys
Critical hallucination check:
- No automatic primary keys.
- No automatic business identifiers.
- No automatic unique keys.
- No automatic foreign keys.
- A relationship does not imply an FK.
- If no explicit key exists, state that none is identified.

## 4. Relationships
- Every relationship connects two supported entities.
- Source evidence explicitly supports the relationship.
- No relationship is inferred from process order.
- No relationship is inferred from business plausibility.
- No relationship is inferred from shared attributes.
- No technical relationship is included.

## 5. Cardinality
- Cardinality is included only when source-supported.
- Plural wording alone is not treated as cardinality.
- Explicit quantity such as `one or more` may support cardinality.
- Unknown cardinality remains `UNSPECIFIED`.

## 6. Data Rules and Constraints
- Rules are actual constraints, conditions, policies, or required
  relationships.
- Ordinary facts are not converted into database constraints.
- `SOURCE_STATED`, `DERIVED`, and `OPEN` are used correctly.
- Derived constraints remain clearly identified as derived.

## 7. Status and Lifecycle
- Status concepts are source-supported.
- Status values are not invented.
- Transitions are not invented.
- Lifecycle behavior is not inferred from process order.

## 8. Data Boundary
Reject:
- SQL tables;
- column definitions;
- SQL types;
- ORM classes;
- migrations;
- indexes;
- join tables inferred from normalization;
- audit fields;
- soft-delete fields;
- API payloads;
- database implementation details.

## 9. Traceability
Every:
- entity;
- attribute;
- key;
- relationship;
- rule
must trace to original evidence where applicable.

Generated IDs are not evidence.

## 10. Ambiguity
Check gaps affecting:
- entity scope;
- attribute scope;
- identifiers;
- relationships;
- cardinality;
- status/lifecycle;
- constraints.

Do not fill gaps with conventional database design.

## 11. Open Questions
Questions must be capable of changing the model.
Reject generic questions such as:
- "What database will be used?"
- "Should we normalize the database?"
unless the user explicitly requests physical design.

## 12. Quality Gate
PASS if:
- model concepts are source-supported;
- no material structural invention exists;
- traceability is complete.

PASS WITH QUESTIONS if:
- core concepts are supported;
- important structure is unresolved and clearly flagged;
- no material unsupported model element is invented.

FAIL if:
- entities are invented;
- attributes are invented materially;
- keys are invented;
- relationships are inferred without evidence;
- cardinality is invented;
- lifecycle/status is invented;
- database implementation leaks into the conceptual model;
- source requirements are silently dropped.

## Final Review

1. Does every entity trace to source evidence?
2. Did any noun automatically become an entity?
3. Did any generic field such as `id` get invented?
4. Were PK/FK/unique keys invented?
5. Does every relationship have evidence?
6. Was cardinality inferred?
7. Were statuses or transitions invented?
8. Were SQL/database details introduced?
9. Were business rules confused with data constraints?
10. Are ambiguous structures still ambiguous?
11. Are open questions model-changing and focused?
12. Are all requirements covered?
If unsupported model structure is found, correct it before finalizing.
