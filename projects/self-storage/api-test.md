# API Generator — Self-Storage Test

## Source Condition

The Self-Storage project source describes business capabilities, functional
requirements, use cases, and a conceptual data model, but does not explicitly
specify REST endpoints, HTTP methods, URL paths, request/response contracts,
or API security mechanisms.

## Expected Behavior

The generator must NOT create endpoints merely from:
- customer reservation capability;
- facility/unit management;
- payment capability;
- user/account management;
- entities such as Customer, Facility, Storage Unit, Reservation, or Rental Contract.

Expected result:
- No API contracts identified from the source.
- No HTTP methods.
- No paths.
- No request/response fields.
- No status codes.
- No authentication mechanism.
- No authorization mechanism.
- API-related gaps recorded as open questions.

## Expected Quality Gate

PASS WITH QUESTIONS is acceptable if the output clearly states that the
current source is not API-defining and does not fabricate an API contract.
