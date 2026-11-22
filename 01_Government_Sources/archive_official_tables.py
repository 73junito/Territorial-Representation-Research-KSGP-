from pathlib import Path
import requests,hashlib,csv,re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
root=Path(r"I:\Territorial-Representation-Research")
folder=root/"01_Government_Sources"/"official_2020_archives"
items={
"GU":("https://www.census.gov/data/tables/2020/dec/2020-guam.html",153836),
"VI":("https://www.census.gov/data/tables/2020/dec/2020-us-virgin-islands.html",87146),
"AS":("https://www.census.gov/data/tables/2020/dec/2020-american-samoa.html",49710),
"MP":("https://www.census.gov/data/tables/2020/dec/2020-commonwealth-northern-mariana-islands.html",47329)}
rows=[]
for geo,(page,expected) in items.items():
 try:
  r=requests.get(page,timeout=20);r.raise_for_status()
  soup=BeautifulSoup(r.content,"html.parser")
  links=[urljoin(page,a.get("href")) for a in soup.select("a[href]") if (a.get("href") or "").lower().endswith("phc-table01.csv")]
  if len(links)!=1:raise RuntimeError("Expected 1 table01 CSV link, found "+str(links))
  url=links[0]
  r=requests.get(url,timeout=20);r.raise_for_status()
  body=r.content
  if len(body)>3000000 or len(body)<100:raise RuntimeError("Unexpected CSV size")
  text=body.decode("utf-8-sig",errors="replace")
  if not re.search(r"\b"+str(expected)+r"\b",text.replace(",","")):raise ValueError("Expected population not in source CSV")
  dest=folder/f"CENSUS_{geo}_PHC_Table01_2020.csv"
  dest.write_bytes(body)
  rows.append([geo,url,str(dest.relative_to(root)),len(body),hashlib.sha256(body).hexdigest(),"PASS"])
  print(geo,"PASS",len(body),flush=True)
 except Exception as e:
  rows.append([geo,page,"",0,"","BLOCKED "+str(e)[:100]])
  print(geo,"BLOCKED",repr(e),flush=True)
with (root/"01_Government_Sources"/"official_tables_manifest.csv").open("w",newline="",encoding="utf-8-sig") as f:
 w=csv.writer(f)
 w.writerow(["geo_code","source_url","archive_path","bytes","sha256","status"])
 w.writerows(rows)
print("OFFICIAL_CSV",sum(r[5]=="PASS" for r in rows),"/",len(rows),flush=True)
