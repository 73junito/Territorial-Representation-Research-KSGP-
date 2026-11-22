import pandas as pd
import numpy as np
import pyreadstat

csv_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.csv'
sav_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav'

a = pd.read_csv(csv_path, keep_default_na=False)
b, meta = pyreadstat.read_sav(str(sav_path))

# Sort both by geo_code to compare
a_sorted = a.sort_values('geo_code').reset_index(drop=True)
b_sorted = pd.DataFrame(b).sort_values('geo_code').reset_index(drop=True) if 'geo_code' in b else b.sort_index().reset_index(drop=True)

print('=== After sorting by geo_code ===')
print('CSV geo_code:', a_sorted['geo_code'].tolist())
print('SPSS geo_code:', b_sorted['geo_code'].tolist() if 'geo_code' in b_sorted else 'N/A')

print('\n=== Column-by-column comparison after sorting ===')
for col in a_sorted.columns:
    is_numeric = pd.api.types.is_numeric_dtype(a_sorted[col])
    print(f'{col}: is_numeric={is_numeric}')
    if is_numeric:
        try:
            result = np.allclose(a_sorted[col].to_numpy(), b_sorted[col].to_numpy(), atol=1e-8, rtol=0)
            print(f'  allclose: {result}')
        except Exception as e:
            print(f'  allclose error: {e}')
    else:
        try:
            result = (a_sorted[col] == b_sorted[col]).all()
            print(f'  equality: {result}')
        except Exception as e:
            print(f'  equality error: {e}')