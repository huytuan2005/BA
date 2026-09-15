# Development Standards

**Version:** `v1.0`
**Status:** `ACTIVE`

## Purpose

This file defines the governance model for development standards used by implementation-oriented skills.

Development standards constrain implementation practice. They do not create product requirements or business behavior unless an individual standard explicitly states that such behavior is required.

## Applicability

Standards may apply at these scopes:

```text
Global / Default
    ↓
Root / Organization
    ↓
Project
    ↓
Project-specific implementation scope
```

A more specific scope overrides a less specific scope only when the governing policy explicitly defines that precedence.

## Inheritance

If an applicable child scope does not define a value, the applicable parent value is inherited.

If two applicable standards conflict and no explicit precedence rule resolves the conflict, the decision remains `CONTRADICTION` and implementation MUST NOT silently choose one.

## Standard Boundaries

Applicable standards may govern:

- API/interface conventions;
- architecture conventions;
- coding conventions;
- data handling conventions;
- dependency management;
- documentation;
- error handling and logging;
- quality practices;
- security practices;
- testing practices.

A standard establishes only what it explicitly states.

For example, a coding standard may require a naming convention without establishing a database engine, API style, authentication mechanism, or deployment architecture.

## Precedence

Explicit project decisions and approved implementation decisions take precedence over general development conventions where the governing project policy says so.

Where precedence is undefined, the conflict MUST remain explicit.

## Evidence Rule

A development standard is authoritative only within its declared scope.

A standard MUST NOT be used to manufacture:

- product behavior;
- business rules;
- requirements;
- APIs not otherwise required;
- database structures not otherwise required;
- architecture not otherwise required;
- security behavior not otherwise required;
- testing targets not otherwise required.

## Change Control

Changes to a locked or active standard MUST be versioned and reviewed for impact on downstream implementation skills.
