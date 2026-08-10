# SEXA Master Ruthless Audit — Execution Report

Total classified checks: **79**

- **PASS: 69**
- **FAIL: 1**
- **REFERENCE_REPRODUCTION: 2**
- **NOT_INDEPENDENTLY_EXECUTABLE: 3**
- **PENDING_EXPERIMENT: 1**
- **PENDING_IMPLEMENTATION: 1**
- **UNRESOLVED: 2**

## Interpretation
`PASS` means the coded arithmetic, structural, reference, or simulation target reproduced under the stated test.
It does **not** by itself establish experimental validation of the associated physical interpretation.

## Failures
### SEX-002 — Source-stated 60^18.86 = 3.47e33 reproduces within ±3e31
- Observed: `3.43504619773213e+33`
- Target: `3.47e+33`
- Note: Direct computation rounds to 3.44e33 at three significant figures.


## Non-independent / pending / unresolved
- **SIG-RAW-001 [NOT_INDEPENDENTLY_EXECUTABLE]** — 32 triality orbit statistics: arithmetic 47.50, geometric 35.97, harmonic 18.86, RMS 54.99. — The supplied PDF reports aggregate statistics but does not embed the complete raw 96-class graph/orbit excitation vector needed to regenerate them independently.
- **SIG-RAW-002 [NOT_INDEPENDENTLY_EXECUTABLE]** — Reachability growth 1→4, 2→9, 3→16, 4→24, 5→32 classes. — The raw transition graph / @uor-foundation/sigmatics package dataset is not embedded in the supplied material.
- **SIG-RAW-003 [NOT_INDEPENDENTLY_EXECUTABLE]** — R transform yields 8 independent 4-cycles; T has period 3; M partially mixes orbits. — These are reported graph properties; the complete machine-readable graph is absent from the supplied PDFs.
- **EXP-001 [PENDING_EXPERIMENT]** — ON-state Yukawa deviation via torsion-balance protocol. — The source explicitly states that no physical measurement has yet been performed.
- **HW-001 [PENDING_IMPLEMENTATION]** — FPGA/ASIC/AI-accelerator realization. — The conference paper explicitly describes hardware realization as future work, not a completed benchmark.
- **SCAN-001 [UNRESOLVED]** — SEXA_UFT_Structural_Audit(10).pdf equation-level extraction. — The 13-page source is image/scan-only under text extraction. It is hashed and inventoried but equations are not invented from unavailable machine text.
- **SIG-RAW-004 [UNRESOLVED]** — Source statement: each dimensional reduction loses ~1.42 bits per class. — The supplied text does not define the denominator or derivation for 1.42 bits/class. From the explicit 2048→632 figures, total loss is 1416 bits; 1416/96 = 14.75, so the 1.42 figure cannot be uniquely reconstructed from the stated quantities.