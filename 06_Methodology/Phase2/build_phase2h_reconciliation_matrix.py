from pathlib import Path
import csv,hashlib
root=Path(r'I:\Territorial-Representation-Research')
source=root/'02_SPSS_Data'/'Phase2'/'phase2f_prdc_derived_rate_moe90.csv'
with source.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
assert len(rows)==12
out=[]
for r in rows:
 g=r['jurisdiction']
 domain=r['domain']
 v='DP02PR_0068PM' if domain=='education' and g=='PR' else 'DP02_0068PM' if domain=='education' else 'DP03_0009PM' if domain=='unemployment' else 'DP03_0128PM'
 e=v[:-1]+'E'
 period=r['source_period']
 year='2019' if period=='2019_1yr' else '2020'
 product='acs1' if year=='2019' else 'acs5'
 fips='72' if g=='PR' else '11'
 url=f'https://api.census.gov/data/{year}/acs/{product}/profile/variables/{v}.html'
 out.append(dict(jurisdiction=g,period=period,domain=domain,derived_estimate_pct=r['estimate_pct'],derived_moe90_pp=r['moe90_percentage_points'],derived_ci90_lower=r['ci90_lower_pct'],derived_ci90_upper=r['ci90_upper_pct'],published_profile_estimate_variable=e,published_profile_moe_variable=v,published_variable_definition_url=url,published_profile_estimate_pct='',published_profile_moe90_pp='',moe_delta_pp='',reconciliation_status='BLOCKED_PUBLISHED_NUMERIC_VALUE_NOT_RETRIEVED',source_blocker='Official Census numeric API redirected to missing_key.html; legacy downloadable profile directory 404',non_equivalence_caution='Verify Puerto Rico DP02PR universe; profile rounding and method may differ from Detailed Table derived estimate',geography_fips=fips))
dst=root/'06_Methodology'/'Phase2'/'PHASE2H_MOE_RECONCILIATION_MATRIX.csv'
assert not dst.exists()
with dst.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
print('CREATED',dst,'ROWS',len(out),'SHA256',hashlib.sha256(dst.read_bytes()).hexdigest())
for r in out:print(r['period'],r['jurisdiction'],r['domain'],r['published_profile_moe_variable'],r['reconciliation_status'])
