from pathlib import Path
import csv,hashlib,json
root=Path(r'I:\Territorial-Representation-Research')
f=[
root/'06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md',
root/'06_Methodology/Phase2/PHASE2J_ACADEMIC_METHODS_REVIEW_GATE.md',
root/'08_Final_Report/Phase2J_Faculty_Academic_Review_Draft.md',
root/'09_Committee_Package/Phase2J_Committee_Review_Brief_Draft.md']
for p in f:
 assert p.exists() and p.stat().st_size>800,p
 s=p.read_text(encoding='utf-8')
 assert ('NO-GO' in s or 'not authorize' in s or 'NO-GO' in s.upper()),p.name
 assert ('pending' in s.lower() or 'not yet' in s.lower()),p.name
 print('PASS_DOC',p.name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest())
with (root/'01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv').open(encoding='utf-8-sig',newline='') as file:rows=list(csv.DictReader(file))
assert len(rows)==17
for r in rows:
 q=root/r['relative_path'];assert hashlib.sha256(q.read_bytes()).hexdigest()==r['sha256'],q
with (root/'06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv').open(encoding='utf-8-sig',newline='') as file: rows=list(csv.DictReader(file))
assert len(rows)==12
assert sum('MATCH_' in r['comparison_result'] for r in rows)==10
diagnostic=root/'06_Methodology/Phase2/PHASE2I_DC_EDUCATION_VARIANCE_DIAGNOSTIC.csv'
with diagnostic.open(encoding='utf-8-sig',newline='') as file:r=list(csv.DictReader(file))
assert len(r)==2
assert all(round(float(x['direct_count_method_derived_rate_moe90_pp']),1)==float(x['published_profile_rate_moe90_pp']) for x in r)
old=root/'08_Final_Report/Phase2F_Integrated_Demographic_Socioeconomic_Research_Report.md'
assert old.exists()
print('PASS_RESEARCH_PROVENANCE',17,'phase2i_reconciled',12,'historical_phase2f_intact',hashlib.sha256(old.read_bytes()).hexdigest())
print('PHASE2J_INTERNAL_QA_PASS; EXTERNAL_ACADEMIC_REVIEW_PENDING; PUBLICATION_NO_GO')
