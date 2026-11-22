# TRR Phase 2D — Live Acquisition Gate (2026-11-21)
Workspace: I:\Territorial-Representation-Research

## Findings verified during live execution
1. The currently archived official Census 2020 ACS five-year Profile metadata declares `DP02_0068PE`, `DP03_0009PE`, `DP03_0062E`, and `DP03_0128PE`.
2. It does NOT declare `DP3_0062E`, `DP3_0062M`, `DP02_0068PM`, `DP03_0009PM`, `DP03_0062M`, or `DP03_0128PM`. Consequently, the acquisition plan's MOE requests are not valid *against the archived variables.json*; they must be resolved using another official dataset/interface (e.g., appropriate detailed ACS/PRCS tables with published MOEs) or another confirmed release, not invented.
3. Live numeric data API queries for `2020/acs/acs5/profile` and `2019/acs/acs1/profile` were redirected to `https://api.census.gov/data/missing_key.html`, an HTML page, although each response reported HTTP 200. This is an **acquisition failure**, not successful JSON retrieval; no numeric ACS observations should be claimed.
4. The existing Phase 2C `prdc_acquisition_plan.md` still contains stale identifiers in several sections and includes impossible territory/state-geography mappings (e.g., Guam and Northern Mariana Islands are not ACS states). Actual PR/DC State FIPS codes are DC=11 and PR=72.
5. Technical layout validation of socioeconomic DP2/DP3 field positions remains OPEN. Population at segment 01 raw position 6 cannot be re-used to map values in segments 02/03.

## Status
- ACS/PRCS numeric acquisition: BLOCKED BY API RESPONSE (HTML missing_key; alternate official method needed).
- Island Area socioeconomic raw numeric extraction: PENDING independently validated segment layouts and correct island-wide geography selection.
- Source definitions inventory: PASS.
- Six-way socioeconomic comparability: NO-GO.
- No demographic, Census original archives, SPSS data, or SPSS .spv files were modified.
- No Windows security settings changed.

## Next controlled action
Find alternate official Census bulk tables/CSV files for 2019 ACS/PRCS and 2016–2020 ACS/PRCS with estimate/MOE values, and obtain the Island Areas 2020 Demographic Profile technical documentation and layout. Archive originals and verify dimensions, geography, segments, reference universe and cells against Census reports. Record successful numeric extraction, or a named BLOCKED condition; never classify metadata-only review as data acquisition.
