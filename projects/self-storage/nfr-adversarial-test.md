# Self-Storage — NFR Generator Adversarial Test

## Purpose

Stress-test the generator against words and domain concepts that commonly
cause hallucinated NFRs.

## Adversarial evidence

Treat the following as source-like statements:

- Facility Manager can `manage` units.
- Business Operations Manager can `monitor` revenue.
- A customer may rent `one or more` storage units.
- Units have a `status`.
- Customers can make `payment`.
- The actor is a `customer`.
- The system manages user `accounts`.
- The system contains customer, facility, unit, reservation, contract,
  payment, and report concepts.
- The system is expected to be useful and professional. No measurable target
  is provided.

## Forbidden automatic derivations

The generator must NOT create NFRs such as:

- "The system shall respond within 2 seconds."
- "The system shall support 1,000 concurrent users."
- "The system shall have 99.9% availability."
- "The system shall use JWT/OAuth/MFA."
- "The system shall encrypt payment data."
- "The system shall use TLS."
- "The system shall enforce a password policy."
- "The system shall provide WCAG AA/AAA."
- "The system shall retain audit logs for 7 years."
- "The system shall provide 24/7 service."
- "The system shall guarantee payment security."
- "The system shall provide 99.99% data integrity."
- "The system shall use PostgreSQL/Redis/Kafka/etc."

## Expected checks

PASS if:
- `manage` remains functional/ambiguous and does not become an NFR.
- `monitor` remains functional/ambiguous and does not become an NFR.
- `one or more` does not become a scalability target.
- `status` does not become a reliability/availability NFR.
- `payment` does not become a security/compliance NFR.
- `customer` does not create usability/security/privacy NFRs.
- `accounts` does not create authentication/security controls.
- business objects do not create NFRs.
- "professional" does not become a measurable usability target.
- no numeric target, SLA, security mechanism, compliance framework, or
  technology is invented.
