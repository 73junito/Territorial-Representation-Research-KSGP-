from pathlib import Path
import pyreadstat, pandas as pd, hashlib
p=Path(r'I:\Territorial-Representation-Research\02_SPSS_Data')
a=p/'population_2010_2020.sav'
b=p/'population_2010_2021.sav'
assert a.is_file() and b.is_file(), 'File missing; no deletion'
da,ma=pyreadstat.read_sav(str(a))
db,mb=pyreadstat.read_sav(str(b))
pd.testing.assert_frame_equal(da,db,check_dtype=True,check_exact=True)
assert len(da)==6 and set(da.geo_code)=={'PR','DC','GU','VI','AS','MP'}
assert int(da.population_2020.sum())==4313440
print('DATASETS_IDENTICAL',len(da),len(da.columns),flush=True)
print('PRIMARY_SHA256',hashlib.sha256(a.read_bytes()).hexdigest(),flush=True)
print('EXTRA_SHA256',hashlib.sha256(b.read_bytes()).hexdigest(),flush=True)
b.unlink()
assert not b.exists() and a.is_file()
verify,_=pyreadstat.read_sav(str(a))
pd.testing.assert_frame_equal(da,verify,check_exact=True)
print('EXTRA_REMOVED_PRIMARY_REVALIDATED',flush=True)
