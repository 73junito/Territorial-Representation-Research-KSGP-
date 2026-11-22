"""Retrieve official ACS/PRCS published Data Profile rate MOEs when authorized API key is configured.

Never logs, writes, or commits the API key. Read-only until four valid JSON
responses are obtained and source values are validated. Never overwrites evidence.
"""
from pathlib import Path
import csv
import hashlib
import json
import os
import requests
import sys

ROOT = Path(__file__).resolve().parents[2]
CENSUS = ROOT / "01_Government_Sources" / "Phase2_Socioeconomic" / "Census"
DATA = ROOT / "02_SPSS_Data" / "Phase2"
REPORT = ROOT / "06_Methodology" / "Phase2"
KEY = os.environ.get("CENSUS_API_KEY", "").strip()
if not KEY:
    print("BLOCKED: CENSUS_API_KEY environment variable not present. No network calls or writes performed.")
    sys.exit(2)

periods = [
    ("2019_1yr", "2019", "acs1"),
    ("2016_2020_5yr", "2020", "acs5"),
]
places = [("DC", "11"), ("PR", "72")]
domains = {
    "education": ("DP02_0068PE", "DP02_0068PM"),
    "unemployment": ("DP03_0009PE", "DP03_0009PM"),
    "poverty": ("DP03_0128PE", "DP03_0128PM"),
}

with (DATA / "phase2f_prdc_derived_rate_moe90.csv").open(
    encoding="utf-8-sig", newline=""
) as file:
    calculated = {
        (r["source_period"], r["jurisdiction"], r["domain"]): r
        for r in csv.DictReader(file)
    }
assert len(calculated) == 12

results = []
originals = []
for period, year, dataset in periods:
    for geo, state in places:
        variants = dict(domains)
        if geo == "PR":
            variants["education"] = ("DP02PR_0068PE", "DP02PR_0068PM")
        fields = ["NAME"] + [v for pair in variants.values() for v in pair]
        url = f"https://api.census.gov/data/{year}/acs/{dataset}/profile"
        # Never print response.url, as requests places the key in its query string.
        try:
            response = requests.get(
                url,
                params={"get": ",".join(fields), "for": f"state:{state}", "key": KEY},
                timeout=45,
                allow_redirects=True,
            )
        except requests.RequestException:
            # Do not stringify request exceptions; they can contain URLs with the key.
            raise RuntimeError(f"BLOCKED {period} {geo}: network request failed (details suppressed)") from None
        if response.status_code != 200 or "missing_key.html" in response.url:
            raise RuntimeError(
                f"BLOCKED {period} {geo}: Census returned status {response.status_code} "
                "or redirected to missing_key.html; key and raw response not logged."
            )
        try:
            payload = response.json()
        except ValueError as err:
            raise RuntimeError(f"BLOCKED {period} {geo}: response is not JSON") from err
        if (
            not isinstance(payload, list)
            or len(payload) != 2
            or not all(isinstance(row, list) for row in payload)
            or len(payload[0]) != len(payload[1])
        ):
            raise RuntimeError(f"BLOCKED {period} {geo}: unexpected Census result shape")
        observed = dict(zip(payload[0], payload[1]))
        if observed.get("state") != state:
            raise RuntimeError(f"BLOCKED {period} {geo}: geography mismatch")
        for domain, (estimate_field, moe_field) in variants.items():
            if estimate_field not in observed or moe_field not in observed:
                raise RuntimeError(f"BLOCKED {period} {geo} {domain}: profile field missing")
            try:
                estimate = float(observed[estimate_field])
                moe = float(observed[moe_field])
            except (TypeError, ValueError) as err:
                raise RuntimeError(f"BLOCKED {period} {geo} {domain}: suppressed or invalid published field") from err
            if not (0 <= estimate <= 100 and 0 < moe <= 100):
                raise RuntimeError(f"BLOCKED {period} {geo} {domain}: implausible numeric value")
            derived = calculated[(period, geo, domain)]
            derived_estimate = float(derived["estimate_pct"])
            derived_moe = float(derived["moe90_percentage_points"])
            results.append({
                "jurisdiction": geo,
                "period": period,
                "domain": domain,
                "published_profile_estimate_variable": estimate_field,
                "published_profile_moe_variable": moe_field,
                "published_profile_estimate_pct": estimate,
                "published_profile_moe90_pp": moe,
                "derived_estimate_pct": derived_estimate,
                "derived_moe90_pp": derived_moe,
                "estimate_delta_pp": round(derived_estimate - estimate, 5),
                "moe_delta_pp": round(derived_moe - moe, 5),
                "status": "REVIEW_REQUIRED_NOT_AUTOMATIC_PASS",
                "source_api_endpoint_no_key": url,
                "source_geography_fips": state,
                "source_archive": f"ACS_Profile_{year}_{dataset}_{geo}_official.json",
                "reference_period": period,
            })
        original_name = f"ACS_Profile_{year}_{dataset}_{geo}_official.json"
        original_bytes = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        originals.append((CENSUS / original_name, original_bytes))
assert len(results) == 12 and len(originals) == 4

output = REPORT / "PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv"
destinations = [p for p, _ in originals] + [output]
conflicts = [str(p) for p in destinations if p.exists()]
if conflicts:
    raise RuntimeError("BLOCKED: refusing to overwrite existing archive/result: " + "; ".join(conflicts))

# No writes until all four official API responses and all 12 numeric pairs validate.
for p, raw in originals:
    p.write_bytes(raw)
    print(f"ARCHIVED {p.name}: SHA256 {hashlib.sha256(raw).hexdigest()}")
with output.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=list(results[0]))
    writer.writeheader()
    writer.writerows(results)
print(f"RETRIEVED 12 independently published percentage MOEs; cross-check status REVIEW_REQUIRED")
print(f"OUTPUT {output} SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}")
