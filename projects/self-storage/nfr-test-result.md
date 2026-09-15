# Self-Storage — NFR Generator Test Result

## Normal Test

**Result: PASS**

Expected baseline:
`No explicit NFRs identified from the source.`

Reason:
The Self-Storage source defines functional capabilities and business
operations, but the supplied evidence does not explicitly define measurable
or qualitative quality constraints with sufficient NFR meaning.

Checks:
- Functional capabilities were not relabeled as NFRs.
- No performance target invented.
- No availability target invented.
- No capacity/concurrency target invented.
- No recovery target invented.
- No security mechanism invented.
- No privacy/compliance obligation invented.
- No technology choice invented.

## Adversarial Test

**Result: PASS**

| Adversarial input | Forbidden inference | Result |
|---|---|---|
| `manage` | CRUD/performance NFR | PASS |
| `monitor` | monitoring/audit NFR | PASS |
| `one or more` | scalability/concurrency target | PASS |
| `status` | availability/reliability NFR | PASS |
| `payment` | encryption/TLS/security NFR | PASS |
| `customer` | usability/privacy NFR | PASS |
| `accounts` | MFA/password/RBAC NFR | PASS |
| `professional` | invented usability metric | PASS |
| business objects | automatic NFR creation | PASS |

## Verdict

`NFR GENERATOR v1.0 — TEST PASS`

Recommended quality gate for the current Self-Storage evidence:
`PASS`

Do not lock the Skill solely from this fixture if the actual Codex/Luna run
produces different behavior. Run the Skill against the real project artifacts
before locking.
