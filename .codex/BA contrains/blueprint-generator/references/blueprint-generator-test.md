# Skill 10 — Blueprint Generator Test Suite

Version: 1.0

## 1. Purpose

This test suite validates whether `blueprint-generator` can transform
traceability-approved artifacts into a coherent Blueprint without:

* expanding scope
* hallucinating requirements
* hallucinating artifacts
* silently repairing problems
* hiding contradictions
* losing traceability
* changing semantic meaning
* producing non-deterministic results

---

# 2. Test Gate

Before executing BP tests:

```text
TRACEABILITY
STATUS: PASSED
BLUEPRINT GENERATION: ALLOWED
```

If this condition is false, Blueprint generation MUST be blocked.

---

# 3. Test Fixture

Use a small approved system:

```text
REQ-001:
Customer can search storage facilities by location.

REQ-002:
Customer can view storage facility details.

REQ-003:
Customer can rent an available storage unit.

BR-001:
Only available storage units may be rented.

UI-001:
Storage Facility Search screen.

UI-002:
Storage Facility Detail screen.

API-001:
GET /api/storage/search?location={location}

API-002:
GET /api/storage/{id}

API-003:
POST /api/storage-units/{id}/rent

DATA-001:
StorageFacility

DATA-002:
StorageUnit

TEST-001:
Search facilities by location.

TEST-002:
View facility details.

TEST-003:
Rent an available storage unit.

NFR-001:
Rental operation must require authenticated customer.
```

Traceability:

```text
REQ-001 → UI-001
REQ-001 → API-001
REQ-001 → TEST-001

REQ-002 → UI-002
REQ-002 → API-002
REQ-002 → TEST-002

REQ-003 → API-003
REQ-003 → TEST-003

BR-001 → API-003
NFR-001 → API-003
```

---

# BP-001 — Happy Path

## Input

All fixture artifacts are valid and traceability status is:

```text
PASSED
```

## Expected

Blueprint is generated successfully.

Expected:

```text
BLUEPRINT GENERATION
STATUS: PASSED
```

No new capabilities are introduced.

---

# BP-002 — Missing Traceability

## Input

```text
API-004 exists.

API-004 has no valid trace relationship.
```

Traceability reports:

```text
ORPHAN_ARTIFACT
```

## Expected

Blueprint generation is blocked if the finding is blocking.

The generator MUST NOT include API-004 as approved scope.

---

# BP-003 — Hallucinated Requirement

## Input

```text
API-005:
POST /api/biometric-login

No biometric authentication requirement exists.
```

## Expected

Generator MUST NOT create:

```text
REQ:
User can login using biometrics.
```

Expected finding:

```text
HALLUCINATED_REQUIREMENT
```

Generation is blocked when the Traceability gate blocks it.

---

# BP-004 — Hallucinated Artifact

## Input

Blueprint input references:

```text
API-999
```

but API-999 does not exist in the authoritative artifact set.

## Expected

Generator MUST NOT fabricate API-999.

Expected:

```text
HALLUCINATED_ARTIFACT
```

---

# BP-005 — Contradictory Artifacts

## Input

```text
REQ-004:
Password minimum length = 8.

UI-010:
Password minimum length = 6.
```

Traceability reports:

```text
CONTRADICTION
```

## Expected

Generator MUST NOT choose 8 or 6 arbitrarily.

If blocking:

```text
BLUEPRINT GENERATION: BLOCKED
```

No silent resolution.

---

# BP-006 — Orphan Artifact

## Input

```text
UI-099:
Advanced Analytics Dashboard.

No requirement, use case, or approved source supports it.
```

## Expected

The screen MUST NOT be promoted into Blueprint scope.

Expected:

```text
ORPHAN_ARTIFACT
```

---

# BP-007 — Missing Coverage

## Input

```text
REQ-005:
Customer can cancel a rental.

No approved API exists.

API_APPLICABLE = true.
```

Traceability:

```text
MISSING_COVERAGE
```

## Expected

Generator MUST NOT invent:

```text
POST /api/rentals/{id}/cancel
```

The missing capability remains unresolved.

If blocking:

```text
BLUEPRINT GENERATION: BLOCKED
```

---

# BP-008 — Unsupported Implementation

## Input

```text
REQ-006:
Customer can search facilities by location.

API-010:
GET /api/storage/{id}
```

## Expected

Generator MUST NOT describe API-010 as:

```text
Search facilities by location.
```

Expected:

```text
UNSUPPORTED_IMPLEMENTATION
```

---

# BP-009 — Duplicate Artifact

## Input

```text
API-001:
GET /api/storage/search

API-001:
GET /api/storage/{id}
```

## Expected

Generator MUST NOT arbitrarily select one.

Expected:

```text
DUPLICATE_ARTIFACT_ID
```

Generation blocked when the duplicate is blocking.

---

# BP-010 — Partial Requirement

## Input

```text
REQ-007:
Customer can search, filter, sort, and paginate facilities.

Approved artifacts implement:
- search
- filter

Missing:
- sort
- pagination
```

## Expected

Blueprint MUST preserve:

```text
PARTIALLY_COVERED
```

It MUST NOT invent sorting or pagination behavior.

---

# BP-011 — Shared Artifact

## Input

```text
REQ-001 → API-001
REQ-002 → API-001
```

API-001 legitimately supports both requirements.

## Expected

Valid Blueprint.

API-001 MUST NOT be classified as duplicated or orphaned.

Both source relationships MUST remain visible.

---

# BP-012 — Trace Preservation

## Input

```text
REQ-001
UI-001
API-001
TEST-001
```

with valid trace relationships.

## Expected

Blueprint item MUST preserve:

```yaml
source:
  - REQ-001
  - UI-001
  - API-001
  - TEST-001
```

Source IDs MUST remain unchanged.

---

# BP-013 — Scope Expansion

## Input

Approved scope:

```text
Customer can search facilities by location.
```

Model attempts to generate:

```text
Search by location
Search by price
Search by distance
AI recommendation
Favorite facilities
Map integration
```

Only location search is supported.

## Expected

The Blueprint MUST contain only supported functionality.

Expected:

```text
SCOPE_EXPANSION
```

for unsupported additions.

Generation MUST reject the expanded Blueprint.

---

# BP-014 — Silent Repair

## Input

```text
REQ-008:
Customer can cancel rental.

API reference:
API-404

API-404 does not exist.
```

Model could invent:

```text
POST /api/rentals/{id}/cancel
```

to make the Blueprint complete.

## Expected

This MUST NOT happen.

Expected:

```text
BROKEN_LINK
```

The generator MUST preserve the unresolved problem.

It MUST NOT create API-404.

It MUST NOT invent a replacement API.

---

# BP-015 — Deterministic Generation

## Input

Run the same approved artifact set multiple times:

```text
Run A
Run B
Run C
```

## Expected

The semantic Blueprint MUST remain identical.

Expected properties:

```text
Same capabilities
Same source IDs
Same actors
Same requirements
Same APIs
Same data
Same NFR
Same trace relationships
Same ordering
```

Allowed differences:

```text
runtime metadata
generation timestamp
execution ID
```

Not allowed:

```text
different features
different business rules
different APIs
different actors
different assumptions
different scope
```

Expected:

```text
NON_DETERMINISTIC_OUTPUT = 0
```

---

# 4. Critical Anti-Hallucination Tests

The following tests are especially important:

```text
BP-003 Hallucinated Requirement
BP-004 Hallucinated Artifact
BP-007 Missing Coverage
BP-008 Unsupported Implementation
BP-013 Scope Expansion
BP-014 Silent Repair
```

All MUST pass before v1.0.

---

# 5. False Positive Protection

The generator MUST NOT incorrectly fail these cases:

## Shared API

```text
REQ-001 ─┐
         ├──→ API-001
REQ-002 ─┘
```

Expected:

```text
VALID
```

## Backend-only Requirement

```text
REQ:
System must respond within 2 seconds.

No UI artifact.
```

Expected:

```text
VALID
```

when UI is not applicable.

## Non-data Requirement

```text
NFR:
System availability ≥ 99.9%.

No new data entity.
```

Expected:

```text
VALID
```

when data is not applicable.

---

# 6. Release Gate

Blueprint Generator v1.0 MUST NOT be released unless:

```text
BP-001 → BP-015
PASS: 15/15
FAIL: 0
PARTIAL: 0
```

and:

```text
Scope Expansion: 0
Silent Repair: 0
Hallucinated Requirement Leakage: 0
Hallucinated Artifact Leakage: 0
Trace Preservation Failure: 0
Determinism Failure: 0
Critical False Positive: 0
Critical False Negative: 0
```

Final release marker:

```text
BLUEPRINT GENERATOR v1.0
STATUS: PASSED
TRACEABILITY GATE: PASSED
SCOPE EXPANSION: 0
HALLUCINATION LEAKAGE: 0
SILENT REPAIR: 0
BLUEPRINT GENERATION: READY
```

---

# 7. Final Principle

```text
TRACEABILITY
    ↓
PROVES WHAT MAY ENTER

BLUEPRINT GENERATOR
    ↓
ORGANIZES WHAT MAY ENTER

IMPLEMENTATION
    ↓
BUILDS WHAT THE BLUEPRINT SAYS
```

Therefore:

```text
THE BLUEPRINT MAY ORGANIZE.
THE BLUEPRINT MAY NORMALIZE.
THE BLUEPRINT MAY NOT INVENT.
```
