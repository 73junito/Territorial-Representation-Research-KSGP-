# Territorial Representation Research: Demographic and Source-Specific Socioeconomic Evidence for Five Inhabited U.S. Territories and Washington, D.C.

**Phase 2M-D — Academic manuscript, working draft for external faculty review**  
**Prepared:** November 21, 2026  
**Status:** Internal evidence QA only; not independently peer-reviewed, accepted, or authorized for final publication.  
**Scope:** Five permanently inhabited U.S. territories and the federal District of Columbia. The District is not a territory.

## Abstract

This descriptive secondary-data study examines demographic and source-specific socioeconomic evidence for Puerto Rico, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, the U.S. Virgin Islands, and Washington, D.C. The validated 2020 population across the six jurisdictions totals **4,313,440** residents. Four socioeconomic domains—educational attainment, civilian unemployment, median household income, and poverty—are documented as **32 source-specific jurisdiction-domain-product observations**, not 32 exchangeable persons or independent sampling units. Four Island Areas use the 2020 Island Areas Census Demographic Profile; Puerto Rico and D.C. use distinct 2019 one-year and 2016–2020 five-year ACS/PRCS estimates. All 12 targeted published ACS/PRCS Data Profile percentage margins of error (MOEs) were independently retrieved. Ten reproduce earlier derived MOEs at published precision; two D.C. educational-attainment differences are numerically reconciled using directly published composite-count MOEs. The study permits descriptive reporting within each source family but does **not** establish a harmonized six-jurisdiction socioeconomic sample suitable for unqualified ranking, inferential hypothesis testing, or causal claims. A historical SPSS file byte-hash discrepancy remains unresolved despite validated record contents.

**Keywords:** U.S. territories; District of Columbia; Island Areas Census; American Community Survey; Puerto Rico Community Survey; margins of error; evidence provenance; reproducibility.

## Introduction and geographic scope

Five permanently inhabited U.S. territories—Puerto Rico (PR), Guam (GU), American Samoa (AS), the U.S. Virgin Islands (VI), and the Commonwealth of the Northern Mariana Islands (MP)—form the territory scope. Washington, D.C. (DC) is included as a **separate federal district** for geographically defined descriptive study. Its inclusion is not a claim that D.C. is a territory or that the six jurisdictions share a single constitutional status, electoral framework, or Census design.

The uninhabited or nonpermanently inhabited U.S. Minor Outlying Islands and other U.S.-claimed small islands are outside the analysis because the selected jurisdiction-level data sources do not supply equivalent socioeconomic profiles. The study does not purport to establish a complete legal inventory of every U.S. territorial possession.

The primary research question is: **What do the selected original Census Bureau data products document about population, age/sex distribution and selected socioeconomic characteristics for the defined jurisdictions, and which source differences restrict interpretation?**

Subquestions ask (a) whether 2020 six-jurisdiction demographic totals reconcile to the archived population/age-sex source; (b) how each of the three distinct socioeconomic source families reports four selected measures; and (c) how the published survey uncertainty affects proper reporting for D.C. and Puerto Rico.

## Research design and evidence sources

This is a **descriptive, nonexperimental secondary-data** study using aggregated U.S. Census Bureau material. No person-level records, randomized interventions, causal estimators or political-opinion survey data are used. An archived SPSS age/sex pilot supports descriptive review, while original government source files, field matrices, provenance manifests and executable checks support the data extraction.

The socioeconomic evidence is partitioned by **source family**:

1. **2020 Island Areas Census Demographic Profile** — AS, GU, MP, VI. These four Island Areas were surveyed through the Island Areas Census long-form operation, **not** the ACS. The income and poverty measures refer to 2019; coverage/denominator exceptions, especially military-housing exclusions in Guam, require product-specific review.
2. **2019 one-year ACS/PRCS** — DC, PR; estimates from 2019 survey data. Median income is expressed in 2019 inflation-adjusted dollars. These are sample-survey estimates, not 2020 Island Areas census counts.
3. **2016–2020 five-year ACS/PRCS** — DC, PR; pooled survey estimates expressed with 2020 inflation-adjusted household-income dollars. These should not be interpreted as an independent single-year 2020 cross-section.

Each of four socioeconomic domains appears in four Island Areas observations plus two D.C./PR one-year and two D.C./PR five-year observations: `(4 + 2 + 2) × 4 = 32` **table observations**. They are not independent statistical cases and cannot justify a pooled six-jurisdiction significance test.

The four domains have **different population universes**: bachelor's-degree attainment among adults aged 25 and older, unemployment in the applicable civilian labor-force universe, median household income among households, and poverty among persons for whom poverty status is determined. Interpreting one denominator as the jurisdiction's total resident population is inappropriate.

## Data quality, provenance, and analysis plan

The 2020 six-jurisdiction population and source-specific age/sex totals are maintained in `02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv`. The Phase 2D government acquisition manifest inventories **17 original files** with source URLs, size and SHA-256 hash. Phase 2M's portable Python validator checked 17 of 17 government source files, the six-jurisdiction sex/age component sums, all 12 profile estimate/MOE pairs and the two special D.C. composite-count uncertainty reconciliations on Windows and GitHub-hosted Linux.

The analysis reports descriptive values **within each source product**, with separate tables and units. The manuscript provides neither pooled p-values nor claims of statistically significant differences between incompatible programs. Any use of descriptive comparisons requires explicit product, geographic coverage, reference period and universe qualifications.

### Table 1. Validated 2020 jurisdiction population

| Jurisdiction | Classification for this study | Population in 2020 |
|---|---|---:|
| Puerto Rico | U.S. territory | 3,285,874 |
| Washington, D.C. | Federal district; **not** a territory | 689,545 |
| Guam | U.S. territory | 153,836 |
| U.S. Virgin Islands | U.S. territory | 87,146 |
| American Samoa | U.S. territory | 49,710 |
| Northern Mariana Islands | U.S. commonwealth / territory | 47,329 |
| **Six-jurisdiction total** | **Descriptive aggregate only** | **4,313,440** |

*Note.* Values are the archived 2020 decennial demographic pilot. Classifications do not imply comparable political rights or source design for later socioeconomic measures.

The archived sex total is **2,047,330 males** and **2,266,110 females**. Age groups sum to **880,002 under age 20**, **2,573,093 ages 20–64**, and **860,345 age 65 or older**; each set reconciles to the 4,313,440 total. These counts are descriptive and not estimates of voting eligibility.

### Table 2. 2020 Island Areas Census Demographic Profile measures

| Area | Bachelor's+ (age 25+), % | Civilian unemployment, % | Median household income, 2019 USD | Poverty in 2019, % |
|---|---:|---:|---:|---:|
| American Samoa | 13.3 | 13.2 | $28,352 | 54.59 |
| Guam | 25.3 | 10.2 | $58,289 | 20.21 |
| Northern Mariana Islands | 21.0 | 14.1 | $31,362 | 38.01 |
| U.S. Virgin Islands | 22.3 | 9.7 | $40,408 | 22.81 |

*Note.* Four Island Areas source products; not sample-based ACS figures. Poverty is calculated using the source's applicable poverty universe. Area coverage restrictions (particularly Guam) prevent the table from being treated as the same population definition as D.C./PR survey data. An ACS 90% sample MOE must **not** be attached to these decennial counts.

### Table 3. 2019 one-year ACS/PRCS survey measures (D.C. and Puerto Rico)

| Jurisdiction | Bachelor's+ (age 25+), % | Civilian unemployment, % | Median household income, 2019 USD | Poverty, % |
|---|---:|---:|---:|---:|
| Washington, D.C. | 59.67 | 6.26 | $92,266 | 13.45 |
| Puerto Rico | 27.22 | 14.11 | $20,474 | 43.47 |

*Note.* Survey estimates and corresponding 90% MOEs. Uncertainty intervals are source-specific; see Table 5. Displaying these numbers beside Table 2 does not establish cross-product equivalence.

### Table 4. 2016–2020 five-year ACS/PRCS survey measures (D.C. and Puerto Rico)

| Jurisdiction | Bachelor's+ (age 25+), % | Civilian unemployment, % | Median household income, 2020 inflation-adjusted USD | Poverty, % |
|---|---:|---:|---:|---:|
| Washington, D.C. | 59.76 | 7.12 | $90,842 | 15.45 |
| Puerto Rico | 26.67 | 15.07 | $21,058 | 43.41 |

*Note.* Pooled five-year survey estimates are not a second independent year-2020 measurement, and the household-income dollar bases of Tables 3 and 4 differ.

## Survey uncertainty and independent cross-validation

For ACS/PRCS results, the standard reported margin of error is associated with a **90% confidence level**. The directly published Data Profile percentage MOEs were retrieved independently in Phase 2I from official Census data-profile variables: D.C. education `DP02_0068PM`; PR education `DP02PR_0068PM`; unemployment `DP03_0009PM`; poverty `DP03_0128PM`. The corresponding profile percentages are rounded to one decimal place. These published MOEs—not earlier conflicting formula-derived approximations—are used for any reported Data Profile uncertainty.

### Table 5. Independently published profile percentage MOEs (90%, percentage points)

| Survey | Jurisdiction | Education MOE | Unemployment MOE | Poverty MOE |
|---|---|---:|---:|---:|
| 2019 one-year | Washington, D.C. | ±1.1 | ±0.6 | ±1.3 |
| 2019 one-year | Puerto Rico | ±0.6 | ±0.7 | ±0.8 |
| 2016–2020 five-year | Washington, D.C. | ±0.6 | ±0.5 | ±0.5 |
| 2016–2020 five-year | Puerto Rico | ±0.3 | ±0.3 | ±0.3 |

*Note.* These are the **published 90% percentage MOEs**, not MOEs recomputed from category counts. They were validated against six original official Census Data Profile API response tables, including two direct D.C. composite count-response tables for the discrepancy investigation.

Ten of the twelve formula-derived Phase 2F percentage MOEs round to the same one-decimal figure as the independently published MOEs. For D.C. bachelor's+ attainment, Phase 2F combined the four detailed-table numerator category count MOEs by quadrature; it produced approximate MOEs **±1.59719 pp (2019)** and **±0.81966 pp (2016–2020)**, compared with the official Data Profile **±1.1 pp** and **±0.6 pp**. The published **composite count** MOEs for bachelor's-or-higher D.C. attainment are **±5,612 persons (2019)** and **±2,793 persons (five-year)**. Applying the subset-proportion approximation to these direct composite count MOEs produces approximately **±1.11022 pp** and **±0.55633 pp**, respectively, rounding to the official published percentage MOEs. The four detailed-table category point estimates sum exactly to the direct composite-count estimates.

This reconciles the **numerical result**, not the entire Census Bureau replicate-weight covariance mechanism. Phase 2F component calculations remain historical evidence and must not be silently presented as official Data Profile MOEs. The published rate/MOE precision also limits claims of numerical identity before rounding.

The four median-household-income MOEs come directly from source `B19013_001` and give these illustrative 90% intervals: D.C. 2019 $92,266 ±$2,497 ([$89,769, $94,763]); Puerto Rico 2019 $20,474 ±$382 ([$20,092, $20,856]); D.C. five-year $90,842 ±$1,580 ([$89,262, $92,422]); Puerto Rico five-year $21,058 ±$186 ([$20,872, $21,244]). Income intervals follow the corresponding product's own dollar base and denominator.

## Discussion

The decennial population and age/sex evidence can be aggregated for the **six explicitly selected jurisdictions**, but the selected socioeconomic indicators cannot support a similarly pooled sample. The Island Areas Census profiles differ from D.C. and Puerto Rico ACS/PRCS survey operations, as well as from one-year and pooled five-year survey products. The figures document each source's own measurements; they are neither evidence of equivalent sampling errors nor a validated ranking of socioeconomic outcomes across the six.

Directly published MOEs improve fidelity in uncertainty reporting, but a nominal 90% interval is not a license to compare estimates from incompatible universes or inflation years. Even within ACS/PRCS, a comparison of two reported estimates would require an appropriately justified difference-of-estimates uncertainty calculation and a clearly defined hypothesis; this study makes no such significance claim.

No data in this study measure jurisdiction-wide political preferences, causally estimate effects of territorial status, establish legal voting entitlements, or represent the position of the Kansas Green Party or any committee. Demographic or socioeconomic measurements must not be equated with political endorsement.

## Limitations and research integrity

**Source design.** Four Island Areas reflect long-form decennial Census profiles, while D.C./PR observations are sample-survey measures. Population coverage and military housing may differ; Guam requires an explicit qualification. **Time and currency.** Island Areas income/poverty refer to 2019, the 2019 one-year survey measures represent 2019, and the 2016–2020 measures pool five years and express income in 2020-adjusted dollars. **Universes.** Education, unemployment, income and poverty refer to different denominators. **Inference.** Six jurisdiction-level demographic cases and 32 source-product observations do not provide independent subject-level records for the proposed inferential comparisons.

**Archival exception.** The current six-jurisdiction SPSS `.sav` file and its Git-tracked archive have identical bytes (SHA-256 `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`). The previously recorded SAV hash (`300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`) differs. The six-by-15 fields reconcile to the canonical CSV by jurisdiction, but the earlier binary is not present in the examined repository and the historical cause **cannot be established**. Matching content does not prove uninterrupted historical byte preservation. The original datasets have not been modified for this manuscript.

**Academic status.** The external faculty methods review has been requested by the research owner but no review, approval or response has been independently verified as of this draft. References and methodology remain subject to qualified faculty and APA 7 verification; institutional or committee authorization has not been granted.

## Conclusion

The project provides a source-linked account of the selected six jurisdictions' demographic data and **carefully bounded** socioeconomic information, with validated primary-source inventories, independently reconciled ACS/PRCS percentage MOEs, and a read-only cross-platform evidence validator. The strongest supported output is **source-specific descriptive reporting**. A pooled six-jurisdiction inferential analysis, causal explanation, constitutional inference or final committee publication is **not** supported by the current evidence and has a **NO-GO** disposition pending separately justified evidence and review.

## References — provisional APA 7 entries for faculty verification

U.S. Census Bureau. (2020). *2019 American Community Survey 1-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2019/release.html

U.S. Census Bureau. (2020). *Understanding and using American Community Survey data: What all data users need to know* [Handbook]. https://www.census.gov/programs-surveys/acs/library/handbooks/general.html

U.S. Census Bureau. (2022). *2016–2020 American Community Survey 5-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2020/release.html

U.S. Census Bureau. (2022). *2020 Island Areas Censuses: Demographic Profile Summary File* [Data set]. https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html

U.S. Census Bureau. (2022). *2020 Island Areas Censuses (IAC) Demographic Profile Summary File: Technical documentation* [Technical documentation]. https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/2020-iac-dpsf-technical-documentation.pdf

*Bibliographic gate:* Multiple U.S. Census Bureau items share publication years; final alphabetical reference ordering, APA year-letter suffixes, document title-page year and in-text citation disambiguation must be completed and confirmed by the academic reviewer before formal submission. The Phase 2J citation audit preserves the current primary-source metadata crosswalk.

## Evidence and reproducibility appendix

- Original source manifest: `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`.
- Original Island Areas product-specific values: `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md`.
- Original detailed values and historical methods: `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md`.
- Census published profile source JSON: `01_Government_Sources/Phase2_Socioeconomic/Census/ACS_Profile_*_official.json`.
- Published percentage MOEs and reconciliation: `06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv`.
- Direct D.C. composite-count MOEs: `06_Methodology/Phase2/PHASE2I_DC_EDUCATION_VARIANCE_DIAGNOSTIC.csv`.
- Current SAV history decision: `06_Methodology/Phase2/PHASE2MC_SAV_HISTORICAL_PROVENANCE_DECISION.md`.
- Portable evidence validation: `python 06_Methodology/Phase2/validate_phase2m_portable.py`.
- External academic review handoff: `09_Committee_Package/Phase2K_Faculty_Review_Handoff.md`.

**Acceptance:** DRAFT GO for faculty review; scientific comparability claims CONDITIONAL/NO-GO as identified; final publication **NO-GO** until independent qualified academic review and any applicable publication/committee authorization.
