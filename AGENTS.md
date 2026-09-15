# BA Agent Instructions

## Scope
This repository is a reusable Business Analysis framework. Reusable behavior belongs in `.codex/skills/`; project evidence belongs in `projects/<project>/`.

## Rules
- Source evidence is authoritative.
- Never invent requirements, rules, fields, statuses, APIs, database structures, UI behavior, security mechanisms, or NFRs.
- Separate `SOURCE_FACT`, `CANDIDATE_REQUIREMENT`, `ASSUMPTION`, and `OPEN_QUESTION`.
- Preserve traceability from every candidate requirement to its source evidence.
- Prefer the smallest useful output. Do not repeat source text unnecessarily.
- Use stable IDs and terminology.
- If evidence is insufficient, flag the gap instead of guessing.

## User priority
Follow explicit user instructions. If they conflict with this framework, follow the user's instruction unless it would make the result misleading.

## Quality baseline
A candidate requirement should be actor-specific, observable, testable, unambiguous enough for its current discovery stage, and traceable.
