# Issue #1 — Official Census profile data acquisition gate (2026-11-21)

## Confirmed blocker
The U.S. Census Bureau requires an API key for data API requests as of May 2026. The earlier `missing_key.html` responses reflect that requirement, not simply malformed geography syntax. Official metadata is available without an API key, but the **numerical published Data Profile percentage MOEs** are not yet archived.

Reference: https://www.census.gov/data/developers/guidance/api-user-guide.API_Key.html

## New reproducible acquisition script
`06_Methodology/Phase2/fetch_phase2i_official_profile_moes.py`

This script:
1. Reads an approved `CENSUS_API_KEY` environment variable at runtime and never writes the key into code, output archives, logs, or Git.
2. Requests 2019 ACS/PRCS one-year and 2020 ACS/PRCS five-year Data Profile numeric fields for D.C. (state 11) and Puerto Rico (state 72).
3. Uses `DP02_0068PE/PM` for D.C. education, `DP02PR_0068PE/PM` for Puerto Rico education, and `DP03_0009PE/PM` and `DP03_0128PE/PM` for unemployment and poverty.
4. Validates all four JSON replies, archive integrity, field presence and numerical scope before writing anything, and refuses to overwrite existing files.
5. Writes four official response archives and a 12-row independent comparison matrix.
6. Labels all resulting comparisons `REVIEW_REQUIRED_NOT_AUTOMATIC_PASS` to avoid assuming calculation and published profile estimates have identical definitions.

### Current execution result
`BLOCKED: CENSUS_API_KEY environment variable not present. No network calls or writes performed.`

The Python syntax passed AST parsing. The **existing 0/12 published numeric reconciliation count is unchanged**.

## Execution after key is locally configured
Set the Census Bureau API key *locally on the research machine*, not in GitHub or this chat, then run:

```powershell
python .\06_Methodology\Phase2\fetch_phase2i_official_profile_moes.py
```

The script will detect an unavailable or invalid key and reject HTML responses without writing those as data. Do not mark Issue #1 closed until each of 12 numerical published profile MOEs is retrieved, independently compared, and definition differences adjudicated.

## Protected evidence
Existing source datasets, original Census ZIPs, SPSS .sav and .spv files, and the Phase 2H blocked status have not been changed.