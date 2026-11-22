import requests,pathlib,zipfile,hashlib
p=pathlib.Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\2019_1yr_Summary_FileTemplates_original.zip')
u='https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/2019_1yr_Summary_FileTemplates.zip'
if not p.exists():
 r=requests.get(u,timeout=55);r.raise_for_status();p.write_bytes(r.content)
with zipfile.ZipFile(p) as z:
 assert z.testzip() is None
 print('ARCHIVED',len(z.namelist()),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
 print('SAMPLES',z.namelist()[:25])
