"""Read-only Phase 2M-E figure QA. Validates artifacts and values against input sources."""
from pathlib import Path
import csv
import hashlib
import json
from decimal import Decimal

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"05_Statistical_Graphics/Phase2ME"
SP=ROOT/"02_SPSS_Data/Phase2"

def csv_rows(p):
    with p.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

index=csv_rows(OUT/"FIGURE_INDEX.csv")
assert len(index)==14
assert len({r["figure"] for r in index})==14
expected={"01_2020_population_logscale","02_2020_age_structure"}
expected.update("03_island_areas_"+x for x in ("education","unemployment","poverty","median_household_income"))
expected.update(f"{prefix}_{period}_{dom}" for prefix,period in (
    ("04","2019_1yr"),("05","2016_2020_5yr")) for dom in ("education","unemployment","poverty","median_household_income"))
assert {r["figure"] for r in index}==expected
assert sum(int(r["observations"]) for r in index)==6+6+4*4+8*2
assert len(list(OUT.glob("*.png")))==14
assert len(list(OUT.glob("*.svg")))==14
pops=csv_rows(SP/"age_sex_2020_six_jurisdictions.csv")
pop={r["jurisdiction"]:int(r["population_2020"]) for r in pops}
islands={(r["jurisdiction"],r["domain"]):r for r in csv_rows(SP/"island_areas_2020_socioeconomic_source_specific.csv")}
detailed={
 "2019_1yr":{(r["jurisdiction"],r["domain"]):r for r in csv_rows(SP/"prdc_2019_acs_one_year_detailed_source_specific.csv")},
 "2016_2020_5yr":{(r["jurisdiction"],r["domain"]):r for r in csv_rows(SP/"prdc_2020_acs_five_year_detailed_source_specific.csv")}}
profiles={(r["period"],r["jurisdiction"],r["domain"]):r for r in csv_rows(ROOT/"06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv")}
assert len(profiles)==12
for item in index:
    stem=item["figure"]
    for ext in ("png","svg"):
        path=OUT/(stem+"."+ext)
        assert path.is_file() and path.stat().st_size>400,path
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        assert actual==item[ext+"_sha256"],path
    assert (OUT/(stem+".png")).read_bytes()[:8]==b"\x89PNG\r\n\x1a\n"
    svg=(OUT/(stem+".svg")).read_text(encoding="utf-8")
    assert "<svg" in svg
    values=json.loads(item["evidence_values"])
    if stem=="01_2020_population_logscale":
        assert sum(values.values())==4313440
        assert set(v for v in values.values())==set(pop.values())
    elif stem=="02_2020_age_structure":
        assert len(values)==3
        for geo in pop:
            assert abs(sum(values[group][geo] for group in values)-100)<1e-8,geo
    elif stem.startswith("03_"):
        assert len(values)==4
        for geo, rec in values.items():
            assert Decimal(rec["value"])==Decimal(islands[(geo,item["domain"])]["value"])
            assert rec["source_variable"]==islands[(geo,item["domain"])]["source_variable"]
    else:
        period=item["reference_period"]
        period_id="2019_1yr" if stem.startswith("04_") else "2016_2020_5yr"
        assert len(values)==2
        for geo,rec in values.items():
            source=detailed[period_id][(geo,item["domain"])]
            assert Decimal(rec["estimate"])==Decimal(source["estimate"])
            if item["domain"]=="median_household_income":
                assert Decimal(str(rec["published_moe90"]))==Decimal(source["margin_of_error"])
            else:
                assert Decimal(str(rec["published_moe90"]))==Decimal(profiles[(period_id,geo,item["domain"])]["published_profile_moe90_pp"])
print("PHASE2ME_PASS 14 figure evidence maps, 14 PNG headers, 14 SVG bodies, 28 SHA-256 checks",flush=True)
print("SOURCE_FAMILY_SEPARATION_PASS 2020 demographics 2; Island Areas 4; one-year ACS/PRCS 4; five-year ACS/PRCS 4",flush=True)
print("NO_GO pooled six-way socioeconomic inferential graphs, no external faculty approval",flush=True)
