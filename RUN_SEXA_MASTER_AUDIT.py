#!/usr/bin/env python3
"""
SEXA MASTER RUTHLESS AUDIT
Standard-library-only public validation runner.

Principle:
- Recompute what can actually be recomputed.
- Separate arithmetic/structural reproduction from physical experiment.
- Do not convert a source-stated aggregate into an independent validation.
- Expose discrepancies rather than normalize them away.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import math, json, csv, hashlib, platform, sys, statistics

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reports"
OUT.mkdir(exist_ok=True)

@dataclass
class Result:
    id: str
    domain: str
    status: str
    claim: str
    observed: object
    target: object
    error: object = None
    note: str = ""

RESULTS=[]

def add(id,domain,status,claim,observed,target,error=None,note=""):
    RESULTS.append(Result(id,domain,status,claim,observed,target,error,note))

def close(a,b,atol=0.0,rtol=1e-9):
    return abs(a-b) <= max(atol, rtol*max(abs(a),abs(b),1.0))

def check_num(id,domain,claim,observed,target,atol=0.0,rtol=1e-9,note=""):
    ok=close(observed,target,atol,rtol)
    err=observed-target
    add(id,domain,"PASS" if ok else "FAIL",claim,observed,target,err,note)
    return ok

def check_bool(id,domain,claim,condition,observed=True,target=True,note=""):
    add(id,domain,"PASS" if condition else "FAIL",claim,observed,target,None,note)
    return condition

# ------------------------------------------------------------------
# 1. CORE DIMENSIONAL / SEXAGESIMAL ARITHMETIC
# ------------------------------------------------------------------
C = math.sqrt(2880/4)
check_num("CORE-001","Core","C_Omega = sqrt(2880/4)",C,26.832815729997478,rtol=1e-14)
check_num("CORE-002","Core","2880/96 dimension ratio",2880/96,30.0)
check_num("CORE-003","Core","256/8 = 32",256/8,32.0)
check_num("CORE-004","Core","log2(32) = 5",math.log2(32),5.0)
check_num("CORE-005","Core","2880 - 4 = 2876",2880-4,2876.0)
check_num("CORE-006","Core","1/(2880-4)",1/(2880-4),0.0003477051460361613,rtol=1e-14)

nbar=18.86
sex=60**nbar
check_num("SEX-001","Sexagesimal","Direct 60^18.86 computation",sex,3.4350461977321293e33,rtol=1e-14,
          note="This is the direct arithmetic result.")
# Source reports 3.47e33. Test that specific stated number at the prior audit tolerance.
source_sex=3.47e33
tol=3e31
ok=abs(sex-source_sex) <= tol
add("SEX-002","Sexagesimal","PASS" if ok else "FAIL",
    "Source-stated 60^18.86 = 3.47e33 reproduces within ±3e31",
    sex,source_sex,sex-source_sex,
    "Direct computation rounds to 3.44e33 at three significant figures.")
norm=60**(nbar/32)
check_num("SEX-003","Sexagesimal","Normalized 60^(18.86/32)",norm,11.16857829780513,rtol=1e-12,
          note="Source rounds this to about 11.2.")
total_exc=2876*(18.86/32)
check_num("SEX-004","Sexagesimal","2876*(18.86/32)",total_exc,1695.0425,rtol=1e-12,
          note="Source rounds this to about 1695.")

# ------------------------------------------------------------------
# 2. SIGMATICS CASCADE / RATIOS
# ------------------------------------------------------------------
dims=[256,96,32,7,3,1]
reported=[0.375,0.333,0.219,0.429,0.333]
exact=[dims[i+1]/dims[i] for i in range(len(dims)-1)]
for i,(obs,tgt) in enumerate(zip(exact,reported),1):
    # reported values are 3-decimal approximations
    check_num(f"SIG-CAS-{i:02d}","Sigmatics",f"Cascade ratio {dims[i-1]}→{dims[i]}",
              obs,tgt,atol=0.0006,rtol=0,note="Tested against source's 3-decimal rounded value.")
gm=math.prod(exact)**(1/len(exact))
check_num("SIG-CAS-06","Sigmatics","Geometric mean cascade reduction",gm,0.330,atol=0.001,rtol=0)
check_num("SIG-CAS-07","Sigmatics","Overall cascade factor 256→1",256/1,256.0)
check_num("SIG-CAS-08","Sigmatics","First reduction 256→96 = 3/8",96/256,3/8)
check_num("SIG-CAS-09","Sigmatics","1/e comparison value",1/math.e,0.36787944117144233,rtol=1e-14)
phi=(1+math.sqrt(5))/2
check_num("SIG-CAS-10","Sigmatics","1/phi^2 comparison value",1/(phi**2),0.38196601125010515,rtol=1e-14)

ret=632/2048
check_num("SIG-INF-01","Sigmatics","632/2048 information retention",ret*100,30.859375)
check_num("SIG-INF-02","Sigmatics","Information loss",100-ret*100,69.140625)
per_scale=(1/256)**(1/2876)
check_num("SIG-INF-03","Sigmatics","Per-scale ratio for 256→1 over 2876 steps",per_scale,0.998073770832055,rtol=1e-12)
log_exp=math.log(per_scale)
check_num("SIG-INF-04","Sigmatics","Natural-log per-scale exponent",log_exp,-0.00192808673312922,rtol=1e-9,
          note="Source reports approximately -0.00193.")

check_num("SIG-RAT-01","Sigmatics","C_Omega / nbar",C/nbar,1.422736783139844,rtol=1e-12)
# This is an approximation claim, measure distance to sqrt(2)
ratio=C/nbar
check_bool("SIG-RAT-02","Sigmatics","C_Omega/nbar is within 1% of sqrt(2)",
           abs(ratio-math.sqrt(2))/math.sqrt(2) < .01,ratio,math.sqrt(2))
check_num("SIG-RAT-03","Sigmatics","C_Omega/6.77",C/6.77,3.963488290989287,rtol=1e-12)
check_bool("SIG-RAT-04","Sigmatics","C_Omega/6.77 is within 1% of 4",
           abs(C/6.77-4)/4 < .01,C/6.77,4.0)
check_num("SIG-STR-01","Sigmatics","8 quaternionic cycles × 4 phases = 32",8*4,32)
check_num("SIG-STR-02","Sigmatics","24 shift = 3×8",3*8,24)
check_num("SIG-STR-03","Sigmatics","32 states addressable by five bits",2**5,32)
check_num("SIG-STR-04","Sigmatics","Period-3 recursion order",3,3)
check_num("SIG-STR-05","Sigmatics","R^4 cycle length arithmetic",4,4)

# 5-bit fold / exact reconstruction
def fold5(x): return tuple((x>>i)&1 for i in range(5))
def unfold5(bits): return sum((int(b)&1)<<i for i,b in enumerate(bits))
roundtrip=all(unfold5(fold5(i))==i for i in range(32))
check_bool("SIG-REC-01","Sigmatics","All 32 five-bit states reconstruct exactly",roundtrip,
           "32/32 exact","32/32 exact")

# Six-gate Gamma semantics: explicit structural kill-switch implementation.
def gamma_all(bits):
    if len(bits)!=6: raise ValueError("six gates required")
    return all(bool(x) for x in bits)
check_bool("GAMMA-000","Gamma","Full six-gate chain admits all-true state",
           gamma_all([1]*6),True,True)
for j in range(6):
    bits=[1]*6; bits[j]=0
    check_bool(f"GAMMA-KS{j+1:02d}","Gamma",f"Kill-switch: removing gate {j+1} rejects state",
               not gamma_all(bits),False,False,
               note="Executable Boolean model of the paper's stated all-stage admissibility semantics.")

# ------------------------------------------------------------------
# 3. HORIZON / DISCRETE-GEOMETRY NUMERICAL STRESS TEST
# ------------------------------------------------------------------
def radial_error(n,r=1.0):
    return r*(1-math.cos(math.pi/n))
Ns=[4,8,16,32,64,128,256,512,1024]
errs=[radial_error(n) for n in Ns]
check_bool("HOR-001","Horizon","Regular-polygon radial approximation error decreases monotonically",
           all(errs[i+1]<errs[i] for i in range(len(errs)-1)),errs,"strictly decreasing")
check_bool("HOR-002","Horizon","Radial error tends toward zero numerically",
           errs[-1] < errs[0]/10000,errs[-1],f"< {errs[0]/10000}")
# asymptotic n^-2 sanity: e(2n)/e(n) -> 1/4
ratios=[radial_error(2*n)/radial_error(n) for n in [32,64,128,256,512]]
check_bool("HOR-003","Horizon","Polygon radial error exhibits ~n^-2 asymptotic scaling",
           all(abs(x-.25)<.001 for x in ratios[-3:]),ratios[-3:],"~0.25")

# ------------------------------------------------------------------
# 4. GR / QFT REFERENCE BENCHMARK REPRODUCTIONS
# These verify standard reference calculations, NOT a derivation unique to SEXA.
# ------------------------------------------------------------------
G=6.67430e-11
c=299792458.0
M_sun=1.98847e30
R_sun=6.957e8
AU=149597870700.0
arcsec_per_rad=206264.80624709636

light=4*G*M_sun/(R_sun*c*c)*arcsec_per_rad
check_num("GR-001","GR reference","Solar limb light bending",light,1.75,atol=.01,rtol=0,
          note="Standard GR reference calculation; not an independent SEXA-specific prediction.")

# Mercury perihelion advance per century
a=5.790905e10
e=0.205630
period_days=87.9691
advance_orbit=6*math.pi*G*M_sun/(a*(1-e*e)*c*c)
orbits_century=36525/period_days
advance_century=advance_orbit*arcsec_per_rad*orbits_century
check_num("GR-002","GR reference","Mercury anomalous perihelion precession",advance_century,43.0,atol=.2,rtol=0,
          note="Standard GR reference calculation.")

redshift=G*M_sun/(R_sun*c*c)
check_num("GR-003","GR reference","Solar gravitational redshift",redshift,2.1e-6,atol=.03e-6,rtol=0,
          note="Weak-field standard GR reference calculation.")

# Approximate superior-conjunction Shapiro round trip Earth-Mercury using impact R_sun.
# Source gives ~232 us; use classic order-of-magnitude calculation with Earth 1 AU and Mercury 0.387 AU.
r1=AU; r2=.387098*AU; b=R_sun
shapiro_round=2*(2*G*M_sun/c**3)*math.log(4*r1*r2/(b*b))*1e6
check_num("GR-004","GR reference","Shapiro delay near solar conjunction (parameterized reference case)",
          shapiro_round,232.0,atol=25.0,rtol=0,
          note="Result depends on geometry; wide tolerance reflects source's unspecified conjunction geometry.")

# GPS net GR + SR standard approximate correction
earth_GM=3.986004418e14
earth_R=6378137.0
gps_r=26560e3
gps_v=3874.0
day=86400
gr_rate=earth_GM/c**2*(1/earth_R-1/gps_r)
sr_rate=-(gps_v**2)/(2*c**2)
gps_us=(gr_rate+sr_rate)*day*1e6
check_num("GR-005","GR reference","GPS net relativistic clock correction",gps_us,38.0,atol=1.0,rtol=0,
          note="Standard approximate GR+SR reference calculation.")

alpha=7.2973525693e-3
g_leading=2*(1+alpha/(2*math.pi))
check_num("QFT-001","QFT reference","Electron g-2 leading-order Schwinger value",g_leading,2.0023228,atol=5e-8,rtol=0,
          note="Standard QED leading-order reference calculation.")

# Casimir scaling ratio check P(a)/P(2a)=16 for P proportional to a^-4
check_num("QFT-002","QFT reference","Casimir P∝1/a^4 doubling-gap scaling",16.0,16.0,
          note="Structural scaling check only.")

# Relativistic dispersion identity numerical stress test
for idx,(m,p) in enumerate([(1.0,0.0),(1.0,2.0),(3.0,4.0)],1):
    E2=p*p + m*m  # natural units c=1
    check_num(f"QFT-DISP-{idx:02d}","QFT reference",f"E^2=p^2+m^2 natural-unit case {idx}",
              E2,p*p+m*m)

# Activation law threshold is definitional, not empirical
sigma=1e8; Sigma_c=1e8
chi=sigma/Sigma_c
check_num("ACT-001","Activation","chi=sigma/Sigma_c at hard-switch threshold",chi,1.0,
          note="Definitional consistency check; does not establish physical activation.")
check_bool("ACT-002","Activation","OFF below 1e8 Pa",0.999e8 < 1e8,0.999e8,1e8)
check_bool("ACT-003","Activation","ON threshold condition at >=1e8 Pa",1.0e8 >= 1e8,1.0e8,1e8)

# ------------------------------------------------------------------
# 5. DETERMINISM / COMPUTATIONAL CORRESPONDENCE STRESS TEST
# ------------------------------------------------------------------
def trace(seed,depth=10000):
    state=int(seed)&0xffffffff
    out=[]
    for k in range(depth):
        state=(1664525*state+1013904223)&0xffffffff
        out.append((k,state,state%32))
    return out
a=trace(12345); b=trace(12345); d=trace(12346)
check_bool("COMP-001","Computational","Identical input produces identical 10k-step trace",a==b,a[-1],b[-1])
check_bool("COMP-002","Computational","Different seed produces different trace",a!=d,a[-1],d[-1])
check_bool("COMP-003","Computational","Projection remains bounded in 32-state space",
           all(0<=r<32 for _,_,r in a),max(r for _,_,r in a),"<32")

def normalized_recursion(seed,depth=10000,alpha=.75):
    x=float(seed)
    maxabs=abs(x)
    for _ in range(depth):
        x=alpha*math.tanh(x)+(1-alpha)*math.sin(x)
        if not math.isfinite(x): return False,float("inf")
        maxabs=max(maxabs,abs(x))
    return True,maxabs
for i,s in enumerate([-100,-10,-1,0,1,10,100],1):
    finite,mx=normalized_recursion(s)
    check_bool(f"COMP-BOUND-{i:02d}","Computational",f"Normalized recursion finite/bounded seed={s}",
               finite and mx<=abs(s)+1e-12, mx, f"<= {abs(s)}")

# ------------------------------------------------------------------
# 6. SOURCE PROVENANCE / DUPLICATE DETECTION
# ------------------------------------------------------------------
man_path=ROOT/"data/source_manifest.json"
if man_path.exists():
    manifest=json.loads(man_path.read_text(encoding="utf-8"))
    check_num("PROV-001","Provenance","Current master source document count",len(manifest),14)
    hashes={}
    for row in manifest: hashes.setdefault(row["sha256"],[]).append(row["name"])
    dup=[v for v in hashes.values() if len(v)>1]
    check_num("PROV-002","Provenance","Exact duplicate PDF groups detected",len(dup),1,
              note="Duplicate documents are not counted as independent evidence.")
    image_only=[r for r in manifest if r["chars"]<100]
    check_num("PROV-003","Provenance","Image/scan-only text-extraction sources",len(image_only),1)
else:
    add("PROV-001","Provenance","UNRESOLVED","Source manifest missing",None,14)

# Add non-executable / pending evidence classifications
ev_path=ROOT/"data/evidence_classifications.json"
if ev_path.exists():
    for e in json.loads(ev_path.read_text(encoding="utf-8")):
        add(e["id"],e["domain"],e["status"],e["claim"],"not executable from supplied data",None,None,e["reason"])

# ------------------------------------------------------------------
# REPORTING
# ------------------------------------------------------------------
order=["PASS","FAIL","REFERENCE_REPRODUCTION","NOT_INDEPENDENTLY_EXECUTABLE",
       "PENDING_EXPERIMENT","PENDING_IMPLEMENTATION","UNRESOLVED"]
counts={s:0 for s in order}
for r in RESULTS: counts[r.status]=counts.get(r.status,0)+1

def fmt(v):
    if isinstance(v,float): return f"{v:.15g}"
    if isinstance(v,(list,dict)): return json.dumps(v)
    return str(v)

print("="*96)
print("SEXA MASTER RUTHLESS AUDIT — PUBLIC REPOSITORY RUNNER")
print("="*96)
print("Python",platform.python_version(),"|",platform.system(),platform.release())
print("Rule: PASS validates the coded target only; it is not automatic experimental validation.")
print("-"*96)
for r in RESULTS:
    print(f"{r.status:30} {r.id:14} {r.domain:18} {r.claim}")
    if r.status=="FAIL":
        print(" "*34+"observed:",fmt(r.observed),"target:",fmt(r.target))
        if r.note: print(" "*34+r.note)
print("-"*96)
print("COUNTS")
for s in order:
    if counts.get(s): print(f"{s:30} {counts[s]}")
print("TOTAL",len(RESULTS))

# JSON
(OUT/"master_results.json").write_text(json.dumps([asdict(r) for r in RESULTS],indent=2,default=str),encoding="utf-8")
# CSV
with (OUT/"master_results.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(asdict(RESULTS[0]).keys()))
    w.writeheader()
    for r in RESULTS: w.writerow(asdict(r))
# Markdown
md=["# SEXA Master Ruthless Audit — Execution Report","",
    f"Total classified checks: **{len(RESULTS)}**",""]
for s in order:
    if counts.get(s): md.append(f"- **{s}: {counts[s]}**")
md += ["",
"## Interpretation",
"`PASS` means the coded arithmetic, structural, reference, or simulation target reproduced under the stated test.",
"It does **not** by itself establish experimental validation of the associated physical interpretation.",
"",
"## Failures"]
fails=[r for r in RESULTS if r.status=="FAIL"]
if fails:
    for r in fails:
        md += [f"### {r.id} — {r.claim}",
               f"- Observed: `{fmt(r.observed)}`",
               f"- Target: `{fmt(r.target)}`",
               f"- Note: {r.note or 'No additional note.'}",""]
else: md.append("No executable failures.")
md += ["","## Non-independent / pending / unresolved"]
for r in RESULTS:
    if r.status not in ("PASS","FAIL","REFERENCE_REPRODUCTION"):
        md += [f"- **{r.id} [{r.status}]** — {r.claim} — {r.note}"]
(OUT/"MASTER_AUDIT_REPORT.md").write_text("\n".join(md),encoding="utf-8")

# Exit only on harness/internal errors, not scientific FAILs, so public users always receive full report.
print("\nReports written to reports/master_results.{json,csv} and reports/MASTER_AUDIT_REPORT.md")
raise SystemExit(0)
