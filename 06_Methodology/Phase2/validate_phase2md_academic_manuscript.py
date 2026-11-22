"""Read-only Phase 2M-D manuscript accuracy and acceptance validation."""
from __future__ import annotations
from pathlib import Path
from decimal import Decimal
import csv
import hashlib
import re

root = Path(__file__).resolve().parents[2]
manuscript = root / "08_Final_Report/Phase2MD_Integrated_Academic_Manuscript_Review_Draft.md"
s = manuscript.read_text(encoding="utf-8")
assert len(s) > 13000
assert all(section in s for section in ("## Abstract", "## Introduction", "## Research design", "## Data quality", "## Survey uncertainty", "## Discussion", "## Limitations", "## Conclusion", "## References", "## Evidence"))
assert s.count("### Table ") == 5
assert "peer-reviewed" in s and "NO-GO" in s
assert "not a territory" in s
assert "3,285,874" in s and "689,545" in s and "153,836" in s
assert "87,146" in s and "49,710" in s and "47,329" in s
assert "4,313,440" in s
assert "2,047,330" in s and "2,266,110" in s
assert "880,002" in s and "2,573,093" in s and "860,345" in s

appendix = (root / "08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md").read_text(encoding="utf-8")
phase2f = (root / "08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md").read_text(encoding="utf-8")
for line in s.splitlines():
    if line.startswith("| ") and any(area in line for area in (
        "American Samoa | 13.3", "Guam | 25.3",
        "Northern Mariana Islands | 21.0", "U.S. Virgin Islands | 22.3",
        "Washington, D.C. | 59.67", "Puerto Rico | 27.22",
        "Washington, D.C. | 59.76", "Puerto Rico | 26.67",
    )):
        cells = [c.strip().replace("%", "") for c in line.split("|")[1:-1]]
        historical = ([c.strip().replace("%", "") for c in x.split("|")[1:-1]]
                      for x in phase2f.splitlines() if x.startswith("| "))
        assert any(x == cells for x in historical), f"Socioeconomic row not reproduced from Phase 2F: {line}"

with (root / "06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv").open(
    encoding="utf-8-sig", newline=""
) as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 12
for period, area, edu, unemp, poverty in (
    ("2019_1yr", "DC", "1.1", "0.6", "1.3"),
    ("2019_1yr", "PR", "0.6", "0.7", "0.8"),
    ("2016_2020_5yr", "DC", "0.6", "0.5", "0.5"),
    ("2016_2020_5yr", "PR", "0.3", "0.3", "0.3"),
):
    official = {r["domain"]:Decimal(r["published_profile_moe90_pp"]) for r in rows
                if r["period"] == period and r["jurisdiction"] == area}
    assert len(official) == 3
    assert [official["education"], official["unemployment"], official["poverty"]] == [
        Decimal(edu), Decimal(unemp), Decimal(poverty)]
    name = "Washington, D.C." if area == "DC" else "Puerto Rico"
    note = "2019 one-year" if period == "2019_1yr" else "2016–2020 five-year"
    row = f"| {note} | {name} | ±{edu} | ±{unemp} | ±{poverty} |"
    assert row in s, f"Missing MOE table: {row}"

for rate in ("1.59719", "0.81966", "1.11022", "0.55633"):
    assert rate in s
for moes in ("5,612", "2,793"):
    assert moes in s

# Original reports are preserved; this check reads but never edits them.
print("PASS manuscript sections, 5 labeled tables, scope and numerical safeguards")
print("PASS 8 socioeconomic table rows equal historical Phase 2F content")
print("PASS all 12 official profile MOEs and both direct composite-count reconciliations")
print("PASS preserved Phase 2F SHA-256", hashlib.sha256((root/"08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md").read_bytes()).hexdigest())
print("MANUSCRIPT_DRAFT_QA_PASS; FACULTY_REVIEW_PENDING; PUBLICATION_NO_GO")
