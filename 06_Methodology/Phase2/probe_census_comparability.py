import requests
from pathlib import Path
root=Path(r'I:\Territorial-Representation-Research')
for code,url in [
 ('US_DP','https://api.census.gov/data/2020/dec/dp/variables.json'),
 ('GU_DP','https://api.census.gov/data/2020/dec/dpgu/variables.json'),
 ('AS_DP','https://api.census.gov/data/2020/dec/dpas/variables.json'),
 ('MP_DP','https://api.census.gov/data/2020/dec/dpmp/variables.json'),
 ('VI_DP','https://api.census.gov/data/2020/dec/dpvi/variables.json')]:
 try:
  res=requests.get(url,timeout=20)
  print(code,res.status_code,len(res.content),flush=True)
  if res.ok:
   doc=res.json()['variables']
   for pattern in ('Median age','Median household income','Poverty','Bachelor','Unemployed','Total population'):
    found=[(k,v.get('label','')[:75]) for k,v in doc.items() if pattern.lower() in v.get('label','').lower()]
    print(pattern,found[:3],flush=True)
   path=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'/f'{code}_variables.json'
   path.write_bytes(res.content)
 except Exception as e:print(code,'ERROR',str(e),flush=True)
