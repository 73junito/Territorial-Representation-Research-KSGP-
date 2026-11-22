# TRR-PHASE2G — Corrective Acceptance Addendum
Date: November 21, 2026
Workspace: I:\Territorial-Representation-Research

## Purpose
This addendum preserves the three Phase 2G source documents while correcting unsupported completion claims and preventing Phase 2F work from being repeated.

## Findings confirmed from live file inspection
1. `PHASE2G_PUBLISHED_MOE_RECONCILIATION.md` contains an **archival provenance review**, not a table-by-table independent reconciliation against published ACS/PRCS profile or subject-table percentage MOEs. It substantially duplicates `PHASE2G_ARCHIVAL_PROVENANCE_REVIEW.md`. The published-MOE comparison remains **PENDING**.
2. `PHASE2G_METHODS_ACCEPTANCE.md` incorrectly asserts derived-rate MOEs "not yet calculated" and recommends returning to Phase 2F. This is stale. Phase 2F already computed the 12 approximate derived 90% percentage MOEs in `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv`. Its `validate_phase2f_research.py` independently verified the formulas and intervals. A **published-source reconciliation**, not repeat calculation, is outstanding.
3. `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md` exists and contains the integrated report. Phase 2G should create a review-facing derivative, not restart Phase 2F.
4. The demographic SAV record contents match the canonical CSV when aligned by `geo_code`, but the earlier SAV SHA-256 `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8` differs from current `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`. The changed case order is evidence consistent with re-saving, not proof of root cause. Historical byte integrity remains OPEN.

## Revised Phase 2G gates
| Gate | Decision | Basis |
|---|---|---|
| 32 Census-sourced, source-specific socioeconomic observations | GO | Phase 2D archive/extraction validation |
| 80 ACS/PRCS component estimate/MOE records | GO | Phase 2D source and validator |
| 12 approximate derived 90% percentage intervals | GO for explicitly labeled *method-derived approximations* | Phase 2F formulas independently recomputed |
| Four directly published median-household-income 90% MOEs/intervals | GO, source-specific | ACS/PRCS Summary File tables |
| Independent validation against published ACS/PRCS *profile* percentage MOEs | PENDING | Not established by a duplicate archival report |
| Cross-six unqualified socioeconomic hypothesis testing | NO-GO | Different source products, periods, universes |
| Demographic .sav content continuity | PASS | CSV/SAV matched by geo_code |
| Demographic .sav historical byte identity | OPEN exception | Different SHA-256; cause unknown |
| Academic review and committee dissemination | CONDITIONAL DRAFT ONLY | Subject to independent methodological and reference review |

## Accuracy corrections to prior status
- The four published median-income confidence intervals represent **2 jurisdictions × 2 products = 4**, not eight.
- The 12 calculated percentage intervals are **derived, approximate 90% intervals**. They are not independently matched to official published profile MOEs.
- A created document does not by itself constitute source-reconciliation completion or academic signoff.
- Phase 2F is already complete as a calculation/report-integration stage; do not route work backward to it.

## Next acceptance requirements
A. Retrieve official 2019 one-year and 2016–2020 five-year ACS/PRCS **Data Profile/Subject** percentage estimates and MOEs for education, unemployment and poverty. Map their definitions to the Detailed Table counts, compute percentage-point deltas, document applicable rounding and universe differences, and record PASS, CONDITIONAL or UNAVAILABLE for each of 12 cross-checks. Do not substitute previously derived rates as independent sources.
B. Independently review the draft report and committee brief for sources, definitions, uncertainty labels, nonpartisan neutrality, and limitations.
C. Seek archived SAV historical version or operation logs only if available without file modification; otherwise preserve the exception.

**Decision:** Phase 2G evidence preparation may continue, but full published-MOE reconciliation and final academic/committee signoff are **NOT YET COMPLETE**.
