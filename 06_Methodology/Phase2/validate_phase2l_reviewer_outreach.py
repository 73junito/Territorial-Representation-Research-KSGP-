from pathlib import Path
import hashlib

root = Path(r'I:\Territorial-Representation-Research')
draft = root / '09_Committee_Package/Phase2L_Greg_Belcher_Independent_Review_Request_Draft.md'
gate = root / '06_Methodology/Phase2/PHASE2L_REVIEWER_SELECTION_AND_OUTREACH_GATE.md'
assert draft.is_file() and gate.is_file()
draft_text = draft.read_text(encoding='utf-8')
gate_text = gate.read_text(encoding='utf-8')
assert 'UNSENT DRAFT' in draft_text  # Historically accurate draft status
assert 'USER-CONFIRMED SENT' in gate_text
assert 'student email' in gate_text
assert 'no message ID or delivery receipt inspected' in gate_text
assert 'PENDING' in gate_text and 'NO-GO' in gate_text
for p in (draft, gate):
    assert 'gbelcher@pittstate.edu' not in p.read_text(encoding='utf-8')
    print('PASS', p.name, hashlib.sha256(p.read_bytes()).hexdigest())
print('PHASE2L_SEND_REPORTED_BY_OWNER; DELIVERY_UNVERIFIED; FACULTY_REVIEW_PENDING')
