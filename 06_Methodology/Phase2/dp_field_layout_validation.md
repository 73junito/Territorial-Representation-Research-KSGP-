# TRR-PHASE2C: DP File Layout Validation Key Findings

**Workspace:** `I:\Territorial-Representation-Research`  
**Date:** November 21, 2026

## Summary

- **4 Island Areas DP files analyzed** (AS, GU, MP, VI)
- **Population at position 6 verified** for all jurisdictions
- **All 4 target variables extract same raw value** without layout validation
- **Census technical documentation required** for field-to-variable mapping

## DP File Summary

| Jurisdiction | DP File | Summary Fields | Population (pos 6) |
|---|---|---|---|
| American Samoa | `as000012020.dp` | 23,959 | 49,710 |
| Guam | `gu000012020.dp` | 19,672 | 153,836 |
| Northern Mariana Islands | `mp000012020.dp` | 98,115 | 47,329 |
| U.S. Virgin Islands | `vi000012020.dp` | 289,722 | 87,146 |

## Critical Finding

All four target socioeconomic variables (education DP2_0016P, unemployment DP3_0009C, median income DP3_0104C, poverty DP3_0151P) currently extract the **same raw value** at position 6. This proves that **field position mapping requires official Census technical-layout documentation**.

## Next Step

Obtain `2020-iac-dpsf-technical-documentation.pdf` from Census Bureau to map field positions to variable IDs.

## Related Files

- `06_Methodology/Phase2/extract_island_values.py` — Reproducible extraction script
- `06_Methodology/Phase2/TRR_PHASE2C_COMPLETION_REPORT.md` — Phase 2C completion report
- `01_Government_Sources/Phase2_Socioeconomic/socioeconomic_harmonization_matrix.csv` — Updated with extraction status