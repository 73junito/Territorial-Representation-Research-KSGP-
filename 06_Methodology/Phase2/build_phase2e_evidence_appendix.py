from pathlib import Path
import csv,hashlib,zipfile,collections
ROOT=Path(r'I:\Territorial-Representation-Research')
DATA=ROOT/'02_SPSS_Data'/'Phase2'
SRC=ROOT/'01_Government_Sources'/'Phase2_Socioeconomic'
def read(name):
 with (DATA/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
islands=read('island_areas_2020_socioeconomic_source_specific.csv')
a19=read('prdc_2019_acs_one_year_detailed_source_specific.csv')
a20=read('prdc_2020_acs_five_year_detailed_source_specific.csv')
components19=read('prdc_2019_acs_one_year_raw_components_with_moe.csv')
components20=read('prdc_2020_acs_five_year_raw_components_with_moe.csv')
assert (len(islands),len(a19),len(a20),len(components19),len(components20))==(16,8,8,40,40)
manifest=list(csv.DictReader((SRC/'phase2d_official_acquisition_manifest.csv').open(encoding='utf-8-sig')))
assert len(manifest)==17
for r in manifest:
 p=ROOT/r['relative_path']
 assert p.is_file() and p.stat().st_size==int(r['size_bytes'])
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
 if p.suffix.lower()=='.zip':
  with zipfile.ZipFile(p) as z:assert z.testzip() is None
def fmt(domain,val):
 if domain=='median_household_income':return '$'+format(float(val),',.0f')
 return f'{float(val):.2f}%'
name={'AS':'American Samoa','GU':'Guam','MP':'Northern Mariana Islands','VI':'U.S. Virgin Islands','DC':'Washington, D.C.','PR':'Puerto Rico'}
lines=['# TRR Phase 2E — Source-Specific Socioeconomic Evidence Appendix','',
'**Evidence date:** November 21, 2026  ',
'**Scope:** 32 jurisdiction-domain-product observations: 16 Island Areas 2020 Census, eight 2019 one-year ACS/PRCS, eight 2016–2020 five-year ACS/PRCS. These three products **must not be treated as one harmonized six-jurisdiction dataset**.','',
'## A. Original source families and uncertainty',
'- **2020 Island Areas Census Demographic Profile:** AS, GU, MP, VI; education and unemployment tabulated in the 2020 Census, income and poverty reference 2019; census table percentages and poverty ratio. No ACS sample MOE is assigned to these census values. Different population and military-housing universes exist.',
'- **2019 ACS/PRCS one-year Detailed Tables:** DC and PR; sample estimates with published underlying count MOEs at the **90% confidence level**. Income figures are in 2019 inflation-adjusted dollars, not automatically interchangeable with an Island Areas income universe.',
'- **2016–2020 ACS/PRCS five-year Detailed Tables:** DC and PR; pooled sample estimates with published underlying count MOEs at the **90% confidence level**. Median income figures are expressed in 2020 inflation-adjusted dollars.',
'- **All ACS-derived percentage measures:** This extraction preserves original numerator/denominator count MOEs. It does not yet calculate a valid ratio MOE or 90% interval. A component MOE is not a ratio MOE; the displayed point estimate alone is not a significance test.',
'','## B. Island Areas 2020 Census original profile values',
'','| Jurisdiction | Measure | Original value | Official source field | Segment / one-based field | Poverty denominator (where applicable) |',
'|---|---|---:|---|---|---:|']
for r in sorted(islands,key=lambda x:(x['jurisdiction'],x['domain'])):
 lines.append(f"| {name[r['jurisdiction']]} | {r['domain'].replace('_',' ').title()} | {fmt(r['domain'],r['value'])} | `{r['source_variable']}` | {r['source_segment']} / {r['source_one_based_field_position']} | {r.get('source_denominator_raw') or '—'} |")
lines += ['','**Field validation:** All Island Areas values were extracted from the island-wide `LOGRECNO=0000001` row using the original government matrix workbooks, with exact segment and offset recorded in the source-specific CSV. Poverty derives from below-poverty population divided by population for whom poverty status is determined.','']
for label,arr in [('C. 2019 ACS/PRCS one-year detailed values',a19),('D. 2016–2020 ACS/PRCS five-year detailed values',a20)]:
 lines += ['## '+label,'','| Jurisdiction | Measure | Point estimate | Published income MOE / 90% interval | Source Detailed Table fields | Uncertainty classification |','|---|---|---:|---|---|---|']
 for r in sorted(arr,key=lambda x:(x['jurisdiction'],x['domain'])):
  moe=r['margin_of_error'].strip()
  if r['domain']=='median_household_income' and moe:
   val=float(r['estimate']);m=float(moe)
   ci=f"± ${m:,.0f}; [${val-m:,.0f}, ${val+m:,.0f}]"
   unc='Published median 90% MOE; symmetric interval from estimate ± MOE'
  else:
   ci='Not available for derived rate'
   unc='Published component count MOEs available; derived ratio interval not calculated'
  lines.append(f"| {name[r['jurisdiction']]} | {r['domain'].replace('_',' ').title()} | {fmt(r['domain'],r['estimate'])} | {ci} | `{r['source_variable_ids']}` | {unc} |")
 lines += ['']
lines += ['## E. Provenance and limitations',
'- Original government source URLs, hashes and file size: `01_Government_Sources/Phase2_Socioeconomic/phase2d_official_acquisition_manifest.csv` (17 files).',
'- Detailed source-specific observation CSVs and 80 estimate/MOE component records: `02_SPSS_Data/Phase2/`.',
'- Reproducible scripts: `06_Methodology/Phase2/extract_verified_island_socioeconomic.py`, `extract_2019_prdc_acs_detailed.py`, `extract_2019_acs_moe_components.py`, `extract_2020_prdc_acs_detailed.py`, `validate_phase2d_numeric_acquisition.py`.',
'- Island Areas source definitions and exclusions must be taken from the four product-specific table matrices and the official `2020-iac-dpsf-technical-documentation.pdf`. Not every Area has the same household/military-housing universe.',
'- Census/PRCS sample estimates and 2020 Island Areas decennial profiles differ in survey design, time base, possible sampling error, population scope and dollars. In particular, Washington, D.C. is a federal district, **not** a U.S. territory.',
'- Do not infer voting eligibility, citizenship proportions, self-determination preferences or policy views from these aggregate measures.',
'','## F. Preservation exception',
'The previously audited age-and-sex SPSS .sav byte hash differs from the current SHA-256. All six jurisdiction records and all substantive source values reconcile with CSV after sorting by geo_code. **Byte-level continuity remains OPEN**, regardless of matching data contents. Do not overwrite, repair, or re-sort the .sav to force a matching hash.',
'']
OUT=ROOT/'08_Final_Report'/'Phase2E_Source_Specific_Evidence_Appendix.md'
assert not OUT.exists(),OUT
OUT.write_text('\n'.join(lines),encoding='utf-8')
print('APPENDIX_WRITTEN',OUT,'LINES',len(lines),'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest(),flush=True)
