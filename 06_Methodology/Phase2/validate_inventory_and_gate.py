from pathlib import Path
import json,csv,hashlib,zipfile
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'
cen=base/'Census'
with (base/'source_inventory_phase2.csv').open(encoding='utf-8-sig',newline='') as f: inv=list(csv.DictReader(f))
assert len(inv)==4 and all(x['status']=='VERIFIED_ZIP' for x in inv)
for e in inv:
 p=root/e['local_file']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256']
 with zipfile.ZipFile(p) as z:assert len(z.namelist())==5 and z.testzip() is None
codes=['US_DP','GU_DP','AS_DP','MP_DP','VI_DP']
metadata={name:json.loads((cen/(name+'_variables.json')).read_text(encoding='utf-8'))['variables'] for name in codes}
topics={
'Population, age and sex':'DP1',
'Household and housing characteristics':'DP1',
'Education attainment':'DP2',
'Labor force and employment':'DP3',
'Household income (2019)':'DP3',
'Poverty (income in 2019)':'DP3',
}
rows=[]
for topic,group in topics.items():
 for code,meta in metadata.items():
  matches=[k for k in meta if k.startswith(group+'_')]
  status='VARIABLE_FAMILY_PRESENT' if matches else 'NOT_IN_THIS_2020_PRODUCT'
  note=('2020 decennial DP1 only (no socioeconomic DP2/DP3); use ACS/PRCS separately for income/employment/education.' if code=='US_DP' and group!='DP1'
  else '2020 Island Areas DP; individual universes differ, especially group quarters and military housing. Verify variable labels and denominators.' if code!='US_DP'
  else '2020 decennial DP1 age/housing categories require variable-level harmonization.')
  rows.append(dict(topic=topic,source=code,variable_family=group,metadata_variables=len(matches),status=status,comparison_gate=('PRELIMINARY_ONLY' if group=='DP1' else 'NOT_COMPARABLE_AS_IS'),notes=note))
with (base/'variable_comparability_inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
report='''# Phase 2 — 2020 demographic profile source inventory and comparability gate
Date: 2026-11-21

## Downloads and integrity
Four original Census Bureau Island Areas demographic profile ZIP archives were downloaded and checked (AS, GU, MP, VI). See source_inventory_phase2.csv for government URLs, byte counts, SHA-256 checksums, and ZIP entries. No archive was extracted or modified. All four pass ZIP CRC integrity checks.

## Census API variable dictionaries
2020/dec/dpas, dpgu, dpmp, dpvi and the standard 2020/dec/dp variable dictionaries were retrieved as original JSON files. They are source metadata only, not population measurement downloads. Both Puerto Rico (state FIPS 72) and District of Columbia (state FIPS 11) are covered by standard U.S. decennial geographic programs, rather than the Island Areas 2020 DP2 and DP3 products.

## Comparable domains — initial gate
- Age, sex and selected housing indicators: 2020 DP1 available for the island areas and standard decennial 2020 DP1 for PR/DC, but population universe, definitions, and variable labels must still be checked before combining.
- Education, employment, 2019 income and poverty: island-area 2020 DP2/DP3 variables exist; these are NOT in standard 2020 decennial DP1 for PR/DC. Puerto Rico Community Survey and American Community Survey are different survey programs and reference periods. Direct six-jurisdiction comparisons are therefore NOT cleared.
- Differences within Island Areas: some income/employment/education universes exclude persons in military housing or group quarters depending on table and location. Cross-area percent comparisons require denominator inspection.
- Raw ZIPs contain Census profile flat files (.dp), not SPSS .sav files. Extraction, column positions and geography records require Census technical documentation.

## Stage result
SOURCE_ACQUISITION: COMPLETE FOR FOUR ISLAND AREAS.
API_METADATA_DISCOVERY: COMPLETE FOR 2020 DP PRODUCTS.
SIX_JURISDICTION_SOCIOECONOMIC_COMPARABILITY: NOT CLEARED.
SPSS_SOCIOECONOMIC_ANALYSIS: NOT STARTED.
For any publication, obtain matching source definitions and harmonized time frames; do not fill absent values with zero.

## Next recommended decision
Choose a 2020 Census demographic DP1-only pilot (age and sex), obtaining PR/DC census records via official API and parsing island-area DP using the official layout. Treat income/employment comparisons as a separate methods review.
'''
(root/'06_Methodology'/'Phase2'/'SOURCE_COMPARABILITY_GATE.md').write_text(report,encoding='utf-8')
print('ZIP_ARCHIVES_VALIDATED',len(inv))
print('METADATA_FILES_VALIDATED',len(metadata))
print('TOPIC_SOURCE_MATRIX_ROWS',len(rows))
print('COMPARABILITY_NOT_CLEARED_SOCIOECONOMIC')
