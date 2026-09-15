# Dependency Development Standard

**Version:** `v1.0`
**Status:** `ACTIVE`
**Scope:** External and internal software dependencies

## Purpose

Control dependencies introduced during implementation.

## Rules

1. Dependencies MUST be explicitly approved or required by an applicable project standard.
2. A library or service MUST NOT be added merely because it is convenient or popular.
3. Dependency versioning MUST follow the project's package-management conventions.
4. Security and licensing review MUST follow applicable project policy when required.
5. Unused dependencies SHOULD be removed.
6. Dependency upgrades that may affect behavior require impact review.
7. A dependency MUST NOT be used to introduce unsupported business behavior.

## Boundary

This standard governs dependency management. It does not authorize new product scope.
