# TRR-PHASE2F — Research Report: Demographic and Socioeconomic Evidence
**Evidence review date:** November 21, 2026  
**Research workspace:** `I:\Territorial-Representation-Research`  
**Status:** Source-specific descriptive analysis GO; unqualified six-jurisdiction socioeconomic inference NO-GO.

## Abstract
This research documents demographic and socioeconomic evidence for five inhabited U.S. territories (Puerto Rico, American Samoa, Guam, Northern Mariana Islands, U.S. Virgin Islands) and Washington, D.C., which is a federal district, not a territory. The 2020 decennial population and age/sex pilot covers all six jurisdictions, totaling **4,313,440 residents** in 2020. Separately, four socioeconomic measures were sourced from 2020 Island Areas Census Demographic Profiles for AS, GU, MP and VI; 2019 one-year ACS/PRCS and 2016–2020 five-year ACS/PRCS for DC and PR. The output contains 32 source-specific socioeconomic observations. The source programs use different denominators, collection periods, geographic coverage and inflation conventions and must not be presented as a unified six-jurisdiction analytical sample.

## Research design
Descriptive secondary-source analysis from archived, Census Bureau-issued data; reproducible per-source extraction; no person-level records; no experimental assignment; no causal claims. The age/sex pilot has a validated SPSS dataset and existing Viewer archive. Socioeconomic comparisons are organized by source family rather than pooled for formal statistical testing.

## Demographic pilot
The six-jurisdiction 2020 decennial population total is **4,313,440**. The previously validated age/sex component sums are male 2,047,330; female 2,266,110; under 20 years 880,002; age 20–64 years 2,573,093; age 65+ years 860,345. Source dataset: `02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv`. Earlier 2010–2020 population comparison remains in the Phase 1 records.

## Socioeconomic evidence by source family
### Island Areas 2020 Census profiles
All income observations refer to calendar 2019. Population denominators and military-housing exceptions vary by area. The four-area education percentages, civilian unemployment rates and income figures are directly published in DP summary profiles. Poverty shares are calculated from the documented poverty-universe denominator, not total 2020 population.

| Area | Bachelor's degree or higher | Civilian unemployment | Median household income (2019) | Poverty in 2019 |
|---|---:|---:|---:|---:|
| American Samoa | 13.3% | 13.2% | $28,352 | 54.59% |
| Guam | 25.3% | 10.2% | $58,289 | 20.21% |
| Northern Mariana Islands | 21.0% | 14.1% | $31,362 | 38.01% |
| U.S. Virgin Islands | 22.3% | 9.7% | $40,408 | 22.81% |

### Puerto Rico and Washington, D.C., 2019 one-year ACS/PRCS
These are **survey estimates**, not 2020 Island Areas Census counts. Rates are computed from official 2019 Detailed Table counts; published underlying count MOEs and derived percentage MOEs are retained separately.

| Area | Bachelor's+ | Civilian unemployment | Median household income (2019 dollars) | Poverty |
|---|---:|---:|---:|---:|
| Washington, D.C. | 59.67% | 6.26% | $92,266 | 13.45% |
| Puerto Rico | 27.22% | 14.11% | $20,474 | 43.47% |

### Puerto Rico and Washington, D.C., 2016–2020 five-year ACS/PRCS
These are pooled survey estimates with income expressed in **2020 inflation-adjusted dollars**. They are not a second 2020 snapshot directly comparable with the 2020 Island Areas Census.

| Area | Bachelor's+ | Civilian unemployment | Median household income (2020 dollars) | Poverty |
|---|---:|---:|---:|---:|
| Washington, D.C. | 59.76% | 7.12% | $90,842 | 15.45% |
| Puerto Rico | 26.67% | 15.07% | $21,058 | 43.41% |

## Statistical uncertainty
The published margin of error for median household income is a 90% MOE. The confidence interval displayed in the appendix is point estimate ± published MOE. The 12 remaining ACS/PRCS percentage intervals were calculated using the Census Bureau's subset-proportion MOE formula (2020 ACS Data Users Handbook, chapter 8), including the quadrature MOE for the four educational attainment numerator count categories. These **derived 90% intervals are approximate**; they still require cross-check against official published ACS/PRCS profile or subject-table MOEs before final publication. They must not be presented as original published profile confidence intervals. The Island Areas decennial figures have no ACS sample-derived MOEs.

Reproducible calculations and all 12 derived confidence intervals: `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv`, produced by `06_Methodology/Phase2/calculate_phase2f_ratio_moe.py`.

**Method reference:** U.S. Census Bureau, *Understanding and Using American Community Survey Data: What All Data Users Need to Know* (2020), Chapter 8: `https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf`.

## Interpretation and limitations
These are observed source-specific patterns, **not** a validated six-way comparative socioeconomic ranking. Specific limitations include: (1) demographic census vs survey measurement; (2) 2019 one-year and 2016–2020 pooled survey periods vs 2020 Island Areas Census; (3) household-only and military-housing exclusions in Island Areas, especially Guam; (4) 2019 vs inflation-adjusted 2020 income dollars; (5) formula-derived percentage MOEs rather than downloaded profile MOEs; (6) ecological fallacy and low number of jurisdictions. No statistical significance, causal relationship, electoral eligibility, political preferences, or policy outcomes are inferred.

## Archival and audit limitations
The demographic `.sav` and `.csv` are equivalent by jurisdiction and value, but the earlier `.sav` byte hash differs from its current hash; `PHASE2F_SAV_HASH_FORENSIC.md` records a read-only review. This exception must remain visible in any final archival sign-off. All original source ZIPs and existing SPSS Viewer files were left intact for this phase.

## Research acceptance and next steps
- **GO:** Source-specific descriptive evidence and publication of a clearly caveated methods appendix.
- **CONDITIONAL:** Side-by-side tables that separate source family, reference period, uncertainty and universe; further profile-MOE cross-check.
- **NO-GO:** Unqualified six-jurisdiction socioeconomic SPSS comparison, significance testing, ranking, or causal/political inference.
- **OPEN:** Confirm derived MOEs against published profile/subject tables; resolve SAV byte-hash provenance; obtain academic review before releasing a policy-facing summary.

## Evidence trail
- `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md`
- `06_Methodology/Phase2/PHASE2E_UNCERTAINTY_HARMONIZATION_GATE.md`
- `06_Methodology/Phase2/PHASE2D_NUMERIC_ACQUISITION_ACCEPTANCE.md`
- `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`
- `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv`
- `06_Methodology/Phase2/PHASE2F_SAV_HASH_FORENSIC.md`
