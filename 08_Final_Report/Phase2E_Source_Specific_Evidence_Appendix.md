# TRR Phase 2E — Source-Specific Socioeconomic Evidence Appendix

**Evidence date:** November 21, 2026  
**Scope:** 32 jurisdiction-domain-product observations: 16 Island Areas 2020 Census, eight 2019 one-year ACS/PRCS, eight 2016–2020 five-year ACS/PRCS. These three products **must not be treated as one harmonized six-jurisdiction dataset**.

## A. Original source families and uncertainty
- **2020 Island Areas Census Demographic Profile:** AS, GU, MP, VI; education and unemployment tabulated in the 2020 Census, income and poverty reference 2019; census table percentages and poverty ratio. No ACS sample MOE is assigned to these census values. Different population and military-housing universes exist.
- **2019 ACS/PRCS one-year Detailed Tables:** DC and PR; sample estimates with published underlying count MOEs at the **90% confidence level**. Income figures are in 2019 inflation-adjusted dollars, not automatically interchangeable with an Island Areas income universe.
- **2016–2020 ACS/PRCS five-year Detailed Tables:** DC and PR; pooled sample estimates with published underlying count MOEs at the **90% confidence level**. Median income figures are expressed in 2020 inflation-adjusted dollars.
- **All ACS-derived percentage measures:** This extraction preserves original numerator/denominator count MOEs. It does not yet calculate a valid ratio MOE or 90% interval. A component MOE is not a ratio MOE; the displayed point estimate alone is not a significance test.

## B. Island Areas 2020 Census original profile values

| Jurisdiction | Measure | Original value | Official source field | Segment / one-based field | Poverty denominator (where applicable) |
|---|---|---:|---|---|---:|
| American Samoa | Education | 13.30% | `DPAS0200001` | 1 / 173 | — |
| American Samoa | Median Household Income | $28,352 | `DPAS0630001` | 3 / 21 | — |
| American Samoa | Poverty | 54.59% | `DPAS0900002` | 3 / 105 | 48506 |
| American Samoa | Unemployment | 13.20% | `DPAS0510001` | 2 / 142 | — |
| Guam | Education | 25.30% | `DPGU0200001` | 1 / 180 | — |
| Guam | Median Household Income | $58,289 | `DPGU0630001` | 3 / 21 | — |
| Guam | Poverty | 20.21% | `DPGU0900002` | 3 / 105 | 145543 |
| Guam | Unemployment | 10.20% | `DPGU0510001` | 2 / 149 | — |
| Northern Mariana Islands | Education | 21.00% | `DPMP0200001` | 1 / 176 | — |
| Northern Mariana Islands | Median Household Income | $31,362 | `DPMP0630001` | 3 / 21 | — |
| Northern Mariana Islands | Poverty | 38.01% | `DPMP0900002` | 3 / 105 | 47035 |
| Northern Mariana Islands | Unemployment | 14.10% | `DPMP0510001` | 2 / 147 | — |
| U.S. Virgin Islands | Education | 22.30% | `DPVI0200001` | 1 / 182 | — |
| U.S. Virgin Islands | Median Household Income | $40,408 | `DPVI0630001` | 3 / 21 | — |
| U.S. Virgin Islands | Poverty | 22.81% | `DPVI0900002` | 3 / 105 | 84766 |
| U.S. Virgin Islands | Unemployment | 9.70% | `DPVI0510001` | 2 / 146 | — |

**Field validation:** All Island Areas values were extracted from the island-wide `LOGRECNO=0000001` row using the original government matrix workbooks, with exact segment and offset recorded in the source-specific CSV. Poverty derives from below-poverty population divided by population for whom poverty status is determined.

## C. 2019 ACS/PRCS one-year detailed values

| Jurisdiction | Measure | Point estimate | Published income MOE / 90% interval | Source Detailed Table fields | Uncertainty classification |
|---|---|---:|---|---|---|
| Washington, D.C. | Education | 59.67% | Not available for derived rate | `B15003_001,B15003_022..025` | Published component count MOEs available; derived ratio interval not calculated |
| Washington, D.C. | Median Household Income | $92,266 | ± $2,497; [$89,769, $94,763] | `B19013_001` | Published median 90% MOE; symmetric interval from estimate ± MOE |
| Washington, D.C. | Poverty | 13.45% | Not available for derived rate | `B17001_001,B17001_002` | Published component count MOEs available; derived ratio interval not calculated |
| Washington, D.C. | Unemployment | 6.26% | Not available for derived rate | `B23025_003,B23025_005` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Education | 27.22% | Not available for derived rate | `B15003_001,B15003_022..025` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Median Household Income | $20,474 | ± $382; [$20,092, $20,856] | `B19013_001` | Published median 90% MOE; symmetric interval from estimate ± MOE |
| Puerto Rico | Poverty | 43.47% | Not available for derived rate | `B17001_001,B17001_002` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Unemployment | 14.11% | Not available for derived rate | `B23025_003,B23025_005` | Published component count MOEs available; derived ratio interval not calculated |

## D. 2016–2020 ACS/PRCS five-year detailed values

| Jurisdiction | Measure | Point estimate | Published income MOE / 90% interval | Source Detailed Table fields | Uncertainty classification |
|---|---|---:|---|---|---|
| Washington, D.C. | Education | 59.76% | Not available for derived rate | `B15003_001,B15003_022..025` | Published component count MOEs available; derived ratio interval not calculated |
| Washington, D.C. | Median Household Income | $90,842 | ± $1,580; [$89,262, $92,422] | `B19013_001` | Published median 90% MOE; symmetric interval from estimate ± MOE |
| Washington, D.C. | Poverty | 15.45% | Not available for derived rate | `B17001_001,B17001_002` | Published component count MOEs available; derived ratio interval not calculated |
| Washington, D.C. | Unemployment | 7.12% | Not available for derived rate | `B23025_003,B23025_005` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Education | 26.67% | Not available for derived rate | `B15003_001,B15003_022..025` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Median Household Income | $21,058 | ± $186; [$20,872, $21,244] | `B19013_001` | Published median 90% MOE; symmetric interval from estimate ± MOE |
| Puerto Rico | Poverty | 43.41% | Not available for derived rate | `B17001_001,B17001_002` | Published component count MOEs available; derived ratio interval not calculated |
| Puerto Rico | Unemployment | 15.07% | Not available for derived rate | `B23025_003,B23025_005` | Published component count MOEs available; derived ratio interval not calculated |

## E. Provenance and limitations
- Original government source URLs, hashes and file size: `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` (17 files).
- Detailed source-specific observation CSVs and 80 estimate/MOE component records: `02_SPSS_Data/Phase2/`.
- Reproducible scripts: `06_Methodology/Phase2/extract_verified_island_socioeconomic.py`, `extract_2019_prdc_acs_detailed.py`, `extract_2019_acs_moe_components.py`, `extract_2020_prdc_acs_detailed.py`, `validate_phase2d_numeric_acquisition.py`.
- Island Areas source definitions and exclusions must be taken from the four product-specific table matrices and the official `2020-iac-dpsf-technical-documentation.pdf`. Not every Area has the same household/military-housing universe.
- Census/PRCS sample estimates and 2020 Island Areas decennial profiles differ in survey design, time base, possible sampling error, population scope and dollars. In particular, Washington, D.C. is a federal district, **not** a U.S. territory.
- Do not infer voting eligibility, citizenship proportions, self-determination preferences or policy views from these aggregate measures.

## F. Preservation exception
The previously audited age-and-sex SPSS .sav byte hash differs from the current SHA-256. All six jurisdiction records and all substantive source values reconcile with CSV after sorting by geo_code. **Byte-level continuity remains OPEN**, regardless of matching data contents. Do not overwrite, repair, or re-sort the .sav to force a matching hash.
