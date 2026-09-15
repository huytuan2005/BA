# Coding Development Standard

**Version:** `v1.0`
**Status:** `ACTIVE`
**Scope:** Source-code quality and consistency

## Purpose

Define baseline coding practices without creating product behavior.

## Rules

1. Follow the project's approved language and framework choices.
2. Use consistent naming for variables, functions, types, modules, and files.
3. Keep functions and modules focused on their approved responsibility.
4. Avoid speculative abstractions that are not required by approved scope.
5. Do not duplicate existing approved logic when reuse is appropriate and already supported by the architecture.
6. Handle errors explicitly according to the approved error-handling conventions.
7. Keep comments and documentation factual and synchronized with implemented behavior.
8. Do not hide unsupported business rules inside helper code, validators, defaults, or constants.
9. Changes MUST remain traceable to their approved implementation item.

## Boundary

Coding conventions control how approved work is written. They do not decide what the product should do.
