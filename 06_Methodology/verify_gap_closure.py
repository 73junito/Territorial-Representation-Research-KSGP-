from pathlib import Path
import csv,zipfile,hashlib,re
import pyreadstat,pandas as pd
root=Path(r"I:\Territorial-Representation-Research")
sdir=root/"01_Government_Sources"
with (sdir/"archive_manifest.csv").open(encoding="utf-8-sig",newline="") as f:a=list(csv.DictReader(f))
with (sdir/"official_tables_manifest.csv").open(encoding="utf-8-sig",newline="") as f:b=list(csv.DictReader(f))
assert len(a)==6 and all(x["validation"]=="PASS" for x in a)
assert len(b)==4 and all(x["status"]=="PASS" for x in b)
for item in a:
 p=root/item["archive_path"]
 assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==item["sha256"]
for item in b:
 p=root/item["archive_path"]
 assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==item["sha256"]
reference={"GU":(159358,153836),"VI":(106405,87146),"AS":(55519,49710),"MP":(53883,47329)}
for item in b:
 r=reference[item["geo_code"]]
 source=(root/item["archive_path"]).read_text(encoding="utf-8-sig",errors="replace").replace(",","")
 for n in r:assert str(n) in source,("Raw CSV missing source number",item["geo_code"],n)
p=root/"02_SPSS_Data"
s1,_=pyreadstat.read_sav(str(p/"population_2010_2020.sav"))
s2,_=pyreadstat.read_sav(str(p/"population_2010_2021.sav"))
pd.testing.assert_frame_equal(s1,s2)
assert int(s1.population_2020.sum())==4313440
with zipfile.ZipFile(root/"04_SPSS_Output"/"01_population_comparison.spv") as z:
 text=" ".join(z.read(n).decode("utf-8",errors="replace") for n in z.namelist() if n.endswith(".xml"))
 assert "population_2010_2021.sav" in text
 assert "5334" in text
print("ALL SIX OFFICIAL ARCHIVE LINKS VALIDATED")
print("FOUR ISLAND CSV TABLES VALIDATED BOTH YEARS")
print("SPSS 2021 MISNAMED DUPLICATE CONFIRMED")
print("SPV SAVE CONTENTION CONFIRMED")
