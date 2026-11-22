from pathlib import Path
import zipfile, hashlib, re, html, json
import pandas as pd
import pyreadstat
root=Path(r"I:\Territorial-Representation-Research")
p=root/"04_SPSS_Output"/"Phase2"/"01_age_sex_2020_descriptive.spv"
data=root/"02_SPSS_Data"/"Phase2"/"age_sex_2020_six_jurisdictions.sav"
assert p.exists() and p.stat().st_size>1000
df,_=pyreadstat.read_sav(str(data))
assert len(df)==6
with zipfile.ZipFile(p) as z:
 assert z.testzip() is None
 a=z.read("outputViewer0000000000_heading.xml").decode("utf-8")
 b=z.read("outputViewer0000000001_heading.xml").decode("utf-8")
 table=z.read("00000000012_lightTableData.bin")
 assert 'commandName="List"' in a and 'Number' in a
 assert 'commandName="Descriptives"' in b
 assert 'subType="Descriptive Statistics"' in b
 assert b'Descriptive Statistics' in table and b'Sum' in table and b'Mean' in table
 text=html.unescape(re.sub(r"<[^>]+>"," ",re.sub(r"<br\s*(?:/?>|></br>)","\n",a,flags=re.I)))
 text=text.replace("\xa0"," ")
 results=[]
 for row in df.itertuples():
  # SPSS LIST outputs each record in one monospaced text line,
  # matching exact counts in the expected source order.
  pattern=r"(?m)^\s*"+re.escape(row.geo_code)+r"\s+"
  matches=[line for line in text.splitlines() if re.search(pattern,line)]
  assert len(matches)==1,(row.geo_code,"expected exactly one listing",matches)
  line=matches[0]
  for val in [row.population_2020,row.male_2020,row.female_2020,row.under20_2020,row.age20to64_2020,row.age65plus_2020]:
   assert re.search(r"(?<![0-9])"+str(int(val))+r"(?:\.0+)?(?![0-9])",line),(row.geo_code,val,line)
  results.append(row.geo_code)
 assert len(results)==6
 assert "Number of cases read:" in text and re.search(r"Number\s+of\s+cases\s+listed:\s*6",text)
 assert not re.search(r"(?i)warning\s*#|error\s*#|command\s+not\s+recognized",text)
expected={
"population_sum":int(df.population_2020.sum()),
"male_sum":int(df.male_2020.sum()),
"female_sum":int(df.female_2020.sum()),
"under20_sum":int(df.under20_2020.sum()),
"age20to64_sum":int(df.age20to64_2020.sum()),
"age65plus_sum":int(df.age65plus_2020.sum())
}
assert expected["population_sum"]==4313440
assert expected["male_sum"]+expected["female_sum"]==expected["population_sum"]
assert expected["under20_sum"]+expected["age20to64_sum"]+expected["age65plus_sum"]==expected["population_sum"]
report=[
"# Phase 2 — SPSS Viewer Acceptance",
"",
"Date: 2026-11-21",
"",
"## Verified outcome",
"- PASS: SPSS-produced output file exists and is a valid ZIP-based .spv Viewer document.",
"- PASS: The SPSS Viewer includes LIST for all six jurisdictions and a Descriptives section with a Descriptive Statistics pivot table.",
"- PASS: All six LIST population, sex, and harmonized age group counts match the canonical .sav data.",
"- PASS: SPSS LIST states six cases were read and listed.",
"- PASS: No numbered command warnings or errors were found in exposed LIST text.",
"- PASS: Source .sav remains readable; no input dataset rewrite was required.",
"- CONDITIONAL: The proprietary binary Descriptives pivot payload is confirmed to exist with Sum/Mean metadata but individual binary table cell values were not directly decoded. Source-derived aggregates are independently recalculated below; inspect these against the GUI pivot table for full cell-level signoff.",
"",
"## Source-derived reconciliation values",
]+[f"- {k}: {v:,}" for k,v in expected.items()]+[
"",
"## Files",
f"- SPV: {p.relative_to(root)}",
f"- SPV size: {p.stat().st_size:,} bytes",
f"- SPV SHA256: {hashlib.sha256(p.read_bytes()).hexdigest()}",
f"- SAV SHA256: {hashlib.sha256(data.read_bytes()).hexdigest()}",
"",
"## Decision",
"Phase 2 age-sex pilot output-generation gate: PASS.",
"SPSS LIST vs Census data reconciliation: PASS.",
"SPSS proprietary Descriptives pivot cell-by-cell verification: NOT FULLY VERIFIED (binary table payload).",
"Socioeconomic income, poverty, employment, and education comparability gate remains separate and NOT CLEARED.",
]
out=root/"06_Methodology"/"Phase2"/"SPSS_VIEWER_ACCEPTANCE.md"
out.write_text("\n".join(report)+"\n",encoding="utf-8")
print("SPV_PASS",p.stat().st_size,"CASES",results,flush=True)
print("EXPECTED_SUMS",json.dumps(expected),flush=True)
print("SAVED_AUDIT",out,flush=True)
