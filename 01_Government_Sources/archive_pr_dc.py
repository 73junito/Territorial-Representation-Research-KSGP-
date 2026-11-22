from pathlib import Path
import requests,zipfile,hashlib,csv
root=Path(r"I:\Territorial-Representation-Research")
archive=root/"01_Government_Sources"/"official_2020_archives"
url="https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment-2020-tableE.xlsx"
resp=requests.get(url,timeout=25)
resp.raise_for_status()
p=archive/"CENSUS_PR_DC_TableE_2020_2010.xlsx"
if not resp.content.startswith(b"PK"):raise RuntimeError("XLSX signature not found")
p.write_bytes(resp.content)
with zipfile.ZipFile(p) as z:
 xml=" ".join(z.read(n).decode("utf-8",errors="replace") for n in z.namelist() if n.endswith(".xml"))
 for val in ["3285874","3725789","689545","601723"]:
  if val not in xml: raise ValueError("Expected Census count not found in workbook XML: "+val)
hash_value=hashlib.sha256(p.read_bytes()).hexdigest()
manifest=root/"01_Government_Sources"/"archive_manifest.csv"
with manifest.open("r",newline="",encoding="utf-8-sig") as f:
 reader=csv.DictReader(f)
 rows=list(reader)
 columns=reader.fieldnames
for row in rows:
 if row["geo_code"] in ("PR","DC"):
  row["source_url"]=url
  row["archive_path"]=str(p.relative_to(root))
  row["byte_count"]=str(p.stat().st_size)
  row["sha256"]=hash_value
  row["validation"]="PASS"
  row["notes"]="2020 Census Table E official XLSX; both 2010 and 2020 counts checked against workbook XML; QuickFacts returned 403"
with manifest.open("w",newline="",encoding="utf-8-sig") as f:
 writer=csv.DictWriter(f,fieldnames=columns)
 writer.writeheader()
 writer.writerows(rows)
print("OFFICIAL XLSX VALIDATED",p,p.stat().st_size)
print("ARCHIVED",sum(r["validation"]=="PASS" for r in rows),"of",len(rows))
