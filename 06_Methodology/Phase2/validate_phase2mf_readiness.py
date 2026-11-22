"""Phase 2M-F consolidated acceptance gate: read-only audit of manuscript and figure evidence.

Run from any working directory. Never edits datasets or documents and never
asserts independent faculty approval.
"""
from pathlib import Path
from hashlib import sha256
import csv
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "09_Committee_Package/Phase2MF_Consolidated_Academic_Readiness_Decision.md"
REQUIRED = [
    "06_Methodology/Phase2/PHASE2M_REPRODUCIBILITY_ACCEPTANCE.md",
    "06_Methodology/Phase2/PHASE2M_LINUX_VALIDATION_ACCEPTANCE_ADDENDUM.md",
    "06_Methodology/Phase2/PHASE2MC_SAV_HISTORICAL_PROVENANCE_DECISION.md",
    "06_Methodology/Phase2/PHASE2MD_ACADEMIC_MANUSCRIPT_ACCEPTANCE.md",
    "06_Methodology/Phase2/PHASE2ME_ACADEMIC_FIGURE_ACCEPTANCE.md",
    "08_Final_Report/Phase2MD_Integrated_Academic_Manuscript_Review_Draft.md",
    "05_Statistical_Graphics/Phase2ME/FIGURE_INDEX.csv",
    "06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md",
    "06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md",
    "09_Committee_Package/Phase2K_Faculty_Review_Handoff.md",
    "09_Committee_Package/Phase2K_Faculty_Review_Decision_Form.md",
    "06_Methodology/Phase2/PHASE2L_REVIEWER_SELECTION_AND_OUTREACH_GATE.md",
]
for rel in REQUIRED:
    path = ROOT / rel
    assert path.is_file() and path.stat().st_size > 100, f"missing: {rel}"
    print("PASS evidence link", rel, flush=True)

packet = PACKET.read_text(encoding="utf-8")
assert all(word in packet for word in (
    "Phase 2M-A", "Phase 2M-B", "Phase 2M-C", "Phase 2M-D",
    "Phase 2M-E", "12", "17", "14", "28", "4,313,440",
    "PENDING", "NO-GO", "not a territory"))
assert "unresolved" in packet.lower()
assert "Dr. Belcher" not in packet or "PENDING" in packet
assert "USER-REPORTED" not in packet or "NO-GO" in packet
assert sha256((ROOT / "08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md").read_bytes()).hexdigest() == "18c47e750bf36d56f6f4a8f07edadbd09f1327ad82368c05188a9307ef5c931b"

with (ROOT / "05_Statistical_Graphics/Phase2ME/FIGURE_INDEX.csv").open(
        newline="", encoding="utf-8-sig") as stream:
    figures = list(csv.DictReader(stream))
assert len(figures) == 14 and len({f["figure"] for f in figures}) == 14

scripts = [
    "validate_phase2m_portable.py",
    "validate_phase2mc_sav_provenance_readonly.py",
    "validate_phase2md_academic_manuscript.py",
    "validate_phase2me_figures.py",
]
for name in scripts:
    cmd=[sys.executable, str(ROOT / "06_Methodology/Phase2" / name)]
    result = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False)
    if result.returncode:
        print(result.stdout)
        raise AssertionError(f"failed embedded validation: {name}")
    print("PASS validator", name)
print("PASS: consolidated evidence and 14 figure records")
print("GO: qualified independent faculty review handoff; NO-GO: unapproved public/committee publication")
