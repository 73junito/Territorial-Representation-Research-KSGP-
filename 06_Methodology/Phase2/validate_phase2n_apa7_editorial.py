"""Read-only APA-7 citation and archival numerical regression QA for Phase 2N."""
from pathlib import Path
import re
import csv
import hashlib

root = Path(__file__).resolve().parents[2]
current = root / "08_Final_Report/Phase2N_APA7_Cited_Academic_Manuscript_Review_Draft.md"
prior = root / "08_Final_Report/Phase2MD_Integrated_Academic_Manuscript_Review_Draft.md"
report = root / "06_Methodology/Phase2/PHASE2N_APA7_CITATION_EDITORIAL_AUDIT.md"
s = current.read_text(encoding="utf-8")
assert prior.is_file() and report.is_file()
assert current != prior
assert s.count("### Table ") == 5
assert all(fragment in s for fragment in ("4,313,440", "32 source-specific", "1.11022", "0.55633", "5,612", "2,793", "NO-GO", "not a territory", "unresolved"))
assert len(re.findall(r"\(U\.S\. Census Bureau, 20", s)) >= 8
ref = s.split("## References — APA 7 editorial draft")[1].split("## Evidence and reproducibility appendix")[0]
defined = re.findall(r"U\.S\. Census Bureau\. \((20\d\d[abc])\)", ref)
assert defined == ["2020a", "2020b", "2022a", "2022b", "2022c"], defined
body = s.split("## References — APA 7 editorial draft")[0]
assert all(y in body for y in defined)
assert "D.C./PR DHC" in s and "does not document the D.C./PR DHC" in s
assert "publication-year suffixes are provisionally assigned" in s
assert "No faculty" not in s or "PENDING" in s
# Do not claim a recent review or missing original provenance was resolved.
assert "historical cause **cannot be established**" in s
data = root / "02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv"
with data.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 6
assert sum(int(r["population_2020"]) for r in rows) == 4313440
baseline_hash = hashlib.sha256((root / "08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md").read_bytes()).hexdigest()
assert baseline_hash == "18c47e750bf36d56f6f4a8f07edadbd09f1327ad82368c05188a9307ef5c931b"
print("PASS 5 APA reference author-year suffixes and in-text linkage")
print("PASS 5 tables; original Census derived values and 2020 DHC source-classification caveat")
print("PASS historical Phase 2F report unchanged", baseline_hash)
print("CONDITIONAL final APA metadata and faculty bibliographic signoff; publication NO-GO")
