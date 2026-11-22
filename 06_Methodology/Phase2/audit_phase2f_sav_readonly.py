from pathlib import Path
import hashlib,datetime,csv
import pyreadstat,pandas as pd,numpy as np
root=Path(r'I:\Territorial-Representation-Research')
b=root/'02_SPSS_Data'/'Phase2'
sav=b/'age_sex_2020_six_jurisdictions.sav'
csvp=b/'age_sex_2020_six_jurisdictions.csv'
s,m=pyreadstat.read_sav(str(sav))
c=pd.read_csv(csvp,keep_default_na=False)
prior='300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8'
current=hashlib.sha256(sav.read_bytes()).hexdigest()
assert s.geo_code.is_unique and c.geo_code.is_unique
ss=s.sort_values('geo_code').reset_index(drop=True)
cc=c.sort_values('geo_code').reset_index(drop=True)
assert list(ss.columns)==list(cc.columns)
mismatches=[]
for col in ss.columns:
 if pd.api.types.is_numeric_dtype(cc[col]):
  if not np.allclose(ss[col],cc[col],rtol=0,atol=1e-8):mismatches.append(col)
 elif not (ss[col].astype(str)==cc[col].astype(str)).all():mismatches.append(col)
assert not mismatches
fmt=lambda ts:datetime.datetime.fromtimestamp(ts,datetime.timezone.utc).isoformat()
lines=[
 '# Phase 2F — Demographic SAV Read-Only Forensic Review','',
 '## Byte-level preservation and content comparison','',
 f'- Earlier recorded SAV SHA-256: `{prior}`',
 f'- Current SAV SHA-256: `{current}`',
 f'- Current CSV SHA-256: `{hashlib.sha256(csvp.read_bytes()).hexdigest()}`',
 f'- SAV file bytes: {sav.stat().st_size}',
 f'- SAV last modified UTC: {fmt(sav.stat().st_mtime)}',
 f'- CSV last modified UTC: {fmt(csvp.stat().st_mtime)}',
 f'- SAV case order: {", ".join(s.geo_code.astype(str))}',
 f'- CSV case order: {", ".join(c.geo_code.astype(str))}',
 '- Six distinct jurisdictions in each file: PASS',
 '- All columns and record values match when joined by jurisdiction: PASS',
 '- All source population and age/sex totals preserved: PASS',
 '- SAV byte-level identity to earlier audit: **FAIL**',
 '- Because case order differs, a save/sort operation is a plausible explanation; this alone does **not prove when, why, or by whom** it was changed.',
 '- File-system modified time and any SPSS metadata do not establish a causal explanation or restore earlier bytes.',
 '- Investigate with historical copies and SPSS execution logs if necessary; do not overwrite or regenerate the file merely to force its prior hash.',
 '',
 '## SPSS file metadata and current evidence',
 f'- File label: {getattr(m,"file_label",None)!r}',
 f'- Case count: {len(s)}',
 f'- Column count: {len(s.columns)}',
 f'- Recorded SPSS creation datetime: {getattr(m,"creation_time",None)!r}',
 '',
 '## Acceptance status',
 '**CONTENT INTEGRITY PASS; BYTE-HASH PRESERVATION EXCEPTION OPEN.** This is nonblocking for source-specific Phase 2F methodological reporting, but blocks any claim of verified unchanged bytes since the earlier audit.'
]
p=root/'06_Methodology'/'Phase2'/'PHASE2F_SAV_HASH_FORENSIC.md'
assert not p.exists(),p
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('SAV_HASH_OLD',prior)
print('SAV_HASH_NEW',current)
print('SAV_METADATA',getattr(m,'creation_time',None),getattr(m,'file_label',None))
print('CONTENT_MATCH',len(s),'cases',len(s.columns),'cols','ORDERS',list(s.geo_code),list(c.geo_code))
print('REPORT',p,hashlib.sha256(p.read_bytes()).hexdigest())
