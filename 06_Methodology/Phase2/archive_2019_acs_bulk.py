import requests,pathlib,zipfile,hashlib
base=pathlib.Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
u='https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/1_year_by_state/'
for k,name in [('DC','DistrictofColumbia_All_Geographies.zip'),('PR','PuertoRico_All_Geographies.zip')]:
 p=base/f'{k}_2019_ACS_1YR_summary_original.zip'
 if not p.exists():
  r=requests.get(u+name,timeout=75);r.raise_for_status();assert r.content.startswith(b'PK');p.write_bytes(r.content)
 with zipfile.ZipFile(p) as z:
  assert z.testzip() is None
  print(k,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),'entries',len(z.namelist()),'first',z.namelist()[:9],flush=True)
