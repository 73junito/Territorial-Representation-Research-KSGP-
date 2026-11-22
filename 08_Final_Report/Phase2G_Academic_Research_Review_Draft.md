# Territorial Representation Research — Academic Review Draft
**Draft status:** Methodological peer review requested; not approved for public release
**Research date:** November 21, 2026

## Research objective
Document and contextualize 2010–2020 demographic changes and source-specific 2020-era socioeconomic conditions in Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, the Northern Mariana Islands, and Washington, D.C. Washington, D.C. is a federal district, not a territory.

## Methods and evidence
Official decennial Census population, age and sex data supply the six-jurisdiction demographic pilot, with 2020 total population of **4,313,440**. Four 2020 Island Areas Demographic Profile archives provide source-specific education, civilian unemployment, median household income, and poverty for AS/GU/MP/VI. Separate official 2019 one-year ACS/PRCS and 2016–2020 five-year ACS/PRCS Summary Files provide the same broad domains for Washington, D.C. and Puerto Rico. There are **32 source-specific socioeconomic observations**, but not 32 exchangeable cases.

Source-specific datasets and official file checksums are recorded in `02_SPSS_Data/Phase2/` and `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`. Every observation is traceable to its raw table field. Reproducible extraction and validation scripts are in `06_Methodology/Phase2/`.

## Findings
The completed Phase 2F integrated report contains the full separate source-family tables:
`08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md`.
The detailed provenance appendix is `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md`.

2020 total population: 4,313,440; male: 2,047,330; female: 2,266,110; under 20: 880,002; age 20–64: 2,573,093; age 65+: 860,345.

Socioeconomic patterns are **descriptive and product-specific**. Island Areas profiles use 2020 Census data with 2019 income/poverty reference. For PR/DC, the one-year and pooled five-year ACS/PRCS survey estimates are separately reported; household/personal universes, design, inflation conventions, and military-housing exclusions prevent direct six-jurisdiction inferential comparisons.

## Uncertainty review
For Puerto Rico and D.C., four directly published median-income MOEs generate four 90% confidence intervals. The 12 educational attainment, unemployment, and poverty percentage intervals were **calculated using Census subset-proportion methods from archived source MOEs**, and independently recomputed in Phase 2F. They are *approximate derived intervals*, not directly published profile MOEs. Independent comparison with the Census Bureau's published profile/subject-table percentage MOEs **is still pending**; published uncertainty should not be characterized as independently reconciled.

The Island Areas Census profile observations do not have ACS sample MOEs; absence of a survey MOE is not an assertion of error-free measurement.

## Interpretation limits and ethics
No unqualified six-way socioeconomic significance testing, ordering as though measurements are fully comparable, causal claims, or inferences about residents' political preferences are permitted. The scope is secondary-source demographic and socioeconomic documentation; constitutional, representation and voting-policy analysis requires separately grounded legal and historical sources.

## Open review issues
1. Match 12 derived percentage intervals to official published profile/subject-table values, or document source unavailability/definition mismatches.
2. Determine whether four Island Areas universes and exclusions are sufficiently disclosed in any proposed side-by-side display.
3. Resolve the historical demographic .sav byte-hash discrepancy if a prior file/log exists. The content matches CSV by jurisdiction, but hash continuity is not proven.
4. Verify primary-source APA references and any policy-facing legal context before publication.

## Academic reviewer decision requested
Evaluate source-to-variable mapping, subset-proportion uncertainty formulas, denominator definitions, difference in reference years/products, clarity about D.C. versus territories, strength of limitations, and whether conditional side-by-side descriptive reporting is acceptable. This is a **review draft, not a final accepted statistical comparison**.

## Referenced source documents
U.S. Census Bureau, 2020 Island Areas Demographic Profile Technical Documentation and four Area Table Matrix workbooks (originals archived); U.S. Census Bureau 2019 ACS/PRCS one-year Summary Files; U.S. Census Bureau 2016–2020 ACS/PRCS five-year Summary Files; U.S. Census Bureau, *Understanding and Using American Community Survey Data: What All Data Users Need to Know* (2020), Chapter 8. Source URLs and cryptographic checksums: Phase 2D acquisition manifest. Full final APA-style bibliographic verification remains pending.
