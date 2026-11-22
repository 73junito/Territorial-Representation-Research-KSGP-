"""Verify direct published composite count MOE vs approximate category-sum MOE.
Preserve published JSON and create audited diagnosis. Does not replace Phase 2F records.
"""
from pathlib import Path
import csv,json,hashlib,math,shutil

root=Path(r"I:\Territorial-Representation-Research")
stage=root/"06_Methodology"/"Phase2"/"_phase2i_direct_count_stage"
reports=root/"06_Methodology"/"Phase2"
data=root/"02_SPSS_Data"/"Phase2"
with (stage/"PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv").open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==2
records=[]
raw_sources=[]
for r in rows:
 year=r["year"];period=r["period"]
 source=stage/r["source_json"]
 payload=json.loads(source.read_text())
 assert len(payload)==2
 fields=dict(zip(*payload))
 assert fields["state"]=="11"
 assert float(fields["DP02_0068M"])==float(r["count_moe90"])
 assert float(fields["DP02_0068E"])==float(r["count_estimate"])
 raw_sources.append((source,reports/r["source_json"]))
 detail=data/("prdc_2019_acs_one_year_raw_components_with_moe.csv" if year=="2019" else "prdc_2020_acs_five_year_raw_components_with_moe.csv")
 with detail.open(encoding="utf-8-sig",newline="") as f:comp={(x["table_variable"],x["component_type"]):float(x["value"]) for x in csv.DictReader(f) if x["jurisdiction"]=="DC"}
 den=comp[("B15003_001","estimate")]
 den_moe=comp[("B15003_001","published_90pct_MOE")]
 numerator=sum(comp[(f"B15003_{i:03}","estimate")] for i in range(22,26))
 numerator_quadrature=math.sqrt(sum(comp[(f"B15003_{i:03}","published_90pct_MOE")]**2 for i in range(22,26)))
 published_count=float(r["count_estimate"])
 published_count_moe=float(r["count_moe90"])
 assert numerator==published_count,(period,numerator,published_count)
 p=numerator/den
 direct_percent_moe=100*math.sqrt(published_count_moe**2 - p*p*den_moe**2)/den
 quad_percent_moe=100*math.sqrt(numerator_quadrature**2-p*p*den_moe**2)/den
 implied_covariance_in_moe_squared=published_count_moe**2-numerator_quadrature**2
 records.append({
  "period":period,
  "direct_published_composite_count":published_count,
  "detailed_sum_count":numerator,
  "published_direct_composite_count_moe90":published_count_moe,
  "detailed_category_quadrature_count_moe90":round(numerator_quadrature,5),
  "denominator_count":den,
  "denominator_moe90":den_moe,
  "direct_count_method_derived_rate_moe90_pp":round(direct_percent_moe,5),
  "component_quadrature_derived_rate_moe90_pp":round(quad_percent_moe,5),
  "published_profile_rate_moe90_pp":float(r["rate_moe90_pp"]),
  "implied_sum_of_pairwise_covariance_terms_in_moe_squared":round(implied_covariance_in_moe_squared,3),
  "classification":"DIRECT_AGGREGATE_COUNT_MOE_MATCHES_PUBLISHED_PROFILE_RATE_MOE_AT_0_1PP_PRECISION",
  "precision_caveat":"Coarse published MOEs and differing variance methodology; covariance implied, not independently observed",
 })
 assert abs(round(direct_percent_moe,1)-float(r["rate_moe90_pp"]))<1e-9,(period,direct_percent_moe,r["rate_moe90_pp"])
 assert abs(quad_percent_moe-float(r["rate_moe90_pp"]))>0.15,(period,quad_percent_moe)
out=reports/"PHASE2I_DC_EDUCATION_VARIANCE_DIAGNOSTIC.csv"
targets=[out,reports/"PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv"]+[t for s,t in raw_sources]
assert all(not t.exists() for t in targets),"Refuse to overwrite already archived evidence."
for s,t in raw_sources:
 shutil.copyfile(s,t);print("ARCHIVED",t.name,hashlib.sha256(t.read_bytes()).hexdigest(),flush=True)
shutil.copyfile(stage/"PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv",reports/"PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv")
with out.open("w",encoding="utf-8-sig",newline="") as f:
 w=csv.DictWriter(f,fieldnames=records[0]);w.writeheader();w.writerows(records)
for r in records:print("DIAGNOSIS",r,flush=True)
print("ARCHIVED_DIAGNOSTIC_SHA256",hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
