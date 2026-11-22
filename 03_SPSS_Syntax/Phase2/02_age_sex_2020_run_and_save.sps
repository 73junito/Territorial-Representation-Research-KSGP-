* Phase 2 - execute in IBM SPSS Statistics interactive Syntax Editor.
* New viewer isolates this run from other active outputs.
* Output must not already exist; do not overwrite existing research output.
OUTPUT NEW.
GET FILE='I:\Territorial-Representation-Research\02_SPSS_Data\Phase2\age_sex_2020_six_jurisdictions.sav'.
DATASET NAME age_sex_2020_review.
SORT CASES BY geo_code (A).
LIST VARIABLES=geo_code jurisdiction population_2020 male_2020 female_2020
 under20_2020 age20to64_2020 age65plus_2020 male_pct female_pct
 under20_pct age65plus_pct.
DESCRIPTIVES VARIABLES=population_2020 male_2020 female_2020
 under20_2020 age20to64_2020 age65plus_2020
 /STATISTICS=SUM MEAN MIN MAX.
OUTPUT SAVE OUTFILE='I:\Territorial-Representation-Research\04_SPSS_Output\Phase2\01_age_sex_2020_descriptive.spv'.
* Do not SAVE the input dataset.
