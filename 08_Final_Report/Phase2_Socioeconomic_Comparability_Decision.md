# Phase 2 socioeconomic comparability — Decision Summary
Date: November 21, 2026
Status: SOURCE/VARIABLE INVENTORY PASS; UNQUALIFIED SIX-JURISDICTION COMPARABILITY NO-GO.

Scope: Puerto Rico, Guam, U.S. Virgin Islands, American Samoa, Northern Mariana Islands, Washington, D.C.

Four domains reviewed: educational attainment, civilian unemployment, median household income, and poverty. Twenty-four source- and jurisdiction-specific variable definitions were validated. Four original Island Areas Census ZIPs and two official ACS variable metadata JSONs passed integrity review.

**Finding:** The 2020 Island Areas Census DP2/DP3 tabulations cannot presently be compared as if they were methodologically interchangeable with Puerto Rico and D.C. 2016–2020 ACS/PRCS five-year profile estimates. The Island Areas universes differ for household residence and military housing. The Census income/poverty measures refer to 2019, while pooled survey estimates refer to different measurement periods and (for household income) inflation-adjusted dollars. Conventional 2020 ACS one-year estimates were not released.

**Do not** run inferential tests or produce six-jurisdiction rankings for these socioeconomic indicators until denominators, collection periods, exclusions and measurement units are harmonized. A six-row jurisdiction file is not an independent microdata sample.

Source records:
- 01_Government_Sources/Phase2_Socioeconomic/socioeconomic_comparability_matrix.csv
- 01_Government_Sources/Phase2_Socioeconomic/socioeconomic_source_register.csv
- 06_Methodology/Phase2/SOCIOECONOMIC_COMPARABILITY_REVIEW.md
- 06_Methodology/Phase2/validate_socioeconomic_review.py

Next qualified sub-phase: inspect the official Island Areas DP technical layout and footnotes; extract and verify original DP2/DP3 island records; obtain official PR/DC ACS/PRCS actual estimates including margins of error; then prepare separate, explicitly labeled product/period comparison panels before reconsidering SPSS analysis.

The previously accepted Phase 2 age-and-sex dataset and SPSS .spv remain unchanged.
