import json

# Load the ACS variable metadata
with open(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2020_5YR_variables.json', 'r') as f:
    acs20 = json.load(f)

with open(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census\ACS_2019_1YR_variables.json', 'r') as f:
    acs19 = json.load(f)

# Target variables from the Phase 2B instructions
vars_target = ['education', 'unemployment', 'median_income', 'poverty']

# Mappings from existing review
var_map = {
    'education': 'DP2_0016P (Island Areas) / DP2_0068PE (ACS)',
    'unemployment': 'DP3_0009C (Island Areas) / DP3_0009PE (ACS)',
    'median_income': 'DP3_0104C (Island Areas) / DP3_0062E (ACS)',
    'poverty': 'DP3_0151P (Island Areas) / DP3_0128PE (ACS)',
}

print('=== SOCIOECONOMIC VARIABLE DEFINITIONS ===')
print()

for var in vars_target:
    print(f'--- {var.upper()} ---')
    print(f'Census field: {var_map[var]}')
    
    # Check ACS 2020 5-year
    # Extract the ACS variable name from the mapping
    usvar_20 = var_map[var].split('/')[-1].strip()
    if usvar_20 in acs20:
        v20 = acs20[usvar_20]
        label20 = v20.get('label', 'N/A')[:200]
        concept20 = v20.get('concept', 'N/A')[:200]
        pred20 = v20.get('predicateType', 'N/A')
        attrs20 = v20.get('attributes', 'N/A')
        print(f'ACS 2020 5YR:')
        print(f'  Variable: {usvar_20}')
        print(f'  Label: {label20}')
        print(f'  Concept: {concept20}')
        print(f'  Type: {pred20}')
        print(f'  Attributes: {attrs20}')
    else:
        print(f'ACS 2020 5YR: {usvar_20} NOT FOUND')
    
    # Check ACS 2019 1-year for relevant variables
    # DP3_0062E exists in both, DP3_0128PE exists in both, etc.
    for check_var in ['DP3_0062E', 'DP3_0128PE', 'DP2_0068PE', 'DP3_0009PE']:
        if check_var in acs20:
            v = acs20[check_var]
            label_prefix = v.get('label', '')[:60]
            print(f'  ACS 2020 5YR {check_var}: label starts with {label_prefix}...')
        if check_var in acs19:
            v = acs19[check_var]
            label_prefix = v.get('label', '')[:60]
            print(f'  ACS 2019 1YR {check_var}: label starts with {label_prefix}...')

print()
print('=== KEY OBSERVATIONS ===')
print('1. Island Areas DP2/DP3 fields use decennial census universe definitions')
print('2. ACS/PRCS five-year estimates use sample-based period estimates')
print('3. Income/poverty reference periods differ: 2019 nominal vs inflation-adjusted')
print('4. 2020 ACS one-year estimates were NOT released (COVID-19)')
print('5. Island Areas universes differ: household-only vs total resident population')
print('6. Guam education/employment explicitly excludes military housing')
print('7. Puerto Rico and D.C. use ACS sample-based estimates, not decennial equivalents')