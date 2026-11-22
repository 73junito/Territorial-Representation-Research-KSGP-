# Phase 2I — D.C. bachelor's-or-higher MOE reconciliation

**Status:** Numerical discrepancy explained by choice of aggregated numerator MOE; published percentage MOEs independently reproduced at 0.1 percentage-point precision. **Exact covariance/replicate-variance mechanism not directly measured.**

## Archived official evidence
The authenticated Census Bureau Data Profile API was queried for `DP02_0068E`, `DP02_0068M`, `DP02_0068PE`, and `DP02_0068PM` for District of Columbia (FIPS 11), in 2019 ACS 1-year and 2020 ACS 5-year. Successful GitHub Actions diagnostic: https://github.com/73junito/Territorial-Representation-Research-KSGP-/actions/runs/44972665482 . The earlier attempt failed safely because the main acquisition script refused to overwrite existing Census archives; the diagnostic was isolated and then succeeded.

Original source JSON: `06_Methodology/Phase2/ACS_DC_2019_Direct_Education_Profile_Count_Official.json` and `ACS_DC_2020_Direct_Education_Profile_Count_Official.json`. Original API values and calculations are in `PHASE2I_DC_EDUCATION_VARIANCE_DIAGNOSTIC.csv`. The archived 2019 and 2020 Detailed Table B15003 components and published DC Data Profiles were checked against source values independently.

## Direct composite vs four-category MOE method

| Published product | Bachelor's+ estimate (count) | Direct published count MOE | Quadrature MOE of four count categories | Percent MOE using direct numerator | Percent MOE using quadrature numerator | Published profile percent MOE |
|---|---:|---:|---:|---:|---:|---:|
| 2019 ACS 1-year, DC | 301,429 | ±5,612 | ±8,070.76 | ±1.11022 pp | ±1.59719 pp | **±1.1 pp** |
| 2016–2020 ACS 5-year, DC | 299,975 | ±2,793 | ±4,114.79 | ±0.55633 pp | ±0.81966 pp | **±0.6 pp** |

Detailed Table numerator count sums match directly published composite estimates **exactly** in both periods. Using the Census Bureau's **direct composite count MOE** with the 25+ denominator and the subset-proportion approximation reproduces the Census Bureau's directly published profile **percent** MOE after one-decimal rounding in both periods.

The earlier Phase 2F computation took the root sum of squares of the MOEs of four categories B15003_022–025, rather than the separately published `DP02_0068M` aggregate count MOE. The four-category approximation is larger in these cases. The Census Bureau documents that root-sum-of-squares formulas are approximations and that variance-replicate estimates incorporate covariance terms unavailable in component-only MOEs. Negative *implied aggregate cross-term contributions* are consistent with the smaller composite MOE, but are **not an independent estimate of the actual covariance matrix or a proven account of the Bureau's internal variance algorithm**.

## Decision
- **PASS:** All 12 official Census Data Profile **point estimates** reconcile at display precision.
- **PASS:** Ten Phase 2F percentage MOEs reconcile directly at display precision.
- **RESOLVED NUMERICALLY:** The remaining two DC education percent MOEs reproduce published rates once the **direct published composite numerator MOE** is used instead of quadrature of four component MOEs.
- **PENDING OPTIONAL EXPERT ANALYSIS:** Confirm exactly how composite variances were generated using compatible official replicate tables and survey statistical documentation; not necessary to report the direct published Census profile MOE as published.
- **PRESERVE PHASE 2F:** Original derived calculations remain archival evidence; this memo explains their limitation rather than overwriting them.
- **NO-GO:** No unqualified six-way socioeconomic comparison, hypothesis testing or inference.
- **SEPARATE OPEN EXCEPTION:** Historical demographic .sav byte hash provenance remains unresolved.

## Official Census methodology
U.S. Census Bureau, *Understanding and Using American Community Survey Data: What All Data Users Need to Know* (2020), ch. 8: https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020.pdf ; Census variance-replicate tables: https://www.census.gov/programs-surveys/acs/data/variance-tables.html .

**Reproducible diagnostic:** `06_Methodology/Phase2/diagnose_phase2i_dc_education_variance.py`. **Published-source comparison baseline:** `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv`.
