from pathlib import Path
import hashlib, csv
root=Path(r'I:\Territorial-Representation-Research')
paths=[
'09_Committee_Package/Phase2K_Faculty_Review_Handoff.md',
'09_Committee_Package/Phase2K_Faculty_Review_Decision_Form.md',
'09_Committee_Package/Phase2K_Faculty_Review_Request_Draft.md',
'06_Methodology/Phase2/PHASE2K_REVIEW_SUBMISSION_GATE.md']
for relative in paths:
 p=root/relative
 text=p.read_text(encoding='utf-8')
 assert len(text)>800 and p.exists(),p
 assert ('PENDING' in text.upper() or 'NOT SENT' in text.upper() or 'UNSENT' in text.upper()),p
 print('PASS',relative,'sha256',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
old=[
'08_Final_Report/Phase2J_Faculty_Academic_Review_Draft.md',
'06_Methodology/Phase2/PHASE2J_APA7_PRIMARY_SOURCE_REFERENCE_AUDIT.md',
'06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md',
'06_Methodology/Phase2/PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md',
'01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv']
assert all((root/x).is_file() for x in old)
print('REVIEW_HANDOFF_PREPARED_UNSENT; EXTERNAL_SIGNOFF_PENDING; PUBLICATION_NO_GO',flush=True)
