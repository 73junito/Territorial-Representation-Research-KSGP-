from pathlib import Path
import hashlib, json, zipfile
import numpy as np
import pandas as pd
import pyreadstat
root=Path(r'I:\Territorial-Representation-Research')
base=root/'02_SPSS_Data'/'Phase2'
csv=base/'age_sex_2020_six_jurisdictions.csv'
sav=base/'age_sex_2020_six_jurisdictions.sav'
assert csv.is_file() and sav.is_file()
a=pd.read_csv(csv,keep_default_na=False)
b,meta=pyreadstat.read_sav(str(sav))
assert len(a)==6 and len(b)==6 and a.geo_code.is_unique and b.geo_code.is_unique
assert set(a.geo_code)==set(b.geo_code)=={'AS','DC','GU','MP','PR','VI'}
# SPSS may reorder cases; join by stable jurisdiction code, not row position.
a=a.sort_values('geo_code').reset_index(drop=True)
b=b.sort_values('geo_code').reset_index(drop=True)
for col in a.columns:
 if pd.api.types.is_numeric_dtype(a[col]):
  assert np.allclose(a[col].to_numpy(),b[col].to_numpy(),atol=1e-8,rtol=0),col
 else:assert (a[col]==b[col]).all(),col
assert int(a.population_2020.sum())==4313440
for _,row in a.iterrows():
 assert row.male_2020+row.female_2020==row.population_2020
 assert row.under20_2020+row.age20to64_2020+row.age65plus_2020==row.population_2020
 for k,count in [('male_pct','male_2020'),('female_pct','female_2020'),('under20_pct','under20_2020'),('age65plus_pct','age65plus_2020')]:
  assert abs(row[k]-100*row[count]/row.population_2020)<1e-8
archive=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
for geo in ['AS','GU','MP','VI']:
 with zipfile.ZipFile(archive/f'{geo}_2020_demographic_profile_original.zip') as z:assert z.testzip() is None
for geo in ['DC','PR']:
 with zipfile.ZipFile(archive/f'{geo}_2020_DHC_original.zip') as z:assert z.testzip() is None
out=root/'04_SPSS_Output'/'Phase2'/'01_age_sex_2020_descriptive.spv'
if out.exists():
 assert zipfile.is_zipfile(out)
 status='SPV_EXISTS_PIVOT_CONTENT_PENDING_REVIEW'
else:status='SPV_NOT_YET_GENERATED_IN_SPSS'
print('PASS: 6 jurisdiction records, demographic sums, percentages, CSV/SAV identity, six Census ZIP CRCs')
print('SPSS_OUTPUT',status)
print('CSV_SHA256',hashlib.sha256(csv.read_bytes()).hexdigest())
print('SAV_SHA256',hashlib.sha256(sav.read_bytes()).hexdigest())
