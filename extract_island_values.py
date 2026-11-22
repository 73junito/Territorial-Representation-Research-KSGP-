import zipfile
import struct

# Extract socioeconomic values from Island Areas DP files
# Based on analysis of geo header and data records

def extract_from_dp_file(zp, target_vars=None):
    """Extract values from a single DP file.
    
    DP file format: pipe-delimited records
    First record appears to be summary/aggregation
    """
    results = {}
    
    with zipfile.ZipFile(zp) as z:
        # Get the main data file (first non-geo DP file)
        dp_files = [f for f in z.namelist() if f.startswith(('as00', 'gu00', 'mp00', 'vi00')) 
                    and f.endswith('.dp') and not 'geo' in f.lower()]
        
        if not dp_files:
            print(f'  No DP data files found in {zp}')
            return results
        
        # Get the first data record (summary record)
        data_file = dp_files[0]
        data = z.read(data_file).decode('utf-8')
        records = data.strip().split('\\n')
        
        if not records:
            print(f'  No records in {data_file}')
            return results
        
        # First record is the summary
        first_record = records[0]
        rec_fields = first_record.split('|')
        print(f'  {data_file}: {len(rec_fields)} fields')
        print(f'  First record: {first_record[:200]}')
        
        # Also get the geo header for field reference
        geo_files = [f for f in z.namelist() if 'geo' in f.lower() and f.endswith('.dp')]
        if geo_files:
            geo_data = z.read(geo_files[0]).decode('utf-8')
            geo_lines = geo_data.strip().split('\\n')
            if geo_lines:
                geo_fields = geo_lines[0].split('|')
                print(f'  Geo header: {len(geo_fields)} fields')
                print(f'  Geo header first record: {geo_fields[:15]}...')
        
        # Try to map known variable positions
        # From analysis, position 6 (index 5) often corresponds to total population
        # Other positions vary by variable
        if len(rec_fields) > 6:
            try:
                pop_value = rec_fields[5]  # Position 6 (0-indexed 5)
                print(f'  Position 6 (likely population): {pop_value}')
            except:
                pass
        
        # Record available fields for each target variable
        for var_key in (target_vars or []):
            if var_key == 'education':
                # DP2_0016P: Bachelor's degree or higher (percent)
                # In Island Areas DP files, education data is at specific positions
                # that require technical layout validation
                results[var_key] = {
                    'census_field': 'DP2_0016P',
                    'raw_value': rec_fields[6] if len(rec_fields) > 6 else 'N/A',
                    'extraction_note': 'Field position requires technical-layout validation of DP file format'
                }
            elif var_key == 'unemployment':
                results[var_key] = {
                    'census_field': 'DP3_0009C',
                    'raw_value': rec_fields[6] if len(rec_fields) > 6 else 'N/A',
                    'extraction_note': 'Field position requires technical-layout validation of DP file format'
                }
            elif var_key == 'median_income':
                results[var_key] = {
                    'census_field': 'DP3_0104C',
                    'raw_value': rec_fields[6] if len(rec_fields) > 6 else 'N/A',
                    'extraction_note': 'Field position requires technical-layout validation of DP file format'
                }
            elif var_key == 'poverty':
                results[var_key] = {
                    'census_field': 'DP3_0151P',
                    'raw_value': rec_fields[6] if len(rec_fields) > 6 else 'N/A',
                    'extraction_note': 'Field position requires technical-layout validation of DP file format'
                }
    
    return results


# Extract from all four Island Areas ZIPs
zip_paths = [
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\GU_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\MP_2020_demographic_profile_original.zip',
    r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\VI_2020_demographic_profile_original.zip',
]

target_vars = ['education', 'unemployment', 'median_income', 'poverty']

print('=== TRR-PHASE2C: Island Areas DP File Value Extraction ===')
print()

all_results = {}
for zp in zip_paths:
    # Extract geo code from filename
    basename = zp.split('\\\\')[-1]
    geo_code = basename.split('_')[1].upper() if '_' in basename else basename.split('.')[0].upper()
    
    print(f'\\n=== Processing {geo_code} ===')
    results = extract_from_dp_file(zp, target_vars)
    all_results[geo_code] = results
    
    print(f'\\nExtracted results for {geo_code}:')
    for var, var_data in results.items():
        print(f'  {var}: census_field={var_data["census_field"]}, raw_value={var_data["raw_value"]}, note={var_data["extraction_note"]}')

print('\\n=== Extraction Complete ===')
print('Key findings:')
print('1. DP file format requires technical-layout validation (Census documentation)')
print('2. Raw values extracted at position 6 (index 5) but meaning not yet verified')
print('3. All four target variables documented with census field IDs')
print('4. Extraction notes indicate need for technical layout validation')
print('5. ACS 2016-2020 five-year numeric observations for PR/DC: NOT_ARCHIVED')
print('6. 2019 ACS one-year observations: PENDING (requires API pull)')
PYEOF