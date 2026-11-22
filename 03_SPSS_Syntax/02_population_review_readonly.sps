* Read-only Phase 1 reproduction: does not SAVE to a locked input file.
* SPSS will display a file-in-use warning if this file is open elsewhere.
GET FILE='I:\Territorial-Representation-Research\02_SPSS_Data\population_2010_2020.sav'.
DATASET NAME territorial_population_review.
COMPUTE population_change = population_2020 - population_2010.
COMPUTE population_change_pct = 100 * population_change / population_2010.
FORMATS population_change (F12.0) population_change_pct (F8.2).
EXECUTE.
SORT CASES BY population_2020 (D).
LIST VARIABLES=geo_code jurisdiction population_2010 population_2020 population_change population_change_pct.
DESCRIPTIVES VARIABLES=population_2010 population_2020 /STATISTICS=SUM MEAN MIN MAX.
* End of read-only analysis: deliberately no SAVE OUTFILE.
