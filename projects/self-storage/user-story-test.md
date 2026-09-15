# User Story Generator v1.0 — Self-Storage Test

## Test Basis

- Project: Self-Storage Facility Rental and Management System.
- Source: `projects/self-storage/context.md` plus the discovered functional requirements and use-case baseline.
- Test objective: verify source coverage, actor preservation, acceptance-criteria safety, ambiguity handling, and `US → UC → FR → FN` traceability.

## 1. Project Context

- Self-Storage Facility Rental and Management System.
- Stories are derived from the five source actor groups and their supported capabilities.
- Ambiguous operational behavior remains unresolved.

## 2. Actors

| ID | Actor | Story Goal Summary |
|---|---|---|
| ACT-001 | Storage Customer | Discover units, reserve and pay, check in, manage rented units, request support |
| ACT-002 | Facility Staff | Check reservations, support handover/check-in, update unit status, confirm returns, handle problems/support |
| ACT-003 | Facility Manager | Manage units, assign units, monitor rentals/payments, manage handover/return/renewal/overdue handling, assign staff, view reports |
| ACT-004 | Business Operations Manager | Manage facilities, set policies, manage pricing/fees/discounts, monitor performance, view/export reports |
| ACT-005 | System Administrator | Manage accounts, assign roles, configure access permissions, track login/activity logs |

## 3. User Story Inventory

| ID | Actor | User Story | Source | Confidence |
|---|---|---|---|---|
| US-SELF-STORAGE-001 | Storage Customer | As a Storage Customer, I want to view storage facilities, unit types, sizes, rental prices, and available units. | FR-SELF-STORAGE-001 / UC-SELF-STORAGE-001 | MEDIUM |
| US-SELF-STORAGE-002 | Storage Customer | As a Storage Customer, I want to reserve a unit by facility, unit type, start date, and rental period. | FR-SELF-STORAGE-002 / UC-SELF-STORAGE-002 | HIGH |
| US-SELF-STORAGE-003 | Storage Customer | As a Storage Customer, I want to pay a deposit, rental fee, renewal fee, or extra charge. | FR-SELF-STORAGE-003 / UC-SELF-STORAGE-003 | HIGH |
| US-SELF-STORAGE-004 | Storage Customer | As a Storage Customer, I want to check in and receive an assigned unit in connection with a scheduled appointment. | FR-SELF-STORAGE-004 / UC-SELF-STORAGE-004 | MEDIUM |
| US-SELF-STORAGE-005 | Storage Customer | As a Storage Customer, I want to manage one or more rented units. | FR-SELF-STORAGE-005 / UC-SELF-STORAGE-005 | LOW |
| US-SELF-STORAGE-006 | Storage Customer | As a Storage Customer, I want to send support requests concerning a unit, lock, access code, payment, or stored items. | FR-SELF-STORAGE-006 / UC-SELF-STORAGE-006 | MEDIUM |
| US-SELF-STORAGE-007 | Facility Staff | As Facility Staff, I want to check reservations when customers arrive. | FR-SELF-STORAGE-007 / UC-SELF-STORAGE-007 | HIGH |
| US-SELF-STORAGE-008 | Facility Staff | As Facility Staff, I want to support check-in and handover of a unit, lock, access card, or access code. | FR-SELF-STORAGE-008 / UC-SELF-STORAGE-008 | MEDIUM |
| US-SELF-STORAGE-009 | Facility Staff | As Facility Staff, I want to update unit status after handover, during use, after return, or when inspection or maintenance is needed. | FR-SELF-STORAGE-009 / UC-SELF-STORAGE-009 | MEDIUM |
| US-SELF-STORAGE-010 | Facility Staff | As Facility Staff, I want to check and confirm unit condition on return. | FR-SELF-STORAGE-010 / UC-SELF-STORAGE-010 | HIGH |
| US-SELF-STORAGE-011 | Facility Staff | As Facility Staff, I want to handle on-site problems and support requests. | FR-SELF-STORAGE-011 / UC-SELF-STORAGE-011 | LOW |
| US-SELF-STORAGE-012 | Facility Staff | As Facility Staff, I want to track daily customers needing unit receipt, return, or support. | FR-SELF-STORAGE-012 / UC-SELF-STORAGE-012 | LOW |
| US-SELF-STORAGE-013 | Facility Manager | As a Facility Manager, I want to manage units at my assigned facility, including type, size, location, rental price, and status. | FR-SELF-STORAGE-013 / UC-SELF-STORAGE-013 | LOW |
| US-SELF-STORAGE-014 | Facility Manager | As a Facility Manager, I want to assign a unit using unit type, rental period, and availability as the stated selection factors. | FR-SELF-STORAGE-014 / UC-SELF-STORAGE-014 | LOW |
| US-SELF-STORAGE-015 | Facility Manager | As a Facility Manager, I want to monitor customers, rental contracts, rental periods, and payment status. | FR-SELF-STORAGE-015 / UC-SELF-STORAGE-015 | LOW |
| US-SELF-STORAGE-016 | Facility Manager | As a Facility Manager, I want to manage handover, return, renewal, and overdue handling. | FR-SELF-STORAGE-016 / UC-SELF-STORAGE-016 | LOW |
| US-SELF-STORAGE-017 | Facility Manager | As a Facility Manager, I want to assign staff for handover, inspection, and problem handling. | FR-SELF-STORAGE-017 / UC-SELF-STORAGE-017 | MEDIUM |
| US-SELF-STORAGE-018 | Facility Manager | As a Facility Manager, I want to view facility reports covering available units, rented units, revenue, usage rate, and overdue cases. | FR-SELF-STORAGE-018 / UC-SELF-STORAGE-018 | MEDIUM |
| US-SELF-STORAGE-019 | Business Operations Manager | As a Business Operations Manager, I want to manage all storage facilities. | FR-SELF-STORAGE-019 / UC-SELF-STORAGE-019 | LOW |
| US-SELF-STORAGE-020 | Business Operations Manager | As a Business Operations Manager, I want to set general policies for deposits, renewals, cancellations, returns, and overdue handling. | FR-SELF-STORAGE-020 / UC-SELF-STORAGE-020 | MEDIUM |
| US-SELF-STORAGE-021 | Business Operations Manager | As a Business Operations Manager, I want to manage price ranges, extra fees, overdue fees, discounts, and fee waivers. | FR-SELF-STORAGE-021 / UC-SELF-STORAGE-021 | LOW |
| US-SELF-STORAGE-022 | Business Operations Manager | As a Business Operations Manager, I want to monitor revenue, usage rate, and operating performance by facility. | FR-SELF-STORAGE-022 / UC-SELF-STORAGE-022 | LOW |
| US-SELF-STORAGE-023 | Business Operations Manager | As a Business Operations Manager, I want to view and export system-wide reports by facility, unit type, revenue, and rental status. | FR-SELF-STORAGE-023 / UC-SELF-STORAGE-023 | MEDIUM |
| US-SELF-STORAGE-024 | System Administrator | As a System Administrator, I want to manage user accounts. | FR-SELF-STORAGE-024 / UC-SELF-STORAGE-024 | LOW |
| US-SELF-STORAGE-025 | System Administrator | As a System Administrator, I want to assign roles to Storage Customers, Facility Staff, Facility Managers, and Business Operations Managers. | FR-SELF-STORAGE-025 / UC-SELF-STORAGE-025 | HIGH |
| US-SELF-STORAGE-026 | System Administrator | As a System Administrator, I want to configure data access permissions by role and assigned facility. | FR-SELF-STORAGE-026 / UC-SELF-STORAGE-026 | MEDIUM |
| US-SELF-STORAGE-027 | System Administrator | As a System Administrator, I want to track login history and user activity logs. | FR-SELF-STORAGE-027 / UC-SELF-STORAGE-027 | MEDIUM |

## 4. Acceptance Criteria

Source-supported criteria are intentionally limited. Most source statements define capabilities but do not define enough behavior for detailed acceptance criteria.

| User Story | Acceptance Criteria | Source | Confidence |
|---|---|---|---|
| US-SELF-STORAGE-001 | Customer can view facility, unit type, size, rental price, and availability information. | FR-001 | MEDIUM |
| US-SELF-STORAGE-002 | Customer can specify facility, unit type, start date, and rental period when reserving a unit. | FR-002 | HIGH |
| US-SELF-STORAGE-003 | Customer can pay a deposit, rental fee, renewal fee, or extra charge. | FR-003 | HIGH |
| US-SELF-STORAGE-004 | Customer check-in is associated with a scheduled appointment and an assigned unit. | FR-004 / BR-002 | MEDIUM |
| US-SELF-STORAGE-007 | Staff can check a reservation when the customer arrives. | FR-007 | HIGH |
| US-SELF-STORAGE-008 | Staff can support handover of a unit, lock, access card, or access code during check-in/handover. | FR-008 | MEDIUM |
| US-SELF-STORAGE-009 | Staff can update unit status in the source-stated contexts: after handover, during use, after return, or when inspection/maintenance is needed. | FR-009 | MEDIUM |
| US-SELF-STORAGE-010 | Staff can check and confirm unit condition on return. | FR-010 | HIGH |
| US-SELF-STORAGE-014 | Unit assignment considers unit type, rental period, and availability. | FR-014 / BR-001 | LOW |
| US-SELF-STORAGE-017 | Manager can assign staff for handover, inspection, and problem handling. | FR-017 | MEDIUM |
| US-SELF-STORAGE-018 | Facility reports cover available units, rented units, revenue, usage rate, and overdue cases. | FR-018 | MEDIUM |
| US-SELF-STORAGE-020 | General policies cover deposits, renewals, cancellations, returns, and overdue handling. | FR-020 / BR-004 | MEDIUM |
| US-SELF-STORAGE-023 | System-wide reports can be viewed/exported by facility, unit type, revenue, and rental status. | FR-023 | MEDIUM |
| US-SELF-STORAGE-025 | Roles can be assigned to the four source-listed actor groups. | FR-025 | HIGH |
| US-SELF-STORAGE-026 | Data access permissions are configured by role and assigned facility. | FR-026 / BR-003 | MEDIUM |
| US-SELF-STORAGE-027 | Login history and user activity logs can be tracked. | FR-027 | MEDIUM |

For US-SELF-STORAGE-005, 006, 011, 012, 013, 015, 016, 019, 021, 022, and 024:
`None explicitly identified from the source.`

## 5. Story Inputs and Outputs

| User Story | Inputs | Outputs | Source |
|---|---|---|---|
| US-SELF-STORAGE-002 | Facility; unit type; start date; rental period | Unit reservation capability | FR-002 |
| US-SELF-STORAGE-004 | Scheduled appointment; assigned unit | Check-in / assigned-unit outcome only where explicitly stated | FR-004 / BR-002 |
| US-SELF-STORAGE-014 | Unit type; rental period; availability | Assigned unit | FR-014 / BR-001 |

No other explicit story-level inputs/outputs are identified without adding assumptions.

## 6. Story Rules and Constraints

| ID | User Story | Rule | Source | Status |
|---|---|---|---|---|
| BR-SELF-STORAGE-001 | US-SELF-STORAGE-014 | Unit assignment considers unit type, rental period, and availability. | FR-014 | SOURCE_STATED |
| BR-SELF-STORAGE-002 | US-SELF-STORAGE-004 | Customer check-in is associated with a scheduled appointment and an assigned unit. | FR-004 | SOURCE_STATED |
| BR-SELF-STORAGE-003 | US-SELF-STORAGE-026 | Data access permissions are configured by role and assigned facility. | FR-026 | SOURCE_STATED |
| BR-SELF-STORAGE-004 | US-SELF-STORAGE-020 | General rental policies cover deposits, renewals, cancellations, returns, and overdue handling. | FR-020 | SOURCE_STATED |

## 7. Unsupported or Ambiguous Behavior

- Exact operations included in `manage` are undefined.
- Exact behavior required by `monitor`, `track`, `support`, and `handle` is undefined.
- Definitions and lifecycle/status behavior for available, rented, and overdue cases are undefined.
- Exact rules for policies, fees, discounts, waivers, renewals, cancellations, returns, and overdue handling are undefined.
- Exact permission scope, report formats, export formats, and payment methods are undefined.

## 8. Story Traceability

All 27 user stories map to the corresponding 27 functional requirements and corresponding use cases. No requirement is uncovered.

Pattern:
`US-SELF-STORAGE-NNN → UC-SELF-STORAGE-NNN → FR-SELF-STORAGE-NNN → FN-SELF-STORAGE-NNN`

No source capability is silently dropped.

## 9. Open Questions

1. What operations are included in each ambiguous `manage` capability?
2. What observable behavior is required for `monitor`, `track`, `support`, and `handle`?
3. What exact rules, statuses, and transitions define availability, rental, renewal, return, cancellation, and overdue handling?
4. What exact permissions and assigned-facility access behavior must be accepted?
5. What report/export formats and payment methods are required?

## 10. Quality Gate

`PASS WITH QUESTIONS`

- All 27 requirements are represented and traceable.
- Actors and source terminology are preserved.
- Acceptance criteria are generated only where the source supports observable behavior.
- Ambiguous capabilities are not expanded into invented workflows or CRUD.
- Open questions capture the remaining acceptance/scope gaps.

## Test Review

### Passed
- Source coverage: PASS
- Actor accuracy: PASS
- Story boundary: PASS
- Generic business value invention: PASS
- Acceptance-criteria safety: PASS
- Ambiguity handling: PASS
- Technical-detail exclusion: PASS
- Traceability: PASS

### Correction applied during test
The initial test approach would have treated the user-story `so that` clause as mandatory. This was rejected because the source does not consistently provide explicit business value. The locked skill therefore allows a story without a `so that` clause when no source-supported purpose exists.

The skill also avoids forcing acceptance criteria for ambiguous capabilities.
