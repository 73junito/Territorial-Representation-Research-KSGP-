# Phase 2 SPSS execution and acceptance status
Date: 2026-11-21

## Source dataset
Six-jurisdiction 2020 Census age-and-sex data in 02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.sav and matching CSV.

## Actual IBM SPSS Statistics execution
The user completed the interactive IBM SPSS Statistics run via 03_SPSS_Syntax/Phase2/02_age_sex_2020_run_and_save.sps. The output is present at 04_SPSS_Output/Phase2/01_age_sex_2020_descriptive.spv (6,579 bytes).

## Verified outcomes
- PASS: SPV exists and ZIP integrity test passes.
- PASS: SPV contains List and Descriptives sections, with the Descriptive Statistics table present.
- PASS: Six List rows contain source-matching population, male, female, under-20, age 20–64, and age 65+ counts.
- PASS: SPSS lists six cases read and six cases listed.
- PASS: No numbered SPSS command warnings/errors were detected in the exposed LIST text.
- PASS: Original .sav remains readable.
- LIMITATION: Proprietary binary Descriptives pivot-table cell values were not fully decoded. Full cell-by-cell signoff requires GUI inspection of the pivot table.

## Aggregate values from validated source dataset
Population: 4,313,440
Male: 2,047,330
Female: 2,266,110
Under 20: 880,002
Age 20-64: 2,573,093
Age 65+: 860,345

## Audit artifacts
06_Methodology/Phase2/verify_spv_output.py
06_Methodology/Phase2/SPSS_VIEWER_ACCEPTANCE.md

## Decision
Phase 2 demographic age-and-sex pilot: DATA VALIDATION PASS.
IBM SPSS output generation and LIST reconciliation: PASS.
SPSS proprietary Descriptives pivot cell-by-cell inspection: PENDING.
Broader socioeconomic data harmonization: NOT YET CLEARED.

## Previous execution blocker
The separate SPSS Python integration was blocked by Windows Application Control. The interactive SPSS run succeeded; no Windows security settings were altered.
