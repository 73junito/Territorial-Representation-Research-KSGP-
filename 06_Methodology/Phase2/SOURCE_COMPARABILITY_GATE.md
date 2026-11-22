# Phase 2 — 2020 demographic profile source inventory and comparability gate
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

## Puerto Rico / D.C. access limitation
The standard 2020 Census DP variable dictionary was downloaded, but a live 2020 Census API query for state codes 11 and 72 returned an HTML 'Missing Key' page rather than JSON records. Thus Puerto Rico and D.C. 2020 DP observations are NOT archived or directly verified in this phase. Access to those actual data rows must be resolved separately; the presence of variable metadata alone does not demonstrate a comparable six-jurisdiction series.

## Stage result
SOURCE_ACQUISITION: COMPLETE FOR FOUR ISLAND AREAS.
API_METADATA_DISCOVERY: COMPLETE FOR 2020 DP PRODUCTS.
SIX_JURISDICTION_SOCIOECONOMIC_COMPARABILITY: NOT CLEARED.
SPSS_SOCIOECONOMIC_ANALYSIS: NOT STARTED.
For any publication, obtain matching source definitions and harmonized time frames; do not fill absent values with zero.

## Next recommended decision
Choose a 2020 Census demographic DP1-only pilot (age and sex), obtaining PR/DC census records via official API and parsing island-area DP using the official layout. Treat income/employment comparisons as a separate methods review.
