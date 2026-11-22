from pathlib import Path
import csv,zipfile,hashlib,math,collections
root=Path(r'I:\Territorial-Representation-Research')
c=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
data=root/'02_SPSS_Data'/'Phase2'
files={
 'island':data/'island_areas_2020_socioeconomic_source_specific.csv',
 'acs2019':data/'prdc_2019_acs_one_year_detailed_source_specific.csv',
 'acs2020':data/'prdc_2020_acs_five_year_detailed_source_specific.csv',
 'components2019':data/'prdc_2019_acs_one_year_raw_components_with_moe.csv',
 'components2020':data/'prdc_2020_acs_five_year_raw_components_with_moe.csv',
}
def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
r={k:read(p) for k,p in files.items()}
assert [len(r[k]) for k in files]==[16,8,8,40,40]
for k in ('island','acs2019','acs2020'):
 assert len({(x['jurisdiction'],x['domain']) for x in r[k]})==len(r[k])
 assert {x['domain'] for x in r[k]}=={'education','unemployment','median_household_income','poverty'}
assert {x['jurisdiction'] for x in r['island']}=={'AS','GU','MP','VI'}
for key in ('acs2019','acs2020'):
 assert {x['jurisdiction'] for x in r[key]}=={'DC','PR'}
 assert all(x['comparability_gate']=='NO_GO_CROSS_SIX' for x in r[key])
 for x in r[key]:
  n=float(x['estimate'])
  if x['domain']!='median_household_income': assert 0<n<100
  else:
   assert n>0 and x['margin_of_error'] and float(x['margin_of_error'])>0
for x in r['island']:
 n=float(x['value'])
 assert 0<n<100 if x['domain']!='median_household_income' else n>0
 if x['domain']=='poverty':
  assert abs(n-(100*float(x['source_raw_value'])/float(x['source_denominator_raw'])))<0.00005
for year in (2019,2020):
 key=f'components{year}'
 grouped=collections.defaultdict(dict)
 for x in r[key]:
  grouped[(x['jurisdiction'],x['table_variable'])][x['component_type']]=float(x['value'])
  archive=c/x['original_source_archive']
  assert archive.exists()
  with zipfile.ZipFile(archive) as z:
   assert x['original_source_file'] in z.namelist()
   assert z.testzip() is None
 assert len(grouped)==20
 assert all(set(k)=={'estimate','published_90pct_MOE'} for k in grouped.values())
 for x in r['acs2019' if year==2019 else 'acs2020']:
  g=x['jurisdiction'];v=lambda k: grouped[(g,k)]['estimate']
  m=x['domain']
  computed={'education':100*sum(v(f'B15003_{i:03}') for i in range(22,26))/v('B15003_001'),
   'unemployment':100*v('B23025_005')/v('B23025_003'),
   'poverty':100*v('B17001_002')/v('B17001_001'),
   'median_household_income':v('B19013_001')}[m]
  assert abs(float(x['estimate'])-computed)<0.00005,(year,x,computed)
  if m=='median_household_income': assert float(x['margin_of_error'])==grouped[(g,'B19013_001')]['published_90pct_MOE']
# Verify native source ZIPs and technical matrix workbooks remain available
for geo in ('AS','GU','MP','VI'):
 with zipfile.ZipFile(c/f'{geo}_2020_demographic_profile_original.zip') as z:assert z.testzip() is None
assert (c/'2020-iac-dpsf-technical-documentation.pdf').read_bytes().startswith(b'%PDF')
prior='300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8'
current=hashlib.sha256((data/'age_sex_2020_six_jurisdictions.sav').read_bytes()).hexdigest()
if prior!=current:print('WARNING demographic SAV byte hash changed from prior audit; confirm provenance separately:',current,flush=True)
import pandas as pd,pyreadstat,numpy as np
s,_=pyreadstat.read_sav(str(data/'age_sex_2020_six_jurisdictions.sav'))
csv_data=pd.read_csv(data/'age_sex_2020_six_jurisdictions.csv',keep_default_na=False)
assert len(s)==len(csv_data)==6
assert s.geo_code.is_unique and csv_data.geo_code.is_unique
s=s.sort_values('geo_code').reset_index(drop=True)
csv_data=csv_data.sort_values('geo_code').reset_index(drop=True)
for col in csv_data.columns:
 if pd.api.types.is_numeric_dtype(csv_data[col]):assert np.allclose(csv_data[col],s[col],rtol=0,atol=1e-8),col
 else:assert csv_data[col].astype(str).tolist()==s[col].astype(str).tolist(),col
for k,path in files.items():print('VALIDATED',k,len(r[k]),hashlib.sha256(path.read_bytes()).hexdigest(),flush=True)
print('PASS 32 source-specific socioeconomic observations; 80 ACS/PRCS source estimate/MOE components; demographic SAV values match CSV; byte-hash drift documented',flush=True)
print('GO extraction acceptance; NO-GO unqualified six-way SPSS socioeconomic comparison',flush=True)
