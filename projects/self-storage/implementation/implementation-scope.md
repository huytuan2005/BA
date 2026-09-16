# Self-Storage — Fresh Implementation Scope

**Skill:** `implementation`  
**Version:** `v1.0`  
**Validation Run:** `SS-P3-E2E-001`  
**Scope Type:** `FRESH`  
**Status:** `PARTIAL`

---

## 1. Purpose

This document defines the implementation scope currently authorized by the existing Self-Storage implementation baseline.

No new implementation items are created by this document.

Production implementation remains blocked.

---

## 2. Authorized Implementation Scope

| Implementation ID | Item | Evidence | Status | Planning Eligibility |
|---|---|---|---|---|
| IMP-SS-DEMO-001 | Facility and unit discovery prototype | `implementation-demo/index.html`, `styles.css`, `app.js` | COMPLETED | VALIDATED |
| IMP-SS-DEMO-002 | Reservation-form prototype using facility, unit type, start date, rental period | `implementation-demo/index.html`, `app.js` | COMPLETED | VALIDATED |

Upstream traceability:

- `IMP-SS-DEMO-001` → demo scope item 1 → `FR-SELF-STORAGE-001`
- `IMP-SS-DEMO-002` → demo scope item 2 → `FR-SELF-STORAGE-002`

---

## 3. Production Boundary

Production implementation is:

```text
BLOCKED