# TRR-PHASE2H — Independent Published MOE Reconciliation
**Review date:** November 21, 2026  
**Status:** **12/12 published numeric MOE cross-checks BLOCKED; official variable identity CONFIRMED; derived arithmetic PASS from Phase 2F.**

## Verified findings
The official Census ACS/PRCS Data Profile variable metadata confirms the following published 90% percentage-point margin-of-error fields, and corresponding `PE` point-estimate fields:
- 2019 ACS 1-year and 2020 ACS 5-year, DC educational attainment: `DP02_0068PM`.
- 2019 PRCS 1-year and 2020 PRCS 5-year, Puerto Rico educational attainment: `DP02PR_0068PM` (the Puerto Rico-specific social profile, not `DP02`).
- Both geography/program families, civilian unemployment: `DP03_0009PM`.
- Both, poverty among all people: `DP03_0128PM`.

**Primary documentation:** `https://api.census.gov/data/{year}/acs/{acs1|acs5}/profile/variables/{variable}.html`, for 2019 and 2020, with distinct `DP02PR` for Puerto Rico social characteristics. Census's official documentation confirms these variable definitions and their 90% MOE meaning.

## Numeric acquisition attempts
- Direct correctly formatted ACS 2019 one-year and ACS 2020 five-year Profile API queries from the authorized research PC redirected to HTML `https://api.census.gov/data/missing_key.html` and never returned actual published numerical observations. HTTP 200 after redirect does not establish data success.
- The legacy official `www2.census.gov/.../2019/data/1_year_data_profiles/` and `.../2020/data/5_year_data_profiles/` paths returned HTTP 404. The 2018 data profile archive has a different structure; do not assume that path pattern survives in later years.
- Published Census **metadata variables** and archived **Detailed Table MOE components** are not independent published *profile percent-MOE values*.
- Do not invent, impute or copy Phase 2F-derived intervals into empty official MOE cells.

## Reconciliation matrix
The full 12-row record is `06_Methodology/Phase2/PHASE2H_MOE_RECONCILIATION_MATRIX.csv`. It records the confirmed official profile MOE variable URL, the previously derived estimate and approximate 90% MOE, blank official numeric estimate and MOE fields, and a named blocking reason. **Reconciliation count 0/12; published-source numeric values not obtained.**

## What remains methodologically valid
Phase 2F already computed 12 *derived* 90% MOEs using Census's subset-proportion formula and source Detailed Table estimate/MOE components, with numerator-sum quadrature for bachelor's degree or higher. The `validate_phase2f_research.py` checks the calculations independently. That is an *arithmetic/formula* validation, not independent agreement with the published data-profile uncertainty measure. Four median household income confidence intervals are supported by directly published `B19013_001` MOEs.

## Remaining work
Acquire official **Data Profile/Subject Table downloadable exports** for exactly the 2019 ACS/PRCS one-year and 2016–2020 five-year periods for state geographies DC=11 and PR=72 (including Puerto Rico's `DP02PR`). Record exact official estimate, 90% MOE, source export URL/file hash, retrieval date and variable label for each of 12 fields; compare to derived percent-point MOE after accounting for display rounding and numerator-universe differences. Treat a mismatch as CONDITIONAL pending adjudication.

**Acceptance:** **BLOCKED for 12 independent published-profile numeric comparisons.** No cross-six socioeconomic inferential comparison is authorized.
