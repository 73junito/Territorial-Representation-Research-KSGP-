from pathlib import Path
import requests, hashlib, zipfile, csv, time
root=Path(r'I:\Territorial-Representation-Research')
dst=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
base='https://www2.census.gov/programs-surveys/decennial/2020/data/demographic-and-housing-characteristics-file/'
items={'DC':('District_of_Columbia','dc'),'PR':('Puerto_Rico','pr')}
rows=[]
for code,(directory,prefix) in items.items():
 url=f'{base}{directory}/{prefix}2020.dhc.zip'
 out=dst/f'{code}_2020_DHC_original.zip'
 sha=hashlib.sha256()
 try:
  with requests.get(url,timeout=(15,70),stream=True) as res:
   res.raise_for_status()
   with out.open('wb') as f:
    for piece in res.iter_content(chunk_size=1024*1024):
     if piece:
      f.write(piece);sha.update(piece)
  with zipfile.ZipFile(out) as z:
   bad=z.testzip()
   if bad:raise RuntimeError('ZIP CRC failure: '+bad)
   names=z.namelist()
  rows.append(dict(geo_code=code,source_url=url,file=str(out.relative_to(root)),sha256=sha.hexdigest(),bytes=out.stat().st_size,status='VERIFIED',members=';'.join(names[:8])))
  print('VERIFIED',code,out.stat().st_size,names[:6],flush=True)
 except Exception as ex:
  rows.append(dict(geo_code=code,source_url=url,file='',sha256='',bytes=0,status='BLOCKED '+str(ex),members=''))
  print('BLOCKED',code,ex,flush=True)
with (dst/'PR_DC_2020_DHC_archive_manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print('COMPLETED',sum(r['status']=='VERIFIED' for r in rows),'/2',flush=True)
