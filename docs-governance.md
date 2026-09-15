# Repository Governance

This repository treats the Skills as reusable lifecycle logic and Git/CI as the external governance layer.

## 1. Ownership

`CODEOWNERS` assigns review responsibility by lifecycle area. Replace placeholder teams with real GitHub users or teams before using this repository in a real project.

## 2. Branch protection

Protect `main` (or the release branch used by the project) with:

- pull request required;
- at least 1 required approval for ordinary artifacts;
- 2 or more approvals for readiness, verification, or closure where separation of duties is required;
- required status check: `Implementation Traceability`;
- dismissal of stale approvals after new commits;
- direct pushes disabled for ordinary contributors;
- force-push disabled;
- optional CODEOWNERS review required.

Branch protection must be configured in GitHub/GitLab repository settings. This file documents the intended policy; it does not claim that remote settings are already enabled.

## 3. Separation of duties

Recommended minimum separation for a real project:

```text
BA → produces / maintains BA artifacts
PM/PO → approves scope and readiness decisions
Developer → implements approved scope
QA → verifies implementation
PM/PO / Client → accepts or rejects closure where applicable
```

The person who wrote the implementation should not be the sole verifier of the same implementation.

## 4. Automated traceability

`python scripts/implementation_traceability_check.py projects/<project>` performs an objective implementation-boundary check. CI should fail when the script returns a non-zero exit code.

The checker does not decide business meaning. It verifies IDs, mappings, and concrete artifact references that can be objectively inspected.

## 5. Human approval

Use the PR templates under `.github/PULL_REQUEST_TEMPLATE/` for readiness, plan validation, verification, and closure reviews.

A checked box is not the approval itself. The GitHub/GitLab reviewer identity and approval event are the authoritative human-governance evidence.

## 6. Locked Skills

`v1.0 LOCKED` means the Skill contract is frozen. Git governance must not silently modify the Skill contract. Changes to locked Skills require a new version and regression evidence.
