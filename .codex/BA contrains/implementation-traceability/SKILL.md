# Skill: implementation-traceability

**Version:** `v0.1`
**Status:** `DRAFT`

## Purpose

Maintain explicit traceability between approved implementation items and the implementation artifacts derived from them.

This skill focuses on the implementation boundary. It does not replace the broader project-level `traceability` skill.

### Core principle

> Every implementation artifact MUST answer what approved item authorizes it and where that approval originates.

## Inputs

Primary inputs:

- approved implementation outputs;
- approved implementation decisions;
- approved blueprint;
- approved functional requirements;
- applicable development standards;
- implementation artifacts;
- implementation item registry, when available.

Unsupported references MUST NOT be treated as valid evidence.

## Outputs

The skill may produce:

```text
implementation-traceability.md
implementation-traceability-findings.md
implementation-traceability-matrix.md
```

## Traceability Chain

Every implementation item SHOULD preserve:

```text
Implementation Artifact
        ↓
Implementation Item
        ↓
Approved Upstream Evidence
```

Where applicable, the upstream chain may continue through:

```text
Implementation
    ↓
Blueprint / Approved Artifact
    ↓
Requirement / Business Rule / NFR
```

## Evidence Classification

Allowed classifications:

| Classification | Meaning |
|---|---|
| `SOURCE_STATED` | Explicit upstream evidence |
| `DERIVED` | Safely derived implementation mapping |
| `DEV_STANDARD` | Explicitly established by an applicable development standard |
| `IMPLEMENTATION` | Approved implementation decision or item |
| `OPEN` | Required traceability information remains unresolved |
| `UNKNOWN` | Required evidence is unavailable |
| `BLOCKED` | Traceability cannot safely be established |
| `CONTRADICTION` | Relevant evidence conflicts |

## Rules

1. Every implementation item MUST have a traceability reference.
2. The reference MUST identify a real approved artifact or decision.
3. Traceability MUST match the implementation item's scope.
4. A syntactically valid ID is not sufficient when the referenced item is unrelated.
5. One approved implementation item may map to many implementation artifacts.
6. Many implementation items may map to one approved artifact when each mapping is explicit.
7. Many-to-many mappings are allowed when each relationship is explicit.
8. Orphan implementation items MUST be reported as `ORPHAN_IMPLEMENTATION`.
9. Invalid references MUST be reported as `INVALID_IMPLEMENTATION_TRACE`.
10. Scope mismatch MUST be reported as `TRACEABILITY_SCOPE_MISMATCH`.
11. The skill MUST NOT create missing implementation items to repair traceability.
12. The skill MUST NOT invent upstream requirements to justify an implementation artifact.
13. A valid trace does not authorize unrelated implementation behavior.

## OPEN / UNKNOWN Handling

`OPEN` and `UNKNOWN` remain unresolved until supported by explicit evidence.

The skill MUST NOT convert:

```text
OPEN → TRACEABLE
UNKNOWN → TRACEABLE
```

without evidence.

## Contradiction Handling

If a traceability relationship is contradicted by authoritative evidence, report:

```text
CONTRADICTION
```

or:

```text
BLOCKED
```

when the conflict prevents safe implementation traceability.

The skill MUST NOT choose the more convenient source without an explicit precedence rule.

## Quality Gate

Pass requires:

```text
100% implementation items traceable
AND
0 invalid references
AND
0 orphan implementation items
AND
0 unresolved scope mismatches
AND
0 material traceability contradictions
```

Possible results:

```text
PASS
PASS WITH OPEN ITEMS
BLOCKED
FAIL
```

## Boundary With Skill 9

Project-level `traceability` validates the complete artifact graph.

`implementation-traceability` focuses specifically on the implementation boundary.

The implementation-focused skill MUST NOT replace or weaken the project-level traceability gate.
