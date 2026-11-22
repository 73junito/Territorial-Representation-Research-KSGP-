from pathlib import Path
import requests,hashlib,csv,re
root=Path(r"I:\Territorial-Representation-Research")
folder=root/"01_Government_Sources"/"official_2020_archives"
base="https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/"
info={
"VI":("us-virgin-islands","us-virgin-islands-phc-table01.csv",87146),
"AS":("american-samoa","american-samoa-phc-table01.csv",49710),
"MP":("commonwealth-of-the-northern-mariana-islands","commonwealth-northern-mariana-islands-phc-table01.csv",47329)}
manifest=root/"01_Government_Sources"/"official_tables_manifest.csv"
with manifest.open("r",newline="",encoding="utf-8-sig") as f:
 reader=csv.DictReader(f);rows=list(reader);columns=reader.fieldnames
for geo,(slug,file,expected) in info.items():
 try:
  url=base+slug+"/population-and-housing-unit-counts/"+file
  response=requests.get(url,timeout=15);response.raise_for_status()
  body=response.content
  text=body.decode("utf-8-sig",errors="replace")
  assert str(expected) in text.replace(",",""),"Census count absent"
  dest=folder/f"CENSUS_{geo}_PHC_Table01_2020.csv"
  dest.write_bytes(body)
  for row in rows:
   if row["geo_code"]==geo: row.update({"source_url":url,"archive_path":str(dest.relative_to(root)),"bytes":str(len(body)),"sha256":hashlib.sha256(body).hexdigest(),"status":"PASS"})
  print(geo,"PASS",len(body),flush=True)
 except Exception as e:
  print(geo,"BLOCKED",str(e),flush=True)
with manifest.open("w",newline="",encoding="utf-8-sig") as f:
 writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader();writer.writerows(rows)
print("MACHINE_READABLE_SOURCE_ARCHIVES",sum(x["status"]=="PASS" for x in rows),"of 4")
