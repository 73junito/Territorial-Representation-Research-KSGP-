# Territorial Representation Research — Phase 2H Academic Review Package
**Draft for faculty or independent methodological review — not final publication**
**Evidence cutoff:** November 21, 2026

## Research question
What demographic changes and socioeconomic patterns are documented in official Census releases for Puerto Rico, American Samoa, Guam, the Northern Mariana Islands, the U.S. Virgin Islands and the federal District of Columbia, and where do unequal data-product definitions prevent valid cross-jurisdiction comparison?

## Evidence and method
The validated 2020 decennial population of six jurisdictions totals **4,313,440**. The six-jurisdiction age/sex pilot is documented in the Phase 2 SPSS archive. Socioeconomic evidence comprises **32 independent source-specific table observations, not 32 independent statistical cases**: 16 observations from the original four 2020 Island Areas Census Demographic Profile archives (income/poverty reference year 2019), eight from 2019 one-year ACS/PRCS Detailed Tables for DC and PR, and eight from the 2016–2020 pooled five-year ACS/PRCS Detailed Tables for DC and PR.

Original government source files, URLs and SHA-256 values are inventoried in `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`. All source-family point estimates and tables are reproduced in `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md` and `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md`.

## Uncertainty
For DC and PR, the four published B19013 household median income margins of error yield four 90% confidence intervals. The 12 education, civilian-unemployment, and poverty-rate intervals were calculated by applying Census-approved sum and subset-proportion formulas to archived published count components. `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv` documents their approximate 90% margins.

**A distinct requirement remains unmet:** none of the 12 derived percentage intervals has been cross-validated against independently retrieved numeric Data Profile/Subject Table MOE values. The variable IDs exist in official Census documentation, including `DP02PR_0068PM` for PR education, but the numeric API requests were redirected to `missing_key.html`. These calculated intervals are accurate against their archived formula inputs, not independently profile-reconciled. See `06_Methodology/Phase2/PHASE2H_PUBLISHED_MOE_RECONCILIATION.md`.

## Known limitations
Island Areas use different household population universes, including a relevant Guam military-housing exclusion. Census tabulations differ from sample-based ACS/PRCS estimates. The one-year period and five-year pooled series cannot be treated as identical moments. Household income 2019 dollars and pooled 2020 inflation-adjusted dollars are different. D.C. is a federal district, not a U.S. territory. Cross-six statistical significance tests, rankings assuming comparability, political preference or causal inference are not authorized.

## Research integrity
The earlier and current SPSS .sav byte hashes differ, though all 6 × 15 content fields match the source CSV by jurisdiction. Original provenance cannot be causally reconstructed with available workspace files, and the historical byte-hash exception remains OPEN.

## Review recommendations
1. Retrieve the 12 published Data Profile or Subject Table numeric percentage MOEs via an authenticated Census API route or official table exports, verifying Puerto Rico-specific social-profile definitions.
2. Have a qualified statistical reviewer check subset-proportion formula applicability, survey design details, confidence conventions and domain-specific universe exclusions.
3. Verify APA 7 bibliographic entries against original documents before public release and obtain academic signoff.
4. Preserve NO-GO on unqualified six-jurisdiction socioeconomic inferential comparison.

**Decision:** Academically reviewable **draft**, NOT accepted final report; publication status CONDITIONAL/BLOCKED pending independently published MOEs and external methodological review.
