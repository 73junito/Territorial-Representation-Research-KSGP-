from pathlib import Path
import zipfile,io,openpyxl,re,csv,hashlib
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
z=zipfile.ZipFile(base/'2019_1yr_Summary_FileTemplates_original.zip')
vars=['B15003_001']+[f'B15003_{i:03}' for i in range(22,26)]+['B17001_001','B17001_002','B19013_001','B23025_003','B23025_005']
lookup={}
for name in z.namelist():
 if not re.fullmatch(r'seq\d+\.xlsx',name):continue
 heads=next(openpyxl.load_workbook(io.BytesIO(z.read(name)),read_only=True,data_only=True).active.values)
 for pos,var in enumerate(heads):
  if var in vars: lookup[var]=(int(name[3:-5]),pos)
assert set(lookup)==set(vars)
rows=[]
for geo in ('DC','PR'):
 p=base/f'{geo}_2019_ACS_1YR_summary_original.zip'
 with zipfile.ZipFile(p) as archive:
  assert archive.testzip() is None
  for var,(seq,offset) in lookup.items():
   for kind in ('e','m'):
    name=f'{kind}20191{geo.lower()}{seq:04}000.txt'
    r=[row for row in csv.reader(io.StringIO(archive.read(name).decode('latin-1'))) if len(row)>5 and row[5]=='0000001']
    assert len(r)==1
    num=r[0][offset]
    assert num.strip() and num not in ('-','N','(X)')
    rows.append(dict(jurisdiction=geo,reference_period='2019 ACS/PRCS one-year',table_variable=var,component_type='estimate' if kind=='e' else 'published_90pct_MOE',value=float(num),original_source_archive=p.name,original_source_file=name,sequence=seq,zero_based_column_offset=offset,logical_record_number='0000001',source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
out=root/'02_SPSS_Data'/'Phase2'/'prdc_2019_acs_one_year_raw_components_with_moe.csv'
assert not out.exists()
with out.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('ARCHIVED',out,len(rows),'SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
