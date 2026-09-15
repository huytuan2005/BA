# Skill 11 — Implementation Readiness

**Version:** 1.0
**Type:** Final Gate
**Role:** Readiness Validator
**Output:** `IMPLEMENTATION-READY` hoặc `BLOCKED`

---

## 1. Purpose

`implementation-readiness` là **cổng kiểm tra cuối cùng trước Implementation**.

Skill này không tạo Requirement, UI, API, Data Model, Business Rule, NFR, Test Case hoặc bất kỳ artifact mới nào.

Nó chỉ xác định:

```text
SYSTEM BLUEPRINT
      ↓
CAN BE IMPLEMENTED WITHOUT
INVENTION, REPAIR, OR SEMANTIC CHANGE?
      ↓
YES → IMPLEMENTATION-READY
NO  → BLOCKED
```

---

# 2. Core Principle

Skill 11:

* không generate;
* không repair;
* không complete;
* không infer missing requirements;
* không resolve contradiction;
* không choose architecture;
* không expand scope.

Quy trình duy nhất:

```text
READ
 ↓
TRACE
 ↓
DEPENDENCY ANALYSIS
 ↓
VALIDATE
 ↓
CLASSIFY
 ↓
BLOCK OR ALLOW
```

---

# 3. Absolute No-Invention Rule

Không được biến:

```text
UNKNOWN → assumed value
OPEN → selected solution
MISSING → invented artifact
CONFLICT → chosen interpretation
PARTIAL → complete capability
```

Mọi quyết định implementation-critical phải có source support.

---

# 4. Source of Truth

Theo thứ tự:

```text
1. Approved SYSTEM BLUEPRINT
2. Blueprint traceability map
3. Skill 10 validation result
4. Skill 9 traceability result
5. Original approved source artifacts
```

Không sử dụng:

```text
industry convention
framework default
developer preference
technical best practice
"obvious" behavior
implementation convenience
```

để lấp khoảng trống.

---

# 5. Entry Gate

Trước mọi readiness check:

```text
BLUEPRINT = APPROVED
TRACEABILITY = PASSED
```

và:

```text
Hallucinated Requirement = 0
Hallucinated Artifact = 0
Broken Link = 0
Critical Contradiction = 0
Scope Expansion = 0
Semantic Drift = 0
Traceability Failure = 0
```

Nếu không đạt:

```text
BLOCKED
```

Không có best-effort mode.

---

# 6. Immutable Blueprint Rule

Skill 11 chỉ đọc Blueprint.

Nó không được:

```text
add
delete
merge
split
rename
repair
rewrite
reinterpret
```

bất kỳ Blueprint item nào.

Nếu phát hiện lỗi:

```text
REPORT → BLOCK
```

không:

```text
REPORT → REPAIR → PASS
```

---

# 7. Readiness Dimensions

Kiểm tra:

```text
IR-1  Requirement Readiness
IR-2  Business Rule Readiness
IR-3  Actor & Permission Readiness
IR-4  UI Readiness
IR-5  API Readiness
IR-6  Data Readiness
IR-7  Cross-Layer Consistency
IR-8  Security & NFR Readiness
IR-9  Test Readiness
IR-10 Traceability & Scope Integrity
```

---

# 8. Implementation Dependency Graph

Skill 11 phải xây dependency graph từ Blueprint:

```text
Requirement
    ↓
Capability
    ↓
Business Rule
    ↓
Actor / Permission
    ↓
UI
    ↓
API
    ↓
Data
    ↓
Security / NFR
    ↓
Test
```

Không phải requirement nào cũng cần mọi node.

Nhưng nếu một node được yêu cầu bởi dependency của capability thì node đó phải đủ rõ.

Ví dụ:

```text
Payment
  ↓
Authorization
  ↓
Payment API
  ↓
Payment Data
  ↓
Failure behavior
  ↓
Tests
```

Nếu một implementation-critical dependency là `UNKNOWN`, `OPEN`, missing hoặc contradictory:

```text
BLOCKED
```

---

# 9. Implementation Impact Analysis

Mỗi `UNKNOWN`, `OPEN`, `PARTIAL` phải được đánh giá theo dependency graph.

Không được chỉ nhìn field đó riêng lẻ.

Phân loại:

```text
NON_BLOCKING
IMPLEMENTATION_BLOCKING
```

### Implementation-blocking nếu nó có thể làm thay đổi hoặc quyết định:

```text
business behavior
API contract
data structure
data constraint
authorization
workflow
state transition
architecture
integration
security behavior
critical verification
```

### Non-blocking nếu chỉ ảnh hưởng:

```text
cosmetic presentation
optional wording
non-functional visual preference
documentation detail
non-critical refinement
```

Rule:

```text
IF unresolved item affects an implementation-critical dependency
THEN BLOCKED
```

---

# 10. UNKNOWN Propagation Rule

`UNKNOWN` phải được propagate qua dependency chain.

Ví dụ:

```text
Authentication = UNKNOWN
      ↓
Protected API depends on authentication
      ↓
Authorization cannot be implemented deterministically
      ↓
BLOCKED
```

Một UNKNOWN không được coi là isolated chỉ vì nó nằm trong một section khác.

### Required algorithm

```text
FOR each UNKNOWN:
    identify dependent capabilities
    identify affected implementation layers

    IF any affected layer is implementation-critical:
        classify BLOCKING
```

---

# 11. OPEN Propagation Rule

Tương tự `UNKNOWN`.

```text
OPEN
 ↓
dependency analysis
 ↓
affected capability
 ↓
implementation impact
```

Nếu OPEN ảnh hưởng:

```text
API
Data
Business Rule
Authorization
Workflow
Architecture
Critical Test
```

→ `BLOCKED`.

OPEN không được trở thành non-blocking chỉ vì nó nằm trong:

```text
Open Issues
Notes
Documentation
Comments
```

---

# 12. Requirement Readiness

Mỗi implementation-critical requirement phải có:

```text
Requirement ID
Capability meaning
Scope
Traceability
Implementation-relevant behavior
```

Nếu behavior chưa đủ xác định:

```text
BLOCKED
```

Không được complete requirement.

---

# 13. Business Rule Readiness

Business Rule phải có:

```text
Rule ID
Condition / Trigger
Expected behavior
Affected capability
Traceability
```

Nếu rule ảnh hưởng implementation nhưng enforcement meaning chưa rõ:

```text
BLOCKED
```

---

# 14. Actor & Authorization Readiness

Phải phân biệt:

```text
AUTHENTICATION
    ≠
AUTHORIZATION
```

và:

```text
AUTHENTICATED USER
    ≠
AUTHORIZED ACTOR
```

Nếu requirement có permission boundary:

```text
Actor
 ↓
Capability
 ↓
Permission
 ↓
Enforcement requirement
```

phải xác định đủ để implement.

Ví dụ:

```text
Only horse owner can edit horse.
```

Chỉ có:

```text
User is authenticated.
```

là **không đủ**.

→ `BLOCKED`.

Không được tự chọn enforcement mechanism.

---

# 15. UI Readiness

Implementation-critical screen phải có:

```text
Screen ID
Purpose
Actor
Relevant action
Relevant data
Relevant backend interaction
Navigation dependency
```

Nếu UI action cần backend behavior nhưng API mapping không tồn tại:

```text
BLOCKED
```

Không được invent API.

---

# 16. API Readiness

Implementation-critical API phải có đủ source-supported information:

```text
API ID
Purpose
Method
Endpoint
Input
Output
Relevant rule
Authorization requirement
Traceability
```

Nếu critical contract information là:

```text
UNKNOWN
OPEN
MISSING
```

→ `BLOCKED`.

Không tự tạo:

```text
endpoint
method
field
status
auth mechanism
```

---

# 17. Data Readiness

Data requirement phải được kiểm tra theo dependency.

Ví dụ:

```text
Requirement:
Username must be unique.

Data:
User.username exists.

Constraint:
UNKNOWN
```

Vì requirement phụ thuộc uniqueness:

```text
BLOCKED
```

Skill 11 không được giả định:

```text
database automatically enforces uniqueness
```

---

# 18. Semantic Data Constraint Check

Các constraint implementation-critical gồm:

```text
uniqueness
nullability
required fields
state constraints
referential relationships
range constraints
business-required values
```

Chỉ block khi constraint đó được source yêu cầu hoặc capability phụ thuộc vào nó.

Không tự thêm constraint.

---

# 19. Cross-Layer Consistency

Kiểm tra capability path:

```text
Requirement
 → Business Rule
 → Actor
 → UI
 → API
 → Data
 → Test
```

Chỉ yêu cầu những layer thực sự cần cho capability.

Artifact tồn tại riêng lẻ không chứng minh flow hoàn chỉnh.

---

# 20. UI → API Mapping

Nếu UI action requires backend behavior:

```text
UI Action → API
```

phải có valid traceable relationship.

Nếu không:

```text
MISSING_UI_API_MAPPING
→ BLOCKED
```

Không được suy ra:

```text
"API probably exists"
```

---

# 21. API → Data Mapping

Nếu API cần persistent state:

```text
API → Data Entity
```

phải resolve được.

Nếu không:

```text
MISSING_API_DATA_MAPPING
→ BLOCKED
```

Không tạo entity mới.

---

# 22. Business Rule Enforcement

Mỗi critical rule phải có implementation-relevant enforcement target.

Ví dụ:

```text
Only owner can edit horse.
```

phải có đủ information để implementation xác định:

```text
who may perform action
what action is protected
what rule determines permission
```

Nếu chỉ biết:

```text
authenticated = true
```

thì chưa đủ.

→ `BLOCKED`.

Không được tự quyết định:

```text
controller
service
middleware
filter
database policy
```

---

# 23. Security Readiness

Security-critical behavior phải có:

```text
Authentication requirement
Authorization boundary
Protected capability
Relevant actor
Sensitive-data restrictions where required
```

Nếu mechanism hoặc boundary là implementation-critical UNKNOWN/OPEN:

```text
BLOCKED
```

Không tự chọn:

```text
JWT
Session
OAuth
RBAC
ABAC
```

---

# 24. NFR Readiness

NFR phải được phân loại theo implementation impact.

### Blocking NFR

Nếu NFR có thể ảnh hưởng:

```text
architecture
capacity
data strategy
security architecture
integration strategy
deployment requirements
```

và thông tin cần thiết còn UNKNOWN/OPEN:

```text
BLOCKED
```

Ví dụ:

```text
10,000 concurrent users
Architecture strategy = UNKNOWN
```

→ `BLOCKED`.

### Non-blocking NFR

Ví dụ:

```text
Animation should feel smooth.
Exact duration = UNKNOWN.
```

Không ảnh hưởng architecture/business behavior.

→ `NOT_BLOCKING`.

Skill không tự tạo benchmark.

---

# 25. Test Readiness

Mỗi implementation-critical capability phải có verification path.

Critical examples:

```text
authorization
business rule
state transition
critical validation
security behavior
payment behavior
```

Nếu critical capability không có verification strategy:

```text
BLOCKED
```

Không tự invent test case.

---

# 26. Traceability Readiness

Mỗi approved Blueprint item phải resolve:

```text
Blueprint Item
 ↓
Source Artifact
 ↓
Requirement / Rule / Constraint
```

Nếu không:

```text
UNTRACEABLE_BLUEPRINT_ITEM
→ BLOCKED
```

Technical plausibility không phải provenance.

---

# 27. Hallucinated Capability

Nếu Blueprint chứa capability không được approved source support:

```text
BLOCKED
```

Không cần chờ implementation team phát hiện.

---

# 28. Scope Integrity

So sánh:

```text
Approved Capability Set
        ↓
Blueprint Capability Set
```

Cho phép:

```text
UNCHANGED
NORMALIZATION
NARROWER REPRESENTATION
```

Không cho phép:

```text
SCOPE_EXPANSION
SEMANTIC_DRIFT
UNSUPPORTED_CAPABILITY
```

→ `BLOCKED`.

---

# 29. Semantic Capability Comparison

Không so sánh text đơn thuần.

Phải so sánh:

```text
Actor
Action
Object
Condition
State
Permission
Scope
Constraint
Outcome
```

Ví dụ:

```text
Source:
Cancel pending order.

Blueprint:
Cancel any order.
```

Khác:

```text
State constraint
```

→ `SEMANTIC_DRIFT` → `BLOCKED`.

---

# 30. Normalization Boundary

`NORMALIZATION` chỉ được phép:

```text
rename presentation label
normalize formatting
reorder equivalent information
normalize synonymous wording
```

Không được dùng normalization để:

```text
add capability
broaden actor
broaden permission
remove condition
broaden state
add workflow
add constraint
```

Nếu semantic meaning rộng hơn:

```text
SCOPE_EXPANSION / SEMANTIC_DRIFT
→ BLOCKED
```

---

# 31. Semantic Duplicate Detection

Duplicate không chỉ là duplicate ID.

Skill 11 phải kiểm tra duplicate capability bằng:

```text
Actor
Action
Object
Condition
Outcome
```

Nếu hai Blueprint artifacts:

```text
represent same capability
BUT
have conflicting contracts
```

→ `BLOCKED`.

Không tự merge.

Không tự chọn contract.

---

# 32. Partial Requirement

Nếu source là:

```text
PARTIALLY_COVERED
```

Blueprint không được biến nó thành fully specified capability.

Nếu phần thiếu implementation-critical:

```text
BLOCKED
```

---

# 33. Contradiction

Nếu implementation-critical contradiction tồn tại:

```text
BLOCKED
```

Skill không:

```text
choose
prioritize
merge
average
```

các phía.

---

# 34. Orphan and Historical Findings

Không phải mọi diagnostic đều block.

Nếu artifact:

```text
NOT_APPROVED
OUT_OF_SCOPE
DEPRECATED
```

và không affect approved Blueprint:

```text
NON_BLOCKING
```

Ngược lại, nếu orphan artifact đã lọt vào approved Blueprint:

```text
BLOCKED
```

---

# 35. Hidden Finding Scan

Skill 11 phải recursively scan:

```text
Blueprint sections
nested objects
API contracts
UI actions
Data constraints
Security definitions
NFRs
Tests
Open Issues
Unknown fields
notes that affect behavior
```

Không được chỉ scan top-level fields.

Một `UNKNOWN`/`OPEN` ẩn trong nested structure vẫn phải được dependency analysis.

---

# 36. Silent Repair Prohibition

Nếu phát hiện:

```text
missing API
missing field
missing mapping
missing permission
missing constraint
missing test
```

Skill chỉ:

```text
BLOCK
```

Không được generate replacement.

---

# 37. Blocking Classification

Finding là `BLOCKING` nếu nó có khả năng làm implementation:

```text
impossible
ambiguous
incorrect
insecure
semantically different
untraceable
unsupported
```

Finding không block nếu không ảnh hưởng implementation correctness.

---

# 38. Final Aggregation Rule

```text
IF any BLOCKING finding exists
    → BLOCKED

ELSE IF any implementation-critical dimension = PARTIAL
    → BLOCKED

ELSE
    → IMPLEMENTATION-READY
```

Không có trạng thái:

```text
READY_WITH_WARNINGS
BEST_EFFORT_READY
PROVISIONALLY_READY
```

---

# 39. Final Audit

Trước khi trả kết quả:

```text
[ ] Blueprint approved
[ ] Traceability passed
[ ] No hallucinated capability
[ ] No hallucinated requirement
[ ] No untraceable item
[ ] No scope expansion
[ ] No semantic drift
[ ] No unsupported implementation
[ ] No critical UNKNOWN
[ ] No critical OPEN
[ ] No unresolved contradiction
[ ] Requirement ready
[ ] Business rules ready
[ ] Actor/permission ready
[ ] UI ready
[ ] API ready
[ ] Data ready
[ ] Cross-layer mappings ready
[ ] Security ready
[ ] NFR ready
[ ] Critical tests ready
[ ] Semantic duplicates resolved
[ ] No silent repair
```

---

# 40. Output — READY

```text
IMPLEMENTATION READINESS v1.0

STATUS: PASSED

BLUEPRINT: APPROVED
TRACEABILITY: PASSED
SCOPE INTEGRITY: PASSED
SEMANTIC INTEGRITY: PASSED
CROSS-LAYER CONSISTENCY: PASSED
SECURITY READINESS: PASSED
TEST READINESS: PASSED

BLOCKING FINDINGS: 0

IMPLEMENTATION-READY
```

---

# 41. Output — BLOCKED

```text
IMPLEMENTATION READINESS v1.0

STATUS: BLOCKED

BLUEPRINT: APPROVED
TRACEABILITY: PASSED

BLOCKING FINDINGS: N

IMPLEMENTATION-BLOCKED
```

Mỗi finding phải có:

```text
Finding ID
Category
Severity
Blueprint Item
Source Reference
Dependency Impact
Reason
Decision
```

Skill không cung cấp implementation solution cho missing information.

---

# 42. Resolution Boundary

Skill 11 chỉ được nói:

```text
WHAT is missing
WHY it blocks
WHERE dependency exists
WHICH source level must resolve it
```

Không được nói:

```text
HOW to implement it
```

---

# 43. Implementation Handoff

Chỉ khi:

```text
IMPLEMENTATION-READY
```

mới được handoff:

```text
SYSTEM BLUEPRINT
+
TRACEABILITY MAP
+
READINESS RESULT
```

Nếu:

```text
BLOCKED
```

thì:

```text
NO IMPLEMENTATION
```

---

# 44. No Bypass

Không được bypass bằng:

```text
obvious assumption
developer knows
common practice
framework default
technical best practice
small feature
easy feature
standard behavior
```

---

# 45. Determinism

Cùng:

```text
Blueprint
Traceability
Skill version
Validation rules
```

phải tạo cùng:

```text
readiness status
blocking categories
affected items
semantic findings
```

Runtime metadata được phép khác.

---

# 46. Release Criteria

Skill 11 v1.0 chỉ release khi:

```text
IR-001 → IR-030 = PASS

Critical False Negative = 0
Critical False Positive = 0
Silent Repair = 0
Scope Bypass = 0
Hallucination Leakage = 0
Traceability Bypass = 0
Contradiction Bypass = 0
UNKNOWN Bypass = 0
OPEN Bypass = 0
Semantic Duplicate Bypass = 0
Determinism Failure = 0
```

---

# 47. Non-Goals

Skill 11 không:

* generate code;
* generate API;
* generate database;
* generate UI;
* generate architecture;
* choose framework;
* choose library;
* choose authentication mechanism;
* resolve ambiguity;
* invent requirements;
* repair Blueprint;
* expand scope;
* optimize implementation.

---

# 48. Final Principle

> **Skill 10 quyết định Blueprint chứa gì.**

> **Skill 11 quyết định Blueprint có đủ điều kiện để được triển khai hay không.**

Skill 11 không làm Blueprint đầy hơn.

Skill 11 chỉ bảo vệ implementation khỏi việc:

```text
UNKNOWN
OPEN
MISSING
CONFLICT
PARTIAL
HALLUCINATION
SCOPE EXPANSION
SEMANTIC DRIFT
```

bị biến thành code một cách âm thầm.

```text
NO GUESSING.
NO REPAIR.
NO SCOPE EXPANSION.
NO BYPASS.
```
