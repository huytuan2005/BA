# Self-Storage — Source Context

Project: Self-Storage Facility Rental and Management System.

## Actors and supplied capabilities

### Storage Customer
- View storage facilities, unit types, sizes, rental prices, and available units.
- Reserve a unit by facility, unit type, start date, and rental period.
- Pay deposit, rental fee, renewal fee, and extra charges.
- Check in to receive an assigned unit based on a scheduled appointment.
- Manage one or more rented units.
- Send support requests for unit, lock, access code, payment, stored items.

### Facility Staff
- Check reservations when customers arrive.
- Support check-in and handover of unit, lock, access card/code.
- Update unit status after handover, during use, after return, or when inspection/maintenance is needed.
- Check/confirm unit condition on return.
- Handle on-site problems and support requests.
- Track daily customers needing unit receipt, return, or support.

### Facility Manager
- Manage units at assigned facility: type, size, location, rental price, status.
- Assign suitable units based on type, rental period, and availability.
- Monitor customers, rental contracts, rental periods, and payment status.
- Manage handover, return, renewal, and overdue handling.
- Assign staff for handover, inspection, and problem handling.
- View facility reports: available units, rented units, revenue, usage rate, overdue cases.

### Business Operations Manager
- Manage all storage facilities.
- Set general rental policies: deposit, renewal, cancellation, return, overdue handling.
- Manage price ranges, extra fees, overdue fees, discounts/fee waivers.
- Monitor revenue, usage rate, and operating performance by facility.
- View/export system-wide reports by facility, unit type, revenue, and rental status.

### System Administrator
- Manage user accounts.
- Assign roles to Storage Customer, Facility Staff, Facility Manager, and Business Operations Manager.
- Configure data access permissions by role and assigned facility.
- Track login history and user activity logs.

## Explicitly unknown
Do not invent database fields, API endpoints, payment providers/methods, authentication mechanism, exact status values/transitions, notification behavior, SLA/performance targets, or report formats.
