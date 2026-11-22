"""TRR Phase 2M portable, read-only evidence validation.

Python 3.10+ standard library only. No network, subprocess, or modifications.
Checks core source provenance and published ACS/PRCS profile MOE evidence.
Historical Phase 2F/2H reports and SPSS output are not rebuilt.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def source_path(relative: str) -> Path:
    clean = relative.replace("\\", "/")
    path = (ROOT / clean).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise AssertionError(f"source path escapes repository: {relative}")
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def one_decimal(value: str) -> Decimal:
    return Decimal(value).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def validate() -> None:
    manifest_path = ROOT / "01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv"
    manifest = rows(manifest_path)
    assert len(manifest) == 17, f"expected 17 official source files, got {len(manifest)}"
    for item in manifest:
        path = source_path(item["relative_path"])
        assert path.is_file(), f"missing official source: {path.name}"
        assert path.stat().st_size == int(item["size_bytes"]), f"source size mismatch: {path.name}"
        assert sha256(path) == item["sha256"].lower(), f"source hash mismatch: {path.name}"
    print("PASS: 17 original official Phase 2D source files: size and SHA-256")

    area_rows = rows(ROOT / "02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv")
    assert len(area_rows) == 6
    assert {r["geo_code"] for r in area_rows} == {"PR", "DC", "GU", "VI", "AS", "MP"}
    assert sum(int(r["population_2020"]) for r in area_rows) == 4313440
    for item in area_rows:
        pop = int(item["population_2020"])
        assert int(item["male_2020"]) + int(item["female_2020"]) == pop
        assert sum(int(item[k]) for k in ("under20_2020", "age20to64_2020", "age65plus_2020")) == pop
    print("PASS: six jurisdictions, total 4,313,440; sex and age components balance")

    method = ROOT / "06_Methodology/Phase2"
    census = ROOT / "01_Government_Sources/Phase2_Socioeconomic/Census"
    results = rows(method / "PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv")
    comparison = rows(method / "PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv")
    assert len(results) == len(comparison) == 12
    by_key = {(r["period"], r["jurisdiction"], r["domain"]): r for r in comparison}
    assert len(by_key) == 12
    assert {r["domain"] for r in results} == {"education", "unemployment", "poverty"}
    assert {r["jurisdiction"] for r in results} == {"DC", "PR"}
    matches = 0
    for entry in results:
        key = (entry["period"], entry["jurisdiction"], entry["domain"])
        assert key in by_key
        official_file = census / entry["source_archive"]
        payload = json.loads(official_file.read_text(encoding="utf-8"))
        assert len(payload) == 2
        original = dict(zip(*payload))
        assert original["state"] == entry["source_geography_fips"]
        assert Decimal(original[entry["published_profile_moe_variable"]]) == Decimal(entry["published_profile_moe90_pp"])
        assert Decimal(original[entry["published_profile_estimate_variable"]]) == Decimal(entry["published_profile_estimate_pct"])
        assert one_decimal(entry["published_profile_estimate_pct"]) == one_decimal(entry["derived_estimate_pct"])
        equal = one_decimal(entry["derived_moe90_pp"]) == one_decimal(entry["published_profile_moe90_pp"])
        expected = ("MATCH_AT_PUBLISHED_0_1_PP_PRECISION" if equal
                    else "DISCREPANCY_REQUIRES_VARIANCE_METHOD_REVIEW")
        assert by_key[key]["comparison_result"] == expected
        matches += int(equal)
    assert matches == 10
    print("PASS: 12 Census profile estimates and published MOEs; 10 Phase 2F one-decimal matches")

    direct = rows(method / "PHASE2I_DC_EDUCATION_VARIANCE_DIAGNOSTIC.csv")
    assert len(direct) == 2
    assert {r["period"] for r in direct} == {"2019_1yr", "2016_2020_5yr"}
    for entry in direct:
        assert Decimal(entry["direct_published_composite_count"]) == Decimal(entry["detailed_sum_count"])
        assert one_decimal(entry["direct_count_method_derived_rate_moe90_pp"]) == one_decimal(entry["published_profile_rate_moe90_pp"])
        count = rows(method / "PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv")
        matching = [r for r in count if r["period"] == entry["period"]]
        assert len(matching) == 1
        assert Decimal(entry["published_direct_composite_count_moe90"]) == Decimal(matching[0]["count_moe90"])
        raw = json.loads((method / matching[0]["source_json"]).read_text(encoding="utf-8"))
        fields = dict(zip(*raw))
        assert Decimal(fields["DP02_0068M"]) == Decimal(matching[0]["count_moe90"])
    print("PASS: two DC education published composite-count MOEs and percentage reconciliation")
    print("CONDITIONAL: historical SAV byte-hash causality OPEN; faculty approval PENDING")
    print("NO-GO: unqualified six-way socioeconomic statistical inference or final publication")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="optional checked-out project root")
    args = parser.parse_args()
    global ROOT
    if args.root:
        ROOT = args.root.expanduser().resolve()
    validate()


if __name__ == "__main__":
    main()
