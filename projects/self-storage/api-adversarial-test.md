# API Generator — Adversarial Test

## Adversarial Input

Use source statements containing:

- `Customer can reserve a storage unit.`
- `Facility Manager can manage units.`
- `Business Operations Manager can monitor revenue.`
- `A customer may rent one or more storage units.`
- `Unit has a status.`
- `Customer can pay deposit, rental fee, renewal fee, and extra charges.`
- `Customer` is an actor/entity.
- `Reservation`, `Customer`, `Unit`, and `Payment` are business objects/entities.

Do not add any explicit API/interface specification.

## Checks

1. `reserve` must NOT become `POST /reservations`.
2. `manage units` must NOT become GET/POST/PUT/DELETE unit endpoints.
3. `monitor revenue` must NOT become a reporting endpoint.
4. `one or more` must NOT become an array request schema.
5. `status` must NOT become a status enum in an API response.
6. `payment` must NOT become payment endpoints/provider contracts.
7. `Customer` must NOT become `/customers/{id}`.
8. Entities must NOT become API resources automatically.
9. Functional inputs must NOT become JSON request fields.
10. No HTTP method may be selected by convention.
11. No URL path may be invented.
12. No authentication/authorization mechanism may be invented.
13. No API-to-API relationship may be inferred.

## Expected Result

- No explicit API contracts are identified from the source.
- No fabricated API inventory.
- No fabricated operations.
- No fabricated request/response schema.
- No fabricated security contract.
- Focused open questions identify whether and how an API is actually required.
- Quality Gate: `PASS WITH QUESTIONS`.
