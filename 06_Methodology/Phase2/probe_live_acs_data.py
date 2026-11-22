import requests
p='https://api.census.gov/data/2020/acs/acs5/profile'
qs={'get':'NAME,DP02_0068PE,DP03_0009PE,DP03_0062E,DP03_0128PE','for':'state:11'}
for url in [p,'https://api.census.gov/data/2019/acs/acs1/profile']:
 try:
  r=requests.get(url,params=qs,timeout=25)
  print(r.status_code,len(r.content),r.url,r.text[:180],flush=True)
 except Exception as e:print('ERROR',str(e),flush=True)
