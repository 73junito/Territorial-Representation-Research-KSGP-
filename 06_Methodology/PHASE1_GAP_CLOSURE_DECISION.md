# Phase 1 — Gap Closure Decision Record
Date: 2026-11-21
Scope: five permanently inhabited U.S. territories plus Washington, D.C.

## Reconciliation status
**Statistical/data-provenance acceptance: PASS.** Phase 1 descriptive findings can be reproduced from original Census Bureau downloadable tables and matching .sav data. The 2010 and 2020 totals are 4,702,677 and 4,313,440, net -389,237 (-8.28%).

## Closed gaps
1. **Official sources archived.** Archived four Census Bureau 2020 Island Areas Population and Housing Unit Counts Table 01 CSV files (GU, VI, AS, MP). Also archived Census Bureau 2020 Apportionment Table E XLSX for PR and D.C. and four supporting Census Bureau island-area press releases as HTML.
2. **Source checksums recorded.** 01_Government_Sources/archive_manifest.csv and official_tables_manifest.csv each contain URL, local archive path, SHA-256, and verification status. The executable verification script checks all source hashes and source population values.
3. **Official-source numeric reconciliation.** 2010 and 2020 counts for every jurisdiction were checked in the archived machine-readable originals against the project dataset.
4. **SPSS output inspected.** 04_SPSS_Output/01_population_comparison.spv records all six rows, population differences and percentages, and the SAVE file contention warning.
5. **Duplicate explained.** SPSS created 02_SPSS_Data/population_2010_2021.sav when its primary .sav was in use. Both files have the same six rows and ten variables, including 2010 and 2020 (not 2021) counts. The duplicate was retained for evidence; it is not a separate time series.
6. **Avoiding future contention.** 03_SPSS_Syntax/02_population_review_readonly.sps contains only non-saving SPSS procedures. Prefer this script for reruns. 01_population_comparison.sps is historical and has a SAVE OUTFILE line; do not rerun it with the primary .sav opened.
7. **Validation rerun.** 06_Methodology/verify_gap_closure.py finished successfully with all checks. The SPSS dataset was not modified or overwritten during closure.

## Remaining controls (not research gaps)
- Do not delete or rename population_2010_2021.sav while SPSS may be open. It may be removed later only after checking open sessions and obtaining explicit file-cleanup authorization.
- The original source_register.csv preserves historical QuickFacts links (which returned HTTP 403 to automated archiving). The authoritative local downloadable evidence is listed in archive_manifest.csv and official_tables_manifest.csv.
- Machine-readable island tables are official 2020 PHC Table 01 files; this does not yet verify equivalence of the detailed social and economic tables, which belong to Phase 2.
- The zero congressional voting-membership variables are institutional descriptors, not survey findings or voter counts. Resident population is not eligible voter population.
- The SPSS descriptives and row output were inspected; independent arithmetic revalidation does not replace a separate visual review of every SPSS pivot table cell.

## Phase transition gate
Phase 1 population counts, supporting government originals, statistical output, documentation and file-preservation conditions are complete. No Phase 2 source collection or statistical comparison is authorized by this record.
