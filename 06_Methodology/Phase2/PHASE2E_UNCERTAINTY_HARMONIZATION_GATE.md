# Phase 2E — Statistical Harmonization and Uncertainty Decision

**Review date:** November 21, 2026  
**Workspace:** `I:\Territorial-Representation-Research`

## GO / CONDITIONAL / NO-GO by use

| Source / domain | Education | Civilian unemployment | Median household income | Poverty |
|---|---|---|---|---|
| 2020 Island Areas 4-way, source-specific description | GO with universe footnotes | GO with universe footnotes | GO as 2019 income, household scope labeled | GO if poverty-status universe, formula, and group-quarters exclusions labeled |
| 2019 D.C. and Puerto Rico ACS/PRCS 1-year, source-specific description | GO for point estimates; rate MOE pending | GO for point estimates; rate MOE pending | GO for estimate and published 90% MOE | GO for point estimates; rate MOE pending |
| 2016–2020 D.C. and Puerto Rico ACS/PRCS 5-year, source-specific description | GO for point estimates; rate MOE pending | GO for point estimates; rate MOE pending | GO for estimate and published 90% MOE | GO for point estimates; rate MOE pending |
| All six jurisdictions in a single side-by-side research display | CONDITIONAL; conspicuous universe/method labels | CONDITIONAL; no claims of comparable unemployment sampling or populations | CONDITIONAL; income units/reference years vary | CONDITIONAL; poverty populations/reference years differ |
| Statistical rankings, pairwise significance tests or six-way SPSS comparisons | NO-GO | NO-GO | NO-GO | NO-GO |

**GO means evidence-backed, source-specific reporting only**, not permission to pool three different sources or to run an omnibus statistical test.

## Survey margins of error and interval conventions

For a published survey estimate `E` with a published ACS/PRCS margin of error `MOE90`, the ordinary display interval is `E ± MOE90` at the published 90% confidence level, without treating the endpoints as physical bounds on unbounded estimates. This convention is appropriate for the directly published `B19013_001` median-household-income estimate and its corresponding published `m` Summary File figure. No new distributional assumptions are added.

Education share (sum of B15003 bachelor's/master's/professional/doctorate counts divided by population 25+), unemployment share (B23025 unemployed divided by civilian labor force), and poverty share (B17001 below-poverty divided by poverty-universe total) were **derived** from Detailed Tables. They do **not** inherit the published numerator MOE, the denominator MOE, or an arithmetic sum of component MOEs. Margins for these derived ratios have **not yet been calculated**. The 80 original underlying estimate/MOE components are archived, but their presence alone does not establish an uncertainty interval for each derived rate.

A defensible future interval analysis must use the Census Bureau's official ACS methodology for sums and proportions/ratios, selecting the correct numerator–denominator relationship and handling covariance or replicate estimates where applicable. The distinction is particularly important for ratios whose numerators are subsets of their denominators. Any ratio-MOE calculation must be reconciled to the corresponding published ACS/PRCS data profile, when available, and then independently validated before publication. Do not imply a 95% confidence interval by calling a 90% ACS MOE a 95% MOE.

## Other uncertainty and comparability restrictions

1. **Island Areas tabulations:** Do not attach an ACS sample-based confidence interval to 2020 Island Areas Census socioeconomic profile values. Their measurement limitations and household/military exclusions still must be disclosed.
2. **Time:** Four Island Areas observations are 2020 Census socioeconomic profiles with income/poverty referring to calendar 2019. The D.C./PR 2019 ACS/PRCS one-year and pooled 2016–2020 five-year sample estimates are distinct programs and time windows; 2016–2020 median income uses 2020 dollars.
3. **Population universes:** Education generally concerns age 25+, unemployment civilian labor force, income households, poverty persons whose poverty status was determined. Island Area household-only universes and Guam military housing exclusions prevent assumptions of identical coverage.
4. **Missing and suppressed data:** retain explicit source codes and explanations; do not convert missing/suppressed observations or unpublished margins into zero.
5. **Jurisdiction scope:** D.C. is a federal district, not one of the five inhabited U.S. territories; the four Island Areas profiled here exclude Puerto Rico (which is separately covered through PRCS).
6. **Political interpretation:** Aggregate socioeconomic measures do not indicate political preferences, self-determination choices, voting eligibility, or citizenship.

## Source evidence and formal gate

- `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md` lists all 32 source-specific observations and the published income MOEs/90% intervals.
- `06_Methodology/Phase2/PHASE2D_NUMERIC_ACQUISITION_ACCEPTANCE.md` documents original Census technical layouts and source table positions.
- `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` records 17 official acquisitions and checksums.
- `02_SPSS_Data/Phase2/prdc_2019_acs_one_year_raw_components_with_moe.csv` and `prdc_2020_acs_five_year_raw_components_with_moe.csv` preserve original survey components.
- `06_Methodology/Phase2/validate_phase2d_numeric_acquisition.py` validates numerical extraction.

**Research status:** Numerical acquisition GO; descriptive source-family evidence GO; six-jurisdiction unified statistical comparison NO-GO; derived rate MOE calculations OPEN; age-and-sex SAV byte-hash provenance OPEN.
