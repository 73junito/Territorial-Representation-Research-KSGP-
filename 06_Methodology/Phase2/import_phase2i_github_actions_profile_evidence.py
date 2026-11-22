"""Import the trusted, read-only GitHub Actions Census profile artifact.
Preserve exact official response JSON, the original comparison CSV, and
create an independently validated methodological adjudication table.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv
import hashlib
import json
import shutil

root = Path(r"I:\Territorial-Representation-Research")
stage = root / "06_Methodology" / "Phase2" / "_phase2i_actions_download"
originals = root / "01_Government_Sources" / "Phase2_Socioeconomic" / "Census"
method = root / "06_Methodology" / "Phase2"

source_csv = stage / "06_Methodology" / "Phase2" / "PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv"
csv_target = method / "PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv"
analysis_target = method / "PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv"

with source_csv.open("r", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 12
assert len({(r["period"], r["jurisdiction"], r["domain"]) for r in rows}) == 12
assert {r["jurisdiction"] for r in rows} == {"DC", "PR"}
assert {r["domain"] for r in rows} == {"education", "unemployment", "poverty"}
assert {r["period"] for r in rows} == {"2019_1yr", "2016_2020_5yr"}

source_files = []
for period, year, dataset in [("2019_1yr", "2019", "acs1"), ("2016_2020_5yr", "2020", "acs5")]:
    for geo, fips in [("DC", "11"), ("PR", "72")]:
        filename = f"ACS_Profile_{year}_{dataset}_{geo}_official.json"
        source = stage / "01_Government_Sources" / "Phase2_Socioeconomic" / "Census" / filename
        target = originals / filename
        payload = json.loads(source.read_text(encoding="utf-8"))
        assert isinstance(payload, list) and len(payload) == 2
        fields = dict(zip(payload[0], payload[1]))
        assert fields["state"] == fips
        keys = [r for r in rows if r["period"] == period and r["jurisdiction"] == geo]
        assert len(keys) == 3
        for r in keys:
            assert float(fields[r["published_profile_estimate_variable"]]) == float(r["published_profile_estimate_pct"])
            assert float(fields[r["published_profile_moe_variable"]]) == float(r["published_profile_moe90_pp"])
        assert "key" not in (json.dumps(payload).lower())
        source_files.append((source, target))

def displayed_tenth(value):
    return Decimal(value).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

classified = []
for r in rows:
    published = displayed_tenth(r["published_profile_moe90_pp"])
    derived_display = displayed_tenth(r["derived_moe90_pp"])
    source_estimate = displayed_tenth(r["published_profile_estimate_pct"])
    derived_estimate = displayed_tenth(r["derived_estimate_pct"])
    assert source_estimate == derived_estimate, (r["period"], r["jurisdiction"], r["domain"], source_estimate, derived_estimate)
    equal = published == derived_display
    adjudication = "MATCH_AT_PUBLISHED_0_1_PP_PRECISION" if equal else "DISCREPANCY_REQUIRES_VARIANCE_METHOD_REVIEW"
    classified.append({
        "period": r["period"],
        "jurisdiction": r["jurisdiction"],
        "domain": r["domain"],
        "profile_estimate": r["published_profile_estimate_pct"],
        "derived_estimate": r["derived_estimate_pct"],
        "profile_moe90_pp": r["published_profile_moe90_pp"],
        "derived_moe90_pp": r["derived_moe90_pp"],
        "profile_moe90_rounded": str(published),
        "derived_moe90_rounded": str(derived_display),
        "moe_delta_pp": r["moe_delta_pp"],
        "profile_variable": r["published_profile_moe_variable"],
        "comparison_result": adjudication,
        "source_response": r["source_archive"],
        "github_actions_run": "https://github.com/73junito/Territorial-Representation-Research-KSGP-/actions/runs/44972219452",
    })
assert sum("MATCH_AT_" in r["comparison_result"] for r in classified) == 10
assert {(r["period"], r["jurisdiction"], r["domain"]) for r in classified if "DISCREPANCY" in r["comparison_result"]} == {
    ("2019_1yr", "DC", "education"),
    ("2016_2020_5yr", "DC", "education")
}

destinations = [t for _, t in source_files] + [csv_target, analysis_target]
existing = [str(x) for x in destinations if x.exists()]
assert not existing, "Refusing to overwrite: " + repr(existing)
for source, target in source_files:
    shutil.copyfile(source, target)
    print("ARCHIVED", target.name, hashlib.sha256(target.read_bytes()).hexdigest(), flush=True)
shutil.copyfile(source_csv, csv_target)
with analysis_target.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=classified[0].keys())
    writer.writeheader()
    writer.writerows(classified)
for target in (csv_target, analysis_target):
    print("RECONCILIATION", target.name, hashlib.sha256(target.read_bytes()).hexdigest(), flush=True)
print("PASS 12 point-estimate rounded matches; 10 MOE rounded matches; 2 MOE discrepancies (DC education).", flush=True)
