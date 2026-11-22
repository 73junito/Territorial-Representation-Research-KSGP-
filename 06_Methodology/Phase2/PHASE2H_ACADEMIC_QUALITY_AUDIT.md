# TRR-PHASE2H — Academic Methods and Citation Quality Audit

**Review date:** November 21, 2026  
**Scope:** Phase 2B–2G methods, numerical acquisition, source manifest, Phase 2F integrated report and Phase 2G review/committee drafts.

## Verified methods
- The 2020 decennial six-geography age/sex pilot is **descriptive** and population-based; total population 4,313,440.
- The source-specific 32 socioeconomic observations come from **three product-period series**, not one exchangeable six-jurisdiction sample.
- Four Island Areas Demographic Profiles use 2020 census data, with income and poverty referring to 2019. Explicit tables, profiles and segment layouts preserved in official ZIPs/matrices.
- DC/PR one-year 2019 and pooled five-year 2016–2020 ACS/PRCS Detailed Table estimates have distinct source archives and published source-component MOEs; median household income B19013 has four directly published MOEs.
- The 12 Census-formula-derived percentage MOEs are **approximate 90% uncertainty estimates** with independently checked arithmetic, **not independently reconciled published Data Profile MOEs**. The published numerical cross-validation is BLOCKED.
- Guam exclusion, household universe, income dollar convention, 2019 vs five-year period, and D.C. legal distinction are mandatory notes for any side-by-side layout.

## Citation and nomenclature corrections
- ACS profile education variable should specify `DP02_0068PM` for D.C. versus `DP02PR_0068PM` for Puerto Rico; do not label the latter as ordinary `DP02` if citing the Puerto Rico social profile.
- Use `DP03_0009PM` for percent unemployment MOE and `DP03_0128PM` for percent poverty MOE. Census API `variables.json` in earlier workspace snapshots included just the default estimate subset, so absence of `PM` entries in that local JSON does not mean the official variable is nonexistent.
- Do not describe the four median-income intervals as eight. Count = 2 jurisdictions × 2 releases = four.
- Do not mark Phase 2G published-MOE reconciliation PASS based on the content-duplicated document.
- Avoid equating a verified SPSS .sav content match with historical byte-level archival integrity.
- The official Census source manifest includes primary download URLs and hashes; individual report citations should include year/product/table/variable, geography and downloaded source URL. An academically final APA 7 reference list is not yet independently checked against title pages and publication metadata.

## Report readiness
The files `08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md`, `08_Final_Report/Phase2G_Academic_Research_Review_Draft.md`, and `09_Committee_Package/Phase2G_Research_Brief_Draft.md` are valid **draft sources** but do not constitute peer review, committee approval or final academic signoff. Publication wording must keep these unresolved gates visible.

## Quality gate
- Source-specific descriptive research: GO.
- Approximate ratio MOEs with method clearly labeled: CONDITIONAL.
- Reconciliation with published Profile numeric MOEs: BLOCKED 0/12.
- Six-way socioeconomic significance tests/rankings: NO-GO.
- Historic SAV byte continuity: OPEN.
- Academic external review: NOT YET PERFORMED; draft ready to submit for review after updating uncertainty labels and citations.
