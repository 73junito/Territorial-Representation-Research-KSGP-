from pathlib import Path
import hashlib
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(r"I:\Territorial-Representation-Research")
data=root/"02_SPSS_Data"
output=root/"04_SPSS_Output"
graphics=root/"05_Statistical_Graphics"
method=root/"06_Methodology"
report=root/"08_Final_Report"
csv=pd.read_csv(data/"population_2010_2020_source.csv")
primary,_=pyreadstat.read_sav(str(data/"population_2010_2020.sav"))
alternate,_=pyreadstat.read_sav(str(data/"population_2010_2021.sav"))
pd.testing.assert_frame_equal(primary,alternate)
assert len(csv)==6 and csv.geo_code.is_unique
assert csv.population_2020.sum()==4313440
assert csv.population_2010.sum()==4702677
a=primary.sort_values("geo_code").reset_index(drop=True)
b=csv.sort_values("geo_code").reset_index(drop=True)
for col in ["population_2010","population_2020","house_final_vote_members","senate_members"]:
 assert (a[col].astype("int64")==b[col].astype("int64")).all(),col
assert (primary.population_change == primary.population_2020-primary.population_2010).all()
assert ((primary.population_change_pct - 100*primary.population_change/primary.population_2010).abs()<1e-8).all()
combined_2010=int(csv.population_2010.sum())
combined_2020=int(csv.population_2020.sum())
change=combined_2020-combined_2010
pct=100*change/combined_2010
chart=primary.sort_values("population_2020")
fig,ax=plt.subplots(figsize=(11,5.5))
ax.barh(chart.jurisdiction,chart.population_2020)
ax.set_xlabel("Residents (2020 Census)")
ax.set_title("Resident population in six jurisdictions, 2020")
for i,n in enumerate(chart.population_2020):
 ax.annotate(f"{int(n):,}",(n,i),xytext=(5,0),textcoords="offset points",va="center",fontsize=9)
ax.set_xlim(0,float(max(chart.population_2020))*1.16)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.text(0.01,0.015,"Source: U.S. Census Bureau, 2020 Census and 2020 Island Areas Censuses. Population is not eligible voters.",fontsize=8)
fig.tight_layout(rect=(0,0.04,1,1))
fig.savefig(graphics/"01_population_2020.png",dpi=180)
plt.close(fig)
checks=pd.DataFrame([
 ["Six unique jurisdictions","PASS",str(len(primary))],
 ["Source CSV counts match SPSS","PASS","2010 and 2020, all 6"],
 ["2020 census population checksum","PASS",str(combined_2020)],
 ["2010 census population checksum","PASS",str(combined_2010)],
 ["Change computed from counts","PASS",str(change)],
 ["Percent changes computed from counts","PASS",f"{pct:.4f}%"],
 ["Unexpected 2021 file contents identical","PASS","Only file name and binary encoding differ"],
 ["SPSS output inspected","PASS","List table and descriptive output, SPSS save file contention warning"],
 ["Inference tests required","NOT APPLICABLE","Jurisdiction-level census counts, not a random sample"],
 ["Official raw census data archived","NOT YET","Manual transcriptions validated against official Census pages"],
],columns=["check","status","evidence"])
checks.to_csv(method/"phase1_quality_assurance.csv",index=False)
hashes={}
for f in [data/"population_2010_2020.sav",data/"population_2010_2021.sav",output/"01_population_comparison.spv",data/"population_2010_2020_source.csv"]:
 hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
lines=["# Phase 1 SPSS Output Audit","Date: 2026-11-21","",
"## Status","PASS — Census counts and percentage changes validated. SPSS ran the LIST and DESCRIPTIVES procedures. No statistical inference performed.","",
"## SPSS save warning","The SPSS Output Viewer records Warning #67 (GET FILE: the intended .sav was already in use) and Warning #5334 (SAVE succeeded under a different filename). It saved a second file named population_2010_2021.sav. Both .sav files contain the identical six rows and columns. No evidence of a 2021 dataset. Both have been retained unchanged.","",
"## Reconciliation",
f"- 2010 population: {combined_2010:,}",
f"- 2020 population: {combined_2020:,}",
f"- Absolute change: {change:,}",
f"- Percent change, combined denominator: {pct:.2f}%",
"- Population denominators are total residents, not eligible voters.",
"- No effect sizes/p-values are appropriate for this jurisdiction-level census summary.","",
"## SHA256 integrity record"]
lines += [f"- `{k}`: `{v}`" for k,v in hashes.items()]
lines += ["","## Data provenance and limitations",
"Population counts derived from Census Bureau 2010 and 2020 Census releases, transcribed into a six-row CSV; the government originals are not yet locally archived.",
"Official primary sources: Census QuickFacts for PR and DC, and the 2020 Island Areas Censuses press releases for GU, VI, AS and MP. Refer to source_register.csv.",
"More detailed housing/income/education data will require comparison of census universes and source definitions before aggregation.",
"Detailed Guam social/economic tables exclude military installation populations in some universes. American Samoa social/economic tables may exclude group quarters due to census collection limitations.",
"## Outstanding follow-up",
"1. Review whether the alternate .sav was opened or created in an SPSS session; do not delete while files may be locked.",
"2. For future reruns, use a separate validated-results filename or skip saving the input file.",
"3. Gather original agency table downloads and check detailed data universes before Phase 2.",
]
(method/"SPSS_output_audit.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
table=["| Jurisdiction | 2010 | 2020 | Change | Percent change |","|---|---:|---:|---:|---:|"]
for _,r in primary.iterrows():
 table.append(f"| {r['jurisdiction']} | {int(r['population_2010']):,} | {int(r['population_2020']):,} | {int(r['population_change']):+,} | {r['population_change_pct']:+.2f}% |")
summary=["# Population and Congressional Representation — Phase 1 Results",
"Research summary | Prepared November 21, 2026","",
"## Research question",
"What was the 2010–2020 population change in the five permanently inhabited U.S. territories and the District of Columbia?",
"",
"## Methods",
"Descriptive comparison of official 2010 and 2020 decennial Census resident population counts, with arithmetic calculations checked in SPSS-compatible files. Six jurisdictions are the full scope of the study, not a sample. No inferential hypothesis tests are warranted.",
"",
"## Findings",*table,"",
f"Combined population fell from **{combined_2010:,}** to **{combined_2020:,}**, a change of **{change:,} ({pct:.2f}%)**. This combined figure includes Washington, D.C., which is not a territory.",
"",
"All six currently have no voting House member for final passage and no U.S. senator. This does not mean they have no congressional presence: the territories and D.C. have nonvoting delegates or a resident commissioner.",
"",
"## Interpretation",
"The population figures quantify residents in the six jurisdictions but do not measure eligible voters, political preferences, causes of population change, or policy outcomes. They cannot by themselves establish the preferred constitutional status for any jurisdiction.",
"",
"## Sources",
"U.S. Census Bureau QuickFacts: Puerto Rico and District of Columbia; Census Bureau 2020 Island Areas Censuses (Guam, U.S. Virgin Islands, American Samoa, Northern Mariana Islands). Links and notes in 01_Government_Sources/source_register.csv.",
"",
"## Transparency",
"SPSS output was inspected and calculations independently reproduced. SPSS reported a file-lock contention warning and saved an identical alternate .sav under a misleading 2021 filename. Both originals remain unchanged. See 06_Methodology/SPSS_output_audit.md.",
"",
"## Next research phase",
"Study income, poverty, employment, education, and federal spending using official datasets, recording coverage, reference years, population universes and definition differences before statistical comparisons.",
]
(report/"Phase1_Population_Research_Summary.md").write_text("\n".join(summary)+"\n",encoding="utf-8")
print("PASS QA checks",len(checks))
print(f"NET {change:,} ({pct:.2f}%)")
print("CREATED chart, QA csv, SPSS audit, summary")
