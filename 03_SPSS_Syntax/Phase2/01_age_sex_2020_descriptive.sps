* Phase 2 2020 age-and-sex pilot: six jurisdictions.
* Exact Census population counts. Descriptive only, no inference.
* Existing source dataset is never overwritten.
GET FILE='I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav'.
DATASET NAME age_sex_2020.
SORT CASES BY geo_code (A).
LIST VARIABLES=geo_code jurisdiction population_2020 male_2020 female_2020
 under20_2020 age20to64_2020 age65plus_2020 male_pct female_pct
 under20_pct age65plus_pct.
DESCRIPTIVES VARIABLES=population_2020 male_2020 female_2020
 under20_2020 age20to64_2020 age65plus_2020
 /STATISTICS=SUM MEAN MIN MAX.
* No SAVE: prevents SPSS file-contention duplicates.
