# Phase 1 SPSS Output Audit
Date: 2026-11-21

## Status
PASS — Census counts and percentage changes validated. SPSS ran the LIST and DESCRIPTIVES procedures. No statistical inference performed.

## SPSS save warning
The SPSS Output Viewer records Warning #67 (GET FILE: the intended .sav was already in use) and Warning #5334 (SAVE succeeded under a different filename). It saved a second file named population_2010_2021.sav. Both .sav files contain the identical six rows and columns. No evidence of a 2021 dataset. Both have been retained unchanged.

## Reconciliation
- 2010 population: 4,702,677
- 2020 population: 4,313,440
- Absolute change: -389,237
- Percent change, combined denominator: -8.28%
- Population denominators are total residents, not eligible voters.
- No effect sizes/p-values are appropriate for this jurisdiction-level census summary.

## SHA256 integrity record
- `population_2010_2020.sav`: `0343c9f175af51cc7f3491be13ed2d6cfc491fdce5070de3d7bdac9bc327af7c`
- `population_2010_2021.sav`: `8860978130d1d881c41a5cac2d1feff58146f301cef4c8ea60a750849305a1ac`
- `01_population_comparison.spv`: `5c9f6aa0449e3baf5a4238f1ac51fa93bae2007fe8a1d403f37a9cb2da19c951`
- `population_2010_2020_source.csv`: `33f44b3b7f4fcfee30a0e0d83111445cd6add5b9212edb0321c0c31b56c38d79`

## Data provenance and limitations
Population counts derived from Census Bureau 2010 and 2020 Census releases, transcribed into a six-row CSV; the government originals are not yet locally archived.
Official primary sources: Census QuickFacts for PR and DC, and the 2020 Island Areas Censuses press releases for GU, VI, AS and MP. Refer to source_register.csv.
More detailed housing/income/education data will require comparison of census universes and source definitions before aggregation.
Detailed Guam social/economic tables exclude military installation populations in some universes. American Samoa social/economic tables may exclude group quarters due to census collection limitations.
## Outstanding follow-up
1. Review whether the alternate .sav was opened or created in an SPSS session; do not delete while files may be locked.
2. For future reruns, use a separate validated-results filename or skip saving the input file.
3. Gather original agency table downloads and check detailed data universes before Phase 2.
