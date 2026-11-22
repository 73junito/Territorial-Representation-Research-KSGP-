from pathlib import Path
import json,requests
p=Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
v=json.loads((p/'GU_DP_variables.json').read_text())['variables']
for start,end in [(1,20),(135,162)]:
 print('POVERTY RANGE',start,end)
 for i in range(start,end+1):
  k=f'DP3_{i:04d}C'
  if k in v and ((start==1 and i<=12) or start>100):print(k,v[k]['label'][:185])
urls=[
 'https://api.census.gov/data/2020/acs/acs5/profile/variables.json',
 'https://api.census.gov/data/2019/acs/acs1/profile/variables.json',
 'https://api.census.gov/data/2020/acs/acs5/profile?get=NAME,DP02_0068PE,DP03_0005PE,DP03_0062E,DP03_0128PE&for=state:11'
]
for u in urls:
 try:
  r=requests.get(u,timeout=16)
  print('HTTP',r.status_code,len(r.content),r.url,r.headers.get('content-type'),r.text[:110],flush=True)
  if 'variables.json' in u and r.ok and r.headers.get('content-type','').startswith('application/json'):
   out=p/('ACS_2020_5YR_variables.json' if '/2020/' in u else 'ACS_2019_1YR_variables.json')
   out.write_bytes(r.content)
   doc=r.json()['variables']
   for key in ['DP02_0068PE','DP03_0005PE','DP03_0062E','DP03_0128PE','DP03_0009PE','DP03_0062PE','DP03_0128E']:
    print(key,doc.get(key,{}).get('label','ABSENT')[:170])
 except Exception as ex:print('ERROR',str(ex),flush=True)
