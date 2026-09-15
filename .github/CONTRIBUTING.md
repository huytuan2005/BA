# Contribution and Review Rules

This framework uses Git as the governance evidence layer around the locked Skills.

## Lifecycle reviewers

| Area | Primary reviewer | Suggested secondary reviewer |
|---|---|---|
| Requirements / Process / Functional | BA | PM/PO |
| Implementation Readiness | PM/PO | BA or Tech Lead |
| Implementation | Developer / Tech Lead | Project owner |
| Plan Validation | Tech Lead | PM/PO |
| Verification | QA | Tech Lead |
| Closure | PM/PO | QA / Client representative |

The exact people must be configured through `CODEOWNERS` and repository branch protection.

## Non-negotiable rule

The author of an implementation should not be the sole verifier of that same implementation.

## Evidence

A PR should point to source evidence, traceability mappings, automated checks, and the gate decision it is requesting. A PR checkbox is not proof of approval; the repository host's recorded review event is the human approval evidence.
