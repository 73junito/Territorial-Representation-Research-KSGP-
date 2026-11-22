# TRR-PHASE2I — Published Census Percentage MOE Cross-Validation

**Date:** November 21, 2026  
**Decision:** OFFICIAL NUMERIC ACQUISITION PASS; **10/12 MOEs agree at Census display precision; 2/12 differ materially** and require methodological adjudication. Six-way unqualified socioeconomic comparison remains NO-GO.

## Acquisition
Four original JSON response tables were successfully retrieved from the official U.S. Census Bureau 2019 ACS/PRCS one-year and 2016–2020 ACS/PRCS five-year **Data Profile API** through a manual, read-only GitHub Actions workflow using the repository secret `CENSUS_DATA_API`. No secret value was logged, stored in the data files, or committed. The successful workflow run was:
https://github.com/73junito/Territorial-Representation-Research-KSGP-/actions/runs/44972219452

The authenticated response files were archived at:
- `01_Government_Sources/Phase2_Socioeconomic/Census/ACS_Profile_2019_acs1_DC_official.json`
- `01_Government_Sources/Phase2_Socioeconomic/Census/ACS_Profile_2019_acs1_PR_official.json`
- `01_Government_Sources/Phase2_Socioeconomic/Census/ACS_Profile_2020_acs5_DC_official.json`
- `01_Government_Sources/Phase2_Socioeconomic/Census/ACS_Profile_2020_acs5_PR_official.json`

Exact SHA-256 values are displayed by `import_phase2i_github_actions_profile_evidence.py`. Official profile variables: DC education `DP02_0068PE/PM`; PR education `DP02PR_0068PE/PM`; unemployment `DP03_0009PE/PM`; poverty `DP03_0128PE/PM`. `PM` is the official published 90% percentage margin of error.

## Numerical comparison (percentage-point MOEs)
Census Data Profile percentages and MOEs are published to one decimal place. *Match* here means the independently computed Phase 2F result rounds to the **same one-decimal MOE**, not that the underlying exact sampling variance is identical.

| Survey | Area | Measure | Official profile rate (%) | Official MOE (pp) | Derived MOE (pp) | Outcome |
|---|---|---|---:|---:|---:|---|
| 2019 one-year | DC | Education, bachelor's+ | 59.7 | 1.1 | 1.59719 | **DISCREPANCY** (derived rounds 1.6) |
| 2019 one-year | DC | Unemployment | 6.3 | 0.6 | 0.61394 | Match |
| 2019 one-year | DC | Poverty | 13.5 | 1.3 | 1.27327 | Match |
| 2019 one-year | PR | Education, bachelor's+ | 27.2 | 0.6 | 0.64306 | Match |
| 2019 one-year | PR | Unemployment | 14.1 | 0.7 | 0.66056 | Match |
| 2019 one-year | PR | Poverty | 43.5 | 0.8 | 0.75820 | Match |
| 2016–2020 five-year | DC | Education, bachelor's+ | 59.8 | 0.6 | 0.81966 | **DISCREPANCY** (derived rounds 0.8) |
| 2016–2020 five-year | DC | Unemployment | 7.1 | 0.5 | 0.45776 | Match |
| 2016–2020 five-year | DC | Poverty | 15.5 | 0.5 | 0.50653 | Match |
| 2016–2020 five-year | PR | Education, bachelor's+ | 26.7 | 0.3 | 0.26876 | Match |
| 2016–2020 five-year | PR | Unemployment | 15.1 | 0.3 | 0.28089 | Match |
| 2016–2020 five-year | PR | Poverty | 43.4 | 0.3 | 0.32751 | Match |

**Point-estimate reconciliation: 12/12** at official one-decimal display precision.  
**Margin-of-error reconciliation: 10/12** at official one-decimal display precision.  
**Methodologically unresolved: 2/12**, both DC educational attainment.

## Interpretation of the two differences
For 2019 DC education, calculated ±1.59719 percentage points versus published ±1.1 pp (difference +0.49719 pp). For five-year DC education, calculated ±0.81966 pp versus published ±0.6 pp (difference +0.21966 pp). The 2019 published 90% interval using the displayed rate is approximately **58.6%–60.8%**, and the five-year published interval **59.2%–60.4%**.

The Phase 2F education calculation combines the four detailed-table educational attainment numerator category count MOEs using root-sum-of-squares (quadrature), then applies the Census subset-proportion formula. Covariance among categories, the published profile's direct variance procedure, data-product weighting or other survey-design choices **may** explain the differences; they have **not been causally established**. Rounding cannot explain them. Do not claim that merely applying the standard formula yields the same uncertainty as the published Data Profile value for DC education.

## Research disposition
- GO: Published Data Profile **numeric acquisition** and direct reporting of official profile rate/MOE pairs with source, period, geography and denominator clearly identified.
- GO: Ten method-derived MOEs match published profile values at one-decimal display precision.
- CONDITIONAL: Two DC education Phase 2F approximate MOEs. Prefer the actual **published** profile MOEs for official Data Profile statements; do not silently substitute the calculated values.
- OPEN: Investigate educational category covariance/variance methods with an appropriately qualified ACS statistical reviewer. Document whether the two methods produce a meaningfully distinct statistic.
- NO-GO: Unqualified six-jurisdiction pooled socioeconomic significance tests/rankings; mixing Island Areas Census and ACS/PRCS methods remains prohibited.
- OPEN: Historical demographic .sav byte-hash causality; numerical MOE acquisition does not resolve that separate issue.

## Reproducibility and audit trail
- `06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv` — original workflow-produced 12-row response comparison.
- `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv` — independently verified 10-match / 2-discrepancy classification.
- `06_Methodology/Phase2/import_phase2i_github_actions_profile_evidence.py` — no-overwrite import and source cross-check.
- `06_Methodology/Phase2/fetch_phase2i_official_profile_moes.py` — official API acquisition; key only from Actions secret at runtime.
- `.github/workflows/verify-census-profile-moes.yml` — manual workflow; read-only repository permissions, official response artifact only.
- `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv` — derived MOE baseline.

This Phase 2I report supersedes the Phase 2H 0/12 **acquisition BLOCKED** conclusion while preserving the original historical Phase 2H decision document. The statistical reconciliation is **PARTIAL**, not a full PASS.
