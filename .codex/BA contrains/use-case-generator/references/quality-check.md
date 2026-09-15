# Use Case Generator Quality Check

Use this reference only when validating or reviewing a result.

## 1. Source Coverage

- Every use case maps to ≥1 original FR.
- Every requirement is represented, intentionally covered by another use
  case, or explicitly marked as not use-case-defining.
- No source capability is silently dropped.

## 2. Actor Accuracy

- Actor names match the source.
- No actor is invented.
- Actor responsibility is not expanded.
- No external system/service is introduced without evidence.

## 3. Use-Case Boundary

Check that each use case represents:
- a meaningful actor goal; or
- an observable actor-system interaction.

Reject:
- API endpoints;
- database operations;
- UI components;
- backend services;
- technical jobs;
- implementation mechanisms.

## 4. Naming

Check:
- concise;
- actor goal oriented;
- business-level;
- no invented CRUD.

Reject automatic expansion of:
`manage` → create/read/update/delete.

## 5. Preconditions

Every precondition must be explicitly supported.

Reject preconditions inferred from:
- process order;
- common practice;
- business plausibility;
- another use case existing;
- technical assumptions.

## 6. Postconditions

Every postcondition must be explicitly supported.

Reject invented:
- records;
- statuses;
- confirmations;
- notifications;
- invoices;
- generated IDs;
- database changes.

## 7. Flow Safety

If flows are present:

- Every step is source-supported.
- No missing step is filled using common business practice.
- No automatic validation is invented.
- No automatic notification is invented.
- No approval flow is invented.
- No payment failure path is invented.
- No error handling is invented without evidence.

## 8. Ambiguity

Check:

`manage / monitor / track / support / handle / appropriate / available /
suitable / overdue`

Ambiguous behavior must remain ambiguous.

If scope is affected:
- lower confidence;
- record OPEN_QUESTION.

## 9. Inputs and Outputs

Inputs:
- explicitly supported;
- business-level;
- not technical parameters.

Outputs:
- observable and business-level;
- source-supported.

Reject:
- API request/response;
- database record;
- generated ID;
- authentication token;
- system event;
- UI component.

## 10. Business Rules

- Rules must be constraints, conditions, policies, decisions, or required
  relationships.
- Ordinary business nouns are not rules.
- Selection factors remain rules/context, not use-case relationships.
- Every derived rule traces to original source evidence.

## 11. Use-Case Relationships

Critical check:

Every relationship must connect actual use cases:

`UC-* → UC-*`

Reject relationships such as:

`UC → input`
`UC → business object`
`UC → condition`
`UC → prerequisite`
`UC → selection factor`
`UC → actor information`
`UC → configuration`
`UC → process context`

Do not infer `include`, `extend`, generalization, or dependency from:

- process ordering;
- business plausibility;
- common system design;
- one use case using information from another;
- shared business objects.

If no explicit relationship exists:

`No explicit use-case relationships are identified from the source.`

Do not create a relationship table.

## 12. Functional Decomposition

Check:

- Multiple functions may form one coherent use case.
- One function may form one use case.
- Unrelated functions are not combined.
- Inputs/business objects do not become artificial use cases.
- Broad ambiguous capabilities are not expanded.

## 13. Traceability

Every:

`UC → FR`

and where useful:

`UC → FR → FN`

must be supported.

No generated identifier may replace original source evidence.

## 14. Open Questions

Questions must address unresolved:
- scope;
- behavior;
- actor responsibility;
- rules;
- preconditions;
- postconditions;
- relationships.

Reject generic questions that do not affect the use-case model.

## 15. Quality Gate

### PASS

Use when:
- use cases are source-supported;
- traceability is complete;
- no material ambiguity remains;
- no unsupported relationships or behavior exist.

### PASS WITH QUESTIONS

Use when:
- core use cases are supported;
- unresolved behavior is explicit;
- no material unsupported behavior has been invented.

### FAIL

Use when:
- use cases are untraceable;
- actors are invented;
- CRUD is invented;
- workflows are invented;
- relationships are inferred without evidence;
- pre/postconditions are invented;
- technical implementation leaks into use cases;
- requirements are silently dropped.

## Final Review

Ask:

1. Does every UC trace to an original FR?
2. Is every actor source-supported?
3. Was `manage` expanded into CRUD?
4. Was a workflow invented?
5. Were preconditions inferred?
6. Were postconditions invented?
7. Were inputs/business objects turned into use cases?
8. Were process conditions turned into relationships?
9. Were `include`/`extend`/dependency relationships invented?
10. Does every relationship target another `UC-*`?
11. Are ambiguous capabilities still ambiguous?
12. Are technical details excluded?
13. Are open questions focused?
14. Are all requirements covered?

If any unsupported behavior is found, correct it before finalizing.