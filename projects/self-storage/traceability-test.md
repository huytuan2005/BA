# Traceability Test Suite

## 1. Purpose

This test suite validates **Skill 9 — Traceability** before releasing v1.0.

The tests are designed to verify that Traceability can:

* Build valid requirement → artifact relationships.
* Detect orphan artifacts.
* Detect unsupported artifacts.
* Detect broken traceability links.
* Detect hallucinated artifacts.
* Detect missing requirement coverage.
* Detect contradictions between artifacts.
* Distinguish valid relationships from relationships that only appear plausible.

The goal is not only to verify the **happy path**, but to deliberately inject invalid artifacts and broken relationships so that Skill 9 is forced to expose its weaknesses.

---

# 2. Test Input Model

The tests use the following simplified artifact types:

```text
REQ       = Requirement
UC        = Use Case
UI        = UI Screen / Component
API       = API Endpoint
DATA      = Data Model
NFR       = Non-Functional Requirement
TEST      = Test Case
```

Expected traceability direction:

```text
REQ
 ├──> UC
 ├──> UI
 ├──> API
 ├──> DATA
 ├──> NFR
 └──> TEST
```

A downstream artifact must have a valid upstream justification.

---

# 3. Test Case Matrix

| ID     | Category         | Scenario                                                                | Expected Result |
| ------ | ---------------- | ----------------------------------------------------------------------- | --------------- |
| TR-001 | Happy Path       | Requirement has valid UC/UI/API/DATA/TEST links                         | PASS            |
| TR-002 | Happy Path       | One requirement maps to multiple artifacts                              | PASS            |
| TR-003 | Happy Path       | Multiple requirements map to one shared artifact                        | PASS            |
| TR-004 | Orphan           | UI exists without any requirement                                       | FAIL            |
| TR-005 | Orphan           | API exists without any requirement                                      | FAIL            |
| TR-006 | Orphan           | Data model exists without any requirement                               | FAIL            |
| TR-007 | Unsupported      | Artifact claims support for a requirement but evidence is absent        | FAIL            |
| TR-008 | Unsupported      | API is linked to requirement but endpoint does not implement it         | FAIL            |
| TR-009 | Broken Link      | Traceability references a non-existent artifact ID                      | FAIL            |
| TR-010 | Broken Link      | Artifact references deleted requirement                                 | FAIL            |
| TR-011 | Hallucination    | Artifact exists only in traceability matrix, not source artifacts       | FAIL            |
| TR-012 | Hallucination    | Requirement claims a feature that is not present in source requirements | FAIL            |
| TR-013 | Missing Coverage | Requirement has no downstream implementation artifact                   | FAIL            |
| TR-014 | Missing Coverage | Requirement has implementation but no test coverage                     | FAIL            |
| TR-015 | Contradiction    | Requirement says email login, UI says username login                    | FAIL            |
| TR-016 | Contradiction    | API requires `email`, UI sends `username`                               | FAIL            |
| TR-017 | Contradiction    | Data model marks field optional while API requires it                   | FAIL            |
| TR-018 | Contradiction    | Two artifacts claim incompatible business rules                         | FAIL            |
| TR-019 | Mixed            | Valid + orphan + broken links in same project                           | PARTIAL FAIL    |
| TR-020 | Mixed            | Valid artifacts plus hallucinated artifact                              | FAIL            |

---

# 4. Happy Path Tests

## TR-001 — Complete Requirement Trace

### Input

```text
REQ-001:
Customer can log in using email and password.

UC-001:
Login

UI-001:
Login Screen

API-001:
POST /api/auth/login

DATA-001:
User

TEST-001:
Verify successful login with valid email/password
```

### Traceability

```text
REQ-001
 ├── UC-001
 ├── UI-001
 ├── API-001
 ├── DATA-001
 └── TEST-001
```

### Expected

```text
PASS
```

### Validation

The trace is valid because:

* UC implements the requirement.
* UI provides the required interaction.
* API supports authentication.
* DATA contains the user information required by authentication.
* TEST validates the requirement.

---

## TR-002 — One Requirement → Multiple Artifacts

### Input

```text
REQ-002:
Customer can reset a forgotten password.

UC-002:
Forgot Password

UI-002:
Forgot Password Screen

API-002:
POST /api/auth/forgot-password

API-003:
POST /api/auth/reset-password

TEST-002:
Forgot password flow
```

### Expected

```text
PASS
```

A requirement may legitimately produce multiple downstream artifacts.

---

## TR-003 — Shared Artifact

### Input

```text
REQ-003:
Customer can view their profile.

REQ-004:
Customer can update their profile.

UI-003:
Profile Screen
```

### Traceability

```text
REQ-003 ──┐
          ├──> UI-003
REQ-004 ──┘
```

### Expected

```text
PASS
```

A shared artifact is not automatically an orphan.

---

# 5. Orphan Tests

## TR-004 — Orphan UI

### Input

```text
REQ-001:
Customer can log in.

UI-001:
Admin Analytics Dashboard
```

No requirement references `UI-001`.

### Expected

```text
FAIL

ORPHAN_ARTIFACT:
UI-001
Reason:
No upstream requirement supports this artifact.
```

---

## TR-005 — Orphan API

### Input

```text
REQ-001:
Customer can log in.

API-001:
POST /api/payment/refund
```

### Expected

```text
FAIL

ORPHAN_ARTIFACT:
API-001
```

The existence of a technically valid API does not justify its presence.

---

## TR-006 — Orphan Data Model

### Input

```text
REQ-001:
Customer can log in.

DATA-001:
VehicleMaintenanceRecord
```

No requirement concerns vehicle maintenance.

### Expected

```text
FAIL

ORPHAN_ARTIFACT:
DATA-001
```

---

# 6. Unsupported Artifact Tests

## TR-007 — Claimed Support Without Evidence

### Input

```text
REQ-010:
Customer can log in using email and password.

API-010:
POST /api/auth/login

Description:
Supports login using email, password, OTP and biometric authentication.
```

Source requirement only specifies email/password.

### Expected

```text
FAIL

UNSUPPORTED_CAPABILITY:
OTP authentication

UNSUPPORTED_CAPABILITY:
Biometric authentication
```

Traceability must not treat additional undocumented capabilities as supported merely because they appear in an artifact description.

---

## TR-008 — API Does Not Implement Requirement

### Requirement

```text
REQ-011:
Customer can search storage facilities by location.
```

### API

```text
API-011:
GET /api/storage/{id}
```

This endpoint retrieves a single storage facility but does not provide search functionality.

### Expected

```text
FAIL

UNSUPPORTED_IMPLEMENTATION:
API-011 does not implement REQ-011.
```

---

# 7. Broken Link Tests

## TR-009 — Non-existent Artifact ID

### Traceability

```text
REQ-001
 ├── UI-001
 ├── API-001
 └── API-999
```

But `API-999` does not exist.

### Expected

```text
FAIL

BROKEN_LINK:
REQ-001 -> API-999

Reason:
Target artifact does not exist.
```

---

## TR-010 — Deleted Requirement

### Artifact

```text
UI-010:
Payment Screen

Trace:
Supports REQ-999
```

But `REQ-999` does not exist.

### Expected

```text
FAIL

BROKEN_LINK:
UI-010 -> REQ-999
```

---

# 8. Hallucination Tests

## TR-011 — Artifact Exists Only in Traceability

### Source artifacts

```text
REQ-001
REQ-002

UI-001
API-001
```

### Traceability matrix

```text
REQ-001 -> UI-001
REQ-001 -> API-001
REQ-002 -> UI-002
```

`UI-002` does not exist anywhere else.

### Expected

```text
FAIL

HALLUCINATED_ARTIFACT:
UI-002
```

Traceability must not create an artifact simply because it appears in a mapping.

---

## TR-012 — Hallucinated Requirement

### Source requirements

```text
REQ-001:
Customer can log in.

REQ-002:
Customer can register.
```

### Artifact

```text
UI-003:
Biometric Login Screen
```

Artifact description:

```text
Implements biometric authentication requirement.
```

No biometric requirement exists.

### Expected

```text
FAIL

HALLUCINATED_REQUIREMENT:
Biometric authentication requirement
```

---

# 9. Missing Coverage Tests

## TR-013 — Requirement Has No Implementation

### Input

```text
REQ-020:
Customer can cancel a storage reservation.
```

No UC, UI, API, DATA or TEST references the requirement.

### Expected

```text
FAIL

MISSING_COVERAGE:
REQ-020

Missing:
UC
UI
API
TEST
```

---

## TR-014 — Requirement Has Implementation but No Test

### Input

```text
REQ-021:
Customer can update their profile.

UC-021
UI-021
API-021
DATA-021
```

No test case.

### Expected

```text
FAIL

MISSING_TEST_COVERAGE:
REQ-021
```

The implementation trace may be valid, but verification coverage is incomplete.

---

# 10. Contradiction Tests

## TR-015 — Requirement vs UI

### Requirement

```text
REQ-030:
Customer logs in using email and password.
```

### UI

```text
UI-030:
Login form fields:
- Username
- Password
```

### Expected

```text
FAIL

CONTRADICTION:
REQ-030 requires email authentication.
UI-030 provides username authentication.
```

---

## TR-016 — UI vs API

### UI

```text
UI-031:
Login fields:
- username
- password
```

### API

```text
API-031:
POST /api/auth/login

Request:
{
  "email": "...",
  "password": "..."
}
```

### Expected

```text
FAIL

CONTRADICTION:
UI sends username.
API requires email.
```

---

## TR-017 — Data Model vs API

### DATA

```text
User.email:
nullable = true
```

### API

```text
POST /api/users

email:
required = true
```

### Expected

```text
FAIL

CONTRADICTION:
DATA-032 allows email to be null.
API-032 requires email.
```

---

## TR-018 — Business Rule Contradiction

### Requirement

```text
REQ-033:
A customer can reserve a maximum of 3 storage units.
```

### API

```text
POST /api/reservations

Validation:
maximumUnits = 5
```

### Expected

```text
FAIL

CONTRADICTION:
REQ-033 maximum = 3.
API-033 maximum = 5.
```

---

# 11. Mixed Failure Test

## TR-019 — Multiple Problems in One Project

### Input

```text
REQ-040:
Customer can rent a storage unit.

REQ-041:
Customer can cancel a rental.
```

Artifacts:

```text
UC-040
UI-040
API-040
UI-999
API-041
```

Problems:

```text
UI-999 has no requirement.

API-041 exists but cancellation requirement is not implemented.

REQ-041 has no TEST.

Trace references API-888 which does not exist.
```

### Expected

Traceability must report all independently detectable issues:

```text
ORPHAN_ARTIFACT:
UI-999

UNSUPPORTED_IMPLEMENTATION:
API-041

MISSING_TEST_COVERAGE:
REQ-041

BROKEN_LINK:
REQ-040 -> API-888
```

The skill must not stop after detecting the first error.

---

# 12. Hallucination + Valid Artifact Test

## TR-020 — Valid Project With One Fabricated Artifact

### Input

```text
REQ-050:
Customer can view storage facilities.

UI-050:
Storage Listing

API-050:
GET /api/storage
```

Additional artifact:

```text
API-051:
GET /api/storage/recommendations
```

No requirement supports recommendations.

### Expected

```text
PASS:
REQ-050 -> UI-050
REQ-050 -> API-050

FAIL:
API-051

Reason:
No requirement supports recommendation functionality.
```

The skill must preserve valid traceability while isolating the invalid artifact.

---

# 13. Expected Diagnostic Categories

Skill 9 should normalize findings into the following categories:

```text
ORPHAN_ARTIFACT
UNSUPPORTED_ARTIFACT
BROKEN_LINK
HALLUCINATED_ARTIFACT
HALLUCINATED_REQUIREMENT
MISSING_COVERAGE
MISSING_TEST_COVERAGE
CONTRADICTION
```

Each finding should contain:

```text
ID
category
severity
source_artifact
target_artifact
reason
evidence
recommendation
```

Example:

```yaml
id: TR-009
category: BROKEN_LINK
severity: ERROR

source_artifact: REQ-001
target_artifact: API-999

reason: >
  REQ-001 references API-999,
  but API-999 does not exist in the artifact set.

recommendation: >
  Remove the trace or create the missing artifact
  from an explicitly supported requirement.
```

---

# 14. Severity Rules

```text
ERROR:
- Broken link
- Hallucinated artifact
- Hallucinated requirement
- Contradiction
- Unsupported artifact
- Missing requirement coverage

WARNING:
- Missing test coverage
- Suspicious weak trace
- Artifact with insufficient evidence

INFO:
- Shared artifact
- Multiple valid downstream mappings
```

---

# 15. False Positive Tests

Traceability must NOT incorrectly report the following as errors:

### FP-001 — Shared UI

```text
REQ-001 -> UI-001
REQ-002 -> UI-001
```

Valid.

### FP-002 — Shared API

```text
REQ-001 -> API-001
REQ-002 -> API-001
```

Valid if the API genuinely supports both requirements.

### FP-003 — Requirement Without Data Model

```text
REQ-003 -> UI-003
REQ-003 -> API-003
REQ-003 -> TEST-003
```

No DATA artifact is necessarily required.

### FP-004 — Requirement Without UI

```text
REQ-004 -> API-004
REQ-004 -> TEST-004
```

Valid for a backend-only requirement.

### FP-005 — Internal implementation artifact

An internal technical artifact may not directly map to a requirement if its parent artifact already establishes the trace.

The skill must avoid requiring artificial one-to-one mappings.

---

# 16. Acceptance Criteria

Skill 9 is ready for v1.0 only if it can:

```text
[ ] Detect valid happy-path traceability.

[ ] Detect orphan artifacts.

[ ] Detect unsupported artifacts.

[ ] Detect broken links.

[ ] Detect hallucinated artifacts.

[ ] Detect hallucinated requirements.

[ ] Detect missing requirement coverage.

[ ] Detect missing test coverage.

[ ] Detect contradictions.

[ ] Report multiple failures in one run.

[ ] Preserve valid traces when invalid traces also exist.

[ ] Avoid false positives for shared artifacts.

[ ] Avoid assuming every requirement needs UI.

[ ] Avoid assuming every requirement needs DATA.

[ ] Avoid creating missing artifacts automatically.

[ ] Provide evidence for every reported finding.

[ ] Distinguish "missing evidence" from "proven contradiction".

[ ] Produce deterministic diagnostic categories.

[ ] Never treat an artifact's own claim as sufficient proof of traceability.
```

---

# 17. Final Release Gate

Run:

```text
TR-001 → TR-020
```

Release decision:

```text
PASS
```

only when:

```text
All mandatory detection tests pass
AND
No critical false positives remain
AND
Every finding contains evidence
AND
Hallucinated artifacts are never silently accepted
AND
Broken traceability cannot propagate into downstream generation
```

If any of the following remain undetected:

```text
BROKEN_LINK
HALLUCINATED_ARTIFACT
MISSING_COVERAGE
CONTRADICTION
```

then:

```text
Skill 9 v1.0 = NOT READY
```

The next step is to fix the Skill 9 logic and rerun the failing tests before creating `blueprint-generator`.
