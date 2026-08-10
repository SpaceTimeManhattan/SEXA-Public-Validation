# SEXA Master Public Audit

This repository is the **audience-facing reproducibility package** for the SEXA framework.

## One-command run

### Windows
Double-click:

`RUN_WINDOWS.bat`

### macOS / Linux
Run:

```bash
bash RUN_MAC_LINUX.sh
```

### Any Python 3 installation
```bash
python RUN_SEXA_MASTER_AUDIT.py
```

No third-party Python packages are required.

## What this package does

The runner audits the supplied SEXA stack at several distinct levels:

1. Core dimensional and sexagesimal arithmetic.
2. Sigmatics cascade arithmetic, ratios, information-retention values, and 5-bit reconstruction.
3. Γ six-stage kill-switch semantics.
4. Horizon/discrete-geometry convergence stress tests.
5. Standard GR/QFT reference reproductions used by the SEXA compatibility papers.
6. Activation-threshold consistency.
7. Deterministic recursive-computation stress tests.
8. Source provenance, SHA-256 hashes, exact duplicate detection, and scan-only source detection.
9. Explicit classification of claims that cannot be independently regenerated from the supplied PDFs.
10. Explicit separation of computational survivability from experimental confirmation.

## Result classes

- **PASS** — the coded target reproduced.
- **FAIL** — the stated numerical target failed its declared tolerance.
- **REFERENCE_REPRODUCTION** — a reported benchmark is retained as a reference because the source does not provide enough case-specific input data for an independent derivation.
- **NOT_INDEPENDENTLY_EXECUTABLE** — the paper reports an aggregate/result but the complete raw dataset or graph needed to regenerate it was not supplied.
- **PENDING_EXPERIMENT** — a physical/observational claim remains experimentally untested in the supplied materials.
- **PENDING_IMPLEMENTATION** — hardware or engineering realization is described as future work.
- **UNRESOLVED** — source material could not be made machine-executable without inventing missing information.

## Ruthless-audit rule

This repository does **not** convert a mathematical or computational PASS into a claim of experimental proof. It also does not hide discrepancies. For example, the suite directly recomputes `60^18.86` and separately tests the source-stated `3.47×10^33` figure.

## Repository files

- `RUN_SEXA_MASTER_AUDIT.py` — master public runner
- `data/source_manifest.json` — source hashes and extraction inventory
- `data/duplicate_source_groups.json` — exact duplicate-source groups
- `data/evidence_classifications.json` — non-executable and pending claims
- `data/all_numeric_mentions.csv` — every machine-extracted numerical mention with source/line context across the uploaded stack
- `data/equation_like_lines.csv` — machine-extracted equation/relationship lines
- `evidence/extracted_text/` — text extraction for each supplied PDF, bound to the source manifest hashes
- `reports/MASTER_AUDIT_REPORT.md` — generated human-readable report
- `reports/master_results.csv` — generated machine-readable table
- `reports/master_results.json` — generated full result objects
- `docs/AUDIENCE_HANDOFF.md` — short instructions for the Australia audience

## Source integrity

The source manifest binds the audit to the exact uploaded PDF bytes using SHA-256 hashes. Exact duplicate documents are identified so they are not treated as independent evidence.

## Important scope limitation

The supplied Sigmatics PDF reports aggregate orbit statistics and reachability data, but the complete machine-readable 96-class transition graph / excitation vector is not embedded in the supplied PDF stack. Those claims are therefore **not labeled as independently regenerated** by this package.

Likewise, the conference hardware paper describes FPGA/ASIC/AI-accelerator realization as future work. This package tests deterministic computational properties but does not relabel planned hardware as completed hardware validation.
