---

name: blueprint-generator
description: >
  Generate a complete, implementation-ready system blueprint fromtraceability-approved requirements, analysis, UI, API, data, NFR, business rules, tests, and other validated artifacts. The skill preserves traceability, prevents scope expansion, rejects hallucinated or unsupported artifacts, preserves contradictions as blocking issues, prevents silent repair, and never invents new system behavior. Acts the final structured synthesis step before implementation.
  version: 1.0
---

---

# Skill 10 — Blueprint Generator

## 1. Purpose

The `blueprint-generator` skill transforms validated project artifacts into
one coherent System Blueprint.

The Blueprint MUST be:

- traceability-backed
- scope-preserving
- deterministic
- implementation-oriented
- internally consistent
- auditable
- reversible to source artifacts

The Blueprint MUST NOT introduce new business scope.

The generator is a synthesis engine, not a requirements-discovery engine.

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
    ↓
SYSTEM BLUEPRINT
    ↓
Implementation
```

`blueprint-generator` is downstream from `traceability`.

It MUST NOT bypass the Traceability gate.

---

## 3. Core Principle

The Blueprint is a structured synthesis of approved artifacts.

It is NOT:

- a new requirements document
- a new architecture proposal
- a product redesign
- a feature brainstorming document
- an implementation invention engine

The fundamental rule is:

```text
Validated Source Artifacts
        ↓
Structured Synthesis
        ↓
System Blueprint
```

Never:

```text
Validated Source Artifacts
        ↓
Model Assumption
        ↓
New Business Scope
```

---

## 4. Pre-Generation Gate

Before generation begins, the generator MUST perform a preflight check.

Required:

```yaml
traceability:
  status: PASSED

gate:
  status: PASSED
  blueprint_generation: ALLOWED
```

The following conditions MUST also hold:

```text
blocking findings = 0
hallucinated artifacts = 0
hallucinated requirements = 0
broken links = 0
critical contradictions = 0
critical unsupported capabilities = 0
critical unsupported implementations = 0
duplicate artifact IDs = 0
mandatory missing coverage = 0
```

If any blocking condition exists:

```text
BLUEPRINT GENERATION: BLOCKED
```

The generator MUST stop before producing an approved Blueprint.

It MUST NOT generate a “best effort” Blueprint and mark it approved.

---

## 5. Source of Truth

The authoritative source hierarchy is:

```text
1. Approved Requirements
2. Approved Business Rules
3. Approved Analysis Artifacts
4. Approved UI Artifacts
5. Approved API Artifacts
6. Approved Data Artifacts
7. Approved NFR Artifacts
8. Approved Test Artifacts
9. Traceability Results
```

Lower-level artifacts may provide implementation detail.

They MUST NOT override authoritative requirements.

---

## 6. No Scope Expansion

The Blueprint MUST NOT introduce:

- new features
- new actors
- new business rules
- new permissions
- new workflows
- new APIs
- new database entities
- new UI screens
- new integrations
- new security mechanisms
- new NFRs

unless they already exist in approved source artifacts.

Example:

```text
Requirement:
Customer can search storage facilities by location.
```

Allowed:

```text
Search storage facilities by location
```

Not automatically allowed:

```text
Search by price
Search by distance
AI recommendation
Favorite facilities
Map integration
```

unless explicitly supported by approved artifacts.

---

## 7. Existence Does Not Create Scope

The presence of an existing downstream artifact MUST NOT be treated as
evidence for a new requirement.

Example:

```text
API:
POST /api/biometric-login
```

does NOT create:

```text
Requirement:
User can log in using biometrics.
```

A capability must have authoritative support independently of its downstream
implementation.

---

## 8. Input Contract

The generator SHOULD receive:

```yaml
traceability:
requirements:
business_rules:
use_cases:
user_stories:
ui:
api:
data:
nfr:
tests:
implementation:
```

Not every category is mandatory.

The presence of an artifact category depends on project scope and
applicability.

---

## 9. Artifact Registry

Before generation, the generator MUST build an immutable artifact registry.

The registry MUST contain:

```text
artifact_id
artifact_type
status
provenance
source_ids
semantic_content
```

The registry becomes the authoritative set for this generation run.

The generator MUST NOT create a new source artifact while constructing the
Blueprint.

Any Blueprint-only identifier MUST use a separate `BP-*` namespace.

---

## 10. Artifact Selection

Only artifacts satisfying ALL of the following may enter the approved
Blueprint:

```text
1. Artifact exists.
2. Artifact is approved.
3. Artifact has valid identity.
4. Artifact has valid provenance.
5. Artifact has valid traceability.
6. Artifact is not hallucinated.
7. Artifact is not an unresolved orphan.
8. Artifact does not introduce unsupported scope.
9. Artifact does not participate in an unresolved blocking contradiction.
```

An artifact failing these conditions MUST NOT be promoted to approved
Blueprint scope.

It MAY appear in a diagnostic or blocked-generation report.

---

## 11. Blueprint Structure

The default Blueprint structure is:

```text
1. System Overview
2. Scope
3. Actors & Roles
4. Functional Requirements
5. Business Rules
6. Use Cases / User Flows
7. UI / Screens
8. API / Backend
9. Data Model
10. NFR
11. Security
12. Test & Verification
13. Traceability
14. Implementation Boundaries
15. Open Issues
```

Sections MAY be omitted when genuinely not applicable.

The generator MUST NOT create artificial content merely to populate a section.

---

## 12. System Overview

The overview MUST be derived from approved requirements and analysis.

It MAY summarize:

- system purpose
- business domain
- primary users
- major capabilities
- major system boundaries

It MUST NOT introduce new capabilities.

Every stated capability SHOULD have a source reference.

---

## 13. Scope

The Scope section MUST distinguish:

```text
IN_SCOPE
OUT_OF_SCOPE
UNKNOWN
```

Only explicitly supported scope may be marked:

```text
IN_SCOPE
```

Absence alone MUST NOT be interpreted as `OUT_OF_SCOPE`.

Unknown information MUST remain:

```text
UNKNOWN
```

The generator MUST NOT invent scope decisions.

---

## 14. Actors & Roles

Actors MUST come from approved requirements or approved analysis artifacts.

For each actor:

```yaml
actor:
  id:
  role:
  responsibilities:
  permissions:
  source:
```

Permissions MUST be traceable to approved requirements or business rules.

Do not invent permissions from common industry practice.

---

## 15. Functional Requirements

Each functional requirement MUST preserve its source identity.

Example:

```yaml
requirement:
  id: REQ-001
  name: Search storage facilities
  description: ...
  source:
    - REQ-001
```

The generator MAY normalize wording for clarity.

It MUST NOT change business meaning.

---

## 16. Business Rules

Business rules MUST be copied or faithfully summarized from approved sources.

The generator MUST NOT derive new business rules from implementation details.

---

## 17. Use Cases & User Flows

Use cases MUST be derived from approved requirements and analysis.

Each flow SHOULD contain:

```text
Actor
Preconditions
Trigger
Main Flow
Alternative Flow
Exception Flow
Postconditions
Source
```

The generator MUST NOT invent alternative or exception flows.

Unknown behavior MUST be represented as:

```text
UNKNOWN
```

---

## 18. UI / Screens

Only traceability-approved UI artifacts may be included.

Each screen SHOULD contain:

```yaml
screen:
  id:
  name:
  purpose:
  actor:
  components:
  states:
  actions:
  source:
```

UI actions MUST correspond to supported requirements and interactions.

The generator MUST NOT add:

- buttons
- fields
- filters
- dialogs
- screens
- navigation
- UI states

without source support.

---

## 19. API / Backend

Only approved and traceable APIs may be included.

Each API SHOULD contain:

```yaml
api:
  id:
  method:
  path:
  purpose:
  authentication:
  authorization:
  request:
  response:
  errors:
  source:
```

The Blueprint MUST preserve the semantic meaning of the API.

An API MUST NOT be described as implementing a broader capability than its
source artifact establishes.

Example:

```text
GET /storage/{id}
```

MUST NOT automatically become:

```text
Search storage facilities
```

---

## 20. Data Model

Only approved data artifacts may be included.

Each entity SHOULD contain:

```yaml
entity:
  id:
  name:
  purpose:
  fields:
  relationships:
  constraints:
  source:
```

The generator MUST NOT invent:

- entities
- fields
- relationships
- indexes
- constraints

without source support.

---

## 21. NFR

NFRs MUST be preserved from approved NFR artifacts.

The generator MUST NOT invent numeric targets.

Example:

```text
Approved:
Response time ≤ 2 seconds
```

Allowed:

```text
Response time target: ≤ 2 seconds
```

Not allowed:

```text
Response time target: ≤ 500 ms
```

---

## 22. Security

Security requirements MUST be derived from approved sources.

The generator MUST NOT automatically add:

```text
OAuth2
2FA
Biometric authentication
WAF
IP allowlisting
```

unless supported by approved artifacts.

---

## 23. Test & Verification

Tests MUST preserve their relationship to requirements.

The Blueprint MUST NOT invent tests to hide missing coverage.

If Traceability reports:

```text
MISSING_TEST_COVERAGE
```

the generator MUST preserve that finding.

---

## 24. Traceability Preservation

Every major Blueprint element MUST preserve source references.

Example:

```yaml
blueprint_item:
  id: BP-FUNC-001
  source:
    - REQ-001
    - API-001
    - UI-001
```

Every approved Blueprint item MUST satisfy:

```text
Blueprint Item
      ↓
Source Artifact
      ↓
Authoritative Requirement / Rule / Constraint
```

If this chain cannot be established, the item MUST NOT be approved.

---

## 25. Traceability IDs

Source IDs MUST be preserved exactly.

Do not silently rename:

```text
REQ-001
```

to:

```text
FR-001
```

If Blueprint IDs are introduced:

```yaml
blueprint_id: BP-FUNC-001
source:
  - REQ-001
```

Source IDs remain authoritative.

---

## 26. Shared Artifacts

Shared artifacts MAY appear in multiple Blueprint sections.

Example:

```text
REQ-001 ─┐
REQ-002 ─┼──→ API-001
REQ-003 ─┘
```

The generator MUST preserve all valid relationships.

It MUST NOT duplicate the underlying artifact as separate implementations.

---

## 27. Partial Requirements

If a requirement is partially covered, the Blueprint MUST preserve the
partial state.

Example:

```yaml
requirement:
  id: REQ-003
  status: PARTIALLY_COVERED
  implemented:
    - search
  missing:
    - filtering
```

The generator MUST NOT invent the missing functionality.

If partial coverage is blocking under Traceability rules, generation MUST
stop.

---

## 28. Contradictions

The generator MUST NOT resolve contradictions by selecting one artifact
arbitrarily.

If Traceability identifies a blocking contradiction:

```text
BLUEPRINT GENERATION: BLOCKED
```

The contradiction MUST be preserved in the diagnostic output.

No silent resolution is allowed.

---

## 29. Hallucinated Artifacts

Hallucinated artifacts MUST never enter approved Blueprint scope.

If an artifact is absent from the artifact registry:

```text
HALLUCINATED_ARTIFACT
```

must be preserved.

The generator MUST NOT create a replacement artifact.

---

## 30. Hallucinated Requirements

The generator MUST NOT convert downstream behavior into a new requirement.

Example:

```text
API:
POST /api/biometric-login

No biometric requirement exists.
```

The Blueprint MUST NOT generate a biometric requirement.

---

## 31. Orphan Artifacts

Orphan artifacts MUST NOT become Blueprint scope.

They MAY be listed in diagnostic output or Open Issues only as unresolved
source problems.

They MUST NOT be represented as approved system capabilities.

---

## 32. Missing Coverage

If Traceability reports:

```text
MISSING_COVERAGE
```

the generator MUST NOT invent the missing artifact.

For example:

```text
Missing API
```

MUST NOT become:

```text
POST /api/...
```

unless that API already exists as an approved artifact.

A missing coverage item MAY be preserved as an Open Issue if generation is
otherwise allowed.

---

## 33. Unsupported Implementation

If Traceability reports:

```text
UNSUPPORTED_IMPLEMENTATION
```

the generator MUST NOT rewrite the implementation to make it appear valid.

Example:

```text
Requirement:
Search facilities by location.

API:
GET /storage/{id}
```

The Blueprint MUST preserve the API's actual meaning.

It MUST NOT relabel it as location search.

---

## 34. Duplicate Artifacts

Duplicate IDs MUST be treated according to Traceability findings.

If duplicate IDs are blocking:

```text
BLUEPRINT GENERATION: BLOCKED
```

The generator MUST NOT arbitrarily select one artifact.

---

## 35. Scope Expansion Detection

Before final approval, perform a capability-level scope comparison.

For every Blueprint capability:

```text
Blueprint Capability
        ↓
Find source reference
        ↓
Find authoritative requirement / rule / constraint
        ↓
Compare semantic meaning
```

If no source exists:

```text
SCOPE_EXPANSION
```

MUST be emitted.

If the Blueprint capability is broader than the source capability:

```text
SCOPE_EXPANSION
```

MUST be emitted.

If the Blueprint changes the meaning of the source:

```text
SEMANTIC_DRIFT
```

MUST be emitted.

---

## 36. Capability-Level Scope Rule

Scope comparison MUST operate on capabilities, not merely artifact IDs.

Example:

```text
Source:
Customer can search facilities by location.

Blueprint:
Customer can search, filter, sort and rank facilities.
```

Even if the Blueprint references the correct requirement ID, the additional
capabilities are scope expansion.

Therefore:

```text
Correct source ID
    ≠
Correct semantic scope
```

Both identity and semantic meaning MUST be validated.

---

## 37. Semantic Preservation

For every Blueprint item, compare:

```text
source semantics
        ↓
normalized Blueprint semantics
```

The result MUST be:

```text
EQUIVALENT
```

or a narrower representation that does not change business meaning.

The following are prohibited:

```text
broader meaning
new behavior
new actor
new permission
new constraint
new workflow
new capability
```

These produce:

```text
SEMANTIC_DRIFT
```

or:

```text
SCOPE_EXPANSION
```

as appropriate.

---

## 38. Silent Repair Prevention

The generator MUST NOT:

- fix missing requirements
- fix broken links
- resolve contradictions silently
- rename source IDs silently
- merge conflicting artifacts silently
- create missing APIs
- create missing database fields
- create missing UI screens
- create missing tests
- infer undocumented business rules
- reinterpret unsupported implementations as valid

Generation is synthesis, not repair.

---

## 39. Assumption Policy

Assumptions MUST be explicitly labeled.

Allowed:

```yaml
assumption:
  id: ASM-001
  statement: Deployment platform is not specified.
  status: OPEN
```

Forbidden:

```yaml
framework: React
```

when React is not supported by source artifacts.

An assumption MUST NOT become approved system scope.

---

## 40. Unknown Policy

When source artifacts do not define something:

```text
UNKNOWN
```

MUST be preferred over invention.

Unknown information MUST NOT be converted into a concrete implementation
decision without an approved source.

---

## 41. Implementation Boundaries

The Blueprint MAY identify:

```text
Frontend
Backend
Database
External Services
Infrastructure
Testing
```

but responsibilities MUST come from approved artifacts.

The generator MUST NOT choose a technology stack without evidence.

---

## 42. Blueprint Normalization

The generator MAY normalize:

- wording
- formatting
- presentation names
- section ordering
- duplicate textual descriptions

The generator MUST preserve:

- source IDs
- business meaning
- constraints
- business rules
- actor semantics
- capability semantics
- trace relationships

Normalization MUST NOT become scope expansion.

---

## 43. Canonicalization

Before generation, the generator MUST canonicalize the input artifact set.

Canonicalization MUST:

```text
1. Sort artifacts by stable ID.
2. Sort source references by stable ID.
3. Normalize equivalent formatting.
4. Preserve semantic content.
5. Preserve source identity.
6. Preserve relationship direction.
```

Canonicalization MUST NOT:

- merge different artifacts
- resolve contradictions
- invent missing values
- modify business meaning

This creates a deterministic generation input.

---

## 44. Deterministic Generation

Given the same:

```text
canonical artifact set
+
same Traceability result
+
same generator version
```

the generator MUST produce the same semantic Blueprint.

Determinism applies to:

```text
capabilities
actors
requirements
business rules
use cases
UI
API
data
NFR
tests
trace relationships
section ordering
Blueprint IDs
```

Runtime metadata such as:

```text
timestamp
execution ID
```

may differ.

Semantic output MUST NOT differ.

---

## 45. Blueprint IDs

Blueprint-generated IDs MUST use a namespace distinct from source IDs.

Example:

```text
BP-SYS-001
BP-ACTOR-001
BP-FUNC-001
BP-UC-001
BP-UI-001
BP-API-001
BP-DATA-001
BP-NFR-001
BP-TEST-001
```

IDs MUST be generated deterministically from canonical ordering.

The same input MUST produce the same Blueprint IDs.

---

## 46. Blueprint Status

Each Blueprint section SHOULD have a status:

```text
APPROVED
PARTIAL
OPEN
BLOCKED
```

Meaning:

```text
APPROVED:
Fully supported by validated artifacts.

PARTIAL:
Some supported information exists but coverage is incomplete.

OPEN:
Information is legitimately unspecified.

BLOCKED:
A blocking issue prevents approval.
```

---

## 47. Open Issues

Open Issues MAY contain:

- non-blocking missing information
- explicitly unresolved assumptions
- partial coverage
- implementation decisions not yet specified
- non-blocking source problems

Open Issues MUST NOT be converted into approved capabilities.

Example:

```yaml
open_issue:
  id: OI-001
  description: Deployment platform is not specified.
  status: OPEN
```

This does not authorize selecting AWS, Azure, GCP, or another platform.

---

## 48. Post-Generation Audit

After generating the Blueprint, the generator MUST run a second validation
pass over its own output.

For every Blueprint capability:

```text
1. Resolve source ID.
2. Verify source exists.
3. Verify source is approved.
4. Verify trace relationship exists.
5. Compare source capability with Blueprint capability.
6. Verify no new capability was introduced.
7. Verify no semantic drift occurred.
```

For every Blueprint artifact reference:

```text
1. Verify referenced artifact exists.
2. Verify referenced artifact is approved.
3. Verify relationship is valid.
```

For every Blueprint section:

```text
1. Verify all items have provenance.
2. Verify no unsupported item exists.
3. Verify no orphan was promoted.
```

If the post-generation audit fails:

```text
BLUEPRINT GENERATION: FAILED
```

The Blueprint MUST NOT be marked approved.

---

## 49. Scope Diff

The generator MUST calculate:

```text
Approved Capability Set
        ↓
Generated Capability Set
        ↓
Semantic Diff
```

The expected result is:

```text
Unsupported additions = 0
Semantic expansions = 0
Semantic drift = 0
```

A generated Blueprint MAY reorganize or summarize source information.

Therefore, raw textual difference MUST NOT be treated as scope difference.

Scope comparison MUST be capability-semantic.

---

## 50. Scope Diff Categories

The scope diff MUST classify differences as:

```text
UNCHANGED
NORMALIZATION
NARROWER_REPRESENTATION
SCOPE_EXPANSION
SEMANTIC_DRIFT
UNSUPPORTED_ITEM
```

Allowed:

```text
UNCHANGED
NORMALIZATION
NARROWER_REPRESENTATION
```

Blocking:

```text
SCOPE_EXPANSION
SEMANTIC_DRIFT
UNSUPPORTED_ITEM
```

---

## 51. Error Classification

The generator MAY emit:

```text
BLUEPRINT_GENERATION_BLOCKED
SCOPE_EXPANSION
SEMANTIC_DRIFT
HALLUCINATED_ARTIFACT
HALLUCINATED_REQUIREMENT
UNSUPPORTED_CAPABILITY
UNSUPPORTED_IMPLEMENTATION
BROKEN_LINK
ORPHAN_ARTIFACT
MISSING_COVERAGE
MISSING_TEST_COVERAGE
CONTRADICTION
DUPLICATE_ARTIFACT_ID
INVALID_REFERENCE
NON_DETERMINISTIC_OUTPUT
```

Traceability findings MUST be preserved rather than replaced by generic
Blueprint errors.

---

## 52. Output Contract

A successful Blueprint SHOULD follow:

```yaml
blueprint:
  version: "1.0"
  status: APPROVED

  system:
    overview: ...

  scope:
    in_scope: []
    out_of_scope: []
    unknown: []

  actors: []

  functional_requirements: []

  business_rules: []

  use_cases: []

  ui: []

  api: []

  data: []

  nfr: []

  security: []

  tests: []

  traceability:
    status: PASSED

  implementation_boundaries: []

  open_issues: []

  generation:
    generator: blueprint-generator
    version: "1.0"
```

Every populated item MUST have source provenance.

---

## 53. Blocked Output Contract

When generation is blocked:

```yaml
blueprint:
  status: BLOCKED

generation:
  status: BLOCKED
  reason:
    - ...

traceability:
  status: FAILED

gate:
  blueprint_generation: NOT_ALLOWED
```

The generator MUST NOT output an invented partial Blueprint disguised as
approved output.

---

## 54. Generation Algorithm

The complete deterministic algorithm is:

```text
1. Read Traceability result.
2. Run pre-generation gate.
3. If gate fails → BLOCK.
4. Build immutable artifact registry.
5. Canonicalize artifacts.
6. Validate source references.
7. Select approved artifacts.
8. Build capability map.
9. Build source-to-artifact trace map.
10. Generate Blueprint structure.
11. Populate only source-backed content.
12. Preserve source IDs.
13. Generate deterministic Blueprint IDs.
14. Mark partial/unknown states explicitly.
15. Run capability-level scope diff.
16. Run semantic preservation check.
17. Run post-generation audit.
18. If any blocking finding exists → FAILED.
19. Otherwise → APPROVED.
```

The generator MUST NOT generate first and validate later as its only control.

Both pre-generation and post-generation validation are required.

---

## 55. Final Quality Gate

Blueprint generation is allowed ONLY when:

```text
TRACEABILITY
STATUS: PASSED
BLUEPRINT GENERATION: ALLOWED
```

and:

```text
Scope Expansion = 0
Semantic Drift = 0
Hallucinated Scope = 0
Broken References = 0
Unsupported Capabilities = 0
Unsupported Implementations = 0
```

and:

```text
Post-Generation Audit = PASSED
```

Then:

```text
BLUEPRINT GENERATION
STATUS: PASSED
```

---

## 56. Release Criteria

`blueprint-generator v1.0` MUST NOT be released unless:

```text
BP-001 → BP-015 = PASS
```

and:

```text
Scope expansion false positives = 0
Scope expansion false negatives = 0
Silent repair = 0
Hallucinated capability leakage = 0
Trace preservation failures = 0
Semantic drift = 0
Determinism failures = 0
Critical false positives = 0
Critical false negatives = 0
```

---

## 57. Non-Goals

This skill does NOT:

- discover new requirements
- invent product features
- make product decisions
- repair upstream artifacts
- resolve business contradictions
- select technologies without evidence
- design undocumented APIs
- design undocumented database structures
- invent UI
- invent security mechanisms
- invent tests
- expand system scope

---

## 58. Final Principle

```text
TRACEABILITY PROVES WHAT IS VALID
              ↓
BLUEPRINT ORGANIZES WHAT IS VALID
              ↓
IMPLEMENTATION BUILDS WHAT IS VALID
```

Therefore:

```text
THE BLUEPRINT MAY ORGANIZE.
THE BLUEPRINT MAY NORMALIZE.
THE BLUEPRINT MAY NOT INVENT.
```

And the hard boundary is:

```text
NO TRACE
   ↓
NO BLUEPRINT SCOPE

NO SOURCE
   ↓
NO NEW CAPABILITY

NO EVIDENCE
   ↓
NO INVENTION
```
