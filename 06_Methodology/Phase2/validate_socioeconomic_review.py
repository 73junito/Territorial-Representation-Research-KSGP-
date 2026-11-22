from pathlib import Path
import csv,json,hashlib,zipfile
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'
files=['socioeconomic_source_register.csv','socioeconomic_comparability_matrix.csv']
for x in files:assert (base/x).exists()
with (base/files[0]).open(encoding='utf-8-sig',newline='') as f: reg=list(csv.DictReader(f))
with (base/files[1]).open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
assert len(reg)==6 and len(rows)==24
assert len({(x['geo_code'],x['topic']) for x in rows})==24
assert {x['geo_code'] for x in rows}=={'AS','GU','MP','VI','DC','PR'}
assert {x['topic'] for x in rows}=={'education','employment','household_income','poverty'}
assert all(x['cross_six_gate']=='NO_GO_CROSS_SIX' for x in rows)
for x in reg:
 p=root/x['local_file'];assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256']
 if p.suffix=='.zip':
  with zipfile.ZipFile(p) as z:assert z.testzip() is None
 else: assert 'variables' in json.loads(p.read_text(encoding='utf-8'))
for x in rows:
 assert x['source_label'] and x['variable_id']
 assert (root/x['original_file']).exists()
 assert (x['downloaded_observations']=='YES_ARCHIVE_PRESENT_NOT_PARSED')==(x['geo_code'] in {'AS','GU','MP','VI'})
assert (root/'06_Methodology'/'Phase2'/'SOCIOECONOMIC_COMPARABILITY_REVIEW.md').exists()
print('PASS 24/24 metadata variable assessments')
print('PASS 6/6 official-source integrity checks')
print('PASS explicit NO-GO comparability classification')
print('PASS numerical observations not misstated as downloaded for PR/DC')
