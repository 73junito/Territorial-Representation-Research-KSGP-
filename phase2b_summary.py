import csv
import json

# Read existing variable definitions from the matrix
with open(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\socioeconomic_comparability_matrix.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Summarize the key findings by domain
print('=== PHASE 2B: SOCIOECONOMIC HARMONIZATION SUMMARY ===')
print()

# Group by domain
domains = ['education', 'unemployment', 'median_income', 'poverty']
for domain in domains:
    print(f'\n--- {domain.upper()} ---')
    domain_rows = [r for r in rows if r['topic'] == domain]
    for r in domain_rows:
        print(f'  {r["geo_code"]} {r["jurisdiction"]}: cross_six_gate={r["cross_six_gate"]}, reason={r["reason"][:80]}...')

print('\n=== KEY FINDINGS ===')
print('1. ALL Island Areas domains: NO-GO for cross-six SPSS comparison')
print('2. Reasons vary by domain but center on:')
print('   - Decennial census vs ACS/PRCS survey methodology differences')
print('   - Island Areas household-only vs total resident population universes')
print('   - Guam military housing exclusions')
print('   - 2019 nominal income vs 2020 inflation-adjusted income')
print('   - 2020 ACS one-year estimates NOT released (COVID-19)')
print('   - PR/DC use ACS sample-based estimates, not decennial equivalents')
print('3. SOURCE-INVENTORY: PASS (4 archived ZIPs + 2 ACS metadata JSONs)')
print('4. METADATA FIELD IDENTIFICATION: PASS (24 row-variables)')
print('5. COMPARABILITY FOR SIX-WAY SPSS: NO-GO')
print('6. PR/DC NUMERICAL DATA ACQUISITION: NOT COMPLETE')
print('7. ISLAND AREAS DP2/DP3 EXTRACTION: NOT STARTED (field positions require technical layout)')
PYEOF