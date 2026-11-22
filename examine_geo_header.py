import zipfile

# Examine the geo header file structure
zip_path = r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip'

with zipfile.ZipFile(zip_path) as z:
    # Get the geo header file
    geo_files = [f for f in z.namelist() if 'geo' in f.lower()]
    print('Geo files:', geo_files)
    
    if geo_files:
        geo_data = z.read(geo_files[0]).decode('utf-8')
        print('\nFull geo data:')
        print(geo_data)
        
        # Split by newlines and print first few records
        lines = geo_data.strip().split('\n')
        print('\nFirst 5 lines:')
        for line in lines[:5]:
            print(f'  {line}')
            fields = line.split('|')
            print(f'  Fields ({len(fields)}): {fields[:10]}')
PYEOF