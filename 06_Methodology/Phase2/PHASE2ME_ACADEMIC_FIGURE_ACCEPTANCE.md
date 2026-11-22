# TRR Phase 2M-E — Source-Specific Academic Figure Catalog and Acceptance

**Date:** November 21, 2026
**Status:** INTERNAL FIGURE EVIDENCE QA PASS; EXTERNAL FACULTY REVIEW PENDING; FINAL PUBLICATION NO-GO.

## Figure production

Fourteen manuscript-supporting figures were generated from the preserved source-specific demographic and socioeconomic CSV records by `06_Methodology/Phase2/build_phase2me_source_specific_figures.py` using matplotlib. For each figure there are separate **PNG and SVG** exports. A `FIGURE_INDEX.csv` supplies title, exact source family, reference period, observations, interpretation limits, the original plotted values and SHA-256 for both exports.

### Figures 1–2: Decennial population and age composition

- [Figure 01 — 2020 jurisdiction population (logarithmic horizontal scale)](../../05_Statistical_Graphics/Phase2ME/01_2020_population_logscale.png). All six jurisdiction counts are labeled. Log scale is explicit because Puerto Rico's population is far larger than the other five; D.C. is labeled as a **federal district**.
- [Figure 02 — 2020 age composition](../../05_Statistical_Graphics/Phase2ME/02_2020_age_structure.png). All six jurisdiction populations partitioned into under-20, ages 20–64 and 65+ groups, summing to 100% within jurisdiction.

### Figures 3–6: Four Island Areas Census Demographic Profiles

- [Figure 03a — Bachelor's degree or higher](../../05_Statistical_Graphics/Phase2ME/03_island_areas_education.png).
- [Figure 03b — Civilian unemployment](../../05_Statistical_Graphics/Phase2ME/03_island_areas_unemployment.png).
- [Figure 03c — Poverty in 2019](../../05_Statistical_Graphics/Phase2ME/03_island_areas_poverty.png).
- [Figure 03d — Median household income in 2019 dollars](../../05_Statistical_Graphics/Phase2ME/03_island_areas_median_household_income.png).

**Source:** American Samoa, Guam, Northern Mariana Islands and U.S. Virgin Islands 2020 Island Areas Census long-form profiles. These are **not ACS observations**. No ACS-style 90% sampling error bars appear. Income and poverty refer to 2019; Guam military-housing/coverage exception and differing poverty universes remain material.

### Figures 7–10: 2019 one-year ACS/PRCS

- [Figure 04a — Educational attainment, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/04_2019_1yr_education.png).
- [Figure 04b — Civilian unemployment, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/04_2019_1yr_unemployment.png).
- [Figure 04c — Poverty, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/04_2019_1yr_poverty.png).
- [Figure 04d — Household median income in 2019 dollars, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/04_2019_1yr_median_household_income.png).

**Source:** D.C. and Puerto Rico 2019 ACS/PRCS one-year Detailed Tables; the first three profile-rate MOEs are directly published Census Data Profile values in Phase 2I, while income MOEs are directly published in original B19013 tables. No cross-product comparisons or significance interpretations.

### Figures 11–14: 2016–2020 five-year ACS/PRCS

- [Figure 05a — Educational attainment, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/05_2016_2020_5yr_education.png).
- [Figure 05b — Civilian unemployment, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/05_2016_2020_5yr_unemployment.png).
- [Figure 05c — Poverty, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/05_2016_2020_5yr_poverty.png).
- [Figure 05d — Household median income in 2020 inflation-adjusted dollars, published 90% MOEs](../../05_Statistical_Graphics/Phase2ME/05_2016_2020_5yr_median_household_income.png).

**Source:** D.C. and Puerto Rico pooled 2016–2020 ACS/PRCS five-year Detailed Tables and published profile MOEs. The data cannot be equated with a separate 2020 one-year observation or compared directly with a 2019-dollar income chart.

## Audit and format decisions

- All 14 figure records map back to archived CSV data and Census-published MOE values. No numbers were invented for missing source-family MOEs.
- **28 files** (14 PNG, 14 SVG) were generated in a new versioned directory `05_Statistical_Graphics/Phase2ME/`. Two historical graphics elsewhere in the repository were not overwritten.
- The reproducibility manifest records **28 SHA-256 hashes**, exact plotted data, product labels, periods and captions.
- Each figure is an **individual visualization**; no combined misleading pooled six-jurisdiction socioeconomic plots were constructed. The only six-way figures are 2020 population and age-sex composition sourced from the defined decennial population evidence.
- Percentage survey bars show source-specific official 90% profile MOEs; income survey bars show published original B19013 90% MOEs. Uncertainty bars are **not** tests of pairwise statistical significance.
- `python 06_Methodology/Phase2/validate_phase2me_figures.py`: **PASS** 14 records, two render formats, 28 checksums, values and MOE source mapping.

## Interpretation and approval gates

| Gate | Decision |
|---|---|
| Demographic figures for six explicitly defined jurisdictions | GO for academic draft |
| Island Areas long-form census figures | GO, source-specific |
| Separate 2019 one-year ACS/PRCS charts | GO, with published 90% MOEs |
| Separate 2016–2020 five-year ACS/PRCS charts | GO, with published 90% MOEs |
| Cross-product pooled socioeconomic ranking or significance | NO-GO |
| Academic reviewer signoff | PENDING |
| APA figure numbering/caption and accessibility review | PENDING faculty/editor |
| Final policy/committee publication | NO-GO |

**Source evidence:** `02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv`, `island_areas_2020_socioeconomic_source_specific.csv`, `prdc_2019_acs_one_year_detailed_source_specific.csv`, `prdc_2020_acs_five_year_detailed_source_specific.csv`, `06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv`.

**Next step:** Phase 2M-F consolidated acceptance packet, followed by incorporation of Dr. Belcher's independent written review when received.
