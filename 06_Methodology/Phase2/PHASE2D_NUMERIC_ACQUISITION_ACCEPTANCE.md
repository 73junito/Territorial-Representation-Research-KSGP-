# TRR-PHASE2D — Official Numerical Acquisition and Verification
Date: November 21, 2026
Workspace: I:\Territorial-Representation-Research

## Acceptance decision
**NUMERICAL ACQUISITION: PASS, for the three distinct source series listed here.**
**SIX-JURISDICTION UNQUALIFIED SOCIOECONOMIC COMPARABILITY: NO-GO.**
**Demographic .sav preservation audit: CONTENT PASS / PRIOR BYTE-HASH MISMATCH (investigation warranted).**

This report supersedes the earlier live acquisition block for the specific source series now archived. Earlier API requests returned `missing_key.html`; alternate official Census bulk downloads succeeded. The API itself remains unavailable in that environment.

## Sources archived
- The original U.S. Census 2020 Island Areas Demographic Profile Technical Documentation PDF and all four official, geography-specific table-matrix workbooks.
- The four previously archived 2020 Island Areas Profile ZIPs: AS, GU, MP, VI.
- The original official **2019 ACS/PRCS one-year Summary Files** for PR and DC, plus the Census table-sequence templates.
- The original official **2016–2020 ACS/PRCS five-year** sequence-specific ZIPs (sequences 0042, 0047, 0058, 0078 for each of PR and DC), plus the Census sequence templates.
- File names, official URLs, byte counts and SHA-256 hashes are recorded in `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`.

## Extraction mechanics
The 2020 Island Areas Census original files are pipe-delimited with five linking fields per row: FILEID, STUSAB, CHARITER, CIFSN (segment) and LOGRECNO. We selected the island-wide `LOGRECNO=0000001` record for each file, and mapped data fields using the published per-area table matrix and the correct segment. All four segment lengths were checked against the number of matrix cells. One published U.S. Virgin Islands matrix row (`DPVI0860001`) has a segment-column discrepancy; the correct segment assignment 03 was used and segment record dimensions reconciled. The correction is implemented explicitly in the reproducible extraction script.

Island Areas source table references:
- Bachelor's degree or higher: `DPxx0200001` (percent, directly published).
- Civilian unemployment rate: `DPxx0510001` (percent, directly published).
- Median household income 2019: `DPxx0630001` (2019 dollars, directly published).
- Poverty rate: `100 × DPxx0900002 / DPxx0900001` (derived from below-poverty count and all persons for whom poverty status was determined). No total-resident population denominator was used.

The ACS/PRCS Summary Files' geography rows use state summary level 040 and `LOGRECNO=0000001`, with official template workbooks determining the sequence numbers and cell positions for the 2019 one-year and 2016–2020 five-year products separately. Estimates and original published component 90% MOEs are both preserved. Table identifiers:
- Education: `B15003_001`, `B15003_022`–`B15003_025` (derived bachelor's degree or higher share of population 25+).
- Unemployment: `B23025_005/B23025_003 × 100` (civilian unemployment share).
- Median household income: `B19013_001` (published estimate and directly published MOE).
- Poverty: `B17001_002/B17001_001 × 100` (population below poverty / persons whose poverty status was determined).

**MOE caution:** For bachelor's degree share, unemployment and poverty, the derived ratio has no directly published MOE in the extracted Summary File; corresponding source component MOEs are retained in separate 40-row-per-period component files. DO NOT treat a component MOE as the MOE of the derived ratio. For median household income, the directly published table MOE is included. Derived ratio uncertainty requires appropriate ACS variance formulas, accounting for numerator/denominator dependence, or direct published profile MOEs acquired separately.

## Source-specific observations

| Geography | Product | Bachelor's+ | Civilian unemployment | Median household income | Poverty |
|---|---|---:|---:|---:|---:|
| AS | 2020 Island Areas Census (income/poverty 2019) | 13.3% | 13.2% | $28,352 | 54.5912% |
| GU | 2020 Island Areas Census (income/poverty 2019) | 25.3% | 10.2% | $58,289 | 20.2057% |
| MP | 2020 Island Areas Census (income/poverty 2019) | 21.0% | 14.1% | $31,362 | 38.0057% |
| VI | 2020 Island Areas Census (income/poverty 2019) | 22.3% | 9.7% | $40,408 | 22.8134% |
| DC | 2019 ACS one-year (2019 dollars) | 59.6718% | 6.2638% | $92,266 | 13.4515% |
| PR | 2019 PRCS one-year (2019 dollars) | 27.2221% | 14.1053% | $20,474 | 43.4710% |
| DC | 2016–2020 ACS five-year (2020 dollars) | 59.7576% | 7.1196% | $90,842 | 15.4525% |
| PR | 2016–2020 PRCS five-year (2020 dollars) | 26.6719% | 15.0735% | $21,058 | 43.4075% |

These lines are **source-specific descriptive observations**, not a normalized comparative ranking; do not pool or run omnibus tests. Differences in survey period, collection design, household population coverage, military housing exclusions, and monetary adjustment remain. In particular, D.C. is a federal district, not a U.S. territory.

## Validation
`06_Methodology/Phase2/validate_phase2d_numeric_acquisition.py` passed:
- 16 official Island Areas source-specific observations.
- Eight 2019 one-year ACS/PRCS domain observations; 40 original estimate/MOE component records.
- Eight 2016–2020 five-year ACS/PRCS domain observations; 40 original estimate/MOE component records.
- ACS values independently recomputed from archived detailed-table components and the corresponding population denominators.
- Original ZIPs CRC-validated, PDFs identified, source hashes recorded.
- No original downloaded archive or preexisting .spv was overwritten during this work.

**Preservation exception:** Existing age-and-sex SPSS `.sav` currently SHA256 `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`, whereas an earlier audit recorded `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`. SPSS `.sav` record order is now alphabetic by geo_code; CSV is in original order. After sorting by geo_code, all data columns reconcile exactly or to the established floating tolerance. Bytewise preservation is NOT verified. No original file was changed by the extraction scripts; investigate past SAV rewriting or SPSS sorting without automatically reverting or replacing it.

## Output files
- `02_SPSS_Data/Phase2/island_areas_2020_socioeconomic_source_specific.csv` — 16 records.
- `02_SPSS_Data/Phase2/prdc_2019_acs_one_year_detailed_source_specific.csv` — eight records.
- `02_SPSS_Data/Phase2/prdc_2020_acs_five_year_detailed_source_specific.csv` — eight records.
- `02_SPSS_Data/Phase2/prdc_2019_acs_one_year_raw_components_with_moe.csv` — 40 records.
- `02_SPSS_Data/Phase2/prdc_2020_acs_five_year_raw_components_with_moe.csv` — 40 records.
- `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` — 17 newly acquired source artifacts.
- Source acquisition, mapping, extraction and validation Python scripts in `06_Methodology/Phase2`.

## GO/NO-GO next gate
- GO: Distinct source-family socioeconomic reporting with periods, universes, exclusions and MOE caveats noted.
- CONDITIONAL: Side-by-side descriptive display only if differences are prominently labeled, not statistically normalized.
- NO-GO: Any unqualified all-six socioeconomic comparison, ranks, significance tests, or policy inference from unequal source products.
- Recommended: Resolve prior demographic SAV hash change, review the four measure-specific universe definitions/footnotes, establish ratio MOE method, and prepare an academically reviewable evidence appendix before revisiting SPSS socioeconomic analysis.
