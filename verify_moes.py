import csv
import math

# Read the derived MOE CSV
with open(r'I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\phase2f_prdc_derived_rate_moe90.csv', 'r') as f:
    rows = list(csv.DictReader(f))

print('=== Phase 2G: Verify 12 Calculated Percentage MOEs ===')
print()

for row in rows:
    jurisdiction = row['jurisdiction']
    period = row['source_period']
    domain = row['domain']
    derived_moe = float(row['moe90_percentage_points'])
    
    print(f'\n--- {jurisdiction} {period} {domain} ---')
    print(f'  Derived MOE: {derived_moe}%')
    print(f'  Formula: {row["formula"]}')
    print(f'  CI bounds: [{float(row["ci90_lower_pct"])}, {float(row["ci90_upper_pct"])}]')
    print(f'  Estimate: {float(row["estimate_pct"])}%')
    
    # Verify: CI = estimate +/- MOE (approximately)
    lower_check = round(float(row['estimate_pct']) - derived_moe, 4)
    upper_check = round(float(row['estimate_pct']) + derived_moe, 4)
    print(f'  Lower bound check: {lower_check} (actual: {float(row["ci90_lower_pct"])})')
    print(f'  Upper bound check: {upper_check} (actual: {float(row["ci90_upper_pct"])})')

print('\\n=== Verification Complete ===')