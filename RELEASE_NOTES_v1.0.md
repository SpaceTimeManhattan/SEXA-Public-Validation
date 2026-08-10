# SEXA Master Audit v1.0

Built from **14 supplied PDF files**.

Machine extraction inventory:
- Numerical-context lines: **1698**
- Equation/relationship-like lines: **227**
- Exact duplicate source groups: **1**
- Scan/image-only sources under text extraction: **1**

Master executable audit result:
- PASS: **69**
- FAIL: **1**
- REFERENCE_REPRODUCTION: **2**
- NOT_INDEPENDENTLY_EXECUTABLE: **3**
- PENDING_EXPERIMENT: **1**
- PENDING_IMPLEMENTATION: **1**
- UNRESOLVED: **2**
- TOTAL CLASSIFIED CHECKS: **79**

The single executable numerical failure is the source-stated `60^18.86 = 3.47×10^33` at the declared audit tolerance; direct computation yields `3.4350461977321293×10^33`, which rounds to `3.44×10^33` at three significant figures.

This release intentionally preserves pending and non-independent classifications rather than inflating them into PASS results.
