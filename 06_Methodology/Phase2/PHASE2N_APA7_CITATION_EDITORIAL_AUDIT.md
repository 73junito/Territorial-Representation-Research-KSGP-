# Phase 2N — APA 7 Citation and Manuscript Editorial Audit

**Audit date:** November 21, 2026
**Decision:** GO for **source-linked academic draft and faculty review**; CONDITIONAL for final APA 7 compliance; NO-GO for final scholarly or committee publication.

## Scope and corrections

Phase 2N created **a new derivative manuscript**, `08_Final_Report/Phase2N_APA7_Cited_Academic_Manuscript_Review_Draft.md`, instead of overwriting the Phase 2M-D manuscript or any historical dataset.

The baseline manuscript contained a provisional bibliography but no consistently linked APA-style corporate-author citations in the body. The Phase 2N derivative adds in-text Census Bureau citations to study design, the three data families, the separate Tables 1–5, documented uncertainty and discussion. It retains source-field provenance alongside the citations; **a general Census product landing page is not evidence for every individual field**.

### Source/year crosswalk (editorial, provisional)

| In-text form | Reference/list product | Verification |
|---|---|---|
| U.S. Census Bureau (2020a) | 2019 ACS 1-year estimates | Official September 17, 2020 release: https://www.census.gov/newsroom/press-releases/2020/acs-1year.html |
| U.S. Census Bureau (2020b) | *Understanding and Using American Community Survey Data: What All Data Users Need to Know* | Official 2020 handbook listing: https://www.census.gov/programs-surveys/acs/library/handbooks/general.html |
| U.S. Census Bureau (2022a) | 2016–2020 ACS 5-year estimates | Official March 17, 2022 release: https://www.census.gov/newsroom/press-releases/2022/acs-5-year-estimates.html |
| U.S. Census Bureau (2022b) | Island Areas Demographic Profile technical documentation | Official directory timestamp October 20, 2022: https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/ — PDF title-page date **not independently audited** |
| U.S. Census Bureau (2022c) | 2020 Island Areas Demographic Profile data product | Official product page: https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html — exact publication metadata **provisional** |

**Suffix convention:** Same-author/same-year entries are alphabetized by source title, including the technical-document title before the alternate Island Areas product title. The year suffixes are internally consistent between in-text citations and the bibliography but may be revised if the exact underlying product publication dates/titles change during faculty bibliographic inspection. Release year and data-collection period must never be conflated.

## Integrity and editorial limitations

- Original Phase 2M-D manuscript preserved, with its prior numerical QA retained.
- All six 2020 jurisdiction populations, the 4,313,440 total, 32 product-specific socioeconomic observations, 12 Census percentage MOEs, two D.C. composite-count MOE calculations, and 14 graphics remain unchanged.
- Original Census, SPSS SAV/CSV/SPV, historical acceptance files, and figure files were not modified.
- The D.C./PR 2020 Census DHC datasets and the four Island Areas long-form Census files have separate original-file origins. The 2020 Island Areas citation must not be represented as covering all six DHC source records.
- Field-level proof relies on the project's original Census source manifests, raw records, archived official JSON and per-variable extraction records; the reference list names broader official source families.
- A Markdown manuscript is not by itself a fully formatted APA 7 submission. Faculty/editor verification remains needed for heading levels, running-page requirements if applicable, APA table/figure placement, caption/alt-text readability, and publication metadata.
- The old SAV hash difference remains **historically unresolved**. Full older-script portability remains conditional.
- No reviewer acceptance, university endorsement, political/party position, or external methodology approval is claimed.

## Acceptance matrix

| Item | Disposition |
|---|---|
| Five corporate-author source citations represented in reference list | INTERNAL QA PASS |
| Consistent 2020a/2020b and 2022a/2022b/2022c year-letter matching | INTERNAL QA PASS |
| Independent Census 2019 one-year and 2016–2020 five-year release dates | VERIFIED against official web notices |
| Island Areas technical-file directory date | VERIFIED directory metadata; PDF bibliographic year CONDITIONAL |
| All original numeric evidence / figure archival integrity | PREVIOUS PASS; recheck on commit |
| Accurate source scope (D.C./PR DHC not attributed solely to Island Areas) | CORRECTED |
| Faculty or institutional academic acceptance | PENDING |
| Complete APA 7 compliance and final source metadata | CONDITIONAL |
| Final academic/committee publication | NO-GO |

## Next acceptance gate

Send the faculty reviewer the [updated START HERE page](../../START_HERE_FOR_FACULTY_REVIEW.md) only if necessary; the research owner has already confirmed sending that link. The GitHub homepage should surface the Phase 2N cited draft as the current reading option, without sending further unsolicited messages. Maintain [Issue #3](https://github.com/73junito/Territorial-Representation-Research-KSGP-/issues/3) open for independent comments and bibliography signoff.

**Validator:** `python 06_Methodology/Phase2/validate_phase2n_apa7_editorial.py`.
