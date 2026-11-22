from pathlib import Path
import json,csv,hashlib,zipfile
from datetime import datetime,timezone
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'
cen=base/'Census'
methods=root/'06_Methodology'/'Phase2'
islands={'AS':'American Samoa','GU':'Guam','MP':'Northern Mariana Islands','VI':'U.S. Virgin Islands'}
special={'DC':'Washington, D.C.','PR':'Puerto Rico'}
catalog={
 'education':('DP2_0016P','DP02_0068PE','Bachelor degree or higher (%)','Age 25+'),
 'employment':('DP3_0009C','DP03_0009PE','Unemployment rate (%)','Civilian labor force'),
 'household_income':('DP3_0104C','DP03_0062E','Median household income (USD)','Households'),
 'poverty':('DP3_0151P','DP03_0128PE','All-person poverty rate (%)','Poverty-status universe')
}
meta={code:json.loads((cen/f'{code}_DP_variables.json').read_text(encoding='utf-8'))['variables'] for code in islands}
acs=json.loads((cen/'ACS_2020_5YR_variables.json').read_text(encoding='utf-8'))['variables']
rows=[]
for topic,(key,akey,metric,denominator) in catalog.items():
 for code,name in {**islands,**special}.items():
  is_island=code in islands
  ref=meta[code] if is_island else acs
  field=key if is_island else akey
  assert field in ref,(code,topic,field)
  label=ref[field]['label']
  pop_scope='Military housing excluded' if 'excluding people in military housing units' in label or 'excluding families in military housing' in label else ('Household residents only' if 'in households' in label else 'Full or specified table population; verify precise universe')
  if is_island:
   source='2020 Island Areas Census, Demographic Profile (DP2/DP3)'
   period='2020 Census enumeration; income/poverty reference calendar year 2019' if topic in ('poverty','household_income') else '2020 Census enumeration'
   path=cen/f'{code}_2020_demographic_profile_original.zip'
   decision='NO_GO_CROSS_SIX'
   why='Distinct Island Areas census collection, definitions and denominator; differs from ACS/PRCS. Check group quarters/military exclusions.'
  else:
   source='2016-2020 ACS/PRCS five-year Data Profile metadata, estimates NOT archived'
   period='2016-2020 pooled sample; past 12 months, in 2020 inflation-adjusted dollars' if topic in ('poverty','household_income') else '2016-2020 pooled sample'
   path=cen/'ACS_2020_5YR_variables.json'
   decision='NO_GO_CROSS_SIX'
   why='Period and survey methodology differ from 2020 Island Areas decennial enumeration; numeric observations not yet archived.'
  rows.append(dict(topic=topic,metric=metric,geo_code=code,jurisdiction=name,source_product=source,reference_period=period,variable_id=field,source_label=label,desired_universe=denominator,population_scope=pop_scope,original_file=str(path.relative_to(root)),downloaded_observations=('YES_ARCHIVE_PRESENT_NOT_PARSED' if is_island else 'NO_VARIABLE_METADATA_ONLY'),cross_six_gate=decision,reason=why))
out=base/'socioeconomic_comparability_matrix.csv'
with out.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
reg=[]
for code in islands:
 p=cen/f'{code}_2020_demographic_profile_original.zip'
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 reg.append(dict(product=f'2020 Island Areas DP {code}',geo_code=code,original_url={
 'AS':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/american-samoa/demographic_profile/as2020.dp.zip',
 'GU':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/guam/demographic_profile/gu2020.dp.zip',
 'MP':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/commonwealth-of-the-northern-mariana-islands/demographic_profile/mp2020.dp.zip',
 'VI':'https://www2.census.gov/programs-surveys/decennial/2020/data/island-areas/us-virgin-islands/demographic_profile/vi2020.dp.zip'}[code],local_file=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),integrity='ZIP_CRC_PASS',observations='ARCHIVED'))
for name,code,url in [
 ('2020 ACS 5-year Profile variables','DC and PR','https://api.census.gov/data/2020/acs/acs5/profile/variables.json'),
 ('2019 ACS 1-year Profile variables','DC, PR needs PRCS confirmation','https://api.census.gov/data/2019/acs/acs1/profile/variables.json')]:
 p=cen/('ACS_2020_5YR_variables.json' if '2020' in name else 'ACS_2019_1YR_variables.json')
 assert p.exists()
 reg.append(dict(product=name,geo_code=code,original_url=url,local_file=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),integrity='JSON_PARSED',observations='METADATA_ONLY'))
with (base/'socioeconomic_source_register.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(reg[0]));w.writeheader();w.writerows(reg)
print('MATRIX_RECORDS',len(rows),'SOURCES',len(reg))
for topic in catalog:
 print('TOPIC',topic,[(r['geo_code'],r['population_scope']) for r in rows if r['topic']==topic],flush=True)
