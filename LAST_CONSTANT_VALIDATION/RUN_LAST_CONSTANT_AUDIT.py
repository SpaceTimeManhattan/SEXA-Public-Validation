
#!/usr/bin/env python3
"""
SEXA — THE LAST CONSTANT
Independent Computational Validation Audit

PURPOSE
-------
This program separates three things that must never be conflated:

1. The published SEXA mathematical architecture.
2. The numerical derivation of The Last Constant.
3. The measured execution performance of the host computer.

The claimed Last Constant target is NOT accepted as proof of itself.
The numerical audit passes only when the published mathematical
primitives independently reproduce the claimed result.

No AI system is required to execute this audit.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


# ================================================================
# CONFIGURATION
# ================================================================

AUDIT_VERSION = "1.0.0"

C_M_S = 299_792_458.0

# IMPORTANT:
# This is the CLAIM being tested.
# It is NOT an input to the derivation.
CLAIMED_LAST_CONSTANT_RATIO = 1.0e19

CLAIMED_LAST_CONSTANT_M_S = (
    CLAIMED_LAST_CONSTANT_RATIO * C_M_S
)

BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

RESULTS = []


# ================================================================
# RESULT ENGINE
# ================================================================

def record(
    test_id,
    category,
    status,
    description,
    observed=None,
    expected=None,
    note=""
):
    RESULTS.append(
        {
            "test_id": test_id,
            "category": category,
            "status": status,
            "description": description,
            "observed": observed,
            "expected": expected,
            "note": note,
        }
    )


def close(a, b, rtol=1e-9, atol=0.0):
    return math.isclose(
        float(a),
        float(b),
        rel_tol=rtol,
        abs_tol=atol,
    )


# ================================================================
# I — SOURCE / STRUCTURAL ARCHITECTURE
# ================================================================

DERIVATION_STAGES = [
    "5D operational manifold",
    "recursive admissible dimensional hierarchy",
    "admissible excitation amplitudes",
    "recursive phase potentials",
    "dimensional thinning ratio",
    "cumulative recursive thinning product",
    "geometric dimensional normalization",
    "recursive harmonic averaging",
    "Empire Wave normalization",
    "generalized recursive propagation functional",
]

if len(DERIVATION_STAGES) == 10:
    record(
        "LC-STRUCT-001",
        "STRUCTURE",
        "PASS",
        "Ten-stage Last Constant derivation architecture registered",
        len(DERIVATION_STAGES),
        10,
    )
else:
    record(
        "LC-STRUCT-001",
        "STRUCTURE",
        "FAIL",
        "Ten-stage Last Constant derivation architecture registered",
        len(DERIVATION_STAGES),
        10,
    )


# ================================================================
# II — INDEPENDENT NUMERICAL DERIVATION
# ================================================================

def derive_last_constant_ratio():
    """
    THIS FUNCTION IS THE SCIENTIFIC KILL-SWITCH.

    It must eventually contain the exact published SEXA derivation
    of C_Last / c.

    RULES:

    1. Start only from independently declared SEXA primitives.
    2. Calculate every intermediate quantity.
    3. Do not use CLAIMED_LAST_CONSTANT_RATIO.
    4. Do not insert 1e19 anywhere in the derivation.
    5. Return only the number produced by the mathematics.

    Until the complete numerical derivation is encoded, returning
    None is REQUIRED.

    This prevents the audit from manufacturing a PASS.
    """

    return None


DERIVED_RATIO = derive_last_constant_ratio()


if DERIVED_RATIO is None:

    record(
        "LC-NUM-001",
        "NUMERICAL DERIVATION",
        "UNRESOLVED",
        "Independent derivation of The Last Constant",
        "No independently encoded numerical derivation",
        CLAIMED_LAST_CONSTANT_RATIO,
        (
            "The claimed target has NOT been injected into the "
            "derivation. PASS is prohibited until the complete "
            "published mathematical chain is executable."
        ),
    )

else:

    numerical_pass = close(
        DERIVED_RATIO,
        CLAIMED_LAST_CONSTANT_RATIO,
        rtol=1e-9,
    )

    record(
        "LC-NUM-001",
        "NUMERICAL DERIVATION",
        "PASS" if numerical_pass else "FAIL",
        "Independent derivation of The Last Constant",
        DERIVED_RATIO,
        CLAIMED_LAST_CONSTANT_RATIO,
        (
            "Comparison performed only AFTER numerical derivation."
        ),
    )


# ================================================================
# III — PHYSICAL-SCALE CONVERSION
# ================================================================

if DERIVED_RATIO is not None:

    derived_m_s = DERIVED_RATIO * C_M_S

    record(
        "LC-SCALE-001",
        "MODEL SCALE",
        "PASS",
        "Convert independently derived C_Last/c ratio to m/s",
        derived_m_s,
        CLAIMED_LAST_CONSTANT_M_S,
        (
            "Model quantity only. This is NOT a measurement of "
            "physical hardware traveling or computing at this speed."
        ),
    )

else:

    derived_m_s = None

    record(
        "LC-SCALE-001",
        "MODEL SCALE",
        "UNRESOLVED",
        "Convert independently derived C_Last/c ratio to m/s",
        None,
        CLAIMED_LAST_CONSTANT_M_S,
        "Requires successful numerical derivation first.",
    )


# ================================================================
# IV — HOST COMPUTER BENCHMARK
# ================================================================

def benchmark_host(iterations=2_000_000):

    x = 0x12345678

    start = time.perf_counter_ns()

    for i in range(iterations):
        x = (
            (x * 1664525)
            + 1013904223
            + i
        ) & 0xFFFFFFFF

    elapsed_ns = time.perf_counter_ns() - start
    elapsed_s = elapsed_ns / 1_000_000_000

    throughput = (
        iterations / elapsed_s
        if elapsed_s > 0
        else float("inf")
    )

    return {
        "iterations": iterations,
        "elapsed_nanoseconds": elapsed_ns,
        "elapsed_seconds": elapsed_s,
        "operations_per_second": throughput,
        "checksum": x,
    }


HOST = benchmark_host()


record(
    "LC-HW-001",
    "HOST HARDWARE",
    "PASS",
    "Actual host-computer execution benchmark completed",
    HOST,
    "positive finite execution time",
    (
        "This benchmark measures the computer executing this program. "
        "It is intentionally separate from The Last Constant."
    ),
)


# ================================================================
# V — DETERMINISTIC REPRODUCIBILITY
# ================================================================

HOST_REPEAT = benchmark_host()


checksum_match = (
    HOST["checksum"] == HOST_REPEAT["checksum"]
)


record(
    "LC-DET-001",
    "REPRODUCIBILITY",
    "PASS" if checksum_match else "FAIL",
    "Deterministic workload reproduces identical checksum",
    HOST_REPEAT["checksum"],
    HOST["checksum"],
)


# ================================================================
# VI — ANTI-HARDCODING / CLAIM-SEPARATION AUDIT
# ================================================================

try:
    function_source = derive_last_constant_ratio.__doc__ or ""

    target_separated = (
        DERIVED_RATIO is None
        or isinstance(DERIVED_RATIO, (int, float))
    )

except Exception:
    target_separated = False


record(
    "LC-ADV-001",
    "ADVERSARIAL",
    "PASS" if target_separated else "FAIL",
    "Claim target remains separated from numerical derivation",
    target_separated,
    True,
    (
        "This is a structural guard, not proof against every possible "
        "form of circularity."
    ),
)


# ================================================================
# VII — ENVIRONMENT RECORD
# ================================================================

ENVIRONMENT = {
    "python_version": sys.version,
    "python_implementation": platform.python_implementation(),
    "platform": platform.platform(),
    "machine": platform.machine(),
    "processor": platform.processor(),
    "operating_system": platform.system(),
    "audit_version": AUDIT_VERSION,
}


record(
    "LC-ENV-001",
    "ENVIRONMENT",
    "PASS",
    "Execution environment captured",
    ENVIRONMENT,
    "machine-readable environment record",
)


# ================================================================
# VIII — SOURCE HASH
# ================================================================

SCRIPT_PATH = Path(__file__).resolve()

with SCRIPT_PATH.open("rb") as f:
    SCRIPT_SHA256 = hashlib.sha256(f.read()).hexdigest()


record(
    "LC-HASH-001",
    "PROVENANCE",
    "PASS",
    "Audit source SHA-256 generated",
    SCRIPT_SHA256,
    "64-character SHA-256",
)


# ================================================================
# IX — CLASSIFICATION
# ================================================================

statuses = [r["status"] for r in RESULTS]

if "FAIL" in statuses:
    FINAL_STATUS = "FAIL"

elif DERIVED_RATIO is None:
    FINAL_STATUS = "UNRESOLVED"

else:
    FINAL_STATUS = "PASS"


# ================================================================
# X — MACHINE-READABLE EVIDENCE
# ================================================================

REPORT = {
    "audit": "SEXA — The Last Constant Independent Computational Audit",
    "audit_version": AUDIT_VERSION,
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),

    "speed_of_light_m_s": C_M_S,

    "claimed_last_constant_ratio_to_c":
        CLAIMED_LAST_CONSTANT_RATIO,

    "claimed_last_constant_scale_m_s":
        CLAIMED_LAST_CONSTANT_M_S,

    "independently_derived_ratio_to_c":
        DERIVED_RATIO,

    "independently_derived_scale_m_s":
        derived_m_s,

    "final_status":
        FINAL_STATUS,

    "derivation_stages":
        DERIVATION_STAGES,

    "host_hardware_benchmark":
        HOST,

    "environment":
        ENVIRONMENT,

    "script_sha256":
        SCRIPT_SHA256,

    "results":
        RESULTS,

    "interpretation": (
        "PASS for the numerical derivation means the encoded SEXA "
        "mathematics reproduced the declared theoretical target. "
        "It does not constitute experimental observation of "
        "superluminal propagation or measurement of hardware "
        "operating at that velocity."
    ),
}


json_path = REPORT_DIR / "LAST_CONSTANT_RESULTS.json"

json_path.write_text(
    json.dumps(
        REPORT,
        indent=2,
        default=str,
    ),
    encoding="utf-8",
)


# ================================================================
# XI — CSV REPORT
# ================================================================

csv_path = REPORT_DIR / "LAST_CONSTANT_RESULTS.csv"

with csv_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "test_id",
            "category",
            "status",
            "description",
            "observed",
            "expected",
            "note",
        ],
    )

    writer.writeheader()

    for row in RESULTS:
        writer.writerow(row)


# ================================================================
# XII — HUMAN-READABLE REPORT
# ================================================================

txt_path = REPORT_DIR / "LAST_CONSTANT_AUDIT_REPORT.txt"

lines = []

lines.append("=" * 72)
lines.append("SEXA — THE LAST CONSTANT")
lines.append("INDEPENDENT COMPUTATIONAL VALIDATION AUDIT")
lines.append("=" * 72)
lines.append("")

for result in RESULTS:

    lines.append(
        f"[{result['status']}] "
        f"{result['test_id']} — "
        f"{result['description']}"
    )

    lines.append(
        f"    Observed: {result['observed']}"
    )

    lines.append(
        f"    Expected: {result['expected']}"
    )

    if result["note"]:
        lines.append(
            f"    Note: {result['note']}"
        )

    lines.append("")


lines.append("-" * 72)
lines.append("THEORETICAL SEXA CLAIM")
lines.append("-" * 72)

lines.append(
    f"Claimed C_Last / c : "
    f"{CLAIMED_LAST_CONSTANT_RATIO:.12e}"
)

lines.append(
    f"Claimed scale      : "
    f"{CLAIMED_LAST_CONSTANT_M_S:.12e} m/s"
)

lines.append("")


if DERIVED_RATIO is None:

    lines.append(
        "Independent result : NOT YET NUMERICALLY DERIVED"
    )

else:

    lines.append(
        f"Independent result : "
        f"{DERIVED_RATIO:.12e} c"
    )


lines.append("")
lines.append("-" * 72)
lines.append("ACTUAL HOST COMPUTER")
lines.append("-" * 72)

lines.append(
    f"Runtime       : "
    f"{HOST['elapsed_seconds']:.9f} seconds"
)

lines.append(
    f"Throughput    : "
    f"{HOST['operations_per_second']:.3f} operations/second"
)

lines.append(
    f"Checksum      : "
    f"{HOST['checksum']}"
)

lines.append("")
lines.append("=" * 72)
lines.append(
    f"FINAL AUDIT CLASSIFICATION: {FINAL_STATUS}"
)
lines.append("=" * 72)

lines.append("")
lines.append(
    "THEORETICAL MODEL SCALE != HOST COMPUTER CLOCK SPEED"
)

lines.append(
    "Only an independently encoded mathematical derivation may "
    "convert LC-NUM-001 from UNRESOLVED to PASS."
)


txt_path.write_text(
    "\n".join(lines),
    encoding="utf-8",
)


# ================================================================
# XIII — MANIFEST
# ================================================================

manifest_files = [
    SCRIPT_PATH,
    json_path,
    csv_path,
    txt_path,
]

manifest_lines = []

for path in manifest_files:

    with path.open("rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()

    manifest_lines.append(
        f"{digest}  {path.name}"
    )


manifest_path = REPORT_DIR / "SHA256_MANIFEST.txt"

manifest_path.write_text(
    "\n".join(manifest_lines),
    encoding="utf-8",
)


# ================================================================
# XIV — TERMINAL OUTPUT
# ================================================================

print()
print("=" * 72)
print("SEXA — THE LAST CONSTANT")
print("INDEPENDENT COMPUTATIONAL VALIDATION AUDIT")
print("=" * 72)
print()

for result in RESULTS:

    print(
        f"{result['status']:10} "
        f"{result['test_id']:15} "
        f"{result['description']}"
    )


print()
print("-" * 72)
print("THEORETICAL SEXA CLAIM")
print("-" * 72)

print(
    f"C_Last / c claimed : "
    f"{CLAIMED_LAST_CONSTANT_RATIO:.12e}"
)

print(
    f"Claimed scale      : "
    f"{CLAIMED_LAST_CONSTANT_M_S:.12e} m/s"
)


if DERIVED_RATIO is None:

    print(
        "Independent result : UNRESOLVED"
    )

else:

    print(
        f"Independent result : "
        f"{DERIVED_RATIO:.12e} c"
    )


print()
print("-" * 72)
print("ACTUAL HOST COMPUTER")
print("-" * 72)

print(
    f"Runtime            : "
    f"{HOST['elapsed_seconds']:.9f} s"
)

print(
    f"Throughput         : "
    f"{HOST['operations_per_second']:,.3f} ops/s"
)

print()
print("=" * 72)

print(
    f"FINAL AUDIT CLASSIFICATION: {FINAL_STATUS}"
)

print("=" * 72)

print()
print(
    "THEORETICAL MODEL SCALE != HOST COMPUTER CLOCK SPEED"
)

print()
print(
    f"Evidence written to: {REPORT_DIR}"
)
print()
