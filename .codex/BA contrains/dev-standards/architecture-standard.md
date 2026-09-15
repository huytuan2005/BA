# Architecture Development Standard

**Version:** `v1.0`
**Status:** `ACTIVE`
**Scope:** Application architecture and structural implementation conventions

## Purpose

Provide rules for implementing architecture that has already been approved.

## Rules

1. Implement the approved architecture without silently replacing it.
2. Architectural layers or components MUST be used only when they are part of the approved architecture or explicitly required by this standard.
3. New architectural patterns, services, queues, gateways, caches, or distributed components MUST NOT be introduced solely because they are common practice.
4. Responsibilities between approved components MUST remain consistent with the approved architecture.
5. Cross-component dependencies MUST be explicit.
6. Architectural changes require explicit approval and impact review.

## Boundary

This standard does not select an architecture for a project when the project has not approved one.
