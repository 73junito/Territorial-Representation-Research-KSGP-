# TRR Phase 2M-F — Consolidated Academic Research Readiness and GO/NO-GO Decision Packet

**Decision date:** November 21, 2026 (America/Chicago)
**Repository:** https://github.com/73junito/Territorial-Representation-Research-KSGP-
**Workspace:** `I:\Territorial-Representation-Research`
**Evidence baseline:** `7444a247afdf3dea88acf3117fcc9698f08c77e7` (Phase 2M-E); final packet commit recorded in Git history after publication.
**Status:** **INTERNAL READINESS PASS FOR QUALIFIED FACULTY REVIEW; FINAL ACADEMIC OR POLICY PUBLICATION NO-GO.**

## Executive decision

The research is ready to be reviewed by a qualified independent statistical or academic reviewer. The source file integrity, published Census rate margin-of-error cross-validation, read-only cross-platform core verification, new draft manuscript and source-separated figures meet the *internal evidence-preparation* criteria. **No faculty approval, peer-review acceptance, KSGP committee adoption, or public publication authorization is implied.**

The six defined jurisdictions are five inhabited U.S. territories—Puerto Rico, Guam, U.S. Virgin Islands, American Samoa, Commonwealth of the Northern Mariana Islands—plus **Washington, D.C., a federal district, not a territory**. The 2020 population total for those selected jurisdictions is **4,313,440**. The 32 socioeconomic observations are source-product-domain observations, **not independent respondents or one harmonized six-jurisdiction sample**.

### Consolidated acceptance matrix

| Gate | Audited evidence | Disposition | Remaining dependency |
|---|---|---|---|
| Phase 2M-A — repository audit | 66 Python scripts inventoried; 62 contain `I:` references | **PASS audit / CONDITIONAL full historical portability** | Review, test and migrate selected legacy scripts individually; preserve originals |
| Phase 2M-B — portable core source/MOE verification | 17 government files' sizes/SHA-256; 6 demographic records, 4,313,440 total; 12 official rate MOEs; direct two D.C. education count-MOEs | **PASS** Windows Python 3.14.7 and GitHub Linux Python 3.12 | Does not reconstruct all original SPSS/archival extraction operations |
| Phase 2M-C — archival SAV hash review | Current 4,126-byte SAV SHA-256 matches Git-tracked binary; recorded older hash differs; 6 × 15 fields matched CSV in prior Phase 2F audit | **PASS current content/Git identity; OPEN historical byte causality** | Prior binary or corroborating logs from an authorized backup |
| Phase 2M-D — academic manuscript draft | Five labeled data tables; published MOEs; source limits; direct Census references and appendix | **PASS internal numerical QA; CONDITIONAL editorial review** | Qualified faculty review, APA 7 metadata/year-suffix and in-text citation approval |
| Phase 2M-E — source-specific figures | 14 graphics, 28 PNG/SVG files, 28 export checksums, figure index with exact data and MOE sources | **PASS internal data/format QA** | Accessibility, legibility and APA figure caption review by qualified editor |
| Six-jurisdiction pooled socioeconomic significance or causal inference | Distinct 2020 Island Areas Census, 2019 ACS/PRCS one-year and 2016–2020 ACS/PRCS five-year design, coverage, dollar and population universes | **NO-GO** | New justified harmonized design and evidence; none authorized |
| Independent academic review | Owner reported invitation sent to Dr. Greg Belcher from student email | **PENDING** | Documented reviewer acceptance and written methods findings |
| Committee adoption / final public release | No documented approval | **NO-GO** | Separate academic and applicable organizational approval |

## Evidence decisions for faculty

**Primary-source integrity.** The 17 original Phase 2D Census files included in the acquisition manifest are size- and hash-verified. The 2020 age/sex data cover exactly the six jurisdiction codes PR, DC, GU, VI, AS and MP. The population, sex, and three age-group totals reconcile. This does not claim that all original untracked high-volume source archives can be independently acquired through the public repo.

**Published uncertainty.** Official Census Data Profile point estimates and 90% percentage MOEs were retrieved for all twelve targeted D.C./PR domain-period combinations. Ten earlier Phase 2F derived rate MOEs agree at published one-decimal precision. Two D.C. bachelor's-or-higher MOEs differed because the original approximation combined four education-category MOEs by quadrature; using the official directly published composite count MOE reproduces the two Census percentage MOEs at published precision. The true replicate-weight variance/covariance mechanism has **not** been reconstructed.

**Demographic SPSS preservation.** Earlier SAV SHA-256: `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`. Current SAV SHA-256: `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`. The current binary is byte-identical to the Git archive's initial version, and earlier Phase 2F content matches the canonical CSV. No earlier-hash binary was found in the searched repository. **Do not claim the case-order difference establishes a prior sort/save operation.**

**Statistical graphics.** Only population and age-composition figures include all six defined jurisdictions. Four Island Areas Census socioeconomic figures have **no invented ACS-style sample MOEs**. Separate D.C./PR 2019 one-year and 2016–2020 five-year figures show directly published 90% MOEs (or B19013 median-income MOEs) and distinctly label dollar years. No misleading pooled socioeconomic comparisons were produced.

## Repository review entry points

1. **Academic manuscript:** `08_Final_Report/Phase2MD_Integrated_Academic_Manuscript_Review_Draft.md`.
2. **Figure catalog:** `06_Methodology/Phase2/PHASE2ME_ACADEMIC_FIGURE_ACCEPTANCE.md`; figure values, SHA-256 and formats at `05_Statistical_Graphics/Phase2ME/FIGURE_INDEX.csv`.
3. **Core portable verifier:** `06_Methodology/Phase2/validate_phase2m_portable.py`.
4. **Cross-platform acceptance:** `06_Methodology/Phase2/PHASE2M_LINUX_VALIDATION_ACCEPTANCE_ADDENDUM.md`. GitHub-hosted Linux PASS: https://github.com/73junito/Territorial-Representation-Research-KSGP-/actions/runs/44974338736 .
5. **SAV exception:** `06_Methodology/Phase2/PHASE2MC_SAV_HISTORICAL_PROVENANCE_DECISION.md`.
6. **Original source manifest:** `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv`.
7. **Census published-MOE adjudication:** `06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md`.
8. **Provisional APA review:** `06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md`.
9. **Faculty review handoff and unsigned decision form:** `09_Committee_Package/Phase2K_Faculty_Review_Handoff.md` and `Phase2K_Faculty_Review_Decision_Form.md`.
10. **Outreach status:** `06_Methodology/Phase2/PHASE2L_REVIEWER_SELECTION_AND_OUTREACH_GATE.md` (user-confirmed sent; delivery and acceptance not independently verified).

## Independent reviewer checklist and decision fields

- [ ] Validate source-specific jurisdiction classification and study population universes.
- [ ] Evaluate direct published 90% Census MOEs and the two D.C. educational-attainment reconciliations.
- [ ] Assess whether long-form Island Areas Census and ACS/PRCS design differences are adequately explained.
- [ ] Check source-specific inflation-year, Guam geographic coverage and poverty/education/labor denominators.
- [ ] Check the manuscript's exact APA 7 source metadata, year suffixes and citation placement.
- [ ] Review figures for accurate labels, readability, accessibility and no significance implication.
- [ ] Determine acceptable disclosure for the historical SAV byte-hash provenance exception.
- [ ] Return a dated, attributable written PASS / CONDITIONAL / REVISE / NO-GO decision.

**Reviewer selected/accepted:** NOT VERIFIED.
**Invitation:** OWNER-REPORTED SENT from student email; no mailbox delivery inspection.
**Written faculty methodological decision:** PENDING.
**Committee authorization:** NOT GRANTED.
**Final manuscript or policy publication:** **NO-GO** until the actual independent review and required authorizations occur.

## Explicit owner authorization boundaries

- Allowed: use this packet for qualified independent review, read-only source verification, and preparation of corrected drafts.
- Not allowed: rewrite original Census archives, SPSS SAV/CSV/SPV files or historical phase reports; conceal unresolved evidence; infer policy positions, voting eligibility, statistical significance or peer-review endorsement.
- Do not publish private faculty correspondence, reviewer signatures or confidential contact details to the public repo without consent.
- GitHub Issues **#2** (SAV historical byte cause), **#3** (external academic/publication review), and **#4** (broader reproducibility) remain OPEN for their respective unresolved acceptance gates.

## Final Phase 2M-F disposition

**GO** — Reproducible, clearly limited research *review package* and methodological draft presentation.

**CONDITIONAL** — Full historical execution portability, complete APA formatting, figure-editorial acceptance, and source-specific descriptive circulation subject to qualification.

**NO-GO** — Final academic certification or public committee endorsement; unqualified combined six-jurisdiction socioeconomic statistical inference.

This decision describes evidence checked at this revision. It does **not** certify historical byte identity, peer review, or committee adoption.
