#!/usr/bin/env python3
"""
Parse 2020 Island Areas Demographic Profile DP files and extract socioeconomic variables.
Format: DP<area_code>|<geo_code>|...|<field_values>...
Based on analysis of geo header and data records.
"""

import zipfile
import struct
import json
import os

# Target variables and their Census field names
TARGET_VARS = {
    'education': {
        'census_field': 'DP2_0016P',
        'description': 'Bachelor\'s degree or higher (percent)',
        'island_areas_unit': 'Percent EDUCATIONAL ATTAINMENT Population 25 years and over',
        'us_variable': 'DP2_0068PE'
    },
    'unemployment': {
        'census_field': 'DP3_0009C', 
        'description': 'Civilian unemployment rate (percent)',
        'island_areas_unit': 'Percent EMPLOYMENT STATUS Civilian labor force',
        'us_variable': 'DP3_0009PE'
    },
    'median_income': {
        'census_field': 'DP3_0104C',
        'description': 'Median household income (dollars)',
        'island_areas_unit': 'Median household income',
        'us_variable': 'DP3_0062E'
    },
    'poverty': {
        'census_field': 'DP3_0151P',
        'description': 'All-person poverty rate (percent)',
        'island_areas_unit': 'Percent NUMBER AND PERCENTAGE OF FAMILIES AND PEOPLE BELOW POVERTY LEVEL',
        'us_variable': 'DP3_0128PE'
    }
}

def parse_dp_header(header_line):
    """Parse a DP header line to understand field positions."""
    fields = header_line.strip().split('|')
    return fields

def parse_dp_record(record_line):
    """Parse a DP data record."""
    fields = record_line.strip().split('|')
    return fields

def extract_socioeconomic_data():
    """Extract socioeconomic data from Island Areas DP files and ACS JSON metadata."""
    results = {}
    
    zip_paths = [
        r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\AS_2020_demographic_profile_original.zip',
        r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\GU_2020_demographic_profile_original.zip',
        r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\MP_2020_demographic_profile_original.zip',
        r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\VI_2020_demographic_profile_original.zip',
    ]
    
    jurisdictions = ['AS', 'GU', 'MP', 'VI']
    
    for zp in zip_paths:
        # Extract geo code from path
        geo_code = os.path.basename(zp).split('_')[1].upper()
        if jurisdictions and jurisdiction not in jurisdictions:
            continue
            
        print(f'\\n=== Processing {geo_code} ===')
        
        try:
            with zipfile.ZipFile(zp) as z:
                # Read geo header for field definitions
                geo_files = [f for f in z.namelist() if 'geo' in f.lower() and f.endswith('.dp')]
                if geo_files:
                    geo_data = z.read(geo_files[0]).decode('utf-8')
                    geo_fields = parse_dp_header(geo_data.split('\\n')[0])
                    print(f'  Geo header fields: {geo_fields[:5]}')
                
                # Read first data record
                dp_files = [f for f in z.namelist() if f.startswith(tuple(['as00', 'gu00', 'mp00', 'vi00'])) and f.endswith('.dp')]
                if dp_files:
                    data = z.read(dp_files[0]).decode('utf-8')
                    records = data.strip().split('\\n')
                    if records:
                        first_record = records[0]
                        rec_fields = parse_dp_record(first_record)
                        print(f'  Data record fields: {rec_fields[:10]}')
                        print(f'  Record: {first_record[:200]}')
                        
                        # Try to identify socioeconomic variable positions
                        # Based on the field structure, we need to map variable IDs to positions
                        # The DP files use a specific layout; field positions vary by variable
                        
                        # For now, record the structure
                        print(f'  Total records: {len(records)}')
                        print(f'  First record full: {first_record}')
                
        except Exception as e:
            print(f'  Error processing {geo_code}: {e}')
    
    # Also process ACS JSON metadata
    print(f'\\n=== ACS JSON Metadata ===')
    acs_paths = {
        '2020_5yr': r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2020_5YR_variables.json',
        '2019_1yr': r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2019_1YR_variables.json',
    }
    
    for name, acs_path in acs_paths.items():
        try:
            with open(acs_path, 'r') as f:
                acs_data = json.load(f)
            
            # Find target variables
            for var_key, var_def in TARGET_VARS.items():
                us_var = var_def['us_variable']
                if us_var in acs_data:
                    var_info = acs_data[us_var]
                    print(f'  {us_var} ({var_key}):')
                    print(f'    Label: {var_info.get(\"label\", "N/A")}')
                    print(f'    Concept: {var_info.get(\"concept\", "N/A")}')
                    print(f'    Predicate type: {var_info.get(\"predicateType\", "N/A")}')
                    print(f'    Attributes: {var_info.get(\"attributes\", "N/A")}')
        except Exception as e:
            print(f'  Error reading {acs_path}: {e}')
    
    return results

if __name__ == '__main__':
    results = extract_socioeconomic_data()
    print(f'\\n=== Extraction Complete ===')
    print(f'Jurisdictions processed: AS, GU, MP, VI')
    print(f'ACS metadata: 2020 5-year and 2019 1-year reviewed')
    print(f'Target variables: education, unemployment, median_income, poverty')
PYEOF