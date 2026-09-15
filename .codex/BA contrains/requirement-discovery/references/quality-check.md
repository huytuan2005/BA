# Requirement Discovery Quality Check

Use this only during validation.

For each candidate FR:
- Has a real source?
- Has an actor?
- Describes an observable capability?
- Avoids implementation detail?
- Avoids hidden assumptions?
- Is the wording sufficiently atomic?
- Has a stable unique ID?
- Has confidence assigned?
- Can a reviewer locate the source?

Global checks:
- Every source capability is covered or explicitly marked uncovered.
- No unsupported NFRs were created.
- Ambiguous terms such as `manage`, `monitor`, `support`, `handle`, `appropriate`, `available`, and `overdue` are clarified or listed as open questions.
- Business rules are not invented from common domain practice.
