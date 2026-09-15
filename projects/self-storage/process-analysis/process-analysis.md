# Self-Storage — Process Analysis

**Run:** E2E-SELF-STORAGE-001  
**Source:** `discovered-requirements.md`  
**Status:** `PASS WITH QUESTIONS`

## 1. Project Context
- Self-Storage Facility Rental and Management System.
- Process baseline is derived only from FR-SELF-STORAGE-001 through FR-SELF-STORAGE-027 and BR-SELF-STORAGE-001 through BR-SELF-STORAGE-004.
- Undefined workflow, status, payment, notification, and operational details remain open.

## 2. Supported Business Processes

| ID | Process | Supported scope | Source | Confidence |
|---|---|---|---|---|
| BP-SELF-STORAGE-001 | Facility and Unit Discovery | Customer views facilities, unit types, sizes, rental prices, and available units. | FR-SELF-STORAGE-001 | HIGH |
| BP-SELF-STORAGE-002 | Unit Reservation | Customer reserves a unit using facility, unit type, start date, and rental period. | FR-SELF-STORAGE-002 | HIGH |
| BP-SELF-STORAGE-003 | Rental Payment | Customer can pay deposit, rental fee, renewal fee, or extra charge. | FR-SELF-STORAGE-003 | HIGH |
| BP-SELF-STORAGE-004 | Check-In and Handover | Customer check-in is associated with a scheduled appointment and assigned unit; staff support handover. | FR-SELF-STORAGE-004, FR-SELF-STORAGE-008, BR-SELF-STORAGE-002 | MEDIUM |
| BP-SELF-STORAGE-005 | Return and Condition Check | Staff check and confirm unit condition on return and may update unit status. | FR-SELF-STORAGE-009, FR-SELF-STORAGE-010 | MEDIUM |
| BP-SELF-STORAGE-006 | Support Handling | Customer submits support requests; staff provide support/handle problems. | FR-SELF-STORAGE-006, FR-SELF-STORAGE-011 | LOW |
| BP-SELF-STORAGE-007 | Facility Operations Management | Facility manager works with units, assignments, rentals, payments, handover/return, staff assignments, and reports. | FR-SELF-STORAGE-013 through FR-SELF-STORAGE-018 | LOW |
| BP-SELF-STORAGE-008 | Rental Policy and Pricing Management | Business operations manager manages facilities, policies, prices, fees, discounts, waivers, and reports. | FR-SELF-STORAGE-019 through FR-SELF-STORAGE-023 | LOW |
| BP-SELF-STORAGE-009 | User and Access Administration | System administrator manages accounts, roles, facility-scoped access permissions, and activity history. | FR-SELF-STORAGE-024 through FR-SELF-STORAGE-027 | MEDIUM |

## 3. Actor Interactions

| Process | Actor interactions |
|---|---|
| Discovery | Storage Customer views facility/unit information. |
| Reservation | Storage Customer reserves a unit. |
| Payment | Storage Customer makes rental-related payment. |
| Check-In / Handover | Storage Customer and Facility Staff participate; Facility Manager may assign staff. |
| Return | Facility Staff checks/updates condition; Facility Manager may manage return activity. |
| Support | Storage Customer submits support request; Facility Staff handles support/problems. |
| Facility Operations | Facility Manager manages facility-level unit/rental/assignment/report capabilities. |
| Policy / Pricing | Business Operations Manager configures policies and pricing-related values. |
| Administration | System Administrator manages users, roles, access permissions, and activity history. |

## 4. Process Triggers and Inputs

Only source-supported inputs/triggers are recorded.

| Process | Trigger / Input | Source |
|---|---|---|
| Reservation | Facility, unit type, start date, rental period | FR-SELF-STORAGE-002 |
| Check-In | Scheduled appointment and assigned unit are stated associations. | FR-SELF-STORAGE-004 / BR-SELF-STORAGE-002 |
| Unit Assignment | Unit type, rental period, availability are stated selection factors. | FR-SELF-STORAGE-014 / BR-SELF-STORAGE-001 |
| Support | Customer support request concerning a unit, lock, access code, payment, or stored items. | FR-SELF-STORAGE-006 |
| Other processes | Trigger/input not fully specified. | Source / OPEN |

## 5. Process Outcomes

- Customer can view supported facility/unit information.
- Customer can submit a reservation.
- Customer can make supported rental-related payments.
- Customer check-in is associated with a scheduled appointment and assigned unit.
- Staff can support handover and confirm return condition.
- Facility Manager can use supported management/reporting capabilities.
- Business Operations Manager can manage supported policy/pricing/report capabilities.
- System Administrator can manage supported account/role/access/activity capabilities.

## 6. Process Constraints and Business Rules

| ID | Rule | Source | Status |
|---|---|---|---|
| BR-SELF-STORAGE-001 | Unit assignment considers unit type, rental period, and availability. | FR-SELF-STORAGE-014 | SOURCE_STATED |
| BR-SELF-STORAGE-002 | Customer check-in is associated with a scheduled appointment and assigned unit. | FR-SELF-STORAGE-004 | SOURCE_STATED |
| BR-SELF-STORAGE-003 | Data access permissions are configured by role and assigned facility. | FR-SELF-STORAGE-026 | SOURCE_STATED |
| BR-SELF-STORAGE-004 | General rental policies cover deposits, renewals, cancellations, returns, and overdue handling. | FR-SELF-STORAGE-020 | SOURCE_STATED |

## 7. Unsupported or Ambiguous Process Steps

- Exact sequence between reservation, payment, appointment, assignment, and check-in is not defined.
- Meaning of `manage`, `monitor`, `support`, `handle`, `available`, and `overdue` is not fully defined.
- Unit/rental/payment/return/renewal/overdue statuses and transitions are not defined.
- Payment methods, payment confirmation, failure/refund handling, notifications, service levels, and report formats are not defined.

All unresolved items remain `OPEN_QUESTION`.

## 8. Process Traceability

Every process above traces directly to source requirement IDs. No process is sourced only from another generated artifact.

## 9. Open Questions

1. What is the intended sequence and responsibility across reservation, payment, assignment, appointment, check-in, handover, return, renewal, and overdue handling?
2. What concrete operations are included in `manage`, `monitor`, `support`, and `handle`?
3. What states and transitions exist for units, rentals, payments, returns, renewals, and overdue handling?
4. What payment, permission, reporting, export, and notification behavior is required?

## 10. Quality Gate

`PASS WITH QUESTIONS`

- All identified processes are traceable.
- No unsupported workflow was invented.
- Ambiguities remain explicit.
- Open questions identify implementation-relevant unresolved behavior.
