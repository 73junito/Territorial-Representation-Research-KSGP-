# Phase 2D — Socioeconomic Numerical Acquisition Decision
Date: November 21, 2026
Decision: **GO for verified source-specific descriptive observations; NO-GO for unqualified six-jurisdiction socioeconomic statistical comparison.**

## Acquired numerical evidence
The official four Island Areas Census Demographic Profile ZIPs, the published technical documentation and four table matrices were used to extract 16 records (education, unemployment, median household income, poverty). Poverty was calculated using the published poverty-status universe, not total population.

D.C. and Puerto Rico have eight actual 2019 one-year ACS/PRCS Detailed Table observations and eight actual 2016–2020 five-year ACS/PRCS observations. These came from Census official Summary File bulk downloads, avoiding the blocked data API, and use the Census-published source-specific sequence templates. Both periods separately preserve 20 estimate and 20 MOE components. A directly published MOE is provided for median household income; ratio-derived rates need a properly derived MOE and must not inherit a component MOE.

## Important restrictions
- Island Areas socioeconomic data stem from the 2020 Census with 2019 income and poverty reference year.
- D.C./Puerto Rico observations are survey estimates for 2019 one-year or pooled 2016–2020 five-year, not equivalent to the Island Areas decennial product.
- Guam's population exclusions and different denominator universes remain material.
- Never interpret this source-specific collection as a harmonized six-jurisdiction comparative dataset. Do not calculate inter-jurisdiction significance tests, ordinal rankings, or infer policy preferences from differences.

## Validation and source evidence
- `06_Methodology/Phase2/PHASE2D_NUMERIC_ACQUISITION_ACCEPTANCE.md` — method, observations, validation details, caveats.
- `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` — 17 newly acquired original government resources and checksums.
- `06_Methodology/Phase2/validate_phase2d_numeric_acquisition.py` — PASS (32 source-specific observations and 80 ACS/PRCS components).
- `02_SPSS_Data/Phase2/island_areas_2020_socioeconomic_source_specific.csv`
- `02_SPSS_Data/Phase2/prdc_2019_acs_one_year_detailed_source_specific.csv`
- `02_SPSS_Data/Phase2/prdc_2020_acs_five_year_detailed_source_specific.csv`
- Two corresponding `prdc_*_raw_components_with_moe.csv` files.

## Preservation exception
The validated age-and-sex .sav has a different SHA-256 hash from the previous audit. The six records and every CSV column still reconcile when sorted by jurisdiction, indicating a file-level representation/order change; exact provenance remains open. No SAV, original Census ZIP, or existing SPSS .spv was written during this acquisition work.

## Next priority — Phase 2E
Review the published domain-specific universe notes and exclusions, determine appropriate ratio MOE calculations, assess whether academically defensible limited side-by-side reporting is possible, and package a nonpartisan source-specific evidence appendix. Keep the six-way inferential-analysis gate NO-GO until explicit methodological acceptance.
