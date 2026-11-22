# Territorial Representation Research

A source-linked research repository examining demographic data and the limits of socioeconomic comparison for **Puerto Rico, Guam, American Samoa, the U.S. Virgin Islands, the Northern Mariana Islands, and Washington, D.C.** Washington, D.C. is a federal district, not a U.S. territory.

> **Research status: conditional academic and committee review drafts, not approved publication.** Repository naming does not establish endorsement by the Kansas Green Party or its committees.

## Evidence and acceptance gates

| Work | Evidence | Status |
|---|---|---|
| Population and age/sex (2010–2020) | Six jurisdictions; 2020 population total 4,313,440; SPSS pilot | Descriptive content PASS; historical SAV byte-hash discrepancy OPEN |
| Source-specific socioeconomics | 32 observations from four Island Areas 2020 Census profiles plus PR/DC 2019 ACS/PRCS one-year and 2016–2020 five-year | Descriptive GO; unqualified six-way inference NO-GO |
| Survey uncertainty | 80 estimate/MOE components; 4 directly published income intervals; 12 calculated approximate percentage intervals | Derived computations PASS; **published-profile MOE reconciliation 12/12 numerically accounted for (Phase 2I); exact covariance mechanism not reconstructed** |
| Academic and committee review | Phase 2G/2H methodological reports and review drafts | External reviewer approval PENDING; final publication NO-GO |

## Read first

- [Phase 2J faculty academic-review draft](08_Final_Report/Phase2J_Faculty_Academic_Review_Draft.md)
- [Phase 2J source and provisional APA reference audit](06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md)
- [Integrated descriptive report](08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md)
- [Source-specific evidence appendix](08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md)
- [Phase 2H acceptance decision](06_Methodology/Phase2/PHASE2H_ACCEPTANCE_DECISION.md)
- [Phase 2I published-MOE reconciliation and D.C. education variance diagnosis](06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md)
- [Historical Phase 2H acquisition-blocked record](06_Methodology/Phase2/PHASE2H_PUBLISHED_MOE_RECONCILIATION.md)
- [Historical SPSS file preservation review](06_Methodology/Phase2/PHASE2H_ARCHIVAL_ROOT_CAUSE_REVIEW.md)
- [Committee draft](09_Committee_Package/Phase2H_Committee_Research_Brief_Review_Draft.md)

## Repository layout

| Directory | Contents |
|---|---|
| 01_Government_Sources | Census original source archives, manifests, technical documentation |
| 02_SPSS_Data | Source-specific extracts, SAV data, estimate/MOE components |
| 03_SPSS_Syntax and 04_SPSS_Output | SPSS analysis syntax and Viewer evidence |
| 05_Statistical_Graphics | Descriptive figures |
| 06_Methodology | Extraction, validation, uncertainty calculations, acceptance decisions |
| 07_Policy_Analysis | Reserved for separately grounded analysis |
| 08_Final_Report | Working research reports and academic review drafts |
| 09_Committee_Package | Committee **review drafts**, not endorsements |

## Reproduce and audit

Original local workspace: I:\Territorial-Representation-Research. Original environment: Windows, Python 3.14, IBM SPSS Statistics 31. Some scripts contain hard-coded I: paths and are not portable without modification. Review [REPRODUCIBILITY.md](REPRODUCIBILITY.md), [DATA_PROVENANCE.md](DATA_PROVENANCE.md) and [CITATION.md](CITATION.md) before running scripts or citing data.

The two largest official original ZIPs, PR_2020_DHC_original.zip (~136.7 MB) and DC_2020_DHC_original.zip (~13.6 MB), remain local and are Git-ignored. Re-fetch from the official Census sources and validate against the recorded manifests when full historical reproduction requires them.

**Research limits:** Four Island Areas use 2020 Census profile data with income/poverty referring to 2019; PR/DC use distinct 2019 one-year and 2016–2020 five-year ACS/PRCS estimates. Denominators, source designs, exclusions, price bases and time periods differ. No unqualified pooled six-way socioeconomic ranks, p-values, or causal/political conclusions are authorized.
