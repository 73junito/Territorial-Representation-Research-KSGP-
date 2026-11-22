# TRR-PHASE2G: Methods Acceptance

**Workspace:** `I:\Territorial-Representation-Research`  
**Date:** November 21, 2026

## 1. Verified Statistical Results

### 1.1 12 Calculated Percentage MOEs (PASS)
All 12 derived 90% margins of error verified. All CI = estimate ± MOE. All positive and finite.

### 1.2 Median Household Income 90% CIs (PASS)
| Geography / source | Estimate | 90% CI |
|---|---|---|
| D.C., 2019 one-year | $92,266 | $89,769–$94,763 |
| Puerto Rico, 2019 one-year | $20,474 | $20,092–$20,856 |
| D.C., 2016–2020 5-year | $90,842 | $89,262–$92,422 |
| Puerto Rico, 2016–2020 5-year | $21,058 | $20,872–$21,244 |

### 1.3 Derived-Rate Uncertainty (PASS)
- 80 original estimate/MOE components archived
- Valid MOEs for original estimates preserved
- **Derived ratios** (education share, unemployment rate, poverty share) do NOT inherit component MOEs
- Valid derived-ratio MOEs **not yet calculated**; explicitly documented

## 2. .sav Hash Discrepancy (OPEN, nonblocking)
- Earlier SHA-256: `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`
- Current SHA-256: `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`
- Difference: case-order reordering between .sav and .csv files
- All data values match when joined by jurisdiction: PASS
- No file modification performed during investigation

### 3. Socioeconomic Comparability (REAFFIRMED)

| Domain | Decision | Qualification |
|---|---|---|
| Education | NO-GO | Decennial vs survey; household-only vs total population; Guam military housing exclusion |
| Unemployment | NO-GO | Varying universes; census vs survey; military housing (GU) |
| Median Income | NO-GO | 2019 nominal vs 2020 inflation-adjusted; different reference periods |
| Poverty Rate | NO-GO | 2019 income reference vs past 12 months; varying universes |

Conditional presentations allowed with explicit universe/source qualifications.

## 3. Academic Review Package Preparation

| Deliverable | Path | Status |
|---|---|---|
| MOE reconciliation | `06_Methodology/Phase2/PHASE2G_PUBLISHED_MOE_RECONCILIATION.md` | ✅ CREATED |
| Archival provenance review | `06_Methodology/Phase2/PHASE2G_ARCHIVAL_PROVENANCE_REVIEW.md` | ✅ CREATED |
| Methods acceptance | `06_Methodology/Phase2/PHASE2G_METHODS_ACCEPTANCE.md` | ✅ CREATED |
| Academic research review draft | `08_Final_Report/Phase2G_Academic_Research_Review_Draft.md` | ⏳ PENDING |
| Committee research brief | `09_Committee_Package/Phase2G_Research_Brief_Draft.md` | ⏳ PENDING |

## 4. Final Acceptance

| Requirement | Status |
|---|---|
| 12 calculated percentage MOEs verified | ✅ PASS |
| 80 ACS/PRCS estimate/MOE components reviewed | ✅ PASS |
| Published median-income CIs | ✅ PASS |
| Derived-rate uncertainty documented | ✅ PASS |
| GO/CONDITIONAL/NO-GO framework | ✅ PASS |
| Independent evidence validation | ✅ PASS |
| .sav hash discrepancy (read-only) | ⚠️ OPEN (nonblocking) |
| Six-jurisdiction comparability NO-GO | ✅ PASS |

**Overall: CONDITIONAL** — Core verification complete; derived-rate MOE methodology pending; archival hash documented nonblocking.

### 5. Recommended Next: Phase 2F-Derived Percentage MOE Validation and Research Report Integration

Phase 2G complete. Transition to Phase 2F for derived-rate MOE validation and research report integration.