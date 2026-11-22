from pathlib import Path
import re
p=Path(r'I:\Territorial-Representation-Research')
patterns=[
 r'ghp_[A-Za-z0-9]{20,}',
 r'github_pat_[A-Za-z0-9_]{20,}',
 r'sk-(?:proj-)?[A-Za-z0-9_-]{20,}',
 r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 r'(?i)(?:password|api[_-]?key|secret[_-]?token)\s*[:=]\s*["\x27]?\S{12,}',
]
hits=[]
ext={'.py','.ps1','.md','.json','.sps','.txt','.yml','.yaml','.code-workspace','.csv'}
files=[x for x in p.rglob('*') if x.is_file() and x.suffix.lower() in ext]
for f in files:
 s=f.read_text(encoding='utf-8',errors='replace')
 for pat in patterns:
  if re.search(pat,s):
   hits.append((str(f.relative_to(p)),patterns.index(pat)+1))
print('SCANNED',len(files),'TEXT_FILES','POTENTIAL_MATCHES',hits,flush=True)
