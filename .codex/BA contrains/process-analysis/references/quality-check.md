# Process Analysis Quality Check

Use this reference only when validating or reviewing a process-analysis result.

## 1. Source Coverage

Check:

- Every supported process maps to at least one requirement.
- Every requirement is represented by a process or explicitly marked as not process-defining.
- No source capability is silently dropped.

## 2. Actor Accuracy

Check:

- Actor names match the source.
- Actor responsibilities are not expanded without evidence.
- Interactions between actors are source-supported.

## 3. Process Boundary

Check:

- The process describes a business capability or interaction.
- The process does not become an implementation workflow.
- Technical mechanisms are excluded unless explicitly supported.

Reject examples such as:

- API calls;
- database updates;
- frontend screens;
- background jobs;
- technical services.

## 4. Workflow Safety

Check that the analysis does NOT invent:

- step sequences;
- approval flows;
- validation flows;
- notifications;
- payment callbacks;
- automatic assignments;
- escalation;
- status transitions.

If such information is unsupported, it must be an `OPEN_QUESTION`.

## 5. Ambiguity

Check ambiguous terms:

- manage;
- monitor;
- support;
- handle;
- available;
- suitable;
- overdue.

They must not silently become detailed operations.

If interpretation affects behavior or scope:

- lower confidence;
- preserve the source wording;
- create an `OPEN_QUESTION`.

## 6. Trigger and Input Accuracy

Every trigger/input must be:

- explicitly stated; or
- directly supported by a referenced requirement.

Do not infer technical or automatic triggers.

## 7. Outcome Accuracy

Every outcome must be supported by the source.

Do not invent:

- generated IDs;
- records;
- invoices;
- emails;
- notifications;
- status changes;
- confirmations.

## 8. Business Rules

Check that:

- ordinary facts are not incorrectly promoted to business rules;
- explicit constraints are preserved;
- inferred rules are clearly marked `DERIVED`;
- unresolved rules are marked `OPEN`.

## 9. Traceability

Verify:

`BP → FR`

and, where relevant:

`BP → BR`

There must be no unexplained process without a source.

## 10. Quality Gate

### PASS

Use when:

- process scope is well supported;
- traceability is complete;
- no meaningful unsupported workflow exists.

### PASS WITH QUESTIONS

Use when:

- processes are supported;
- important workflow details remain unspecified;
- those gaps are clearly marked as `OPEN_QUESTION`.

### FAIL

Use when:

- processes contain invented behavior;
- traceability is missing;
- actors or responsibilities are materially changed;
- implementation details are presented as requirements;
- major source capabilities are omitted.

## Final review

Before returning the result, ask:

1. Can every process be traced to source requirements?
2. Did I invent any workflow step?
3. Did I invent any status or transition?
4. Did I invent any actor responsibility?
5. Did I introduce API, database, UI, notification, or integration behavior?
6. Are ambiguous capabilities still ambiguous?
7. Are unresolved details marked as `OPEN_QUESTION`?

If any answer indicates unsupported invention,
correct the output before returning it.