import pandas as pd
import numpy as np

# Check CSV
csv_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.csv'
a = pd.read_csv(csv_path, keep_default_na=False)

print("=== CSV FILE ===")
print("geo_codes:", sorted(a['geo_code'].unique()))
print("columns:", list(a.columns))
print("head(3):")
print(a.head(3))

# Check SPSS
import pyreadstat
sav_path = r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav'
b, meta = pyreadstat.read_sav(str(sav_path))

print("\n=== SPSS FILE ===")
print("geo_codes:", sorted(b['geo_code'].unique()))
print("columns:", list(b) if hasattr(b, 'columns') else 'N/A')
print("shape:", b.shape if hasattr(b, 'shape') else 'N/A')

# Compare
print("\n=== COMPARISON ===")
print("CSV rows:", len(a))
print("SPSS rows:", len(b))

# Check geo_code match
csv_codes = set(a['geo_code'].unique())
spss_codes = set(b['geo_code'].unique())
print("CSV geo_codes:", csv_codes)
print("SPSS geo_codes:", spss_codes)
print("Match:", csv_codes == spss_codes)