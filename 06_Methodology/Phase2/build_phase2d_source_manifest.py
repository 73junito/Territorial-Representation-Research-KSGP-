from pathlib import Path
import csv,hashlib,zipfile
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'
c=base/'Census'
prefix='https://www2.census.gov/programs-surveys/'
ia=prefix+'decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/'
acs=prefix+'acs/summary_file/'
urls={
 '2020-iac-dpsf-technical-documentation.pdf':ia+'2020-iac-dpsf-technical-documentation.pdf',
 '2020-iac-american-samoa-table-matrix.xlsx':ia+'2020-iac-american-samoa-table-matrix.xlsx',
 '2020-iac-guam-table-matrix.xlsx':ia+'2020-iac-guam-table-matrix.xlsx',
 '2020-iac-cnmi-table-matrix.xlsx':ia+'2020-iac-cnmi-table-matrix.xlsx',
 '2020-iac-usvi-table-matrix.xlsx':ia+'2020-iac-usvi-table-matrix.xlsx',
 '2019_1yr_Summary_FileTemplates_original.zip':acs+'2019/data/2019_1yr_Summary_FileTemplates.zip',
 '2020_5yr_Summary_FileTemplates_original.zip':acs+'2020/data/2020_5yr_Summary_FileTemplates.zip',
 'DC_2019_ACS_1YR_summary_original.zip':acs+'2019/data/1_year_by_state/DistrictofColumbia_All_Geographies.zip',
 'PR_2019_ACS_1YR_summary_original.zip':acs+'2019/data/1_year_by_state/PuertoRico_All_Geographies.zip',
}
for geo,area in [('DC','DistrictOfColumbia'),('PR','PuertoRico')]:
 for seq in (42,47,58,78):
  fname=f'{geo}_2020_ACS_5YR_seq{seq:04}_original.zip'
  urls[fname]=acs+f'2020/data/5_year_seq_by_state/{area}/All_Geographies_Not_Tracts_Block_Groups/20205{geo.lower()}{seq:04}000.zip'
rows=[]
for name,url in urls.items():
 p=c/name
 assert p.exists(),p
 if p.suffix=='.zip':
  with zipfile.ZipFile(p) as z:assert z.testzip() is None
 else:assert p.stat().st_size>1000
 rows.append(dict(filename=name,source_url=url,relative_path=str(p.relative_to(root)),size_bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),integrity='ZIP_CRC_PASS' if p.suffix=='.zip' else 'FILE_HEADER_VALID'))
out=base/'phase2d_official_acquisition_manifest.csv'
assert not out.exists()
with out.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('SAVED MANIFEST',len(rows),out,'HASH',hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
