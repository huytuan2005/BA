---

name: traceability

description: >
  Validate end-to-end traceability across requirements, analysis, design,data, API, NFR, and UI artifacts. Detect orphan artifacts, unsupported artifacts, broken trace links, hallucinated artifacts, missing coverage, contradictions, duplicate artifacts, and invalid references. Acts as the mandatory quality gate before blueprint generation.
  
## version: 1.0
---

---

name: traceability
description: >
Validate end-to-end traceability across requirements, analysis, design,
data, API, NFR, UI, tests, and implementation artifacts. Detect orphan
artifacts, unsupported artifacts, unsupported implementations, broken trace
links, hallucinated artifacts, hallucinated requirements, missing coverage,
missing test coverage, contradictions, duplicate artifacts, and invalid
references. Acts as the mandatory quality gate before blueprint generation.
version: 1.0
------------

# Skill 9 — Traceability

## 1. Purpose

The `traceability` skill validates whether every downstream artifact is
supported by authoritative upstream evidence and whether every applicable
requirement is sufficiently covered by downstream artifacts.

The skill MUST detect:

* orphan artifacts
* unsupported artifacts
* unsupported implementations
* broken trace links
* hallucinated artifacts
* hallucinated requirements
* missing requirement coverage
* missing test coverage
* contradictions
* duplicate artifact IDs
* invalid references
* unsupported capabilities

The skill acts as a mandatory quality gate before `blueprint-generator`.

---

## 2. Pipeline Position

```text
Requirements
    ↓
Business Analysis
    ↓
Use Cases / User Stories
    ↓
UI / UX
    ↓
Data Model
    ↓
API Design
    ↓
NFR
    ↓
Tests
    ↓
Traceability
    ↓
Blueprint Generator
```

`traceability` MUST NOT generate new business artifacts.

It validates artifacts produced by previous skills.

---

## 3. Core Principle

Traceability answers two questions:

```text
1. Why does this artifact exist?
2. Where is this requirement implemented or verified?
```

Every downstream artifact MUST have an evidence-supported reason to exist.

Every applicable requirement MUST have sufficient downstream coverage.

No artifact may become authoritative merely because another artifact references it.

---

## 4. Source of Truth

Requirements are the primary source of truth for:

* business scope
* capabilities
* actors
* functional intent
* business rules
* explicit constraints
* required behaviors

Approved upstream artifacts may elaborate requirements but MUST NOT silently
introduce new business scope.

Downstream artifacts MUST NOT create requirements implicitly.

For example:

```text
Requirement:
Customer can search storage facilities by location.

Valid:
GET /api/storage/search?location=...

Invalid:
GET /api/storage/{id}
```

The existence of an API does not prove that the required search capability
has been implemented.

---

## 5. Evidence Hierarchy

When validating a claim, use this evidence order:

```text
1. Explicit Requirement
2. Explicit Business Rule
3. Approved Upstream Artifact
4. Explicit Project Constraint
5. Downstream Artifact Claim
```

A lower-level artifact MUST NOT override stronger upstream evidence.

A downstream artifact claim by itself is NOT sufficient evidence for a new
business capability.

---

## 6. Artifact Sources

The skill MAY validate artifacts from:

* requirements
* business rules
* use cases
* user stories
* UI specifications
* API specifications
* data models
* NFR specifications
* test specifications
* implementation specifications
* approved generated artifacts
* artifact registry

Every artifact MUST have a stable identity.

---

## 7. Artifact Identity

Every artifact SHOULD have:

```yaml
id:
type:
name:
description:
status:
version:
source:
provenance:
```

Example:

```yaml
id: REQ-001
type: REQUIREMENT
name: Search storage facilities
```

IDs MUST be unique within the project artifact graph.

Duplicate IDs are a quality failure.

---

## 8. Artifact Metadata

Minimum useful metadata:

```yaml
id
type
name
description
source
provenance
status
version
```

`source` SHOULD identify the upstream artifact(s) that justify the artifact.

`provenance` SHOULD identify which approved skill or source produced it.

Example:

```yaml
id: API-004
type: API
name: Search Storage Facilities
source:
  - REQ-001
provenance: api-generator
status: approved
```

---

## 9. Traceability Graph

Traceability MUST be treated as a directed graph.

```text
Requirement
    ↓
Business Rule
    ↓
Use Case
    ↓
UI
    ↓
API
    ↓
Data
    ↓
Test
```

Not every requirement needs every artifact type.

Valid paths depend on applicability.

For example:

```text
REQ → UI → API → TEST
```

may be valid for a functional web feature.

Another requirement may validly be:

```text
REQ → NFR → TEST
```

without requiring UI or DATA artifacts.

---

## 10. Valid Trace Links

A trace link is valid only when ALL conditions hold:

```text
1. Source artifact exists.
2. Target artifact exists.
3. The relationship type is valid.
4. The target semantically supports the source.
5. The relationship is supported by evidence.
6. The relationship does not contradict authoritative artifacts.
```

Type compatibility alone is NOT sufficient.

Example:

```text
REQ → API
```

is not valid merely because requirements can generally relate to APIs.

The API MUST actually support the capability expressed by the requirement.

---

## 11. Existence ≠ Implementation

The presence of an artifact MUST NOT be interpreted as proof that the
required capability exists.

This rule is mandatory.

```text
Artifact exists
      ≠
Capability implemented
```

For every requirement-to-implementation relationship:

```text
1. Verify requirement exists.
2. Verify implementation artifact exists.
3. Extract required capability from requirement.
4. Extract implemented capability from target.
5. Compare required capability with implemented capability.
6. Verify semantic equivalence or sufficient implementation coverage.
```

If the implementation exists but does not implement the required capability:

```text
UNSUPPORTED_IMPLEMENTATION
```

MUST be emitted.

Example:

```text
Requirement:
Search facilities by location.

Implementation:
GET /api/storage/{id}

Result:
UNSUPPORTED_IMPLEMENTATION
```

The endpoint exists, but it implements retrieval by ID rather than location
search.

---

## 12. Forward Traceability

Forward traceability answers:

```text
Requirement
    ↓
What artifacts exist because of this requirement?
```

Every requirement MUST be evaluated.

Possible states:

```text
COVERED
PARTIALLY_COVERED
UNCOVERED
```

A requirement is `COVERED` when all applicable required downstream coverage
is satisfied.

A requirement is `PARTIALLY_COVERED` when some applicable coverage exists but
one or more required parts are missing.

A requirement is `UNCOVERED` when no valid downstream support exists.

---

## 13. Reverse Traceability

Reverse traceability answers:

```text
Artifact
    ↓
Why does this artifact exist?
```

Every downstream artifact MUST trace back to an authoritative source.

Examples:

```text
UI-001 → REQ-001
API-001 → REQ-001
DATA-001 → REQ-001
TEST-001 → REQ-001
```

An artifact without a valid upstream justification is suspicious and MUST be
evaluated for orphan or unsupported status.

---

## 14. Orphan Detection

An orphan artifact is a downstream artifact with no valid upstream support.

Examples:

```text
UI-099 has no source requirement.

API-088 has no source requirement.

DATA-077 has no source requirement.
```

The skill MUST emit:

```text
ORPHAN_ARTIFACT
```

when the artifact exists but has no valid trace to an authoritative source.

Orphan detection MUST NOT flag legitimately shared or indirectly traced
artifacts.

---

## 15. Unsupported Artifact Detection

An artifact is unsupported when it has a source relationship but the source
does not justify the artifact's business capability.

Example:

```text
Requirement:
Customer can rent a storage unit.

API:
POST /api/biometric-face-recognition
```

If no authoritative source requires biometric authentication, the API is
unsupported.

The skill MUST emit:

```text
UNSUPPORTED_ARTIFACT
```

or:

```text
UNSUPPORTED_CAPABILITY
```

as appropriate.

---

## 16. Unsupported Implementation Detection

`UNSUPPORTED_IMPLEMENTATION` MUST be evaluated independently from artifact
existence.

The validator MUST NOT accept:

```text
Requirement exists
+
API exists
=
Requirement implemented
```

Instead:

```text
Requirement capability
        ↓
Implementation capability
        ↓
Semantic comparison
```

The implementation MUST perform the required operation, behavior, or business
capability.

Examples:

```text
REQ:
Search products by keyword.

API:
GET /products/{id}

Result:
UNSUPPORTED_IMPLEMENTATION
```

```text
REQ:
Reset password using email verification.

API:
POST /login

Result:
UNSUPPORTED_IMPLEMENTATION
```

---

## 17. Broken Trace Link Detection

A broken trace link occurs when an artifact references an ID that does not
exist.

Example:

```yaml
source:
  - REQ-999
```

when `REQ-999` is absent.

The skill MUST emit:

```text
BROKEN_LINK
```

A broken link is different from a hallucinated artifact.

### Broken Link

```text
A real artifact references a nonexistent artifact ID.
```

### Hallucinated Artifact

```text
Something is presented as a real project artifact,
but no authoritative artifact, registry entry, or approved
generation output exists for it.
```

The validator MUST NOT create the missing artifact to repair the link.

---

## 18. Hallucinated Artifact Detection

An artifact is hallucinated when it is presented as an actual project artifact
but cannot be found in:

```text
1. Authoritative artifact set
2. Artifact registry
3. Approved generation output
```

Example:

```text
API-999 is referenced as an existing API,
but API-999 does not exist anywhere in the approved artifact set.
```

Emit:

```text
HALLUCINATED_ARTIFACT
```

Do NOT silently create API-999.

---

## 19. Hallucinated Requirement Detection

A downstream artifact MUST NOT create an implicit requirement.

For every business capability claimed by a downstream artifact:

```text
1. Search authoritative requirements.
2. Search approved business rules.
3. Search approved constraints.
4. Search approved upstream artifacts.
5. Determine whether the capability has authoritative support.
```

If no authoritative source supports the capability:

```text
UNSUPPORTED_CAPABILITY
```

MUST be emitted.

If the artifact explicitly represents the unsupported capability as
requirement-backed, emit:

```text
HALLUCINATED_REQUIREMENT
```

A missing requirement MUST NOT be invented by the validator.

Example:

```text
API:
POST /api/face-recognition/login

Requirements:
No biometric authentication requirement exists.

Result:
HALLUCINATED_REQUIREMENT
```

---

## 20. Missing Coverage Detection

Missing coverage MUST be applicability-aware.

For every requirement, determine:

```yaml
UI_APPLICABLE:
API_APPLICABLE:
DATA_APPLICABLE:
NFR_APPLICABLE:
TEST_APPLICABLE:
```

The validator MUST NOT assume that every requirement needs:

```text
UI + API + DATA + NFR + TEST
```

A missing artifact type is a coverage failure ONLY when:

```text
1. The requirement logically requires that artifact type, OR
2. An approved project rule explicitly requires that artifact type.
```

Example:

```text
REQ:
System must respond within 2 seconds.

UI: not required
API: not necessarily required
DATA: not necessarily required
NFR: required
TEST: required
```

Missing UI is therefore NOT automatically a failure.

If an applicable artifact is missing:

```text
MISSING_COVERAGE
```

MUST be emitted.

---

## 21. Test Coverage

Requirements marked:

```text
TEST_APPLICABLE = true
```

MUST have at least one valid test or verification artifact.

The validator MUST verify:

```text
Requirement
    ↓
Test
```

and ensure that the test actually verifies the required behavior.

If no valid test covers the requirement:

```text
MISSING_TEST_COVERAGE
```

MUST be emitted.

Default severity:

```text
MEDIUM
```

If project rules explicitly mandate test coverage:

```text
HIGH
```

may be used.

A test artifact that merely exists but tests an unrelated behavior does NOT
count as coverage.

---

## 22. Contradiction Detection

The skill MUST detect semantic contradictions across:

```text
Requirement
Business Rule
Use Case
UI
API
Data
NFR
Test
```

Examples:

```text
Requirement:
Password minimum length = 8

UI:
Password minimum length = 6
```

Result:

```text
CONTRADICTION
```

Another example:

```text
Requirement:
Only verified owners may register horses.

API:
Allows every authenticated user to register a horse.
```

Result:

```text
CONTRADICTION
```

---

## 23. Duplicate Artifact Detection

Every artifact ID MUST be unique.

Example:

```text
API-001
API-001
```

Result:

```text
DUPLICATE_ARTIFACT_ID
```

Duplicate IDs are HIGH severity by default and MAY block blueprint generation.

---

## 24. Evidence Validation

Every trace relationship MUST have sufficient evidence.

The validator MUST distinguish:

```text
Explicit evidence
Implicit inference
Unsupported assumption
```

Only explicit evidence or valid semantic derivation from approved upstream
artifacts may justify a trace.

A downstream artifact cannot become evidence for its own existence.

---

## 25. Artifact Necessity

An artifact is necessary when its existence is justified by:

```text
Requirement
Business Rule
Approved Constraint
Approved Upstream Artifact
```

If no valid source requires or supports the artifact, it MUST be flagged as:

```text
ORPHAN_ARTIFACT
```

or:

```text
UNSUPPORTED_ARTIFACT
```

depending on whether a trace exists.

---

## 26. Cross-Artifact Consistency

The validator MUST compare related artifacts for consistency.

Minimum checks include:

```text
Requirement ↔ Use Case
Requirement ↔ UI
Requirement ↔ API
Requirement ↔ Data
Requirement ↔ NFR
Requirement ↔ Test
UI ↔ API
API ↔ Data
Business Rule ↔ API
Business Rule ↔ UI
```

Conflicting claims MUST generate:

```text
CONTRADICTION
```

---

## 27. Relationship Rules

Valid relationships include:

```text
REQUIREMENT → USE_CASE
REQUIREMENT → USER_STORY
REQUIREMENT → UI
REQUIREMENT → API
REQUIREMENT → DATA
REQUIREMENT → NFR
REQUIREMENT → TEST

BUSINESS_RULE → USE_CASE
BUSINESS_RULE → UI
BUSINESS_RULE → API
BUSINESS_RULE → TEST

UI → API
API → DATA
TEST → REQUIREMENT
TEST → API
```

Additional relationships are allowed only when semantically justified.

A relationship MUST NOT be accepted solely because its artifact types are
technically compatible.

---

## 28. Shared Artifacts

One artifact MAY support multiple requirements.

Example:

```text
REQ-001 ─┐
REQ-002 ─┼──→ API-001
REQ-003 ─┘
```

This is valid when API-001 actually supports all three requirements.

The validator MUST NOT classify shared artifacts as orphans merely because
they have multiple sources.

---

## 29. Partial Traceability

An artifact may partially support a requirement.

Example:

```text
REQ:
Customer can search, filter, sort, and paginate facilities.

API:
Only search is implemented.
```

Result:

```text
PARTIALLY_COVERED
```

and:

```text
MISSING_COVERAGE
```

for the unsupported required capabilities.

If the target artifact does not implement the required capability at all,
emit:

```text
UNSUPPORTED_IMPLEMENTATION
```

---

## 30. Reference Validation Order

Validation MUST follow this deterministic order:

```text
1. Load authoritative artifacts.
2. Build artifact registry.
3. Detect duplicate IDs.
4. Validate artifact references.
5. Detect broken links.
6. Detect hallucinated artifacts.
7. Validate source evidence.
8. Validate capability semantics.
9. Detect unsupported implementations.
10. Detect orphan artifacts.
11. Determine requirement applicability.
12. Calculate forward coverage.
13. Calculate reverse coverage.
14. Validate test coverage.
15. Detect contradictions.
16. Produce findings.
17. Evaluate quality gate.
```

This order prevents later checks from treating invalid references as valid
evidence.

---

## 31. Error Classification

Supported finding codes:

```text
ORPHAN_ARTIFACT
UNSUPPORTED_ARTIFACT
UNSUPPORTED_CAPABILITY
UNSUPPORTED_IMPLEMENTATION
BROKEN_LINK
HALLUCINATED_ARTIFACT
HALLUCINATED_REQUIREMENT
MISSING_COVERAGE
MISSING_TEST_COVERAGE
CONTRADICTION
DUPLICATE_ARTIFACT_ID
INVALID_REFERENCE
```

---

## 32. Severity

Default severity levels:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Recommended classification:

### CRITICAL

```text
HALLUCINATED_REQUIREMENT
HALLUCINATED_ARTIFACT
BROKEN_LINK
CONTRADICTION affecting core business behavior
UNSUPPORTED_CAPABILITY affecting business scope
UNSUPPORTED_IMPLEMENTATION of a mandatory core requirement
```

### HIGH

```text
DUPLICATE_ARTIFACT_ID
MISSING mandatory coverage
UNSUPPORTED_ARTIFACT affecting core scope
```

### MEDIUM

```text
MISSING_TEST_COVERAGE
PARTIAL_COVERAGE
non-critical unsupported artifact
```

### LOW

```text
minor metadata/provenance problems
```

---

## 33. Findings

Every finding SHOULD contain:

```yaml
id:
type:
severity:
artifact_id:
source_id:
target_id:
message:
evidence:
recommendation:
```

Example:

```yaml
id: TRF-008
type: UNSUPPORTED_IMPLEMENTATION
severity: HIGH
artifact_id: API-004
source_id: REQ-001
target_id: API-004
message: >
  The requirement requires location-based facility search,
  but the API only retrieves a facility by ID.
evidence:
  - REQ-001
  - API-004
```

---

## 34. No Silent Repair

The traceability skill MUST NOT:

* create missing requirements
* create missing APIs
* create missing UI
* create missing data models
* create missing tests
* invent business rules
* modify artifact meaning
* silently repair broken references
* silently reinterpret contradictions

Its responsibility is detection and reporting.

Repair MUST happen in the appropriate upstream skill.

---

## 35. Hallucination Protection

The validator MUST distinguish between:

```text
Missing
Broken
Unsupported
Hallucinated
```

Definitions:

```text
Missing:
An expected artifact does not exist.

Broken:
A real artifact references a nonexistent artifact.

Unsupported:
An existing artifact has insufficient authoritative justification.

Hallucinated:
An artifact or requirement is presented as real
without existing authoritative evidence.
```

These categories MUST NOT be merged into a single generic error.

---

## 36. Coverage Matrix

The validator SHOULD produce a coverage matrix.

Example:

| Requirement | UI | API | DATA | NFR | TEST | Status            |
| ----------- | -- | --- | ---- | --- | ---- | ----------------- |
| REQ-001     | ✓  | ✓   | ✓    | -   | ✓    | COVERED           |
| REQ-002     | -  | ✓   | -    | ✓   | ✓    | COVERED           |
| REQ-003     | ✓  | ✗   | -    | -   | ✓    | PARTIALLY_COVERED |

`-` means not applicable.

`✗` means applicable but missing or invalid.

---

## 37. Traceability Status

Each requirement MUST receive one of:

```text
COVERED
PARTIALLY_COVERED
UNCOVERED
```

Each artifact MUST receive one of:

```text
SUPPORTED
PARTIALLY_SUPPORTED
UNSUPPORTED
ORPHAN
HALLUCINATED
```

---

## 38. Quality Gate

The traceability gate MUST evaluate all findings.

Blueprint generation MUST be blocked when any unresolved critical issue
exists.

Default blocking conditions:

```text
HALLUCINATED_REQUIREMENT
HALLUCINATED_ARTIFACT
BROKEN_LINK
CRITICAL CONTRADICTION
CRITICAL UNSUPPORTED_CAPABILITY
CRITICAL UNSUPPORTED_IMPLEMENTATION
DUPLICATE_ARTIFACT_ID
MANDATORY MISSING_COVERAGE
```

---

## 39. Quality Gate Algorithm

```text
FOR each artifact:

    validate identity

    IF duplicate ID:
        emit DUPLICATE_ARTIFACT_ID

    FOR each referenced source:
        IF source does not exist:
            emit BROKEN_LINK

    IF artifact is claimed as real
       AND artifact does not exist in authoritative artifact set:
        emit HALLUCINATED_ARTIFACT

    validate upstream evidence

    IF no valid upstream evidence:
        emit ORPHAN_ARTIFACT

    extract artifact capability

    IF capability is not supported by authoritative evidence:
        emit UNSUPPORTED_CAPABILITY

    IF artifact implements a requirement:
        compare required capability with implemented capability

        IF implementation does not satisfy requirement:
            emit UNSUPPORTED_IMPLEMENTATION


FOR each requirement:

    determine applicability:
        UI_APPLICABLE
        API_APPLICABLE
        DATA_APPLICABLE
        NFR_APPLICABLE
        TEST_APPLICABLE

    calculate forward coverage

    IF required applicable artifact is missing:
        emit MISSING_COVERAGE

    IF TEST_APPLICABLE and no valid test exists:
        emit MISSING_TEST_COVERAGE

    detect contradictions


FOR each downstream capability claim:

    search requirements
    search business rules
    search constraints
    search approved upstream artifacts

    IF unsupported capability is presented as requirement-backed:
        emit HALLUCINATED_REQUIREMENT


IF any blocking finding exists:

    gate = BLOCKED

ELSE:

    gate = PASSED
```

---

## 40. Output Contract

The skill MUST produce a structured result.

Example:

```yaml
traceability:
  status: PASSED

summary:
  requirements: 12
  artifacts: 37
  covered: 11
  partially_covered: 1
  uncovered: 0

findings: []

gate:
  status: PASSED
  blueprint_generation: ALLOWED
```

Failure example:

```yaml
traceability:
  status: FAILED

findings:
  - id: TRF-001
    type: BROKEN_LINK
    severity: CRITICAL
    artifact_id: API-004
    source_id: REQ-999
    message: >
      API-004 references requirement REQ-999,
      but REQ-999 does not exist.

gate:
  status: BLOCKED
  blueprint_generation: NOT_ALLOWED
```

---

## 41. Failure Handling

When validation fails:

```text
1. Preserve all findings.
2. Do not repair artifacts.
3. Do not invent missing sources.
4. Do not downgrade severity to pass the gate.
5. Return BLOCKED when blocking findings exist.
```

The output MUST remain deterministic.

---

## 42. False Positive Protection

The validator MUST avoid false positives for:

### Shared artifacts

```text
One API supporting multiple requirements is valid.
```

### Backend-only requirements

```text
A requirement may legitimately have no UI.
```

### Non-data requirements

```text
An NFR may legitimately have no data model.
```

### Indirect traceability

```text
REQ → USE_CASE → API
```

may be valid when the use case provides the semantic bridge.

### Shared APIs

One API may legitimately support multiple UI flows.

### Infrastructure artifacts

Infrastructure artifacts may trace to explicit project constraints rather
than functional requirements.

---

## 43. Deterministic Validation Rules

The following rules are mandatory:

```text
RULE-T01:
Every downstream artifact must have an authoritative justification.

RULE-T02:
Every trace source must exist.

RULE-T03:
Every trace target must exist.

RULE-T04:
Type compatibility alone does not establish trace validity.

RULE-T05:
Existence of an implementation artifact does not prove implementation
of the required capability.

RULE-T06:
Requirement capability must be semantically comparable with implementation
capability.

RULE-T07:
Missing requirements must never be invented.

RULE-T08:
Missing artifacts must never be silently created.

RULE-T09:
A downstream artifact cannot establish its own business requirement.

RULE-T10:
Missing coverage is evaluated only for applicable artifact types.

RULE-T11:
TEST_APPLICABLE requirements require valid test coverage.

RULE-T12:
Broken links and hallucinated artifacts are different failure classes.

RULE-T13:
Unsupported capability and hallucinated requirement are different failure
classes but may coexist.

RULE-T14:
Shared artifacts are valid when they genuinely support multiple sources.

RULE-T15:
Contradictory artifacts cannot be treated as mutually valid.

RULE-T16:
Critical findings block blueprint generation.

RULE-T17:
The validator must report findings instead of repairing artifacts.

RULE-T18:
Indirect traceability is valid when every semantic bridge is itself valid.
```

---

## 44. Test Compatibility

The implementation MUST support the following test categories:

```text
TR-001 Happy Path
TR-002 One Requirement → Multiple Artifacts
TR-003 Shared Artifact
TR-004 Orphan UI
TR-005 Orphan API
TR-006 Orphan Data Model
TR-007 Unsupported Capability
TR-008 Unsupported Implementation
TR-009 Broken Link
TR-010 Deleted Requirement
TR-011 Hallucinated Artifact
TR-012 Hallucinated Requirement
TR-013 Missing Requirement Coverage
TR-014 Missing Test Coverage
TR-015 Requirement/UI Contradiction
TR-016 UI/API Contradiction
TR-017 Data/API Contradiction
TR-018 Business Rule Contradiction
TR-019 Mixed Failures
TR-020 Hallucinated Artifact + Valid Artifacts
```

The validator MUST distinguish all failure categories represented by the
test suite.

---

## 45. Release Criteria

Traceability v1.0 MUST NOT be released unless:

```text
TR-001 → TR-020 = PASS
```

and:

```text
Critical false positives = 0
Critical false negatives = 0
```

and:

```text
No unresolved blocking finding
```

and:

```text
Hallucination protection verified
Unsupported implementation detection verified
Applicability-aware coverage verified
Missing test coverage verified
```

---

## 46. Final Gate Contract

Only when all release criteria pass:

```text
TRACEABILITY v1.0
STATUS: PASSED
BLUEPRINT GENERATION: ALLOWED
```

Otherwise:

```text
TRACEABILITY v1.0
STATUS: FAILED
BLUEPRINT GENERATION: BLOCKED
```

---

## 47. Non-Goals

This skill does NOT:

* generate requirements
* generate APIs
* generate UI
* generate data models
* generate tests
* generate NFRs
* repair inconsistent artifacts
* redesign the system
* decide new business rules

Those responsibilities belong to upstream or downstream skills.

---

## 48. Final Principle

```text
NO SOURCE
    ↓
NO JUSTIFICATION
    ↓
NO TRUST
```

Traceability exists to ensure that the blueprint is generated only from
artifacts that can be proven to belong to the approved system scope.
