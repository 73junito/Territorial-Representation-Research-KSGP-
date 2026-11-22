from pathlib import Path
import requests
paths=[
'https://www2.census.gov/programs-surveys/acs/summary_file/2019/data/1_year_data_profiles/',
'https://www2.census.gov/programs-surveys/acs/summary_file/2020/data/5_year_data_profiles/',
'https://api.census.gov/data/2019/acs/acs1/profile?get=NAME%2CDP02_0068PM&for=state%3A11',
'https://api.census.gov/data/2019/acs/acs1/profile?get=NAME%2CDP02PR_0068PM&for=state%3A72',
'https://api.census.gov/data/2020/acs/acs5/profile?get=NAME%2CDP03_0009PM&for=state%3A11',
]
for u in paths:
 try:
  r=requests.get(u,timeout=16,allow_redirects=True)
  print('URL',u,'RESULT',r.status_code,'FINAL',r.url,'BODY',r.text[:90].replace('\n',' '),flush=True)
 except Exception as e:print('ERROR',u,str(e)[:130],flush=True)
