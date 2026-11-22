from pathlib import Path
import csv,hashlib,re
ROOT=Path(r'I:\Territorial-Representation-Research')
a=ROOT/'08_Final_Report'/'Phase2E_Source_Specific_Evidence_Appendix.md'
b=ROOT/'06_Methodology'/'Phase2'/'PHASE2E_UNCERTAINTY_HARMONIZATION_GATE.md'
assert a.exists() and b.exists()
appendix=a.read_text(encoding='utf-8')
gate=b.read_text(encoding='utf-8')
data=ROOT/'02_SPSS_Data'/'Phase2'
names=[
 'island_areas_2020_socioeconomic_source_specific.csv',
 'prdc_2019_acs_one_year_detailed_source_specific.csv',
 'prdc_2020_acs_five_year_detailed_source_specific.csv',
]
total=0
for fn in names:
 with (data/fn).open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
 total+=len(rows)
 for r in rows:
  place={'AS':'American Samoa','GU':'Guam','MP':'Northern Mariana Islands','VI':'U.S. Virgin Islands','PR':'Puerto Rico','DC':'Washington, D.C.'}[r['jurisdiction']]
  assert place in appendix
  domain=r['domain'].replace('_',' ').title()
  assert domain in appendix,domain
assert total==32
assert appendix.count('Published median 90% MOE; symmetric interval')==4
assert appendix.count('Published component count MOEs available; derived ratio interval not calculated')==12
assert 'NO-GO' in gate and 'CONDITIONAL' in gate
assert 'not yet been calculated' in gate
assert 'byte-hash' in gate
for p in (a,b):
 print('PASS',p.name,'bytes',p.stat().st_size,'SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
print('PASS 32 evidence records, four income intervals, 12 deferred rate intervals, decisions and preservation caveat',flush=True)
