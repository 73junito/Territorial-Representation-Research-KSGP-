from pathlib import Path
import requests, hashlib, zipfile, csv, io
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timezone
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'
urls={
'AS':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/american-samoa/demographic_profile/',
'GU':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/guam/demographic_profile/',
'MP':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/commonwealth-of-the-northern-mariana-islands/demographic_profile/',
'VI':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/us-virgin-islands/demographic_profile/'}
entries=[]
for code,url in urls.items():
 try:
  res=requests.get(url,timeout=17);res.raise_for_status()
  links=[urljoin(url,a.get('href')) for a in BeautifulSoup(res.text,'html.parser').select('a[href]') if (a.get('href') or '').lower().endswith('.zip')]
  if not links:raise RuntimeError('No Census ZIP available')
  choice=next((u for u in links if '.dp.zip' in u.lower()),links[0])
  rr=requests.get(choice,timeout=30);rr.raise_for_status()
  raw=rr.content
  with zipfile.ZipFile(io.BytesIO(raw)) as zz:
   names=zz.namelist()
   if not names or any('..' in Path(n).parts for n in names):raise RuntimeError('Unsafe/empty ZIP')
  dest=base/'Census'/f'{code}_2020_demographic_profile_original.zip'
  dest.write_bytes(raw)
  entries.append(dict(jurisdiction=code,source_page=url,download_url=choice,local_file=str(dest.relative_to(root)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),status='VERIFIED_ZIP',archive_members=' | '.join(names[:10]),retrieved_utc=datetime.now(timezone.utc).isoformat()))
  print('ARCHIVED',code,len(raw),len(names),names[:5],flush=True)
 except Exception as ex:
  entries.append(dict(jurisdiction=code,source_page=url,download_url='',local_file='',bytes=0,sha256='',status='BLOCKED '+str(ex)[:120],archive_members='',retrieved_utc=datetime.now(timezone.utc).isoformat()))
  print('BLOCKED',code,str(ex),flush=True)
with (base/'source_inventory_phase2.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(entries[0]));w.writeheader();w.writerows(entries)
print('SUMMARY',sum(e['status']=='VERIFIED_ZIP' for e in entries),'of 4')
