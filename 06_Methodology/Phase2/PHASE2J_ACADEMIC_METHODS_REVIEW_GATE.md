# TRR-PHASE2J — Academic Methods and Publication Acceptance Review

**Decision:** INTERNAL SOURCE/METHODOLOGY QA PASS WITH QUALIFICATIONS. EXTERNAL FACULTY REVIEW NOT YET PERFORMED. FINAL PUBLICATION NO-GO.

## What was verified in Phase 2J

1. Existing phase methods and integrated research reports were inspected read-only; original Phase 2F and Phase 2H reports remain intact, including their historical claims that profile-MOE verification had been pending.
2. 17 archived original Census source files matched the hashes in the original Phase 2D acquisition manifest. Five official Census reference links returned HTTP 200 during a limited source-availability test.
3. The primary Census site confirms the 2019 one-year estimates' release on September 17, 2020 and the 2016–2020 five-year estimates' release on March 17, 2022.
4. Phase 2I independently recovered the 12 published profile percentage MOEs using the `CENSUS_DATA_API` GitHub secret. Ten match earlier derived uncertainty at profile display precision. For the remaining two D.C. bachelor's+ measures, using the directly published composite count MOEs yields percentage MOEs that agree with published values after display rounding.
5. The two Phase 2F education approximations are not to be used as official Census profile MOEs. The exact survey replicate/covariance mechanism was not reconstructed.
6. The six-jurisdiction socioeconomic GO/CONDITIONAL/NO-GO gate is unchanged: source-family description GO; labeled side-by-side observation CONDITIONAL; unqualified six-way inference NO-GO.

## Mandatory methodology disclosure

- The four Island Areas (AS/GU/MP/VI) are from the 2020 long-form Island Areas Censuses; income/poverty refer to 2019. They are not 2019 ACS one-year observations.
- D.C. and Puerto Rico have separate 2019 one-year ACS/PRCS and pooled 2016–2020 five-year ACS/PRCS survey series.
- Educated population (25+), civilian labor force, households and poverty-status universe are **distinct denominators**; not all estimates refer to the whole jurisdiction population.
- Income dollar bases differ by source product, including five-year data adjusted to 2020 dollars.
- Guam military-housing/population exclusion caveats must follow any display that includes its metrics.
- D.C. is a federal district, not a territory; this study does not infer voting eligibility, political preference or causal/policy effects.
- A verified source value and an arithmetically reproduced confidence interval do not by themselves establish cross-product comparability.

## Historical evidence exception
The currently validated 6-by-15 age/sex .sav dataset reconciles to the canonical CSV by jurisdiction. The earlier and current SHA-256 hashes differ, and a historical binary/log sufficient to establish root cause was not found within the research workspace. **Historical byte-integrity signoff remains OPEN**, without invalidating verified descriptive record values.

## Reviewer checklist (must be independently completed)
- [ ] Research questions and scope distinguish D.C. from the five inhabited territories.
- [ ] Every variable cites product, source year, table code, universe and price base.
- [ ] Survey significance/MOE treatment is approved, including the direct composite-count method.
- [ ] Island Areas and ACS/PRCS source-product differences are clearly disclosed.
- [ ] APA 7 references and same-author/year suffixes checked from original title pages and agency metadata.
- [ ] Findings distinguish descriptive observation from statistical inference and political conclusions.
- [ ] The archived .sav historical byte-hash exception is disclosed to the reviewing faculty member.
- [ ] Faculty reviewer records an explicit PASS, CONDITIONAL, or REVISE with rationale and date.
- [ ] Any committee circulation, adoption or public release has separate documented authorization.

## Source package for reviewer
- `08_Final_Report/Phase2J_Faculty_Academic_Review_Draft.md`
- `06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md`
- `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md`
- `06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md`
- `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md`
- `09_Committee_Package/Phase2J_Committee_Review_Brief_Draft.md`

## Acceptance
**Faculty-review draft GO**. **Independent faculty decision PENDING**. **Final academic approval and public dissemination NO-GO** until approval is recorded. No person or institution is claimed to have reviewed or endorsed this research.
