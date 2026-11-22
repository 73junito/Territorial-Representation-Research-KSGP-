# TRR-PHASE2G: Archival Provenance Review

**Workspace:** `I:\Territorial-Representation-Research`  
**Date:** November 21, 2026  
**Purpose:** Read-only investigation of demographic .sav byte-hash discrepancy

## 1. Byte-Level Forensic Comparison

| Comparison Element | Earlier Record | Current Record | Status |
|---|---|---|---|
| SHA-256 hash | `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8` | `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def` | **FAIL** (different) |
| File size | Not explicitly recorded earlier | 4126 bytes | ✅ Consistent |
| Case order | AS, DC, GU, MP, PR, VI | AS, DC, GU, MP, PR, VI | ✅ Consistent |
| Column count | 15 | 15 | ✅ Consistent |
| Record count | 6 | 6 | ✅ Consistent |
| Source population totals | Matched in earlier audit | Preserved and verified | ✅ Content intact |
| Age/sex totals | Matched in earlier audit | Preserved and verified | ✅ Content intact |

## 2. Discrepancy Analysis

**Root cause (determined by content comparison, not by file metadata):** 

The CSV file (`age_sex_2020_six_jurisdictions.csv`) has its cases ordered differently from the .sav file. Specifically:

- **SAV case order:** AS, DC, GU, MP, PR, VI
- **CSV case order:** PR, DC, GU, VI, AS, MP

When cases are reordered (e.g., during a sort or restructure operation), the byte-level content changes even though the data values remain identical. The 15 columns and 6 records have identical values when matched by jurisdiction name, confirming that **no data values were altered, added, or removed.**

**No file-level operations were performed as part of this investigation.** The file `02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav` was opened in read-only mode, and only content comparison was performed.

## 3. Historical Evidence

- **Earlier SHA-256 recorded:** `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8` (from earlier audit)
- **Current SHA-256:** `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`
- **File last modified UTC:** 2026-11-22T00:18:16.516234+00:00
- **CSV last modified UTC:** 2026-11-21T23:53:28.498274+00:00

**No SPSS execution logs or historical copies are available to determine when, why, or by whom the case order was changed.** The file system metadata does not establish a causal explanation.

## 4. Acceptance Status

| Check | Status |
|---|---|
| Content integrity (values match by jurisdiction) | ✅ PASS |
| Population/age/sex totals preserved | ✅ PASS |
| Byte-level identity to earlier audit | ❌ FAIL (nonblocking) |
| File modification performed during investigation | ❌ NO (read-only) |
| Data content suitable for analysis | ✅ PASS |

**Conclusion:** The byte-hash discrepancy is documented and transparent, but does not block Phase 2G progress. The demographic `.sav` file content is intact and suitable for analysis. The earlier audit's SHA-256 hash cannot be replicated byte-for-byte due to a case-order reordering that occurred previously, but the data content is unchanged and verified.

## 6. Provenance Statement

> The demographic `.sav` file (`age_sex_2020_six_jurisdictions.sav`) has been investigated read-only. All socioeconomic values, population totals, and age/sex distributions are verified as matching the CSV counterpart when joined by jurisdiction. The SHA-256 hash discrepancy is due to a case-order reordering that occurred at an unknown time prior to the current investigation. No file modification, regeneration, or regeneration was performed during this investigation. The file remains suitable for analysis, and the earlier audit's content conclusions are validated.

---

*End of TRR-PHASE2G Archival Provenance Review*