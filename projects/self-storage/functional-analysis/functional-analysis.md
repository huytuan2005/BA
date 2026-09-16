# Self-Storage — Functional Analysis

**Run:** E2E-SELF-STORAGE-001  
**Input:** `discovered-requirements.md` + process-analysis baseline  
**Status:** `PASS WITH QUESTIONS`

## 1. Project Context
- Functional baseline derived from FR-SELF-STORAGE-001 through FR-SELF-STORAGE-027.
- No technical implementation details are introduced.

## 2. Functional Capability Inventory

| ID | Actor | Functional capability | Source | Confidence |
|---|---|---|---|---|
| FN-SELF-STORAGE-001 | Storage Customer | View storage facilities, unit types, sizes, rental prices, and available units. | FR-SELF-STORAGE-001 | MEDIUM |
| FN-SELF-STORAGE-002 | Storage Customer | Reserve a unit by facility, unit type, start date, and rental period. | FR-SELF-STORAGE-002 | HIGH |
| FN-SELF-STORAGE-003 | Storage Customer | Pay a deposit, rental fee, renewal fee, or extra charge. | FR-SELF-STORAGE-003 | HIGH |
| FN-SELF-STORAGE-004 | Storage Customer | Check in and receive an assigned unit in connection with a scheduled appointment. | FR-SELF-STORAGE-004 | MEDIUM |
| FN-SELF-STORAGE-005 | Storage Customer | Manage one or more rented units. Exact operations remain undefined. | FR-SELF-STORAGE-005 | LOW |
| FN-SELF-STORAGE-006 | Storage Customer | Send support requests concerning a unit, lock, access code, payment, or stored items. | FR-SELF-STORAGE-006 | MEDIUM |
| FN-SELF-STORAGE-007 | Facility Staff | Check reservations when customers arrive. | FR-SELF-STORAGE-007 | HIGH |
| FN-SELF-STORAGE-008 | Facility Staff | Support check-in and handover of a unit, lock, access card, or access code. | FR-SELF-STORAGE-008 | MEDIUM |
| FN-SELF-STORAGE-009 | Facility Staff | Update unit status after handover, during use, after return, or when inspection/maintenance is needed. | FR-SELF-STORAGE-009 | MEDIUM |
| FN-SELF-STORAGE-010 | Facility Staff | Check and confirm unit condition on return. | FR-SELF-STORAGE-010 | HIGH |
| FN-SELF-STORAGE-011 | Facility Staff | Handle on-site problems and support requests. Exact operations undefined. | FR-SELF-STORAGE-011 | LOW |
| FN-SELF-STORAGE-012 | Facility Staff | Track daily customers needing unit receipt, return, or support. | FR-SELF-STORAGE-012 | LOW |
| FN-SELF-STORAGE-013 | Facility Manager | Manage units at an assigned facility. Exact operations undefined. | FR-SELF-STORAGE-013 | LOW |
| FN-SELF-STORAGE-014 | Facility Manager | Assign a unit using unit type, rental period, and availability as stated selection factors. | FR-SELF-STORAGE-014 | LOW |
| FN-SELF-STORAGE-015 | Facility Manager | Monitor customers, rental contracts, rental periods, and payment status. | FR-SELF-STORAGE-015 | LOW |
| FN-SELF-STORAGE-016 | Facility Manager | Manage handover, return, renewal, and overdue handling. | FR-SELF-STORAGE-016 | LOW |
| FN-SELF-STORAGE-017 | Facility Manager | Assign staff for handover, inspection, and problem handling. | FR-SELF-STORAGE-017 | MEDIUM |
| FN-SELF-STORAGE-018 | Facility Manager | View facility reports covering available units, rented units, revenue, usage rate, and overdue cases. | FR-SELF-STORAGE-018 | MEDIUM |
| FN-SELF-STORAGE-019 | Business Operations Manager | Manage all storage facilities. | FR-SELF-STORAGE-019 | LOW |
| FN-SELF-STORAGE-020 | Business Operations Manager | Set general policies for deposits, renewals, cancellations, returns, and overdue handling. | FR-SELF-STORAGE-020 | MEDIUM |
| FN-SELF-STORAGE-021 | Business Operations Manager | Manage price ranges, extra fees, overdue fees, discounts, and fee waivers. | FR-SELF-STORAGE-021 | LOW |
| FN-SELF-STORAGE-022 | Business Operations Manager | Monitor revenue, usage rate, and operating performance by facility. | FR-SELF-STORAGE-022 | LOW |
| FN-SELF-STORAGE-023 | Business Operations Manager | View and export system-wide reports by facility, unit type, revenue, and rental status. | FR-SELF-STORAGE-023 | MEDIUM |
| FN-SELF-STORAGE-024 | System Administrator | Manage user accounts. Exact operations undefined. | FR-SELF-STORAGE-024 | LOW |
| FN-SELF-STORAGE-025 | System Administrator | Assign roles to storage customers, facility staff, facility managers, and business operations managers. | FR-SELF-STORAGE-025 | HIGH |
| FN-SELF-STORAGE-026 | System Administrator | Configure data access permissions by role and assigned facility. | FR-SELF-STORAGE-026 | MEDIUM |
| FN-SELF-STORAGE-027 | System Administrator | Track login history and user activity logs. | FR-SELF-STORAGE-027 | MEDIUM |

## 3. Functional Inputs

Only source-supported information is listed:

- Reservation: facility, unit type, start date, rental period.
- Unit assignment: unit type, rental period, availability as selection factors.
- Check-in: scheduled appointment and assigned unit association.

All other function inputs remain `Not specified` unless explicitly stated by source.

## 4. Functional Outputs

- Facility/unit information is available to the customer.
- Reservation capability is supported.
- Rental-related payment capability is supported.
- Check-in/handover support is available.
- Reports can be viewed/exported where explicitly stated.
- Administrative capabilities are supported at the stated actor level.

## 5. Functional Rules and Constraints

| ID | Rule | Source | Status |
|---|---|---|---|
| BR-SELF-STORAGE-001 | Unit assignment considers unit type, rental period, and availability. | FR-SELF-STORAGE-014 | SOURCE_STATED |
| BR-SELF-STORAGE-002 | Customer check-in is associated with a scheduled appointment and assigned unit. | FR-SELF-STORAGE-004 | SOURCE_STATED |
| BR-SELF-STORAGE-003 | Data access permissions are configured by role and assigned facility. | FR-SELF-STORAGE-026 | SOURCE_STATED |
| BR-SELF-STORAGE-004 | General rental policies cover deposits, renewals, cancellations, returns, and overdue handling. | FR-SELF-STORAGE-020 | SOURCE_STATED |

## 6. Functional Dependencies

No additional functional dependencies are asserted beyond explicit source relationships and the four source-stated business rules.

## 7. Unsupported or Ambiguous Behavior

- `manage`, `monitor`, `support`, `handle`, `track`, `available`, and `overdue` remain unresolved.
- Exact validation, status, transition, payment, notification, authentication, and reporting behavior is not defined.

## 8. Functional Traceability

`FN-SELF-STORAGE-* → FR-SELF-STORAGE-* → BP-SELF-STORAGE-*` where a supported process exists.

All FR-SELF-STORAGE-001 through FR-SELF-STORAGE-027 are represented.

## 9. Open Questions

- What exact operations are included in broad management/monitoring capabilities?
- What actor-visible behavior and acceptance conditions define critical functions?
- What status, payment, permission, report, and notification behavior is required?

## 10. Quality Gate

`PASS WITH QUESTIONS`

TODO: intentional governance failure test