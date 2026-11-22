from pathlib import Path
import hashlib
root=Path(r'I:\Territorial-Representation-Research')
paths=[
'09_Committee_Package/Phase2L_Greg_Belcher_Independent_Review_Request_Draft.md',
'06_Methodology/Phase2/PHASE2L_REVIEWER_SELECTION_AND_OUTREACH_GATE.md'
]
for name in paths:
 p=root/name
 assert p.exists()
 content=p.read_text(encoding='utf-8')
 assert ('UNSENT' in content or 'NOT SENT' in content)
 assert ('approval' in content.lower() or 'review' in content.lower())
 assert 'gbelcher@pittstate.edu' not in content
 print('PASS',name,hashlib.sha256(p.read_bytes()).hexdigest())
for name in [
'09_Committee_Package/Phase2K_Faculty_Review_Handoff.md',
'08_Final_Report/Phase2J_Faculty_Academic_Review_Draft.md',
'06_Methodology/Phase2/PHASE2I_DC_EDUCATION_MOE_ROOT_CAUSE_REVIEW.md'
]:
 assert (root/name).is_file()
print('PHASE2L_REVIEWER_CANDIDATE_IDENTIFIED_INVITATION_DRAFTED_UNSENT_PUBLICATION_NO_GO')
