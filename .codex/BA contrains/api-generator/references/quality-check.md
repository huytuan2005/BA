# API Generator Quality Check

Use this reference only when validating or reviewing a result.

## 1. API Evidence
- Every generated API has explicit API/interface evidence.
- FR/FN/UC alone is not treated as API evidence.
- Business actors, entities, and capabilities are not automatically APIs.
- If no API evidence exists, result explicitly states no API contracts are identified.

## 2. API Boundary
Reject:
- automatic FR → endpoint;
- automatic FN → endpoint;
- automatic UC → endpoint;
- automatic entity → resource;
- database CRUD exposed as API without evidence.

API must represent an explicitly supported interface contract.

## 3. Naming
- Preserve source-supported interface names.
- Do not manufacture REST endpoint names.
- No technical naming when source only provides a business capability.

## 4. HTTP Method and Path
- Method explicitly supported?
- Path explicitly supported?
- If not, use `Not specified in source.`
- Never infer GET/POST/PUT/PATCH/DELETE from common REST conventions.

## 5. Request Inputs
Check:
- Every API input is explicitly part of interface evidence.
- Functional inputs are not automatically API inputs.
- No invented IDs, field names, JSON properties, data types, enums, or required flags.
Reject:
- FR/FN input → request parameter without source support.

## 6. Response Outputs
- Every output is explicitly interface-supported.
- Business-level output may be retained when source defines it as interface output.
- No invented response DTO, status code, generated ID, timestamp, confirmation,
  database record, or message.

## 7. Authentication and Authorization
Reject inferred:
- JWT;
- OAuth;
- API keys;
- bearer tokens;
- sessions;
- role guards.
Actor role does not prove API authentication/authorization.

## 8. Business Rules
- Only API-relevant constraints are included.
- Rules trace to original source evidence.
- Ordinary fields and endpoint names are not business rules.

## 9. API Relationships
Critical check:
- Every relationship connects actual `API-*` artifacts.
- No relationship to input, entity, field, condition, actor, or process context.
- No relationship inferred from process/use-case order.
- No relationship inferred from shared data.
- No relationship inferred from business plausibility.
- No INCLUDE/EXTEND/DEPENDENCY/GENERALIZATION unless source explicitly supports it.
- If none exists, do not create a relationship table.

## 10. Data Model Separation
Reject:
- entity → endpoint;
- attribute → JSON field;
- PK → path parameter;
- FK → request field;
- relationship → nested response.
Data-model evidence only supports API detail when source explicitly links them.

## 11. Traceability
Every API/operation must trace to original evidence.
Prefer:
`API → FR → FN → UC`
when supported.
Requirements that are not API-defining must not be silently converted.

## 12. Ambiguity
Check terms such as:
`manage / monitor / track / support / handle / available / suitable / overdue`
No ambiguous business capability may become a fabricated endpoint or CRUD set.

## 13. Open Questions
Questions must determine missing API contract or API necessity:
- Is an API required?
- Which operations are exposed?
- What methods/paths are required?
- What inputs/outputs are part of the contract?
- What security is required?
- What integration/relationship is required?
Avoid generic technical questions.

## 14. Quality Gate
PASS if:
- APIs are explicitly source-supported;
- contract details are source-supported;
- traceability is complete;
- no material invention exists.

PASS WITH QUESTIONS if:
- API/interface existence is supported;
- some contract details remain unresolved;
- no unsupported details were invented.

FAIL if:
- endpoints are generated from FR/FN/UC alone;
- methods/paths/payloads/status codes are invented;
- security is invented;
- relationships are inferred;
- technical details replace missing evidence;
- source evidence is missing.

## Final Review
1. Does every API have explicit interface evidence?
2. Was FR/FN/UC automatically turned into endpoint?
3. Was `manage` turned into CRUD?
4. Was entity turned into API resource?
5. Was HTTP method invented?
6. Was path invented?
7. Were request fields invented?
8. Were response fields/status codes invented?
9. Was authentication invented?
10. Was authorization invented?
11. Were data-model fields mapped automatically?
12. Were API relationships inferred?
13. Does every relationship target another `API-*`?
14. Are non-API requirements explicitly identified?
15. Are open questions focused?

If unsupported API behavior is found, correct it before finalizing.
