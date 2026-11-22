# TRR-PHASE2F — Acceptance and Research Review Packet

**Date:** November 21, 2026  
**Workspace:** `I:\Territorial-Representation-Research`  
**Decision:** **PHASE2F METHODS & INTEGRATION — PASS WITH PENDING QUALIFICATIONS**.

## Work performed and validated

| Gate | Status | Evidence |
|---|---|---|
| 12 derived ACS/PRCS percent 90% MOEs and intervals | PASS (approximations) | `02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv` |
| Independent formula recalculation against source MOE components | PASS | `06_Methodology/Phase2/validate_phase2f_research.py` |
| Census subset-proportion and numerator sum approach | DOCUMENTED | U.S. Census Bureau, 2020 ACS Data Users Handbook, Chapter 8 |
| Integrated demographic/socioeconomic research report | CREATED | `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md` |
| Existing original Census source archives | PRESERVED | Phase 2D source manifest |
| Existing age-and-sex .sav values versus CSV | PASS, aligned by jurisdiction | `06_Methodology/Phase2/PHASE2F_SAV_HASH_FORENSIC.md` |
| Historic .sav byte-hash integrity | OPEN EXCEPTION | Older and current SHA-256 differ |
| Independently verified published survey-profile ratio MOEs | PENDING | No official profile values used as external cross-check |
| Unqualified six-jurisdiction inferential tests | NO-GO | Mixed survey/census universe/time design |

## Confidence-interval status
All calculated intervals use **90%** ACS/PRCS source MOE convention. Twelve percentage intervals were derived with the official proportion formula for subset numerator/denominator, with quadrature MOE for educational attainment numerator sum. They remain **derived approximations**, not original published profile MOEs. Four directly published median-income MOEs were already accepted in Phase 2E. ACS 2019 one-year and ACS 2016–2020 five-year products remain distinct; no conversion into six-way comparable statistics is authorized.

## Read-only preservation exception
SAV historical SHA-256: `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`. Current SHA-256: `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`. Six source geography rows and all 15 fields match by geo_code when the current SAV is compared with its source CSV. The file's case order differs and it has a recorded SPSS creation timestamp of November 21, 2026 18:18:16, but this does not prove exactly what caused the change. No recovery or mutation was authorized or performed.

## Final permissions
- **GO:** Source-specific evidence report, 2010–2020 demographic context, separate 2020 Island Areas socioeconomics, and distinct 2019/2016–2020 ACS/PRCS summaries with explicit caveats.
- **CONDITIONAL:** Publish derived percentage 90% MOEs only when labeled as approximate and independently cross-checked against official published profiles or another accepted statistical method.
- **NO-GO:** Combining six socioeconomics as interchangeable cases for hypothesis testing, p-values, significance, standardized ranking or causal/political conclusions.
- **PENDING:** Final archival byte-integrity signoff until earlier SAV version provenance is reconciled.

## Next academic review step
Obtain/cross-check profile or subject table rate MOEs for each ACS/PRCS estimate, record any discrepancies and their causes; seek methodology review for denominator universe alignment; examine historical SPSS logs or backups for saved-version provenance. Only then consider the final committee-facing narrative.
