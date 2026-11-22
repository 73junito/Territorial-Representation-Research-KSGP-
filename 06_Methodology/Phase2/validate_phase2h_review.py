from pathlib import Path
import csv,hashlib
root=Path(r'I:\Territorial-Representation-Research')
m=root/'06_Methodology'/'Phase2'
p=m/'PHASE2H_MOE_RECONCILIATION_MATRIX.csv'
with p.open(encoding='utf-8-sig',newline='') as f:r=list(csv.DictReader(f))
assert len(r)==12
assert len({(x['jurisdiction'],x['period'],x['domain']) for x in r})==12
for x in r:
 assert x['published_profile_moe_variable'].startswith('DP02PR_' if x['jurisdiction']=='PR' and x['domain']=='education' else 'DP02_' if x['domain']=='education' else 'DP03_')
 assert x['published_profile_estimate_pct']==x['published_profile_moe90_pp']==x['moe_delta_pp']==''
 assert x['reconciliation_status'].startswith('BLOCKED_')
 assert 0<float(x['derived_moe90_pp'])<20
docs=[m/'PHASE2H_PUBLISHED_MOE_RECONCILIATION.md',m/'PHASE2H_ARCHIVAL_ROOT_CAUSE_REVIEW.md',m/'PHASE2H_ACADEMIC_QUALITY_AUDIT.md',m/'PHASE2H_ACCEPTANCE_DECISION.md',root/'08_Final_Report'/'Phase2H_Academic_Quality_Assurance_Review_Draft.md',root/'09_Committee_Package'/'Phase2H_Committee_Research_Brief_Review_Draft.md']
for x in docs:
 assert x.exists() and x.stat().st_size>500
 content=x.read_text(encoding='utf-8')
 assert any(t in content.upper() for t in ['BLOCKED','PENDING','OPEN'])
 print('VALIDATED',x.name,hashlib.sha256(x.read_bytes()).hexdigest(),flush=True)
print('VALIDATED_MATRIX',len(r),'published-MOE responses unverified and unfilled',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
print('PHASE2H_ACCEPTANCE CONDITIONAL; PUBLICATION_NO_GO; NUMERIC_PROFILE_RECONCILIATION 0/12',flush=True)
