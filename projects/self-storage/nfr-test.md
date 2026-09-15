# Self-Storage — NFR Generator Normal Test

## Source basis

Use the existing Self-Storage project context and discovered artifacts.

Relevant source capabilities include:
- customers can view facilities, unit types, sizes, rental prices, and available units;
- customers can reserve units;
- customers can pay deposit, rental, renewal, and extra charges;
- staff and managers operate facilities and monitor business information;
- administrators manage accounts and access permissions;
- reports can be viewed/exported.

The source does not explicitly define numeric performance, availability,
capacity, recovery, accessibility, security, privacy, compliance, or
retention targets.

## Expected behavior

Run `nfr-generator` against the Self-Storage project.

Expected result:
- No generic NFRs are invented.
- Payment does not automatically create a security NFR.
- Account management does not automatically create authentication,
  encryption, MFA, or password NFRs.
- Reports do not automatically create performance or availability targets.
- "available units" is functional/business information, not an availability
  NFR.
- The result should state that no explicit NFRs are identified from the source,
  unless the project evidence contains additional explicit quality
  requirements.
- Quality Gate should be `PASS` if no explicit NFR evidence exists, or
  `PASS WITH QUESTIONS` only if the source contains explicit but incomplete
  quality wording.
