* Territorial Representation Research - Phase 1.
* Population 2010 vs 2020; six jurisdictions, descriptive only.
* Open the .sav file generated from the documented census source CSV.
GET FILE='I:\Territorial-Representation-Research\02_SPSS_Data\population_2010_2020.sav'.
DATASET NAME territorial_population.
COMPUTE population_change = population_2020 - population_2010.
COMPUTE population_change_pct = 100 * population_change / population_2010.
FORMATS population_2010 population_2020 population_change (F12.0).
FORMATS population_change_pct (F8.2).
VARIABLE LABELS population_change '2020 population minus 2010 population'
 /population_change_pct '2010-2020 population change (percent)'.
EXECUTE.
SORT CASES BY population_2020 (D).
LIST VARIABLES=geo_code jurisdiction population_2010 population_2020 population_change population_change_pct.
DESCRIPTIVES VARIABLES=population_2010 population_2020
 /STATISTICS=SUM MEAN MIN MAX.
* Six jurisdictions are the entire study population: no significance tests.
SAVE OUTFILE='I:\Territorial-Representation-Research\02_SPSS_Data\population_2010_2020.sav'.
