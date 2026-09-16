# Self-Storage — Use Case Analysis

**Phase 3 Run ID:** `SS-P3-E2E-001`
**Lifecycle Stage:** `Use Case Analysis`
**Current Status:** `CURRENT — PHASE 3 BA BASELINE / PENDING REVIEW`
**Evidence Source:** `discovered-requirements.md` + `process-analysis/process-analysis.md` + `functional-analysis/functional-analysis.md`
**Traceability References:** FR-SELF-STORAGE-001..027 → UC-SELF-STORAGE-001..027
**Historical Run Basis:** `E2E-SELF-STORAGE-001`


## 1. Project Context
- Use cases are derived only from source-supported actor capabilities.
- Ambiguous capabilities are preserved without CRUD or workflow invention.

## 2. Actors

| ID | Actor | Use-Case Goal Summary |
|---|---|---|
| ACT-001 | Storage Customer | Discover units, reserve, pay, check in, manage rented units, request support. |
| ACT-002 | Facility Staff | Check reservations, support handover/check-in, update unit status, confirm returns, handle support/problems. |
| ACT-003 | Facility Manager | Manage units/assignments/rentals/handover/return/staff/report capabilities. |
| ACT-004 | Business Operations Manager | Manage facilities, policies, pricing, fees, discounts, and reports. |
| ACT-005 | System Administrator | Manage accounts, roles, access permissions, login/activity history. |

## 3. Use Case Inventory

| ID | Actor | Use Case | Goal | Source | Confidence |
|---|---|---|---|---|---|
| UC-SELF-STORAGE-001 | Storage Customer | View Facilities and Units | View facility/unit information including size, rental prices, and available units. | FR-SELF-STORAGE-001 | MEDIUM |
| UC-SELF-STORAGE-002 | Storage Customer | Reserve Unit | Reserve a unit by facility, unit type, start date, and rental period. | FR-SELF-STORAGE-002 | HIGH |
| UC-SELF-STORAGE-003 | Storage Customer | Make Rental Payment | Make deposit, rental, renewal, or extra-charge payment. | FR-SELF-STORAGE-003 | HIGH |
| UC-SELF-STORAGE-004 | Storage Customer | Check In | Check in and receive an assigned unit in connection with a scheduled appointment. | FR-SELF-STORAGE-004 | MEDIUM |
| UC-SELF-STORAGE-005 | Storage Customer | Manage Rented Units | Use the stated rented-unit management capability; exact operations undefined. | FR-SELF-STORAGE-005 | LOW |
| UC-SELF-STORAGE-006 | Storage Customer | Submit Support Request | Send support request concerning unit, lock, access code, payment, or stored items. | FR-SELF-STORAGE-006 | MEDIUM |
| UC-SELF-STORAGE-007 | Facility Staff | Check Reservation at Arrival | Check reservations when customers arrive. | FR-SELF-STORAGE-007 | HIGH |
| UC-SELF-STORAGE-008 | Facility Staff | Support Check-In and Handover | Support check-in/handover of unit, lock, access card, or access code. | FR-SELF-STORAGE-008 | MEDIUM |
| UC-SELF-STORAGE-009 | Facility Staff | Update Unit Status | Update unit status in the source-stated situations; exact status model undefined. | FR-SELF-STORAGE-009 | LOW |
| UC-SELF-STORAGE-010 | Facility Staff | Confirm Return Condition | Check and confirm unit condition on return. | FR-SELF-STORAGE-010 | HIGH |
| UC-SELF-STORAGE-011 | Facility Staff | Handle Support and On-Site Problems | Handle stated support/problem capability; exact operations undefined. | FR-SELF-STORAGE-011 | LOW |
| UC-SELF-STORAGE-012 | Facility Staff | Track Daily Customer Needs | Track daily customers needing receipt, return, or support. | FR-SELF-STORAGE-012 | LOW |
| UC-SELF-STORAGE-013 | Facility Manager | Manage Facility Units | Manage units at assigned facility; exact operations undefined. | FR-SELF-STORAGE-013 | LOW |
| UC-SELF-STORAGE-014 | Facility Manager | Assign Unit | Assign a unit using unit type, rental period, and availability as selection factors. | FR-SELF-STORAGE-014 | LOW |
| UC-SELF-STORAGE-015 | Facility Manager | Monitor Rental Operations | Monitor customers, contracts, rental periods, and payment status. | FR-SELF-STORAGE-015 | LOW |
| UC-SELF-STORAGE-016 | Facility Manager | Manage Handover Return Renewal Overdue | Manage the stated capability; exact workflow/status rules undefined. | FR-SELF-STORAGE-016 | LOW |
| UC-SELF-STORAGE-017 | Facility Manager | Assign Staff | Assign staff for handover, inspection, and problem handling. | FR-SELF-STORAGE-017 | MEDIUM |
| UC-SELF-STORAGE-018 | Facility Manager | View Facility Reports | View stated facility reports. | FR-SELF-STORAGE-018 | MEDIUM |
| UC-SELF-STORAGE-019 | Business Operations Manager | Manage Facilities | Manage all storage facilities; exact operations undefined. | FR-SELF-STORAGE-019 | LOW |
| UC-SELF-STORAGE-020 | Business Operations Manager | Configure Rental Policies | Set stated rental policies. | FR-SELF-STORAGE-020 | MEDIUM |
| UC-SELF-STORAGE-021 | Business Operations Manager | Manage Pricing and Fees | Manage stated pricing/fee/discount/waiver categories. | FR-SELF-STORAGE-021 | LOW |
| UC-SELF-STORAGE-022 | Business Operations Manager | Monitor Operating Performance | Monitor revenue, usage rate, and operating performance by facility. | FR-SELF-STORAGE-022 | LOW |
| UC-SELF-STORAGE-023 | Business Operations Manager | View and Export System Reports | View/export stated system-wide reports. | FR-SELF-STORAGE-023 | MEDIUM |
| UC-SELF-STORAGE-024 | System Administrator | Manage User Accounts | Manage user accounts; exact operations undefined. | FR-SELF-STORAGE-024 | LOW |
| UC-SELF-STORAGE-025 | System Administrator | Assign Roles | Assign stated roles. | FR-SELF-STORAGE-025 | HIGH |
| UC-SELF-STORAGE-026 | System Administrator | Configure Access Permissions | Configure role/facility-scoped access permissions. | FR-SELF-STORAGE-026 | MEDIUM |
| UC-SELF-STORAGE-027 | System Administrator | Track Login and Activity History | Track login history and user activity logs. | FR-SELF-STORAGE-027 | MEDIUM |

## 4. Use Case Preconditions

Only explicit source-supported preconditions are recorded:

| Use Case | Preconditions | Source | Confidence |
|---|---|---|---|
| UC-SELF-STORAGE-004 | Scheduled appointment and assigned unit association. | FR-SELF-STORAGE-004 / BR-SELF-STORAGE-002 | MEDIUM |
| UC-SELF-STORAGE-014 | Unit assignment considers unit type, rental period, availability. | FR-SELF-STORAGE-014 / BR-SELF-STORAGE-001 | LOW |

For other use cases: `None explicitly identified from the source.`

## 5. Use Case Postconditions

No stronger postconditions are inferred beyond stated capabilities. `None explicitly identified from the source.`

## 6. Use Case Inputs and Outputs

Only reservation, check-in, and assignment information explicitly stated by source is included. No API payloads, fields, or technical outputs are inferred.

## 7. Use Case Rules and Constraints

The four BR-SELF-STORAGE rules apply where traceability supports them.

## 8. Use Case Relationships

`No explicit use-case relationships are identified from the source.`

## 9. Unsupported or Ambiguous Behavior

Workflow sequencing, statuses, payment methods, failure handling, notifications, authentication mechanisms, and exact management operations remain open.

## 10. Use Case Traceability

Every UC maps to its corresponding FR. All 27 requirements are represented by one use case each.

## 11. Open Questions

See project-level open questions in `discovered-requirements.md`; only workflow/behavior questions that affect use-case scope are carried forward.

## 12. Quality Gate

`PASS WITH QUESTIONS`
