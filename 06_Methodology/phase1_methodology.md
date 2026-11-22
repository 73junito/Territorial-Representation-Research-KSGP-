# Phase 1 — Census Population Comparison (2010–2020)
Prepared: 2026-11-21

## Study scope
Five permanently inhabited U.S. territories: Puerto Rico, Guam, U.S. Virgin Islands, American Samoa, and Northern Mariana Islands. Washington, D.C. is included separately as a federal district, not as a territory.

## Observation and units
Six jurisdiction-level census population counts; observations are jurisdictions, not sampled individuals. The 2010 and 2020 columns refer to April 1 census enumeration. Use exact integer counts for arithmetic.

## Computation
population_change = population_2020 - population_2010
population_change_pct = 100 * population_change / population_2010

## Representation variables
house_final_vote_members and senate_members = 0 for all six jurisdictions as currently constituted. These indicators are descriptive of voting membership, and do not imply that a delegate or resident commissioner is absent or barred from all legislative participation.

## Analysis rules
Report changes descriptively; do not compute inferential p-values treating the six jurisdictions as a random sample. Do not treat total residents as eligible voters. Do not combine later annual estimates with decennial census counts without explicit year labels. Population change alone does not establish causes, consequences, or preferred political status.

## Data provenance
Exact population count values transcribed from official U.S. Census Bureau QuickFacts (PR/DC) and 2021 Island Areas census press releases (GU/VI/AS/MP). See 01_Government_Sources/source_register.csv for URLs and notes. CSV is a manually transcribed research extract rather than an archived machine-download of raw federal tables.

## Limitations
Census data coverage and universes differ between Puerto Rico/DC and island areas for detailed socioeconomic variables. This Phase 1 file contains only population and representation counts. Missing detailed variables are not zero. No survey inference or socioeconomic comparisons have been executed.

## Planned quality checks
Check unique geo_code, six rows, all counts > 0, 2020 sum = 4313440, and calculated changes within reporting rounding. Cross-check all source URLs before publication.
