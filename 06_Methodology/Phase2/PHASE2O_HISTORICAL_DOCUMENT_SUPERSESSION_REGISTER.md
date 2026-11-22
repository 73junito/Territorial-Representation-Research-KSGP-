# TRR-PHASE2O: Historical Document Supersession Register

**Workspace:** `I:\Territorial-Representation-Research`  
**Date:** November 21, 2026  
**Purpose:** Catalog of historical Phase 2G documents with the evidence-supported current findings that supersede them.

## Register of Historical Phase 2G Documents

| # | Document | Historical phase | Problem | Corrected finding | Authoritative source | Classification | Action |
|---|---|---|---|---|---|---|---|
| 1 | `06_Methodology/Phase2/PHASE2G_METHODS_ACCEPTANCE.md` | Phase 2G | States the 12 derived percentage MOEs were "not yet calculated" and recommends returning to Phase 2F | All 12 derived 90% percentage MOEs were calculated and independently recomputed in Phase 2F (`02_SPSS_Data/Phase2/phase2f_prdc_derived_rate_moe90.csv`) | `validate_phase2f_research.py`; `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md` | Superseded | Preserve original unchanged; supersession documented in this register |
| 2 | `06_Methodology/Phase2/PHASE2G_PUBLISHED_MOE_RECONCILIATION.md` | Phase 2G | Filename promises table-by-table published-MOE reconciliation but the body is a duplicated archival provenance review; independent reconciliation was still pending at that time | All 12 published Census profile percentage MOEs were numerically reconciled in Phase 2I; two D.C. education MOEs reconciled using directly published composite-count MOEs | `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md`; `PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv` | Superseded | Preserve original unchanged; supersession documented in this register |
| 3 | `06_Methodology/Phase2/PHASE2G_ARCHIVAL_PROVENANCE_REVIEW.md` | Phase 2G | Attributes the SAV byte-hash difference to case reordering without proving the cause | The SAV byte-hash difference is confirmed, but its specific cause remains unresolved; case order difference is an observation, not a proven cause | `06_Methodology/Phase2/PHASE2MC_SAV_HISTORICAL_PROVENANCE_DECISION.md` | Superseded in part | Preserve original unchanged; supersession documented in this register |
| 4 | `08_Final_Report/Phase2G_Academic_Research_Review_Draft.md` | Phase 2G | Describes independently published percentage-MOE verification as pending | Published profile-MOE verification was completed in Phase 2I | `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md` | Superseded | Preserve original unchanged; supersession documented in this register |
| 5 | `09_Committee_Package/Phase2G_Research_Brief_Draft.md` | Phase 2G | Describes published-MOE cross-checks as pending | Published profile-MOE cross-checks were completed in Phase 2I | `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md` | Superseded | Preserve original unchanged; supersession documented in this register |
| 6 | `06_Methodology/Phase2/PHASE2G_CORRECTIVE_ACCEPTANCE_ADDENDUM.md` | Phase 2G (corrective) | Correctly identifies several Phase 2G errors, but itself notes the published-MOE reconciliation was still pending at that time | The addendum's identified problems are accurate for its time; the pending reconciliation is now resolved by Phase 2I | `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md` | Historical (accurate for its time) | Preserve as-is |

## Classification legend

| Classification | Meaning |
|---|---|
| **Historical** | Document from an earlier phase; accurate when written; retained for the audit trail |
| **Superseded** | Contains outdated or unsupported conclusions since corrected by a later phase |
| **Current** | Reflects the latest evidence-supported findings |

## Action legend

| Action | Meaning |
|---|---|
| **Preserve original unchanged; supersession documented in this register** | Retain original wording unchanged; this register is the correction mechanism (no in-file notices were added) |
| **Preserve as-is** | Leave unchanged; the document is accurate for its time or must not be altered for integrity reasons |

## Authoritative findings that govern supersession

1. All 12 derived 90% percentage MOEs were calculated in **Phase 2F**.
2. All 12 targeted published Census profile percentage MOEs were numerically reconciled in **Phase 2I**.
3. Two D.C. education MOE discrepancies were reconciled using directly published composite-count MOEs (Phase 2I).
4. The historical `.sav` byte-hash difference is confirmed; its cause remains **unresolved** (Phase 2M-C).
5. The five inhabited U.S. territories and Washington, D.C. remain correctly classified; D.C. is a federal district, not a territory.
6. Unqualified pooled six-jurisdiction socioeconomic inferential comparisons remain **NO-GO**.
7. External faculty methodology approval remains **pending**.

---

*End of TRR-PHASE2O Historical Document Supersession Register*