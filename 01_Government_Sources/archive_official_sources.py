from pathlib import Path
import requests,hashlib,csv,re,time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
root=Path(r"I:\Territorial-Representation-Research")
folder=root/"01_Government_Sources"/"official_2020_archives"
folder.mkdir(exist_ok=True)
sites={
"PR":("https://www.census.gov/quickfacts/fact/table/PR/PST045219",3725789,3285874),
"DC":("https://www.census.gov/quickfacts/fact/table/DC/PST120224",601723,689545),
"GU":("https://www.census.gov/newsroom/press-releases/2021/2020-census-guam.html",159358,153836),
"VI":("https://www.census.gov/newsroom/press-releases/2021/2020-census-us-virgin-islands.html",106405,87146),
"AS":("https://www.census.gov/newsroom/press-releases/2021/2020-census-american-samoa.html",55519,49710),
"MP":("https://www.census.gov/newsroom/press-releases/2021/2020-census-cnmi.html",53883,47329)
}
rows=[]
for geo,(url,p10,p20) in sites.items():
 try:
  response=requests.get(url,timeout=18,headers={"User-Agent":"Mozilla/5.0 (research archive, source verification)"})
  response.raise_for_status()
  body=response.content
  content=BeautifulSoup(body,"html.parser").get_text(" ",strip=True)
  clean=lambda s: re.sub(r"\s+"," ",s)
  normalized=clean(content)
  a=(f"{p10:,}" in normalized or str(p10) in normalized)
  b=(f"{p20:,}" in normalized or str(p20) in normalized)
  path=folder/f"CENSUS_{geo}_2010_2020.html"
  if not(a and b):raise ValueError(f"Numeric values not found in visible HTML text 2010={a} 2020={b}; not saving as verified")
  path.write_bytes(body)
  sha=hashlib.sha256(body).hexdigest()
  rows.append([geo,url,str(path.relative_to(root)),len(body),sha,"PASS",f"2010 {p10}; 2020 {p20}"])
  print(geo,"PASS",len(body),flush=True)
 except Exception as e:
  rows.append([geo,url,"",0,"","BLOCKED",str(e)[:180]])
  print(geo,"BLOCKED",repr(e),flush=True)
with (root/"01_Government_Sources"/"archive_manifest.csv").open("w",newline="",encoding="utf-8-sig") as f:
 w=csv.writer(f)
 w.writerow(["geo_code","source_url","archive_path","byte_count","sha256","validation","notes"])
 w.writerows(rows)
print("ARCHIVE_VALIDATED",sum(r[5]=="PASS" for r in rows),"OF",len(rows))
