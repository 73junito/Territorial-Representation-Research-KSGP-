"""Read the directly published Census count MOE for DC bachelor's degree or higher.
Uses GitHub Actions' existing CENSUS_DATA_API secret. Never logs the key.
"""
from pathlib import Path
import csv, hashlib, json, os, requests, sys

root=Path(__file__).resolve().parents[2]
key=os.environ.get("CENSUS_API_KEY","").strip()
if not key:
 print("BLOCKED: no local Census API key; no network or writes")
 sys.exit(2)
dest=root/"06_Methodology"/"Phase2"
source=root/"02_SPSS_Data"/"Phase2"
items=[]
raw=[]
for period,year,product in [("2019_1yr","2019","acs1"),("2016_2020_5yr","2020","acs5")]:
 endpoint=f"https://api.census.gov/data/{year}/acs/{product}/profile"
 fields=["NAME","DP02_0068E","DP02_0068M","DP02_0068PE","DP02_0068PM"]
 try:
  r=requests.get(endpoint,params={"get":",".join(fields),"for":"state:11","key":key},timeout=40)
 except requests.RequestException:
  raise RuntimeError(f"BLOCKED {period}: request failed, detail suppressed") from None
 if r.status_code!=200 or "missing_key.html" in r.url:
  raise RuntimeError(f"BLOCKED {period}: official API status {r.status_code} or missing_key redirect")
 try:
  payload=r.json()
 except ValueError:
  raise RuntimeError(f"BLOCKED {period}: official API returned non-JSON") from None
 assert isinstance(payload,list) and len(payload)==2
 record=dict(zip(payload[0],payload[1]))
 assert record["state"]=="11"
 for f in fields[1:]:assert f in record and record[f] not in ("","-","N","(X)")
 filename=f"ACS_DC_{year}_Direct_Education_Profile_Count_Official.json"
 raw.append((dest/filename,json.dumps(payload,indent=2).encode("utf-8")))
 items.append(dict(period=period,year=year,count_estimate=float(record["DP02_0068E"]),count_moe90=float(record["DP02_0068M"]),rate_estimate_pct=float(record["DP02_0068PE"]),rate_moe90_pp=float(record["DP02_0068PM"]),variable="DP02_0068E/M/PE/PM",source_endpoint=endpoint,source_json=filename))

assert len(items)==2
report=dest/"PHASE2I_DC_DIRECT_EDUCATION_COUNT_MOE.csv"
assert not report.exists() and all(not p.exists() for p,v in raw)
for p,v in raw:
 p.write_bytes(v)
 print("ARCHIVED",p.name,"SHA256",hashlib.sha256(v).hexdigest())
with report.open("w",encoding="utf-8-sig",newline="") as f:
 writer=csv.DictWriter(f,fieldnames=items[0].keys());writer.writeheader();writer.writerows(items)
print("SUCCESS direct published count MOEs",[(r["period"],r["count_moe90"],r["rate_moe90_pp"]) for r in items])
