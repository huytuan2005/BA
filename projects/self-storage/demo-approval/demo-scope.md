# Self-Storage — Framework Demonstration Approval

**Decision type:** Explicit implementation decision for framework validation only  
**Environment:** Non-production demo  
**Purpose:** Demonstrate the full implementation lifecycle on a real project without pretending that unresolved production scope is approved.

## Approved Demo Scope

1. Implement facility/unit discovery for the source-supported information in FR-SELF-STORAGE-001.
2. Implement a browser-only reservation-form prototype for the inputs explicitly named by FR-SELF-STORAGE-002: facility, unit type, start date, and rental period.
3. No production payment, authentication, persistence, notification, status transition, external integration, or backend API is included.
4. The demo must visibly label itself as a non-production prototype.

## Technical Decision

For this demonstration only:
- Technology: plain HTML, CSS, and JavaScript.
- Persistence: none.
- External dependencies: none.

This decision is a demo implementation decision, not a client requirement and not a production architecture decision.

## Acceptance Criteria

- Discovery page displays the explicitly supported facility/unit information.
- Reservation form exposes the four explicitly supported reservation inputs.
- Submitting the form shows a local confirmation without claiming a persisted reservation.
- No unsupported production behavior is presented as implemented.
- Code contains no external dependency.
