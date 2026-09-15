# BA Framework

This repository is a lifecycle governance framework for software projects.

For a concrete project, place client inputs under `projects/<project>/input/` and run the Skills in sequence. The Self-Storage project is the reference end-to-end example and now contains both a blocked full-product readiness record and an explicitly approved, implemented, verified, and closed MVP release scope.

## Self-Storage E2E example

1. `pm-po/client-decision-round2.md` resolves the prior implementation blockers for `MVP-SS-01`.
2. `implementation-readiness/implementation-readiness-r2.md` authorizes only that MVP.
3. `implementation-plan/implementation-plan-r2.md` and `implementation-validator/implementation-plan-validation-r2.md` prepare and validate execution.
4. `implementation-traceability/implementation-traceability-matrix.md` traces concrete code/test artifacts to approved implementation items.
5. `implementation/`, `backend/`, and `frontend/` contain the actual full-stack MVP implementation.
6. `implementation-test/api-smoke-test.js` provides an executable API/database acceptance check.
7. `implementation-verification/verification-result-r2.md` records verification evidence.
8. `implementation-closure/closure-result-r2.md` closes the MVP scope.

The framework does not silently promote unresolved full-product capabilities into scope. The full Self-Storage product remains open beyond MVP-SS-01.


## Using the repository as a real governance system

The Skills remain the lifecycle logic. Git, CI, and human review provide the enforcement and audit layer around them.

### For a new project

1. Create `projects/<project>/` and place client evidence in the project's input area.
2. Run the BA Skills in sequence and keep outputs inside that project's folders.
3. Do not modify `v1.0 LOCKED` Skills to solve project-specific issues. Record project-specific evidence or decisions in `projects/<project>/`.
4. At each lifecycle gate, open a pull request using the matching template under `.github/PULL_REQUEST_TEMPLATE/`.
5. Let CI run `scripts/run_all_traceability.py`. A failing traceability check blocks merge when repository branch protection requires that status check.
6. Require real human reviewers for the gate. Configure the actual reviewers/teams in `.github/CODEOWNERS`.

### What is enforced automatically

`implementation_traceability_check.py` objectively checks implementation IDs, matrix coverage, explicit upstream references, and concrete repository artifact paths. It does not infer business meaning.

### What still requires repository configuration

Branch protection, required reviewers, CODEOWNERS enforcement, and reviewer separation are repository-host settings. This repository includes the intended policy and templates, but it cannot truthfully claim those remote controls are enabled until an administrator configures them. See `.github/branch-protection.md` and `docs-governance.md`.

### Separation of duties

Use BA → PM/PO → Developer → QA → PM/PO/Client as the default control path. The person who writes implementation should not be the sole verifier.
