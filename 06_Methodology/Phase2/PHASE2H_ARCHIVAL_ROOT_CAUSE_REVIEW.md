# TRR-PHASE2H — Read-Only Demographic SAV Byte-Hash Root-Cause Review

**Status:** CONTENT VERIFIED; BYTE-HASH DIFFERENCE CONFIRMED; ROOT CAUSE **UNRESOLVABLE WITH CURRENT EVIDENCE**.

## Evidence
- Prior recorded SHA-256: `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`.
- Current recorded SHA-256: `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`.
- Current .sav is 4,126 bytes with six cases and 15 columns. Current case order: AS, DC, GU, MP, PR, VI. CSV case order: PR, DC, GU, VI, AS, MP.
- After aligning by `geo_code`, all 15 data fields across all six jurisdictions reconcile; numerical data-content integrity PASS. **Byte-level historical continuity FAIL**.
- Workspace-scoped read-only file search found one `age_sex_2020_six_jurisdictions.sav` and no historical version/backup of that specific file. No historical binary is available for byte-level diff.
- Both `03_SPSS_Syntax/Phase2/01_age_sex_2020_descriptive.sps` and `02_age_sex_2020_run_and_save.sps` contain `SORT CASES BY geo_code (A)`, but neither executes `SAVE OUTFILE` of the .sav. The latter saves only the .spv. Sorting an in-memory SPSS dataset does not itself prove that the underlying file was overwritten.
- Prior forensic report documented SPSS file creation datetime 2026-11-21 18:18:16 and filesystem modification UTC 2026-11-22T00:18:16.516234+00:00, which corresponds to the same moment in America/Chicago. The timestamps support time of this file's recorded save, but do not identify the prior file operation or actor.

## Assessment
The changed case order is a **possible contributor** to byte differences but is not evidence of a confirmed historical re-save operation. Other SPSS file metadata and file-serialization differences can also change hashes. No matching older binary, system activity log, or verified provenance chain is present in the available project. Therefore, no causal determination is supportable; **do not say "hash changed because the cases were reordered."**

## Required disposition
Leave the existing .sav and .csv untouched. Preserve both hashes, the successful per-jurisdiction content test, and this limitation. Additional read-only inspection of an authorized historical backup/OneDrive/File History snapshot or version-control record is permissible only when evidence becomes available. Historical byte-preservation signoff remains OPEN and is separate from validated analytical content.
