# Branch Protection Checklist

Configure this in the repository host before treating the framework as production governance.
----
## `main`

- [ ] Require a pull request before merging.
- [ ] Require at least 1 approval.
- [ ] Require CODEOWNERS review where supported.
- [ ] Require status check: `Implementation Traceability`.
- [ ] Dismiss stale approvals when new commits are pushed.
- [ ] Restrict who can push directly.
- [ ] Disable force pushes.
- [ ] Disable branch deletion for protected branches.

## Elevated gates

For projects requiring stronger separation of duties, use two reviewers for:

- implementation readiness;
- implementation verification;
- implementation closure.

Record the actual reviewer identity, approval timestamp, PR, commit SHA, and decision in the repository host's audit history.
