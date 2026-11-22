# TRR Phase 2M-A/B — Reproducibility and Portable Validation Acceptance

**Date:** November 21, 2026  
**Workspace:** `I:\Territorial-Representation-Research`  
**Research decision:** GO for new **read-only** portability check; CONDITIONAL for full historical environment reproducibility; NO-GO for regeneration or alteration of evidence without separate approval.

## Initial audit

The project contains **66 Python scripts**, of which **62** contain an `I:` path reference. The legacy scripts include archive acquisition, extraction, plotting, SPSS building, exploratory investigation and validation; rewriting all of them without isolated tests could damage the historical evidence chain. Existing Python runtime on the research workstation is **3.14.7**. Original SPSS software remains separately required for `.sav`/`.spv` viewing and embedded SPSS syntax.

The public repository tracks 17 original official Phase 2D source files and their 64-character SHA-256 manifest. Two additional historical original DHC ZIPs (PR and DC) were excluded from public Git for preservation/size reasons and remain a full-archive reproducibility limitation.

## New portable check

`06_Methodology/Phase2/validate_phase2m_portable.py`

- Python **3.10+**, standard library only; no `pip` installation, network requests, secret access, file writes, SPSS, or operating-system modifications.
- Locates the repository from the script's physical path, or accepts `--root /path/to/checkout` for review.
- Converts Windows backslashes in recorded source-relative paths to platform-neutral separators, prevents path traversal, and streams SHA-256 hashing without loading large archives into memory.
- Verifies all 17 official source file sizes/hashes and the six-jurisdiction demographic CSV population/sex/age totals.
- Revalidates all 12 Census Data Profile estimate and published percentage-MOE pairs against preserved official JSON, the original 10 one-decimal matches, and the two D.C. education direct composite-count reconciliations.
- Reports independent faculty decision and SAV historical byte-hash causality as **PENDING/OPEN**; it cannot grant academic/publication approval.

## GitHub validation

New manual and pull-request-scoped workflow:
`.github/workflows/validate-research-evidence.yml`

The workflow uses a checkout with credential persistence disabled and Python 3.12. No write, force push, SPSS rebuild, Census API secret, or download of the two excluded historical archives is authorized. It verifies tracked evidence only.

## What this check does not establish

- It does not prove the historical `.sav` file byte hash matches an earlier unavailable file.
- It does not re-execute every original Python and SPSS extraction/build step.
- It does not lock the historical Python/SPSS environment or prove reproducibility of original graphics.
- It does not establish Island Areas decennial and ACS/PRCS data are one harmonized, mutually comparable socioeconomic sample.
- It does not replace an independent faculty methodology and APA reference review.

## Acceptance

| Gate | Decision |
|---|---|
| Existing historical source data modified | NO — preservation maintained |
| Portable standard-library source/MOE validator | LOCAL PASS |
| GitHub-hosted Linux validation | PENDING execution and evidence |
| Existing source file sizes/SHA-256 | PASS (17/17) |
| Six-jurisdiction demographic source sums | PASS |
| Published profile MOE reconciliation | PASS (12/12 numerically accounted for; 10 directly matched earlier Phase 2F computed MOEs) |
| End-to-end historical build reproducibility | CONDITIONAL — unresolved hard-coded paths and dependency locks |
| Historical SAV binary preservation | OPEN |
| External faculty academic review | PENDING |
| Final research publication | NO-GO |

## Next technical steps

1. Run and inspect the GitHub-hosted Linux workflow. Amend the status above with the actual run ID and result in a new signed-off acceptance addendum, retaining this original decision record.
2. Inventory third-party packages from original scripts and capture an approved non-secret version manifest **without installing or changing the workstation**.
3. Propose incremental root-relative refactors of selected validators, one script at a time and with regression tests; do not automatically rewrite 62 historical files.
4. Keep GitHub Issue #4 open until portability and reproducible dependency work meets its acceptance criteria.
