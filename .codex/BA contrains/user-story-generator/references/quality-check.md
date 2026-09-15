# User Story Generator Quality Check

Use this reference only when validating or reviewing a result.

## 1. Source Coverage
- Every user story maps to ≥1 original FR.
- Every requirement is represented, intentionally covered by another story,
  or explicitly marked as not story-defining.
- No source capability is silently dropped.

## 2. Actor Accuracy
- Actor names match the source.
- No actor is invented.
- Actor responsibility is not expanded.
- No external system/service is introduced without evidence.

## 3. Story Boundary
Check that each story represents:
- a meaningful actor goal; or
- an actor-visible capability.

Reject:
- API stories;
- database-operation stories;
- UI-component stories;
- backend-service stories;
- implementation mechanisms.

## 4. Story Wording
Check:
- actor is explicit;
- goal is source-supported;
- business purpose is source-supported if included;
- no generic benefit is invented.

Reject invented benefits such as:
`save time`, `improve efficiency`, `increase security`, `reduce errors`.

## 5. Story Sizing
- Closely related capabilities may share one coherent actor goal.
- Unrelated goals remain separate.
- Different actors remain separate.
- `manage` is not automatically expanded into CRUD stories.

## 6. Acceptance Criteria
Every criterion must be source-supported and observable.

Reject invented:
- validation behavior;
- status transitions;
- notifications;
- confirmations;
- records;
- invoices;
- generated IDs;
- payment success/failure paths;
- authorization outcomes;
- calculations;
- error handling.

Also check:
- criteria are not merely a restatement of the user story;
- criteria do not contain implementation details;
- if source is insufficient, the result says:
  `None explicitly identified from the source.`

## 7. Ambiguity
Check:
`manage / monitor / track / support / handle / appropriate / available /
suitable / overdue`

Ambiguous behavior must remain ambiguous.
If acceptance scope is affected:
- lower confidence;
- record OPEN_QUESTION.

## 8. Inputs and Outputs
Inputs:
- explicitly supported;
- business-level;
- relevant to the story.

Outputs:
- observable;
- business-level;
- source-supported.

Reject:
- API parameters/responses;
- database records;
- generated identifiers;
- authentication tokens;
- system events;
- UI elements.

## 9. Business Rules
- Rules are constraints, conditions, policies, decisions, or required
  relationships.
- Ordinary nouns are not rules.
- Every derived rule traces to original evidence.
- A rule must not be converted into an unsupported acceptance criterion.

## 10. Traceability
Every:
`US → FR`
and where applicable:
`US → UC → FR → FN`
must be supported.

No generated identifier may replace original source evidence.

## 11. Open Questions
Questions must address unresolved:
- story scope;
- actor responsibility;
- acceptance behavior;
- rules;
- inputs/outputs.

Reject generic questions that do not affect the story model.

## 12. Quality Gate
PASS if:
- stories are source-supported;
- traceability is complete;
- acceptance criteria are supported;
- no material ambiguity remains.

PASS WITH QUESTIONS if:
- core stories are supported;
- unresolved behavior is explicit;
- no material unsupported acceptance behavior has been invented.

FAIL if:
- stories are untraceable;
- actors are invented;
- generic business value is invented;
- CRUD/workflows are invented;
- acceptance criteria are invented;
- technical implementation leaks into stories;
- requirements are silently dropped.

## Final Review
1. Does every US trace to an original FR?
2. Is every actor source-supported?
3. Was a generic benefit invented?
4. Was `manage` expanded into CRUD?
5. Was a workflow invented?
6. Were acceptance criteria inferred without evidence?
7. Were statuses/notifications/confirmations invented?
8. Were inputs/business objects turned into stories?
9. Are ambiguous capabilities still ambiguous?
10. Are inputs/outputs business-level?
11. Are rules traceable?
12. Are technical details excluded?
13. Are open questions focused?
14. Are all requirements covered?
If any unsupported behavior is found, correct it before finalizing.
