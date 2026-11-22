import zipfile
import json

# Examine Island Areas ZIP files
zip_paths = [
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\GU_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\MP_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\VI_2020_demographic_profile_original.zip',
]

for zp in zip_paths:
    print(f'\n=== {zp} ===')
    try:
        with zipfile.ZipFile(zp) as z:
            print(f'Files: {z.namelist()}')
            for name in z.namelist():
                if 'variables' in name.lower() or name.endswith('.json'):
                    print(f'  Examining: {name}')
                    try:
                        content = z.read(name).decode('utf-8')
                        print(f'  First 3000 chars: {content[:3000]}')
                    except Exception as e:
                        print(f'  Error reading: {e}')
    except Exception as e:
        print(f'Error opening ZIP: {e}')

# Examine ACS JSON files
acs_paths = [
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2020_5YR_variables.json',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2019_1YR_variables.json',
]

for acs_path in acs_paths:
    print(f'\n=== {acs_path} ===')
    try:
        with open(acs_path, 'r') as f:
            content = f.read()
            # Find the variable we need
            var_names = ['DP2_0016P', 'DP3_0009C', 'DP3_0104C', 'DP3_0151P', 'DP02_0068PE', 'DP03_0009PE', 'DP03_0062E', 'DP03_0128PE']
            for vn in var_names:
                if vn in content:
                    idx = content.find(vn)
                    print(f'  Found {vn} at position {idx}')
                    # Print context around the variable
                    start = max(0, idx - 200)
                    end = min(len(content), idx + 500)
                    print(f'  Context: {content[start:end]}')
    except Exception as e:
        print(f'Error reading {acs_path}: {e}')
PYEOF