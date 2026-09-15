# Self-Storage — PM/PO + Client Decision Round 2

**Run:** E2E-SELF-STORAGE-002  
**Decision participants:** PM/PO role + Client role (framework-validation simulation)  
**Decision type:** Scope clarification and implementation authorization  
**Decision status:** `SIMULATED APPROVAL FOR E2E VALIDATION`

## Purpose

Resolve the implementation-readiness blockers without inventing undocumented behavior. The decision below is an explicit project decision for the MVP release and is not treated as a source fact.

## Approved MVP Scope

The first release covers only:

1. FR-SELF-STORAGE-001 — customer facility/unit discovery.
2. FR-SELF-STORAGE-002 — customer reservation request.

The following source-stated capabilities remain outside this MVP release and are retained as future/open scope: payment, check-in, handover, returns, support, facility/staff/manager/admin management, reporting, and related authorization behavior.

## Resolved Decisions for MVP

### Workflow

The MVP reservation path is:

```text
Browse facilities/units
    ↓
Select unit
    ↓
Submit reservation request
```

No payment, assignment, check-in, handover, renewal, cancellation, return, or overdue workflow is included in this release.

### Reservation State

The MVP uses one implementation state only:

```text
REQUESTED
```

No additional lifecycle transition is implemented in this release.

### Payment

Payment is explicitly **OUT OF SCOPE** for MVP-SS-01.

### Authorization / Authentication

The MVP is an internal validation release with no authenticated user account boundary. Authentication and role/facility authorization remain future scope.

### API Contract

Approved interface for MVP-SS-01:

```text
GET  /api/facilities
GET  /api/facilities/:facilityId/units
POST /api/reservations
GET  /api/reservations/:reservationId
```

### Data Contract

Approved persistence boundary:

```text
facilities
units
reservations
```

Approved reservation fields:

```text
id
facility_id
unit_id
start_date
rental_period_months
status
created_at
```

### UI Contract

Approved screens for MVP-SS-01:

```text
Facility / Unit Discovery
Reservation Form
Reservation Confirmation
```

### Acceptance Criteria

MVP-SS-01 is accepted when:

- facilities and unit data can be retrieved through the API;
- a customer can submit a reservation containing facility, unit, start date, and rental period;
- the reservation is persisted in SQLite;
- the API returns the created reservation with `REQUESTED` state;
- the confirmation UI displays the created reservation id and state;
- no payment or authentication behavior is claimed by this release.

## Disposition of Previous Blockers

| Previous finding | MVP disposition |
|---|---|
| IR-SS-001 Workflow | RESOLVED by explicit MVP workflow decision |
| IR-SS-002 Status | RESOLVED for MVP with approved single state `REQUESTED` |
| IR-SS-003 Payment | OUT OF SCOPE for MVP |
| IR-SS-004 Authorization | OUT OF SCOPE for MVP |
| IR-SS-005 API | RESOLVED by approved API contract |
| IR-SS-006 Data | RESOLVED by approved SQLite data boundary |
| IR-SS-007 UI | RESOLVED by approved MVP screen contract |
| IR-SS-008 Acceptance | RESOLVED by explicit MVP acceptance criteria |

## Governance Note

This simulated decision authorizes implementation of **MVP-SS-01 only** for framework E2E validation. A real client project would require the corresponding human approval record. It does not convert the remaining Self-Storage product scope into READY status.
