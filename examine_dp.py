import zipfile
import struct

# Examine the DP data files from Island Areas ZIPs
zip_paths = [
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\GU_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\MP_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\VI_2020_demographic_profile_original.zip',
]

dp_field_map = {
    'education': 'DP2_0016P',  # Bachelor's degree or higher
    'unemployment': 'DP3_0009C',  # Civilian unemployment rate
    'median_income': 'DP3_0104C',  # Median household income
    'poverty': 'DP3_0151P',  # Poverty rate
}

for zp in zip_paths:
    print(f'\\n=== {zp} ===')
    try:
        with zipfile.ZipFile(zp) as z:
            dp_files = [f for f in z.namelist() if f.startswith(('as00', 'gu00', 'mp00', 'vi00')) and f.endswith('.dp')]
            print(f'DP files: {dp_files}')
            for dp_file in dp_files[:1]:  # Just examine first DP file
                print(f'\\nExamining: {dp_file}')
                try:
                    data = z.read(dp_file)
                    print(f'Size: {len(data)} bytes')
                    # DP files are dBASE or similar structured format
                    # Try to interpret first bytes
                    print(f'First 100 bytes hex: {data[:100].hex()}')
                    print(f'First 100 bytes raw: {data[:100]}')
                    # Check if it has a header structure
                    if len(data) > 4:
                        # dBASE header: 1 byte version, 32 bytes header, then records
                        version = data[0]
                        print(f'Version byte: {version}')
                        # Header length
                        header_len = struct.unpack('<H', data[8:10])[0] if len(data) > 8 else '?'
                        print(f'Header length: {header_len}')
                except Exception as e:
                    print(f'Error reading DP file: {e}')
    except Exception as e:
        print(f'Error opening ZIP: {e}')

# Also check the geo header file
print('\\n=== Checking geo header files ===')
geo_files = [
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip',
]
for zp in geo_files:
    try:
        with zipfile.ZipFile(zp) as z:
            geo_files_list = [f for f in z.namelist() if 'geo' in f.lower()]
            print(f'Geo files: {geo_files_list}')
            for gf in geo_files_list[:1]:
                print(f'Examining: {gf}')
                data = z.read(gf)
                print(f'Size: {len(data)} bytes')
                print(f'First 200 bytes: {data[:200]}')
    except Exception as e:
        print(f'Error: {e}')
PYEOF