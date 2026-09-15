# NFR Generator Quality Check

Use this reference only when validating or reviewing a result.

## 1. Source Evidence

- Every NFR has explicit supporting evidence.
- No NFR exists only because it is a common best practice.
- Source wording and meaning are preserved.
- NFRs without direct evidence are flagged, not silently accepted.

## 2. Functional-vs-Non-Functional Boundary

Reject:
- functional capabilities relabeled as NFRs;
- business rules relabeled as NFRs;
- domain facts relabeled as NFRs.

Examples:
- "Customer can reserve a unit" → functional requirement, not NFR.
- "System handles payments" → functional requirement, not security NFR.
- "System manages accounts" → functional requirement, not usability NFR.

## 3. Numeric Targets

Check that every metric, threshold, limit, SLA, capacity, timeout,
availability percentage, RPO, RTO, retention period, or response-time target
is explicitly supported.

Reject invented examples such as:
- `< 2 seconds`;
- `99.9% uptime`;
- `1,000 concurrent users`;
- `15-minute RPO`;
- `1-hour RTO`.

## 4. Security / Privacy / Compliance

Do not infer controls from domain sensitivity.

Reject unsupported:
- JWT;
- OAuth;
- MFA;
- encryption;
- TLS;
- password rules;
- RBAC;
- session timeout;
- audit logging;
- privacy laws/compliance frameworks.

A money-related or account-related function is not, by itself, evidence of a
specific security NFR.

## 5. Quality Categories

- Use only categories supported by evidence.
- Do not create placeholder NFRs for every category.
- `OTHER` is allowed only when evidence exists but does not fit another
  category.

## 6. Measurability

- Preserve explicit source target, unit, scope, and condition.
- Qualitative source constraints remain qualitative.
- If a quality requirement lacks a target that matters to implementation or
  acceptance, create an open question instead of inventing a target.

## 7. Derived NFRs

A `DERIVED` NFR is valid only when directly entailed by explicit evidence.

Reject derived NFRs based on:
- common practice;
- architecture assumptions;
- technology preferences;
- domain expectations;
- "good to have" qualities.

## 8. Security of Terms

Words such as:
`secure`, `fast`, `reliable`, `easy`, `available`, `scalable`,
`maintainable`

must not automatically become measurable NFRs.

If the source uses such a term without defining its level or scope:
- preserve the ambiguity;
- lower confidence if an NFR is still represented;
- create an OPEN_QUESTION when material.

## 9. NFR Dependencies

Every dependency must connect actual NFRs:
`NFR-* → NFR-*`

Reject:
- NFR → technology;
- NFR → API;
- NFR → database;
- NFR → actor;
- NFR → functional input;
- NFR → business object;
- NFR → implementation mechanism.

Do not infer dependencies from architecture or implementation plausibility.

## 10. Traceability

Every NFR must trace to source evidence.

Where applicable:
`NFR → FR → Source`

Generated IDs must never replace actual evidence.

## 11. Open Questions

Questions must affect:
- NFR existence;
- scope;
- target;
- condition;
- applicability;
- security/privacy/compliance interpretation.

Reject generic questions.

## 12. Quality Gate

### PASS
- Explicit NFR evidence is clear.
- No material unsupported NFRs.
- Targets and conditions are source-supported.
- Traceability is complete.

### PASS WITH QUESTIONS
- Core NFR evidence is supported.
- Some quality terms/targets/scope remain unresolved.
- No material invention exists.

### FAIL
- NFRs were invented from best practice.
- Numeric targets were invented.
- Security/privacy/compliance controls were invented.
- Functional requirements were relabeled as NFRs.
- Traceability is missing.
- Technical implementation leaked into the NFR baseline.

## Final Review

1. Does every NFR have source evidence?
2. Did any FR become an NFR without quality evidence?
3. Were numeric targets invented?
4. Were SLA/availability/capacity/recovery values invented?
5. Were security controls inferred?
6. Were privacy/compliance obligations invented?
7. Were vague quality terms silently made measurable?
8. Were technical solutions introduced?
9. Are derived NFRs truly entailed?
10. Are dependencies evidence-based and NFR-to-NFR?
11. Are open questions focused?
12. Is traceability complete?

If unsupported behavior or quality constraints are found, correct them before
finalizing.
