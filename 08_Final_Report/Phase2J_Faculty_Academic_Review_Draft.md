# Territorial Representation Research
## Phase 2J — Faculty Methodology and Evidence Review Draft

**Draft for independent academic review only — not an accepted thesis, peer-reviewed article, committee decision or policy endorsement.**

**Research scope:** Puerto Rico, Guam, American Samoa, the Northern Mariana Islands, the U.S. Virgin Islands and Washington, D.C. (a federal district, **not** a territory).

### Research questions

1. How did the total population and age/sex composition of the six jurisdictions appear in the 2010 and 2020 decennial Census source products?
2. What do distinct, documented Census/ACS/PRCS products report about educational attainment, unemployment, median household income and poverty in these jurisdictions?
3. Which data-product and population-universe distinctions prevent a legitimate single six-jurisdiction socioeconomic comparison?

### Design, sources and extraction

A descriptive secondary-data study using official U.S. Census Bureau source files. The validated 2020 six-jurisdiction population totals **4,313,440**. Six-jurisdiction age/sex observations are available in the preserved SPSS pilot. No individual respondent data or causal/inferential study design are involved.

There are **32 source-specific socioeconomic observations** rather than 32 exchangeable respondents: sixteen observations from the 2020 Island Areas Census profiles of AS, GU, MP and VI; eight observations from 2019 one-year ACS/PRCS survey results for D.C. and Puerto Rico; and eight observations from 2016–2020 five-year ACS/PRCS survey results for D.C. and Puerto Rico. The four domains are educational attainment, civilian unemployment, median household income and poverty.

The original official files, 17-file Census checksum manifest and extracted field mapping are documented in the Phase 2D evidence package. The 2020 Island Areas data result from a long-form census operation, **not ACS fieldwork in those four island areas**.

### Findings and uncertainty

The fully documented source-family-specific findings tables are retained in `Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md`. They are not repeated here as if they constituted a harmonized six-case comparison.

For D.C. and Puerto Rico, four median-household-income 90% confidence intervals use original published ACS/PRCS MOEs. Twelve education/unemployment/poverty 90% profile MOEs were acquired independently through official Census API responses in Phase 2I:
- Twelve survey profile rate point estimates agree with the archived estimates to displayed precision.
- Ten Phase 2F computed percentage MOEs agree with official profile MOEs at one-decimal precision.
- The two earlier D.C. education MOEs are overestimates relative to published profiles when computed from quadrature of four category count MOEs. Using official composite count numerator MOEs resolves both discrepancies at displayed precision.
- This does not establish the exact underlying ACS replicate variance-covariance algorithm.

For displayed **profile** percentages, use the **directly published Census MOE**, not a conflicting calculation from earlier Phase 2F. The original Phase 2F files remain as preserved research audit evidence.

### Limitations and interpretation

The Island Areas decennial profiles differ in measurement, coverage and collection from ACS/PRCS samples. Four socioeconomic domains have different denominators (age 25+, civilian workforce, households and poverty status universe). Source years, pooled versus one-year products, Guam military-housing exclusions and income dollar adjustment further restrict comparability. No unqualified six-jurisdiction socioeconomic rankings, significance tests, causal or electoral/political inferences are licensed.

One archival exception remains: the demographic SPSS .sav data match the canonical CSV by jurisdiction and all fields, but a past and current SHA-256 hash differ; the historical cause remains unknown.

### Review requested

Please independently assess:
- source-to-variable mapping and universe definitions;
- the use of official published MOEs and reconciliation of D.C. education;
- whether reference period, program and exclusion qualifiers suffice for descriptive reporting;
- APA 7 agency dataset/technical-document citations;
- whether any statements overstate academic acceptance, representation law, voting status or political inference.

**Faculty reviewer:** Not assigned  
**Review date:** Pending  
**Decision:** Pending (PASS / CONDITIONAL / REVISE)  
**Authorization for public/committee release:** NO-GO. Not granted by creation of this document; external academic and, where applicable, committee approvals remain pending.

### Source trail
- `06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md`
- `06_Methodology/Phase2/PHASE2J_ACADEMIC_METHODS_REVIEW_GATE.md`
- `06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md`
- `06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md`
- `08_Final_Report/Phase2E_Source_Specific_Evidence_Appendix.md`
- `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`

See the reference audit for direct original Census source URLs, published year conventions and full provisional APA entries.
