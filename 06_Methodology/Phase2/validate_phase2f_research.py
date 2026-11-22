from pathlib import Path
import csv,hashlib,math
root=Path(r'I:\Territorial-Representation-Research')
b=root/'02_SPSS_Data'/'Phase2'
def read(name):
 with (b/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
rates=read('phase2f_prdc_derived_rate_moe90.csv')
assert len(rates)==12
assert len({(r['source_period'],r['jurisdiction'],r['domain']) for r in rates})==12
for period in ('2019_1yr','2016_2020_5yr'):
 components=read('prdc_2019_acs_one_year_raw_components_with_moe.csv' if period=='2019_1yr' else 'prdc_2020_acs_five_year_raw_components_with_moe.csv')
 comp={(r['jurisdiction'],r['table_variable'],r['component_type']):float(r['value']) for r in components}
 for r in (x for x in rates if x['source_period']==period):
  g=r['jurisdiction'];d=r['domain']
  val=lambda v,k:comp[(g,v,k)]
  if d=='education':
   numerator=sum(val(f'B15003_{i:03}','estimate') for i in range(22,26))
   num_moe=math.sqrt(sum(val(f'B15003_{i:03}','published_90pct_MOE')**2 for i in range(22,26)))
   den='B15003_001'
  elif d=='unemployment':
   numerator=val('B23025_005','estimate');num_moe=val('B23025_005','published_90pct_MOE');den='B23025_003'
  else:
   assert d=='poverty'
   numerator=val('B17001_002','estimate');num_moe=val('B17001_002','published_90pct_MOE');den='B17001_001'
  total=val(den,'estimate');p=numerator/total
  rad=num_moe**2-p*p*val(den,'published_90pct_MOE')**2
  assert rad>=0 and r['formula']=='subset_proportion'
  moe=100*math.sqrt(rad)/total
  assert abs(float(r['moe90_percentage_points'])-moe)<0.0000051
  assert abs(float(r['estimate_pct'])-100*p)<0.0000051
  assert abs(float(r['ci90_lower_pct'])-max(0,100*p-moe))<0.0000051
  assert abs(float(r['ci90_upper_pct'])-min(100,100*p+moe))<0.0000051
  assert 0<float(r['ci90_lower_pct'])<float(r['ci90_upper_pct'])<100
reports=[
 root/'08_Final_Report'/'Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md',
 root/'06_Methodology'/'Phase2'/'PHASE2F_SAV_HASH_FORENSIC.md'
]
assert all(p.exists() for p in reports)
report=reports[0].read_text(encoding='utf-8')
assert 'NO-GO' in report and 'CONDITIONAL' in report and '90%' in report
assert 'byte hash' in report
for f in [b/'phase2f_prdc_derived_rate_moe90.csv',*reports]:
 print('PASS',f.name,f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest(),flush=True)
print('PASS 12 independently recomputed 90% derived percentage MOEs + intervals, no negative radicands; report gate accepted with cross-check pending',flush=True)
