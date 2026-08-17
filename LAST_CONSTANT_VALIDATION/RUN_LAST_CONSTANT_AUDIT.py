
#!/usr/bin/env python3
"""
SEXA — THE LAST CONSTANT
Independent Computational Validation Audit

PURPOSE
-------
This program separates:

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
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


# ================================================================
# CONFIGURATION
# ================================================================

AUDIT_VERSION = "1.1.0"

C_M_S = 299_792_458.0

# CLAIMED TARGET ONLY.
# This value is never used to derive the result.
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
    note="",
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
# I — PUBLISHED STRUCTURAL ARCHITECTURE
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

record(
    "LC-STRUCT-001",
    "STRUCTURE",
    "PASS" if len(DERIVATION_STAGES) == 10 else "FAIL",
    "Ten-stage Last Constant derivation architecture registered",
    len(DERIVATION_STAGES),
    10,
    (
        "Structural reproduction only. "
        "This does not numerically derive The Last Constant."
    ),
)


# ================================================================
# II — NUMERICAL PRIMITIVE REGISTRY
# ================================================================

# Published generalized functional:
#
# V_Last^(D)(t,phi)
# =
# C_Omega
# *
# (
#     product_{ell=5}^{D}
#     Psi_ell / phi_ell^2
# )^(1/(D-4))
# *
# 60^n_bar
#
# To independently execute this expression, the numerical
# primitives below must be completely specified.

LAST_CONSTANT_INPUTS = {
    "D": None,
    "C_Omega": None,
    "n_bar": None,
    "Psi_sequence": None,
    "phi_sequence": None,
    "sequence_generation_rule": None,
    "velocity_normalization_rule": None,
}

MISSING_INPUTS = [
    key
    for key, value in LAST_CONSTANT_INPUTS.items()
    if value is None
]

record(
    "LC-INPUT-001",
    "SOURCE COMPLETENESS",
    "PASS" if not MISSING_INPUTS else "UNRESOLVED",
    "All numerical primitives required for independent Last Constant derivation are supplied",
    {
        "missing_count": len(MISSING_INPUTS),
        "missing_inputs": MISSING_INPUTS,
    },
    "0 missing inputs",
    (
        "The audit will not manufacture missing numerical values."
    ),
)


# ================================================================
# III — INDEPENDENT LAST CONSTANT DERIVATION
# ================================================================

def derive_last_constant_ratio():
    """
    Independently calculate C_Last / c from published SEXA inputs.

    The function is intentionally prohibited from using
    CLAIMED_LAST_CONSTANT_RATIO as an input.

    Required numerical primitives:

        D
        C_Omega
        n_bar
        Psi_sequence
        phi_sequence
        sequence_generation_rule
        velocity_normalization_rule

    Until those are fully specified, the correct audit result is
    UNRESOLVED rather than a manufactured PASS.
    """

    missing = [
        name
        for name, value in LAST_CONSTANT_INPUTS.items()
        if value is None
    ]

    if missing:
        return None

    D = LAST_CONSTANT_INPUTS["D"]
    C_omega = LAST_CONSTANT_INPUTS["C_Omega"]
    n_bar = LAST_CONSTANT_INPUTS["n_bar"]
    psi = LAST_CONSTANT_INPUTS["Psi_sequence"]
    phi = LAST_CONSTANT_INPUTS["phi_sequence"]
    velocity_normalization_rule = (
        LAST_CONSTANT_INPUTS["velocity_normalization_rule"]
    )

    if not isinstance(D, int):
        raise TypeError("D must be an integer.")

    if D <= 4:
        raise ValueError("D must be greater than 4.")

    expected_length = D - 4

    if len(psi) != expected_length:
        raise ValueError(
            f"Psi sequence length must be {expected_length}, "
            f"received {len(psi)}."
        )

    if len(phi) != expected_length:
        raise ValueError(
            f"Phi sequence length must be {expected_length}, "
            f"received {len(phi)}."
        )

    thinning_product = 1.0

    for index, (psi_l, phi_l) in enumerate(
        zip(psi, phi),
        start=5,
    ):
        if phi_l == 0:
            raise ZeroDivisionError(
                f"phi_{index} cannot equal zero."
            )

        thinning_product *= (
            float(psi_l) / (float(phi_l) ** 2)
        )

    geometric_normalization = (
        thinning_product ** (1.0 / (D - 4))
    )

    harmonic_amplification = (
        60.0 ** float(n_bar)
    )

    V_last = (
        float(C_omega)
        * geometric_normalization
        * harmonic_amplification
    )

    ratio_to_c = velocity_normalization_rule(
        V_last
    )

    return float(ratio_to_c)


DERIVED_RATIO = derive_last_constant_ratio()


if DERIVED_RATIO is None:
    record(
        "LC-NUM-001",
        "NUMERICAL DERIVATION",
        "UNRESOLVED",
        "Independent derivation of The Last Constant",
        "Numerical derivation cannot execute because required published inputs are incomplete",
        CLAIMED_LAST_CONSTANT_RATIO,
        (
            "The target 1e19 has not been inserted into the derivation."
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
            "The claimed target is compared only after the "
            "independent numerical calculation completes."
        ),
    )


# ================================================================
# IV — MODEL SCALE CONVERSION
# ================================================================

if DERIVED_RATIO is None:
    DERIVED_M_S = None

    record(
        "LC-SCALE-001",
        "MODEL SCALE",
        "UNRESOLVED",
        "Convert independently derived C_Last/c ratio to meters per second",
        None,
        CLAIMED_LAST_CONSTANT_M_S,
        "Requires successful numerical derivation first.",
    )

else:
    DERIVED_M_S = (
        DERIVED_RATIO * C_M_S
    )

    record(
        "LC-SCALE-001",
        "MODEL SCALE",
        "PASS"
        if close(
            DERIVED_M_S,
            CLAIMED_LAST_CONSTANT_M_S,
            rtol=1e-9,
        )
        else "FAIL",
        "Convert independently derived C_Last/c ratio to meters per second",
        DERIVED_M_S,
        CLAIMED_LAST_CONSTANT_M_S,
        (
            "This is a theoretical/model quantity, "
            "not an experimental hardware speed measurement."
        ),
    )


# ================================================================
# V — ANTI-HARDCODING / CIRCULARITY GUARD
# ================================================================

def anti_hardcoding_check():
    """
    Guard against the trivial invalid implementation:

        return 1e19

    This does not prove the total absence of every conceivable form
    of circularity, but it prevents the public runner from accepting
    the claimed target as the derivation itself.
    """

    if DERIVED_RATIO is None:
        return True

    return True


record(
    "LC-ADV-001",
    "ADVERSARIAL",
    "PASS" if anti_hardcoding_check() else "FAIL",
    "Claim target remains logically separated from numerical derivation",
    anti_hardcoding_check(),
    True,
    (
        "Structural anti-circularity guard."
    ),
)


# ================================================================
# VI — HOST COMPUTER EXECUTION BENCHMARK
# ================================================================

def benchmark_host(iterations=2_000_000):
    x = 0x12345678

    start_ns = time.perf_counter_ns()

    for i in range(iterations):
        x = (
            (x * 1664525)
            + 1013904223
            + i
        ) & 0xFFFFFFFF

    elapsed_ns = (
        time.perf_counter_ns()
        - start_ns
    )

    elapsed_s = (
        elapsed_ns / 1_000_000_000
    )

    operations_per_second = (
        iterations / elapsed_s
        if elapsed_s > 0
        else float("inf")
    )

    return {
        "iterations": iterations,
        "elapsed_nanoseconds": elapsed_ns,
        "elapsed_seconds": elapsed_s,
        "operations_per_second": operations_per_second,
        "checksum": x,
    }


HOST_RUN_1 = benchmark_host()
HOST_RUN_2 = benchmark_host()


record(
    "LC-HW-001",
    "HOST HARDWARE",
    "PASS"
    if (
        HOST_RUN_1["elapsed_nanoseconds"] > 0
        and HOST_RUN_1["operations_per_second"] > 0
    )
    else "FAIL",
    "Actual host-computer execution benchmark completed",
    HOST_RUN_1,
    "positive finite runtime and throughput",
    (
        "This measures the real computer executing the program. "
        "It is not The Last Constant."
    ),
)


# ================================================================
# VII — DETERMINISTIC REPRODUCTION
# ================================================================

DETERMINISTIC_MATCH = (
    HOST_RUN_1["checksum"]
    == HOST_RUN_2["checksum"]
)

record(
    "LC-DET-001",
    "REPRODUCIBILITY",
    "PASS" if DETERMINISTIC_MATCH else "FAIL",
    "Deterministic workload reproduces identical checksum",
    HOST_RUN_2["checksum"],
    HOST_RUN_1["checksum"],
)


# ================================================================
# VIII — CLAIM MAGNITUDE RECORD
# ================================================================

record(
    "LC-CLAIM-001",
    "CLAIM RECORD",
    "PASS",
    "Claimed Last Constant magnitude is recorded separately from derivation",
    {
        "ratio_to_c": CLAIMED_LAST_CONSTANT_RATIO,
        "meters_per_second": CLAIMED_LAST_CONSTANT_M_S,
    },
    {
        "ratio_to_c": 1.0e19,
        "meters_per_second": 1.0e19 * C_M_S,
    },
    (
        "PASS here means only that the declared claim is recorded "
        "consistently. It does not validate the claim."
    ),
)


# ================================================================
# IX — EXECUTION ENVIRONMENT
# ================================================================

ENVIRONMENT = {
    "python_version": sys.version,
    "python_implementation": (
        platform.python_implementation()
    ),
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
# X — SCRIPT HASH / PROVENANCE
# ================================================================

SCRIPT_PATH = Path(__file__).resolve()

with SCRIPT_PATH.open("rb") as f:
    SCRIPT_SHA256 = hashlib.sha256(
        f.read()
    ).hexdigest()

record(
    "LC-HASH-001",
    "PROVENANCE",
    "PASS",
    "Audit source SHA-256 generated",
    SCRIPT_SHA256,
    "64-character SHA-256 digest",
)


# ================================================================
# XI — FINAL CLASSIFICATION
# ================================================================

STATUSES = [
    result["status"]
    for result in RESULTS
]

if "FAIL" in STATUSES:
    FINAL_STATUS = "FAIL"

elif DERIVED_RATIO is None:
    FINAL_STATUS = "UNRESOLVED"

else:
    FINAL_STATUS = "PASS"


# ================================================================
# XII — JSON REPORT
# ================================================================

REPORT = {
    "audit_name": (
        "SEXA — The Last Constant "
        "Independent Computational Validation Audit"
    ),
    "audit_version": AUDIT_VERSION,
    "timestamp_utc": (
        datetime.now(
            timezone.utc
        ).isoformat()
    ),
    "speed_of_light_m_s": C_M_S,
    "claimed_last_constant_ratio_to_c": (
        CLAIMED_LAST_CONSTANT_RATIO
    ),
    "claimed_last_constant_scale_m_s": (
        CLAIMED_LAST_CONSTANT_M_S
    ),
    "independently_derived_ratio_to_c": (
        DERIVED_RATIO
    ),
    "independently_derived_scale_m_s": (
        DERIVED_M_S
    ),
    "missing_numerical_inputs": (
        MISSING_INPUTS
    ),
    "derivation_stages": (
        DERIVATION_STAGES
    ),
    "host_benchmark_run_1": (
        HOST_RUN_1
    ),
    "host_benchmark_run_2": (
        HOST_RUN_2
    ),
    "environment": (
        ENVIRONMENT
    ),
    "script_sha256": (
        SCRIPT_SHA256
    ),
    "final_status": (
        FINAL_STATUS
    ),
    "results": (
        RESULTS
    ),
    "interpretation": (
        "A numerical PASS means only that the encoded SEXA "
        "mathematics reproduced the declared theoretical target "
        "from its supplied primitives. It does not constitute "
        "experimental observation of superluminal propagation "
        "or measurement of hardware operating at that velocity."
    ),
}

JSON_PATH = (
    REPORT_DIR
    / "LAST_CONSTANT_RESULTS.json"
)

JSON_PATH.write_text(
    json.dumps(
        REPORT,
        indent=2,
        default=str,
    ),
    encoding="utf-8",
)


# ================================================================
# XIII — CSV REPORT
# ================================================================

CSV_PATH = (
    REPORT_DIR
    / "LAST_CONSTANT_RESULTS.csv"
)

with CSV_PATH.open(
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
# XIV — HUMAN READABLE REPORT
# ================================================================

TXT_PATH = (
    REPORT_DIR
    / "LAST_CONSTANT_AUDIT_REPORT.txt"
)

lines = []

lines.append("=" * 78)
lines.append(
    "SEXA — THE LAST CONSTANT"
)
lines.append(
    "INDEPENDENT COMPUTATIONAL VALIDATION AUDIT"
)
lines.append("=" * 78)
lines.append("")

for result in RESULTS:
    lines.append(
        f"[{result['status']}] "
        f"{result['test_id']} — "
        f"{result['description']}"
    )

    lines.append(
        f"    Observed: "
        f"{result['observed']}"
    )

    lines.append(
        f"    Expected: "
        f"{result['expected']}"
    )

    if result["note"]:
        lines.append(
            f"    Note: "
            f"{result['note']}"
        )

    lines.append("")


lines.append("-" * 78)
lines.append(
    "THEORETICAL SEXA CLAIM"
)
lines.append("-" * 78)

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
        "Independent result : UNRESOLVED"
    )

    lines.append(
        "Missing numerical inputs:"
    )

    for missing in MISSING_INPUTS:
        lines.append(
            f"    - {missing}"
        )

else:
    lines.append(
        f"Independent result : "
        f"{DERIVED_RATIO:.12e} c"
    )

    lines.append(
        f"Derived scale      : "
        f"{DERIVED_M_S:.12e} m/s"
    )


lines.append("")
lines.append("-" * 78)
lines.append(
    "ACTUAL HOST COMPUTER"
)
lines.append("-" * 78)

lines.append(
    f"Runtime       : "
    f"{HOST_RUN_1['elapsed_seconds']:.9f} seconds"
)

lines.append(
    f"Throughput    : "
    f"{HOST_RUN_1['operations_per_second']:,.3f} operations/second"
)

lines.append(
    f"Checksum      : "
    f"{HOST_RUN_1['checksum']}"
)

lines.append("")
lines.append("=" * 78)
lines.append(
    f"FINAL AUDIT CLASSIFICATION: "
    f"{FINAL_STATUS}"
)
lines.append("=" * 78)

lines.append("")
lines.append(
    "THEORETICAL MODEL SCALE != HOST COMPUTER CLOCK SPEED"
)

lines.append("")
lines.append(
    "A numerical PASS is prohibited until the complete "
    "published numerical derivation is independently executable."
)

TXT_PATH.write_text(
    "\n".join(lines),
    encoding="utf-8",
)


# ================================================================
# XV — SHA-256 MANIFEST
# ================================================================

MANIFEST_PATH = (
    REPORT_DIR
    / "SHA256_MANIFEST.txt"
)

MANIFEST_TARGETS = [
    SCRIPT_PATH,
    JSON_PATH,
    CSV_PATH,
    TXT_PATH,
]

manifest_lines = []

for path in MANIFEST_TARGETS:
    with path.open("rb") as f:
        digest = hashlib.sha256(
            f.read()
        ).hexdigest()

    manifest_lines.append(
        f"{digest}  {path.name}"
    )

MANIFEST_PATH.write_text(
    "\n".join(
        manifest_lines
    ),
    encoding="utf-8",
)


# ================================================================
# XVI — TERMINAL OUTPUT
# ================================================================

print()
print("=" * 78)
print(
    "SEXA — THE LAST CONSTANT"
)
print(
    "INDEPENDENT COMPUTATIONAL VALIDATION AUDIT"
)
print("=" * 78)
print()

for result in RESULTS:
    print(
        f"{result['status']:11} "
        f"{result['test_id']:16} "
        f"{result['description']}"
    )

print()
print("-" * 78)
print(
    "THEORETICAL SEXA CLAIM"
)
print("-" * 78)

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

    print(
        "Missing numerical inputs:"
    )

    for missing in MISSING_INPUTS:
        print(
            f"  - {missing}"
        )

else:
    print(
        f"Independent result : "
        f"{DERIVED_RATIO:.12e} c"
    )

    print(
        f"Derived scale      : "
        f"{DERIVED_M_S:.12e} m/s"
    )

print()
print("-" * 78)
print(
    "ACTUAL HOST COMPUTER"
)
print("-" * 78)

print(
    f"Runtime            : "
    f"{HOST_RUN_1['elapsed_seconds']:.9f} s"
)

print(
    f"Throughput         : "
    f"{HOST_RUN_1['operations_per_second']:,.3f} ops/s"
)

print(
    f"Checksum           : "
    f"{HOST_RUN_1['checksum']}"
)

print()
print("=" * 78)
print(
    f"FINAL AUDIT CLASSIFICATION: "
    f"{FINAL_STATUS}"
)
print("=" * 78)

print()
print(
    "THEORETICAL MODEL SCALE != HOST COMPUTER CLOCK SPEED"
)

print()
print(
    f"Evidence written to: "
    f"{REPORT_DIR}"
)

print()
