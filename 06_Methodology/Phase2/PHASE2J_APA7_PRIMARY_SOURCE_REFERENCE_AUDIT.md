# TRR-PHASE2J — Census Primary-Source and APA 7 Reference Audit

**Review date:** November 21, 2026  
**Status:** Primary source URLs and archived 17-file manifest hashes VERIFIED; APA 7 references prepared for faculty inspection; external editorial review NOT performed.

## Method and confidence levels

- Original authoring agency: **U.S. Census Bureau**.
- Confirmed on the official website: program/product names and relevant release dates, including 2019 one-year estimates released **September 17, 2020**, and 2016–2020 five-year estimates released **March 17, 2022**.
- File-specific provenance: 17 archived original Census sources match their SHA-256 checksums in `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` at audit time.
- Direct Census Data Profile numeric responses (4 JSON files) and the two D.C. education count-MOE JSON files were independently acquired and verified in Phase 2I. These are separate from the 17-file Phase 2D manifest.
- These references follow an **APA 7 draft format**. Exact handbook PDF title-page details, final dataset version metadata, and university-specific reference requirements need human bibliographic signoff.

## Proposed APA 7 reference entries

U.S. Census Bureau. (2020). *2019 American Community Survey 1-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2019/release.html

U.S. Census Bureau. (2022). *2016–2020 American Community Survey 5-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2020/release.html

U.S. Census Bureau. (2022). *2020 Island Areas Censuses: Demographic Profile Summary File* [Data set]. https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html

U.S. Census Bureau. (2022). *2020 Island Areas Censuses (IAC) Demographic Profile Summary File: Technical documentation* [Technical documentation]. https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/2020-iac-dpsf-technical-documentation.pdf

U.S. Census Bureau. (2020). *Understanding and using American Community Survey data: What all data users need to know* [Handbook]. https://www.census.gov/programs-surveys/acs/library/handbooks/general.html

**APA disambiguation:** Entries sharing the same organizational author and publication year will need alphabetic suffixes (2020a/2020b; 2022a/2022b) based on finalized reference-list title ordering, with matching in-text citations. Do not treat the above standalone entries as a final alphabetically disambiguated list.

## Exact source-field crosswalk for in-text citations

| Domain | Island Areas Demographic Profiles (AS/GU/MP/VI) | D.C./PR 2019 and 2016–2020 ACS/PRCS Detailed Tables | Published profile MOE |
|---|---|---|---|
| Bachelor's degree or higher | `DPxx0200001` (xx=AS,GU,MP,VI) | `B15003_001,022–025` | D.C. `DP02_0068PM`; PR `DP02PR_0068PM` |
| Civilian unemployment | `DPxx0510001` | `B23025_003,005` | `DP03_0009PM` |
| Median household income | `DPxx0630001` | `B19013_001` | original income MOE component `B19013_001` |
| Persons below poverty share | `DPxx0900002 / DPxx0900001` | `B17001_002 / B17001_001` | `DP03_0128PM` |

The `xx` abbreviation is a **notation**, not a literal Census variable to query. Use the complete source-specific field for each area in the final paper.

## Critical documentary distinctions

1. The Island Areas Decennial Demographic Profile is distinct from PRCS/ACS survey products. ACS is not conducted in the four Island Areas; the Census Bureau used a long-form Island Areas questionnaire. The Census Bureau also describes using ACS disclosure-avoidance methods for Island Areas data products. These facts do **not** establish strict survey-method equivalence.
2. The 2019 ACS 1-year estimates were collected in 2019 and released in 2020; the 2016–2020 ACS 5-year estimates were released in 2022. There was no standard 2020 ACS 1-year Summary File.
3. The directly published Data Profile MOEs are preferred for displayed profile percentages; Phase 2F calculated MOEs remain historical, method-derived approximations. Phase 2I resolved two D.C. educational-attainment discrepancies using directly published **composite count MOEs**, not an independently reconstructed covariance matrix.
4. Publication-year labels refer to **release/document year** where independently established, not automatically the survey collection year. Confirm technical documentation title-page year before scholarly submission.
5. These sources do not establish constitutional entitlement, voting eligibility, political opinion or adoption by the Kansas Green Party.

## Primary official verification links

- Island Areas Census source and questionnaire context: https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html
- Technical documentation directory: https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/
- 2019 one-year data release: https://www.census.gov/programs-surveys/acs/news/data-releases/2019/release.html
- 2016–2020 five-year data release: https://www.census.gov/programs-surveys/acs/news/data-releases/2020/release.html
- 2019 Summary File documentation: https://www.census.gov/programs-surveys/acs/data/summary-file/sequence-based/2019.html
- 2020 five-year Summary File documentation: https://www.census.gov/programs-surveys/acs/data/summary-file/sequence-based/2020.html
- ACS handbook: https://www.census.gov/programs-surveys/acs/library/handbooks/general.html

## Gate
**GO** primary Census attribution/source traceability; **CONDITIONAL** final APA 7 formatting and document-year disambiguation pending academic editor; **NO-GO** asserting external faculty acceptance or party endorsement.
