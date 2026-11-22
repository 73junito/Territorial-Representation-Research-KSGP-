from pathlib import Path
import csv,math,hashlib
root=Path(r'I:\Territorial-Representation-Research')
data=root/'02_SPSS_Data'/'Phase2'
def load(name):
 with (data/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
results=[]
for period,detail,parts in [('2019_1yr','prdc_2019_acs_one_year_detailed_source_specific.csv','prdc_2019_acs_one_year_raw_components_with_moe.csv'),('2016_2020_5yr','prdc_2020_acs_five_year_detailed_source_specific.csv','prdc_2020_acs_five_year_raw_components_with_moe.csv')]:
 comp={(r['jurisdiction'],r['table_variable'],r['component_type']):float(r['value']) for r in load(parts)}
 assert len(comp)==40
 def get(g,var,kind):return comp[(g,var,kind)]
 for r in load(detail):
  g=r['jurisdiction'];domain=r['domain'];estimated=float(r['estimate'])
  if domain=='median_household_income': continue
  if domain=='education':
   variables=[f'B15003_{i:03d}' for i in range(22,26)]
   numerator=sum(get(g,v,'estimate') for v in variables)
   numerator_moe=math.sqrt(sum(get(g,v,'published_90pct_MOE')**2 for v in variables))
   denvar='B15003_001'
   rule='Census sum-of-components MOE (quadrature) then subset-proportion MOE'
  elif domain=='unemployment':
   numerator=get(g,'B23025_005','estimate')
   numerator_moe=get(g,'B23025_005','published_90pct_MOE')
   denvar='B23025_003'
   rule='Census subset-proportion MOE'
  else:
   assert domain=='poverty'
   numerator=get(g,'B17001_002','estimate')
   numerator_moe=get(g,'B17001_002','published_90pct_MOE')
   denvar='B17001_001'
   rule='Census subset-proportion MOE'
  denominator=get(g,denvar,'estimate')
  denominator_moe=get(g,denvar,'published_90pct_MOE')
  assert 0<=numerator<=denominator and denominator>0
  p=numerator/denominator
  assert abs(100*p-estimated)<0.000051,(period,g,domain,100*p,estimated)
  rad=numerator_moe**2-(p*denominator_moe)**2
  fallback=rad<0
  if fallback: rad=numerator_moe**2+(p*denominator_moe)**2
  moe=100*math.sqrt(rad)/denominator
  assert math.isfinite(moe) and moe>0
  results.append(dict(jurisdiction=g,source_period=period,domain=domain,estimate_pct=round(100*p,5),numerator_estimate=numerator,numerator_moe90=round(numerator_moe,5),denominator_estimate=denominator,denominator_moe90=denominator_moe,moe90_percentage_points=round(moe,5),ci90_lower_pct=round(max(0,100*p-moe),5),ci90_upper_pct=round(min(100,100*p+moe),5),formula='subset_proportion' if not fallback else 'general_ratio_fallback_negative_radicand',formula_note=rule,moe_method_source='https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf',rate_source_csv=detail,component_source_csv=parts,method_status='DERIVED_90PCT_APPROXIMATION_REQUIRES_PUBLISHED_PROFILE_CROSSCHECK'))
out=data/'phase2f_prdc_derived_rate_moe90.csv'
assert not out.exists(),out
with out.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=results[0].keys());w.writeheader();w.writerows(results)
assert len(results)==12
print('SAVED',out,'SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
for r in results:print(r['source_period'],r['jurisdiction'],r['domain'],r['estimate_pct'],'+/-',r['moe90_percentage_points'],'90CI',r['ci90_lower_pct'],r['ci90_upper_pct'],r['formula'],flush=True)
