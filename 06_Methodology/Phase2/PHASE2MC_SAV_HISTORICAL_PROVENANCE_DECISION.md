# TRR Phase 2M-C — SPSS SAV Historical Provenance Audit and Owner Decision Packet

**Audit date:** November 21, 2026 (America/Chicago)
**Workspace scope:** `I:\Territorial-Representation-Research`
**Decision:** **CONTENT INTEGRITY PASS; CURRENT GIT BYTE INTEGRITY PASS; HISTORICAL BYTE CONTINUITY UNRESOLVED WITH AVAILABLE EVIDENCE.** Issue #2 remains OPEN.

## Protected file and documented evidence

Target: `02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.sav`

| Evidence | Observed |
|---|---|
| Earlier recorded SAV SHA-256 | `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8` |
| Current verified SAV SHA-256 | `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def` |
| Current file size | 4,126 bytes |
| Current Git-tracked SAV SHA-256 | `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def` |
| Git blob vs working copy | **BYTE-FOR-BYTE IDENTICAL** |
| Git commit history for this path | **One commit:** `ee2a1867d7cbce3bd0fcef28849c26de46d88381` |
| Original earlier-hash bytes present in the examined Git path history | **NO** |
| Exact earlier SHA-256 among workspace SAV/archival filename candidates | **NO** |
| Matching canonical CSV | Six cases, 15 columns; six jurisdictions, population 4,313,440 |
| Previously completed SAV-vs-CSV comparison | All 6-by-15 fields match keyed by `geo_code` per Phase 2F archived report |
| Historical SAV reconstruction | **NOT PERFORMED** |

## Read-only scope and findings

The procedure rehashed the current SAV file and compared its entire 4,126 bytes against the Git-tracked version, rather than treating Git's internal object identifier as a file SHA-256. The Git path was introduced at the initial repository archive commit; the earlier recorded hash predates the available Git history, so `git log` cannot establish its source or content.

The search was constrained to authorized files under the research repository. Two `.sav` files were found: `02_SPSS_Data/population_2010_2020.sav` (2,088 bytes; a **different** dataset), and the target Phase 2 SAV. Neither matches the previously recorded SAV SHA-256. No matching historical binary or archive version of the target was found in the examined repository candidates. Existing Phase 2D/2F/2G/2H reports and script references repeat the earlier checksum but do not contain its bytes.

The Phase 2F audit established that the current SAV and CSV contain equivalent values by jurisdiction even though SAV case order `AS, DC, GU, MP, PR, VI` differs from CSV case order `PR, DC, GU, VI, AS, MP`. The SPSS syntax includes in-memory sorting but does not save the SAV as shown in Phase 2H. **That case-order difference is not proof of a particular edit or save event.**

No evidence of who, what operation, or why the historical byte change occurred was recovered. A specific causal explanation **must not** be asserted.

## Preservation assurance and missing evidence

No SAV, CSV, SPV, archived Census source, SPSS syntax, or historical forensic acceptance file was rewritten, reordered, regenerated, restored, or deleted. Read-only data checks were run without launching SPSS. Git commits contain only new methodology and audit documentation.

A future investigation can proceed **only** with an identified, authorized historical backup, Windows File History/version record, archived disk snapshot, or SPSS execution log. Such evidence was not present within the examined repository. Do not assume it does not exist elsewhere.

If a historical binary becomes available:
1. Preserve source location, original times, and a SHA-256 inventory without modification.
2. Verify that the historic candidate matches the earlier recorded SHA-256 **exactly**.
3. Compare both binaries read-only, including SPSS dictionary/metadata and case ordering.
4. Seek corroborating activity logs before attributing a specific edit operation or actor.
5. Record supported conclusions separately; never overwrite the validated current SAV to recreate an old checksum.

## GO / CONDITIONAL / NO-GO

- **GO:** Retain and cite the current source-specific descriptive analysis. Content reconciliation remains valid in the archived Phase 2F comparison.
- **GO:** Current `.sav` working file is identical to the version in the Git research archive, from initial commit onward.
- **CONDITIONAL:** Historical preservation claims must carry both hashes and the unresolved cause; report source content validity separately from historic byte identity.
- **OPEN:** Historical earlier-hash binary recovery, causal reconstruction and independent academic review.
- **NO-GO:** Claiming the earlier and current bytes match, attributing the discrepancy to a sort operation without logs, modifying the current SAV, or declaring final publication approved.

**Reproducibility:** `06_Methodology/Phase2/validate_phase2mc_sav_provenance_readonly.py`.
**Historical reports preserved:** `PHASE2F_SAV_HASH_FORENSIC.md`, `PHASE2H_ARCHIVAL_ROOT_CAUSE_REVIEW.md`.
