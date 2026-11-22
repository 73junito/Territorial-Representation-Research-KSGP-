"""Independent, read-only Phase 2I Census published-MOE audit."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv
import hashlib
import json

root=Path(r'I:\Territorial-Representation-Research')
census=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
meth=root/'06_Methodology'/'Phase2'
sources=meth/'PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv'
classification=meth/'PHASE2I_PUBLISHED_MOE_ADJUDICATION.csv'
with sources.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
with classification.open(newline='',encoding='utf-8-sig') as f: check=list(csv.DictReader(f))
assert len(rows)==len(check)==12
index={(r['period'],r['jurisdiction'],r['domain']):r for r in check}
assert len(index)==12
rounded=lambda v: Decimal(str(v)).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
matched=0
for r in rows:
 k=(r['period'],r['jurisdiction'],r['domain'])
 assert k in index
 assert rounded(r['derived_estimate_pct'])==rounded(r['published_profile_estimate_pct'])
 expected='MATCH_AT_PUBLISHED_0_1_PP_PRECISION' if rounded(r['derived_moe90_pp'])==rounded(r['published_profile_moe90_pp']) else 'DISCREPANCY_REQUIRES_VARIANCE_METHOD_REVIEW'
 assert index[k]['comparison_result']==expected
 matched+=expected.startswith('MATCH_')
 name=r['source_archive']
 p=census/name
 assert p.exists()
 raw=json.loads(p.read_text(encoding='utf-8'))
 assert len(raw)==2
 fields=dict(zip(*raw))
 assert fields['state']==r['source_geography_fips']
 assert Decimal(str(fields[r['published_profile_moe_variable']]))==Decimal(r['published_profile_moe90_pp'])
 assert Decimal(str(fields[r['published_profile_estimate_variable']]))==Decimal(r['published_profile_estimate_pct'])
assert matched==10 and len(rows)-matched==2
assert {(r['jurisdiction'],r['domain']) for r in check if 'DISCREPANCY' in r['comparison_result']}=={('DC','education')}
assert (meth/'PHASE2I_PUBLISHED_MOE_RECONCILIATION_REPORT.md').exists()
print('PASS 12 official estimates agree at 0.1pp; 10 MOE matches; two DC education differences verified')
for p in [sources,classification]:
 print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
