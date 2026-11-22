# Reproducibility — non-destructive workflow

## Environment
The original study was run from I:\Territorial-Representation-Research on Windows with Python 3.14 and IBM SPSS Statistics 31. Python dependencies used across scripts include pandas, numpy, pyreadstat, openpyxl and requests. A full locked environment has not been archived. Some scripts hard-code local paths.

## Existing verification commands

From the original research workspace in PowerShell, run these **read-only validation** scripts:

~~~powershell
python .\06_Methodology\Phase2\validate_phase2_workspace.py
python .\06_Methodology\Phase2\validate_phase2d_numeric_acquisition.py
python .\06_Methodology\Phase2\validate_phase2e_appendix.py
python .\06_Methodology\Phase2\validate_phase2f_research.py
python .\06_Methodology\Phase2\validate_phase2h_review.py
~~~

These checks test internal source reconciliation; the historical Phase 2H matrix intentionally retains its then-blocked published-MOE fields. Phase 2I subsequently acquired all 12 directly published values and reconciled the two D.C. education discrepancies using separately published composite count MOEs; see PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md.

Do not re-run acquisition or build scripts directly over existing evidence. Some scripts write new files or assert that no destination exists. Reproduce source acquisition in a separate test workspace, validate archive hashes, and keep 2019 one-year and 2016–2020 five-year survey series separate.

Do not modify original SAV/SPV, archives or Windows security settings during verification. Embedded SPSS Python syntax must run inside SPSS, not a standalone Python interpreter. The historic SAV byte-hash mismatch is unresolved even though 90 demographic cells match their CSV by jurisdiction.

## Evidence integrity protocol

For each new source or calculation record: agency, source URL, product/version, download date, SHA-256, geography, table variable, reference period, universe, units, published MOE/suppression status and calculation formula. Review staged changes and run validators before a pull request. Distinguish computed approximate MOEs from independently published profile uncertainty.

## Public-clone limitation

Two original DHC ZIPs are omitted from Git due to size; all originals remain on the original I: workspace. The source registers provide retrieval evidence. GitHub is not a complete byte-for-byte backup of the original research folder.
