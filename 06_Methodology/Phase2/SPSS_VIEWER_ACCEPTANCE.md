# Phase 2 — SPSS Viewer Acceptance

Date: 2026-11-21

## Verified outcome
- PASS: SPSS-produced output file exists and is a valid ZIP-based .spv Viewer document.
- PASS: The SPSS Viewer includes LIST for all six jurisdictions and a Descriptives section with a Descriptive Statistics pivot table.
- PASS: All six LIST population, sex, and harmonized age group counts match the canonical .sav data.
- PASS: SPSS LIST states six cases were read and listed.
- PASS: No numbered command warnings or errors were found in exposed LIST text.
- PASS: Source .sav remains readable; no input dataset rewrite was required.
- CONDITIONAL: The proprietary binary Descriptives pivot payload is confirmed to exist with Sum/Mean metadata but individual binary table cell values were not directly decoded. Source-derived aggregates are independently recalculated below; inspect these against the GUI pivot table for full cell-level signoff.

## Source-derived reconciliation values
- population_sum: 4,313,440
- male_sum: 2,047,330
- female_sum: 2,266,110
- under20_sum: 880,002
- age20to64_sum: 2,573,093
- age65plus_sum: 860,345

## Files
- SPV: 04_SPSS_Output\Phase2\01_age_sex_2020_descriptive.spv
- SPV size: 6,579 bytes
- SPV SHA256: 9555832675dd2b05ce1d975cfa300ff724901a4448751aaa194c55b4fad9a7b1
- SAV SHA256: 300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8

## Decision
Phase 2 age-sex pilot output-generation gate: PASS.
SPSS LIST vs Census data reconciliation: PASS.
SPSS proprietary Descriptives pivot cell-by-cell verification: NOT FULLY VERIFIED (binary table payload).
Socioeconomic income, poverty, employment, and education comparability gate remains separate and NOT CLEARED.
