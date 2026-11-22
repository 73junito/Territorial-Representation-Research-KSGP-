import pandas as pd
import numpy as np
import pyreadstat

csv_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.csv'
sav_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav'

a = pd.read_csv(csv_path, keep_default_na=False)
b, meta = pyreadstat.read_sav(str(sav_path))

print('=== CSV geo_code ===')
print('dtype:', a['geo_code'].dtype)
print('values:', a['geo_code'].tolist())
print('unique:', sorted(a['geo_code'].unique()))

print('\n=== SPSS geo_code ===')
print('columns:', list(b))
if 'geo_code' in b:
    print('dtype:', b['geo_code'].dtype)
    print('values:', b['geo_code'].tolist())
    print('unique:', sorted(b['geo_code'].unique()))

print('\n=== Comparison ===')
for col in a.columns:
    is_numeric = pd.api.types.is_numeric_dtype(a[col])
    print(f'{col}: is_numeric={is_numeric}')
    if is_numeric:
        try:
            result = np.allclose(a[col].to_numpy(), b[col].to_numpy(), atol=1e-8, rtol=0)
            print(f'  allclose: {result}')
        except Exception as e:
            print(f'  allclose error: {e}')
    else:
        try:
            result = (a[col] == b[col]).all()
            print(f'  equality: {result}')
        except Exception as e:
            print(f'  equality error: {e}')