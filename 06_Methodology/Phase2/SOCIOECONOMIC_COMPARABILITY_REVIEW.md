# Phase 2 — Socioeconomic Comparability Review
**Review date:** November 21, 2026
**Jurisdictions:** American Samoa (AS), Guam (GU), Northern Mariana Islands (MP), U.S. Virgin Islands (VI), Puerto Rico (PR), Washington, D.C. (DC)
**Decision:** NO-GO for an unqualified six-jurisdiction cross-sectional SPSS comparison of education, unemployment, household income or poverty.

## Scope and provenance
The project already stores 2020 U.S. Census Island Areas original Demographic Profile ZIP files for AS, GU, MP and VI. This review examined locally archived Census API variable dictionaries for the four areas; additionally retrieved/archived the 2016–2020 ACS/PRCS five-year and 2019 ACS one-year variable dictionaries (metadata only). The metadata defines the expected variables, not measured values. No PR/DC socioeconomic numeric observations were downloaded. Source files, original URLs and SHA-256 values are in `01_Government_Sources/Phase2_Socioeconomic/socioeconomic_source_register.csv`; 24 jurisdiction-by-measure assessments are in `socioeconomic_comparability_matrix.csv`.

## Four outcome definitions and gate decisions
| Domain | 2020 Island Areas Demographic Profile | 2016–2020 ACS/PRCS Profile counterpart | Six-way gate |
|---|---|---|---|
| Education | DP2_0016P — Bachelor's degree or higher; people age 25+ (often **in households**, GU additionally excludes military housing) | DP02_0068PE — Bachelor's degree or higher; population 25+ | NO-GO: denominator and 2020 count vs pooled sample differ |
| Employment | DP3_0009C — Civilian labor force unemployment rate (Island Areas subsets differ) | DP03_0009PE — Civilian labor force unemployment rate | NO-GO: household/military population and survey vs census differences |
| Household income | DP3_0104C — Median household income, **calendar 2019 dollars**, GU excludes military housing | DP03_0062E — Median household income in **2020 inflation-adjusted dollars** across ACS/PRCS five-year survey | NO-GO: time, inflation and household scope differ |
| Poverty | DP3_0151P — Individuals below the poverty level **based on 2019 income**, often people in households; GU military housing excluded | DP03_0128PE — Percent of people with income **in past 12 months** below poverty threshold, 2016–2020 sample | NO-GO: poverty universe, time and survey methodology differ |

**Important:** The letters C and P in Island Areas API fields are specific to those products; do not infer that any C-ending field is universally a count. For example, DP3_0009C is labeled *Unemployment Rate* and DP3_0104C is *Median household income*. Use the Census metadata label and its measurement unit, not suffix alone.

## Jurisdiction-specific scope conflicts
- **Guam:** For education and employment, the source expressly describes people in households *excluding people in military housing units*. The same restriction applies to its household income and poverty measures.
- **American Samoa:** Education and employment are described for people in households; the poverty profile uses individuals in households.
- **U.S. Virgin Islands:** Education and employment generally refer to individuals in households; poverty refers to individuals in households.
- **Northern Mariana Islands:** The examined education/employment profile labels refer to population age 25+ or 16+ without a household-only phrase. Do not assume this guarantees identical coverage to other Island Areas without examining the Census universe footnotes.
- **Puerto Rico and D.C.:** The potential standard 2016–2020 ACS five-year/PRCS counterparts are sample-based period estimates and are not a true 2020 decennial socioeconomic census equivalent. Product availability for each geography and the numeric measures themselves must be confirmed before analysis.

## Critical 2020 ACS release issue
U.S. Census Bureau did **not** release conventional 2020 ACS one-year estimates due to COVID-19-related nonresponse problems. The 2020 one-year release was experimental; experimental estimates were not released for Puerto Rico. Do not describe it as a standard 2020 ACS/PRCS one-year source. An archived **2019** one-year ACS dictionary is a potential different-period alternate, not an equal 2020 source.

## Analytical and SPSS restrictions
- Do not merge income, unemployment or poverty rates into a single six-jurisdiction SPSS table and label them equivalent without a harmonization design approved in advance.
- Do not divide an Island Areas household-only numerator by the decennial total resident population, which includes group quarters and potentially military-housing residents.
- Do not compare 2019 nominal household income against ACS 2020 inflation-adjusted income without documented transformations, and even such a transformation alone does not reconcile collection-period or sampling differences.
- Preserve unavailable observations as **missing with explicit reason**; never replace with 0.
- ACS/PRCS sample uncertainty requires published margins of error and survey-aware interpretation; the decennial Island Areas tabulations and the five-year ACS do not form a common independently sampled set for a six-case significance test.
- This review makes no claim about residents' policy preferences, citizenship, eligibility to vote or legal self-determination views.

## Recommended next controlled sub-phase
1. Obtain official Island Areas 2020 Demographic Profile **technical-documentation field layouts and universe/footnote guidance** and confirm the four original ZIPs' DP2/DP3 fields at island-wide records.
2. Acquire official **2019 ACS/PRCS one-year** *and* **2016–2020 ACS/PRCS five-year**  socio-economic observations for PR/DC where available, with margins of error and source definitions. Keep time/product series separate.
3. Prepare four **source-specific** tables first (Education, Employment, Income, Poverty), each carrying jurisdiction, source family, period, denominator, estimate type, inflation convention, exclusions and missing-data reason.
4. Conduct a variable-level sensitivity/harmonization analysis before proposing any cross-six comparisons. Publish descriptive panels labeled as non-equivalent if harmonization is not defensible.
5. Only then authorize SPSS socioeconomic datasets, graphics or statistical analyses.

## Acceptance record
SOURCE-INVENTORY: PASS (four archived 2020 Island Areas ZIPs; five-year and 2019 ACS metadata dictionaries).
METADATA FIELD IDENTIFICATION: PASS (four definitions × six jurisdictions = 24 rows).
COMPARABILITY FOR SIX-WAY SPSS SOCIOECONOMIC COMPARISON: **NO-GO**.
PR/DC NUMERICAL SOCIOECONOMIC DATA ACQUISITION: **NOT COMPLETE**.
ISLAND AREAS DP2/DP3 DATA EXTRACTION AND TECHNICAL-LAYOUT VALIDATION: **NOT STARTED**.

## Census Bureau references
- https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/2020-iac-dpsf-technical-documentation.pdf
- https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2020.html
- https://www.census.gov/data/developers/data-sets/acs-1year/2020.html
- https://www.census.gov/programs-surveys/acs/data/experimental-data.html
- https://api.census.gov/data/2020/acs/acs5/profile/variables.json
- https://api.census.gov/data/2019/acs/acs1/profile/variables.json
