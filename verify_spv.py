import zipfile
import os

spv_path = r'I:\\Territorial-Representation-Research\\04_SPSS_Output\\Phase2\\01_age_sex_2020_descriptive.spv'
csv_path = r'I:\\Territorial-Representation-Research\\02_SPSS_Data\\Phase2\\age_sex_2020_six_jurisdictions.csv'
sav_path = r'I:\\Territorial-Representation-Research\\02_SPSS_Data\\Phase2\\age_sex_2020_six_jurisdictions.sav'

print('=== SPV File Check ===')
print('Exists:', os.path.exists(spv_path))
print('Size:', os.path.getsize(spv_path) if os.path.exists(spv_path) else 'N')
print('Is zipfile:', zipfile.is_zipfile(spv_path) if os.path.exists(spv_path) else 'N')

print('\n=== CSV Check ===')
import pandas as pd
a = pd.read_csv(csv_path, keep_default_na=False)
print('Rows:', len(a))
print('geo_codes:', sorted(a['geo_code'].unique()))

print('\n=== SPSS SAV Check ===')
import pyreadstat
b, meta = pyreadstat.read_sav(str(sav_path))
print('Rows:', len(b))
print('geo_codes:', sorted(b['geo_code'].unique()))

# Compare sorted
a_sorted = a.sort_values('geo_code').reset_index(drop=True)
b_sorted = pd.DataFrame(b).sort_values('geo_code').reset_index(drop=True) if 'geo_code' in b else b

print('\n=== Column comparison (sorted) ===')
for col in a_sorted.columns:
    is_numeric = pd.api.types.is_numeric_dtype(a_sorted[col])
    if is_numeric:
        result = float(np.allclose(a_sorted[col].to_numpy(), b_sorted[col].to_numpy(), atol=1e-8, rtol=0))
        print(f'{col}: allclose={result}')
    else:
        result = (a_sorted[col] == b_sorted[col]).all()
        print(f'{col}: equality={result}')