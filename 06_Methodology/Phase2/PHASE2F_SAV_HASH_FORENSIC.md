# Phase 2F — Demographic SAV Read-Only Forensic Review

## Byte-level preservation and content comparison

- Earlier recorded SAV SHA-256: `300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8`
- Current SAV SHA-256: `15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def`
- Current CSV SHA-256: `8a9e83dedcd95675133e7ba0a2e16a7ce6a30ce27b61381255dca914b503b900`
- SAV file bytes: 4126
- SAV last modified UTC: 2026-11-22T00:18:16.516234+00:00
- CSV last modified UTC: 2026-11-21T23:53:28.498274+00:00
- SAV case order: AS, DC, GU, MP, PR, VI
- CSV case order: PR, DC, GU, VI, AS, MP
- Six distinct jurisdictions in each file: PASS
- All columns and record values match when joined by jurisdiction: PASS
- All source population and age/sex totals preserved: PASS
- SAV byte-level identity to earlier audit: **FAIL**
- Because case order differs, a save/sort operation is a plausible explanation; this alone does **not prove when, why, or by whom** it was changed.
- File-system modified time and any SPSS metadata do not establish a causal explanation or restore earlier bytes.
- Investigate with historical copies and SPSS execution logs if necessary; do not overwrite or regenerate the file merely to force its prior hash.

## SPSS file metadata and current evidence
- File label: None
- Case count: 6
- Column count: 15
- Recorded SPSS creation datetime: datetime.datetime(2026, 11, 21, 18, 18, 16)

## Acceptance status
**CONTENT INTEGRITY PASS; BYTE-HASH PRESERVATION EXCEPTION OPEN.** This is nonblocking for source-specific Phase 2F methodological reporting, but blocks any claim of verified unchanged bytes since the earlier audit.
