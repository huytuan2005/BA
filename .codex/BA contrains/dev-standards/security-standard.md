# Security Development Standard

**Version:** `v1.0`
**Status:** `ACTIVE`
**Scope:** Security implementation practices

## Purpose

Define security practices that apply when implementing approved system behavior.

## Rules

1. Apply explicitly approved security requirements and applicable project security controls.
2. Protect secrets and credentials according to project policy.
3. Do not expose sensitive information through logs, errors, or documentation where prohibited.
4. Access-control behavior MUST follow approved authorization requirements.
5. Authentication mechanisms MUST NOT be invented when the project has not approved one.
6. Security changes that alter behavior or permissions require explicit approval.
7. Security findings MUST identify the affected approved scope.

## Boundary

This standard governs implementation security practices. It does not authorize invention of JWT, OAuth, MFA, session policy, RBAC, encryption, or other mechanisms unless explicitly established by applicable evidence or standard policy.
