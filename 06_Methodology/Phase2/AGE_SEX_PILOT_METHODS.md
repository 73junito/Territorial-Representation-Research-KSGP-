# Phase 2 — 2020 Age-and-Sex Pilot: Data Definitions and Validation
Date: November 21, 2026

## Population and source
All six jurisdictions, 2020 decennial resident population. Puerto Rico and D.C. sourced from the Census 2020 DHC state-level P12 table, segment 06, record LOGRECNO 0000001. American Samoa, Guam, CNMI and USVI sourced from Island Areas 2020 Demographic Profile DP1, segment 01, record LOGRECNO 0000001. Original ZIP sources and hashes retained in age_sex_pilot_source_manifest.csv and PR_DC_2020_DHC_archive_manifest.csv.

## Harmonization
For all six, total population is all residents including those in group quarters. Sex totals correspond to Census tabulations for male and female (not independently observed gender identity). Age bands:
- Under 20: ages 0–19.
- Age 20–64: total less under-20 and 65+.
- Age 65+: 65 and over.

For island-area DP1, 18 five-year age groups from 0–4 to 85+. Under 20 = first four groups; 65+ = last five groups. For DHC P12, each sex's detailed 23 groups includes 15–17, 18–19, 65–66, 67–69 etc. Under 20 = first five sex-specific groups; 65+ = final six sex-specific groups. Counts are never rounded before computing percentages.

## Record offsets (zero-based index)
2020 Island Areas DP1 segment 01: 5 leading metadata fields; total at 5, 18 overall age groups at 6:24, male total at 24, male groups 25:43, female total 43, female groups 44:62.

2020 DHC state segment 06: 5 metadata fields; 71 P10 variables and 73 P11 variables before P12. Thus P12_0001 begins at 5+71+73=149. Male total at 150, male groups 151:174; female total at 174, female groups 175:198.

## Verification conditions
- ZIP CRC for each official archive checked.
- Area-level 2020 resident population totals match Phase 1 for all six.
- Within each jurisdiction, male + female = total.
- All-age male and female age groups sum to respective sex totals.
- Under-20 + age 20–64 + age 65+ = total.
- Percentage values computed without preliminary rounding.
- Newly written SPSS .sav read back with identical values to the derived CSV.
- Primary source archive SHA256 hashes recorded.

## Limits
This phase does not infer eligible-voter counts, political preferences, causal effects, or status preferences. Ages refer to decennial enumeration, not current 2026 population. Although definitions are harmonized for broad age and sex, the different production processes may have disclosure avoidance and data quality differences. The original files are Census summary tabulations, not independent person-level research records. Jurisdiction-level differences require descriptive interpretation rather than unqualified p-values.

## Output
I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav
I:\Territorial-Representation-Research\03_SPSS_Syntax\Phase2\01_age_sex_2020_descriptive.sps

No statistical output viewer (.spv) from IBM SPSS is claimed: syntax has been prepared but not executed through the SPSS application.
