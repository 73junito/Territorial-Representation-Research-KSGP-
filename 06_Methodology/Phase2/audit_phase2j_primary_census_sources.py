from pathlib import Path
import csv,hashlib,requests
ROOT=Path(r'I:\Territorial-Representation-Research')
M=ROOT/'01_Government_Sources'/'Phase2_Socioeconomic'/'phase2d_official_acquisition_manifest.csv'
with M.open(encoding='utf-8-sig',newline='') as f: manifest=list(csv.DictReader(f))
print('MANIFEST',len(manifest))
for r in manifest:
 p=ROOT/r['relative_path']
 assert p.exists()
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
 print('SOURCE',r['filename'],'HASH_OK',len(r['sha256']),flush=True)
urls=[
'https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html',
'https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/2020-iac-dpsf-technical-documentation.pdf',
'https://www.census.gov/programs-surveys/acs/data/summary-file/sequence-based/2019.html',
'https://www.census.gov/programs-surveys/acs/data/summary-file/sequence-based/2020.html',
'https://www.census.gov/programs-surveys/acs/library/handbooks/general.html',
]
for url in urls:
 try:
  r=requests.get(url,timeout=12,stream=True)
  print('URL_CHECK',r.status_code,r.url,len(r.headers.get('Content-Type','')),url,flush=True)
  r.close()
 except Exception as e:print('URL_UNCONFIRMED',url,type(e).__name__,flush=True)
