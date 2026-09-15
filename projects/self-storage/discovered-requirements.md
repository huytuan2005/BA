1. Project Context
- Self-Storage Facility Rental and Management System.
- Source defines capabilities for customers, facility staff, facility managers, business operations managers, and system administrators.
- Several capabilities remain ambiguous and require clarification before detailed acceptance criteria or workflows are defined.
2. Actors
ID	Actor	Source capability summary
ACT-001	Storage Customer	View facilities and units, reserve and pay, check in, manage rented units, submit support requests
ACT-002	Facility Staff	Check reservations, support check-in and handover, update unit status, confirm returns, handle problems and support
ACT-003	Facility Manager	Manage units, assign units, monitor rentals and payments, manage handover and return activities, assign staff, view reports
ACT-004	Business Operations Manager	Manage facilities, rental policies, pricing, fees, discounts, and system-wide reports
ACT-005	System Administrator	Manage accounts, roles, permissions, login history, and activity logs


3. Source Facts
- Customers can view facilities, unit types, sizes, rental prices, and available units.
- Reservations use facility, unit type, start date, and rental period.
- Customers can pay deposits, rental fees, renewal fees, and extra charges.
- Check-in is associated with a scheduled appointment and an assigned unit.
- Facility staff perform or support reservation checks, check-in, handover, return, inspection, maintenance, and problem handling.
- Facility managers work with units, customers, contracts, rental periods, payment status, staff assignments, and facility reports.
- Business operations managers define general rental policies and manage pricing-related values.
- System administrators configure role and assigned-facility access permissions.
- Exact statuses, transitions, payment methods, authentication, notifications, service levels, and report formats are explicitly unknown.
4. Candidate Functional Requirements
ID	Actor	Requirement	Source	Confidence
FR-SELF-STORAGE-001	Storage Customer	The system shall allow the customer to view storage facilities, unit types, sizes, rental prices, and available units.	context.md — Storage Customer	MEDIUM
FR-SELF-STORAGE-002	Storage Customer	The system shall allow the customer to reserve a unit by facility, unit type, start date, and rental period.	context.md — Storage Customer	HIGH
FR-SELF-STORAGE-003	Storage Customer	The system shall allow the customer to pay a deposit, rental fee, renewal fee, or extra charge.	context.md — Storage Customer	HIGH
FR-SELF-STORAGE-004	Storage Customer	The system shall allow the customer to check in and receive an assigned unit in connection with a scheduled appointment.	context.md — Storage Customer	MEDIUM
FR-SELF-STORAGE-005	Storage Customer	The system shall provide the customer with the capability to manage one or more rented units.	context.md — Storage Customer	LOW
FR-SELF-STORAGE-006	Storage Customer	The system shall allow the customer to send support requests concerning a unit, lock, access code, payment, or stored items.	context.md — Storage Customer	MEDIUM
FR-SELF-STORAGE-007	Facility Staff	The system shall allow facility staff to check reservations when customers arrive.	context.md — Facility Staff	HIGH
FR-SELF-STORAGE-008	Facility Staff	The system shall support facility staff in check-in and handover of a unit, lock, access card, or access code.	context.md — Facility Staff	MEDIUM
FR-SELF-STORAGE-009	Facility Staff	The system shall allow facility staff to update unit status after handover, during use, after return, or when inspection or maintenance is needed.	context.md — Facility Staff	MEDIUM
FR-SELF-STORAGE-010	Facility Staff	The system shall allow facility staff to check and confirm unit condition on return.	context.md — Facility Staff	HIGH
FR-SELF-STORAGE-011	Facility Staff	The system shall provide facility staff with the capability to handle on-site problems and support requests.	context.md — Facility Staff	LOW
FR-SELF-STORAGE-012	Facility Staff	The system shall provide facility staff with the capability to track daily customers needing unit receipt, return, or support.	context.md — Facility Staff	LOW
FR-SELF-STORAGE-013	Facility Manager	The system shall provide the facility manager with the capability to manage units at an assigned facility, including type, size, location, rental price, and status.	context.md — Facility Manager	LOW
FR-SELF-STORAGE-014	Facility Manager	The system shall allow the facility manager to assign a unit using unit type, rental period, and availability as stated selection factors.	context.md — Facility Manager	LOW
FR-SELF-STORAGE-015	Facility Manager	The system shall provide the facility manager with the capability to monitor customers, rental contracts, rental periods, and payment status.	context.md — Facility Manager	LOW
FR-SELF-STORAGE-016	Facility Manager	The system shall provide the facility manager with the capability to manage handover, return, renewal, and overdue handling.	context.md — Facility Manager	LOW
FR-SELF-STORAGE-017	Facility Manager	The system shall allow the facility manager to assign staff for handover, inspection, and problem handling.	context.md — Facility Manager	MEDIUM
FR-SELF-STORAGE-018	Facility Manager	The system shall allow the facility manager to view facility reports covering available units, rented units, revenue, usage rate, and overdue cases.	context.md — Facility Manager	MEDIUM
FR-SELF-STORAGE-019	Business Operations Manager	The system shall provide the business operations manager with the capability to manage all storage facilities.	context.md — Business Operations Manager	LOW
FR-SELF-STORAGE-020	Business Operations Manager	The system shall allow the business operations manager to set general policies for deposits, renewals, cancellations, returns, and overdue handling.	context.md — Business Operations Manager	MEDIUM
FR-SELF-STORAGE-021	Business Operations Manager	The system shall provide the business operations manager with the capability to manage price ranges, extra fees, overdue fees, discounts, and fee waivers.	context.md — Business Operations Manager	LOW
FR-SELF-STORAGE-022	Business Operations Manager	The system shall provide the business operations manager with the capability to monitor revenue, usage rate, and operating performance by facility.	context.md — Business Operations Manager	LOW
FR-SELF-STORAGE-023	Business Operations Manager	The system shall allow the business operations manager to view and export system-wide reports by facility, unit type, revenue, and rental status.	context.md — Business Operations Manager	MEDIUM
FR-SELF-STORAGE-024	System Administrator	The system shall provide the system administrator with the capability to manage user accounts.	context.md — System Administrator	LOW
FR-SELF-STORAGE-025	System Administrator	The system shall allow the system administrator to assign roles to storage customers, facility staff, facility managers, and business operations managers.	context.md — System Administrator	HIGH
FR-SELF-STORAGE-026	System Administrator	The system shall allow the system administrator to configure data access permissions by role and assigned facility.	context.md — System Administrator	MEDIUM
FR-SELF-STORAGE-027	System Administrator	The system shall allow the system administrator to track login history and user activity logs.	context.md — System Administrator	MEDIUM


5. Candidate Business Rules
ID	Rule	Source	Status
BR-SELF-STORAGE-001	Unit assignment considers unit type, rental period, and availability.	context.md — Facility Manager	SOURCE_STATED
BR-SELF-STORAGE-002	Customer check-in is associated with a scheduled appointment and an assigned unit.	context.md — Storage Customer	SOURCE_STATED
BR-SELF-STORAGE-003	Data access permissions are configured by role and assigned facility.	context.md — System Administrator	SOURCE_STATED
BR-SELF-STORAGE-004	General rental policies cover deposits, renewals, cancellations, returns, and overdue handling.	context.md — Business Operations Manager	SOURCE_STATED


6. Candidate NFRs
None identified from source.
7. Assumptions
- “View,” “reserve,” “pay,” “assign,” “set,” “export,” and “track” are treated as capabilities without assuming specific screens, workflows, data fields, or integrations.
- Ambiguous terms such as “manage,” “monitor,” “support,” “handle,” “available,” and “overdue” are preserved without defining their operations or meanings.
- “Available units” is treated as source wording only; no availability calculation or status model is assumed.
8. Open Questions
- What operations are included in “manage” for rented units, facility units, facilities, user accounts, pricing, and overdue handling?
- What does “monitor,” “track,” “support,” and “handle” require the system to display or allow users to do?
- How are suitable, available, rented, and overdue units or cases defined, and what statuses and transitions apply?
- What are the exact rules for deposits, renewals, cancellations, returns, overdue handling, fees, discounts, and fee waivers?
- What permissions, report formats, export formats, and payment methods are required?
9. Traceability
- All five actor groups and their listed capability areas are represented in FR-SELF-STORAGE-001 through FR-SELF-STORAGE-027.
- Source-stated decision or constraint information is represented in BR-SELF-STORAGE-001 through BR-SELF-STORAGE-004.
- Ambiguous capabilities remain explicitly qualified and are not expanded into CRUD operations, workflows, statuses, or policies.
- No source capability is currently uncovered.
10. Quality Gate
PASS WITH QUESTIONS
- All supplied capabilities are traceable.
- Ambiguous terms are preserved and confidence is lowered where interpretation is required.
- Open questions identify unresolved scope, behavior, rules, permissions, and acceptance details.
- No unsupported NFRs or implementation details were introduced.