# Data provenance and responsible public sharing

This public repository contains government-source extracts, code, manifests, SPSS outputs, technical references and explicitly qualified **research drafts**. It is not an official Census Bureau publication, an academic peer-review endorsement, or an adopted Kansas Green Party policy.

## Primary provenance
- 01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv: downloaded sources and SHA-256 hashes.
- 01_Government_Sources/Phase2_Socioeconomic/Census/PR_DC_2020_DHC_archive_manifest.csv: original DHC source inventory.
- 06_Methodology/Phase2/PHASE2D_NUMERIC_ACQUISITION_ACCEPTANCE.md: field extraction and source-specific definitions.
- 06_Methodology/Phase2/PHASE2H_ACCEPTANCE_DECISION.md: current research acceptance status.

Two excluded original archives remain at the local workspace: PR_2020_DHC_original.zip (about 136.7 MB) and DC_2020_DHC_original.zip (about 13.6 MB). The first exceeds GitHub's normal 100 MB per-object ceiling. Their omission is deliberate: do not claim a public clone contains all original datasets.

## Method boundaries
The 32 socioeconomic observations are **not** 32 independent subjects. AS, GU, MP and VI use 2020 Island Areas Census profiles; PR/DC use distinct 2019 one-year and 2016–2020 five-year ACS/PRCS estimates. Population universes, Guam military-housing coverage, survey design and income inflation bases differ. Source-specific descriptive work is GO; qualified side-by-side display CONDITIONAL; unqualified six-way socioeconomic inference NO-GO.

Four median-income 90% intervals use directly published source MOEs. Twelve percentage-rate MOEs were derived from original components and checked arithmetically; 0/12 independent published profile numerical MOEs were acquired in Phase 2H. The earlier SAV and current SAV hashes differ; values still reconcile with CSV, but historic byte preservation is OPEN.

## Security and research independence
Do not commit credentials, API tokens, secrets, private correspondence, student records, unpublished review notes or personal data. Inspect file contents before pushing to this **public** repository. A basic automated secret scan cannot guarantee safety. Avoid committing large archives without a documented storage decision. Do not alter history or original evidence in an attempt to conceal source issues.

Project naming does not establish Kansas Green Party endorsement. Separate source-backed factual analysis from advocacy, and do not infer political preferences from aggregate Census measures.
