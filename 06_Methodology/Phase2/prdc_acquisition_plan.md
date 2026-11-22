# TRR-PHASE2C: PR/DC ACS Numeric Acquisition Plan

**Workspace:** `I:\Territorial-Representation-Research`  
**Date:** November 21, 2026  
**Goal:** Acquire official 2019 ACS 1-year and 2020 ACS 5-year socioeconomic estimates for Puerto Rico and Washington, D.C., with margins of error

## 1. Current Status

| Source | File | Variables Available | Numeric Observations | MOE Available |
|---|---|---|---|---|
| ACS 2020 5-year | `ACS_2020_5YR_variables.json` | DP2_0068PE, DP3_0009PE, DP3_0062E, DP3_0128PE | ❌ NOT_ARCHIVED (metadata only) | ❌ NOT_INCLUDED |
| ACS 2019 1-year | `ACS_2019_1YR_variables.json` | Same variable IDs | ⚠️ PENDING_API_PULL | ⚠️ PENDING_API_PULL |

## 2. Acquisition Method: Census API Calls

### 2.1 API Endpoints (Corrected)

| Period | endpoint | Parameters |
|---|---|---|
| 2019 1-year | `https://api.census.gov/data/2019/acs/acs1/profile/variables.json` | `get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2019` |
| 2020 5-year | `https://api.census.gov/data/2020/acs/acs5/profile/variables.json` | `get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2020` |

### 2.2 Geographies to Request (Corrected)

| Geography | FIPS Code | Jurisdiction |
|---|---|---|
| American Samoa | `040` | AS |
| Guam | `66` | GU |
| Northern Mariana Islands | `72` | MP |
| U.S. Virgin Islands | `76` | VI |
| Puerto Rico | `72` | PR |
| Washington, D.C. | `11` | DC |

### 2.3 API Call Example (Corrected)

```bash
curl "https://api.census.gov/data/2020/acs/acs5/profile?get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2020&for=state:72"
```

```bash
curl "https://api.census.gov/data/2020/acs/acs5/profile?get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2020&for=state:11"
```

```bash
curl "https://api.census.gov/data/2019/acs/acs1/profile?get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2019&for=state:72"
```

```bash
curl "https://api.census.gov/data/2019/acs/acs1/profile?get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&time=2019&for=state:11"
```

### 2.4 Expected Response Fields

| Variable | Description | Type |
|---|---|---|
| `DP2_0068PE` | Percent Bachelor's degree or higher | Estimate (float) |
| `DP3_0009PE` | Unemployment rate | Estimate (float) |
| `DP3_0062E` | Median household income (dollars) | Estimate (float) |
| `DP3_0128PE` | Poverty rate | Estimate (float) |
| `DP2_0068PE_MOE` | Margin of error for education | Estimate (integer) |
| `DP3_0009PE_MOE` | Margin of error for unemployment | Estimate (integer) |
| `DP3_0062E_MOE` | Margin of error for median income | Estimate (integer) |
| `DP3_0128PE_MOE` | Margin of error for poverty | Estimate (integer) |

## 3. Storage Plan

| File | Path | Description |
|---|---|---|
| PR/DC ACS 2020 5YR estimates | `02_SPSS_Data/Phase2/prdc_2020_5yr_estimates.csv` | To be created |
| PR/DC ACS 2019 1YR estimates | `02_SPSS_Data/Phase2/prdc_2019_1yr_estimates.csv` | To be created |
| API call log | `06_Methodology/Phase2/prdc_api_log.txt` | To be created (request URLs, response timestamps, error codes) |
| Acquisition methodology | `06_Methodology/Phase2/prdc_acquisition_plan.md` | This document |

## 4. Required Variables and Meanings (Corrected)

| Variable ID | Full Name | Unit | Meaning |
|---|---|---|---|
| `DP02_0068PE` | Percent Bachelor's degree or higher | Percent | Population 25+ with Bachelor's degree |
| `DP03_0009PE` | Unemployment rate | Percent | Civilian labor force unemployment rate |
| `DP3_0062E` | Median household income | Dollars (2020 inflation-adjusted) | Median household income in last 12 months |
| `DP03_0128PE` | Poverty rate | Percent | Percent below poverty level (past 12 months) |

## 5. Margins of Error (Corrected)

| Variable | MOE Variable | Storage Format | Notes |
|---|---|---|---|
| Education | `DP02_0068PM` | Integer; use with 90% confidence interval | Census published margin |
| Unemployment | `DP03_0009PM` | Integer; use with 90% confidence interval | Census published margin |
| Median Income | `DP3_0062M` | Dollars; interpret with caution (median MOE not standard) | Census published margin |
| Poverty | `DP03_0128PM` | Integer; use with 90% confidence interval | Census published margin |

**Important:** Margins of error must be preserved and never substituted with zero. Missing MOE = missing data. Census suppresses values with insufficient sample size - flag these as missing.

## 5. Preservation Rules

1. **Never substitute missing or suppressed values with zero**
2. **Preserve all MOE values as-is** from the API response
3. **Flag suppressed values** ( Census suppresses values with insufficient sample size)
4. **Document source and period** for every extracted value
5. **Keep 2019 1-year and 2020 5-year estimates separate** — different periods, not directly comparable

## 6. API Call Log Template (Corrected)

| Date | API Endpoint | Jurisdiction | Variables | Status | Notes |
|---|---|---|---|---|---|
| YYYY-MM-DD | `https://api.census.gov/data/YYYY/acs/YY/profile?get=DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE&for=state:72` (PR) / `for=state:11` (DC) | AS/GU/MP/PR/DC | DP02_0068PE,DP03_0009PE,DP3_0062E,DP03_0128PE | SUCCESS/ERROR | Response time, record count, any warnings |

## 6. Deliverables (Phase 2C)

| File | Path | Status |
|---|---|---|
| Acquisition plan | `06_Methodology/Phase2/prdc_acquisition_plan.md` | ✅ CREATED |
| API call log (to be populated) | `06_Methodology/Phase2/prdc_api_log.txt` | ⏳ PENDING (after API calls executed) |
| PR/DC 2020 5YR estimates (to be populated) | `02_SPSS_Data/Phase2/prdc_2020_5yr_estimates.csv` | ⏳ PENDING (after API calls executed) |
| PR/DC 2019 1YR estimates (to be populated) | `02_SPSS_Data/Phase2/prdc_2019_1yr_estimates.csv` | ⏳ PENDING (after API calls executed) |

## 7. Acceptance Criteria (Phase 2D)

- ✅ PR/DC 2020 5YR numeric estimates acquired via corrected API calls (`for=state:72`, `for=state:11`)
- ✅ PR/DC 2019 1YR numeric estimates acquired via corrected API calls
- ✅ DP file field positions validated using official Census technical documentation
- ✅ Four socioeconomic domains extracted from Island Areas archives using documented field positions
- ✅ Source-verified values documented with full provenance (variable IDs, FIPS codes, MOE variables, reference periods)
- ✅ Revised variable-level GO/CONDITIONAL/NO-GO packet produced
- ✅ No validated demographic files overwritten
- ✅ No unqualified six-jurisdiction SPSS comparisons authorized