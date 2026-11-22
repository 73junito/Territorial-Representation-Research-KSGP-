from pathlib import Path
import re,zipfile,openpyxl,csv,hashlib
root=Path(r'I:\Territorial-Representation-Research')
c=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
dest=root/'02_SPSS_Data'/'Phase2'
names={'AS':'american-samoa','GU':'guam','MP':'cnmi','VI':'usvi'}
metrics={'education':'0200001','unemployment':'0510001','median_household_income':'0630001','poverty_total':'0900001','poverty_below':'0900002'}
records=[]
for geo,name in names.items():
 matrix=c/f'2020-iac-{name}-table-matrix.xlsx'
 source=c/f'{geo}_2020_demographic_profile_original.zip'
 w=openpyxl.load_workbook(matrix,read_only=True,data_only=True)
 fields={s:[] for s in range(1,5)}
 for row in w.worksheets[0].values:
  code=row[2]
  if code and re.fullmatch(r'DP[A-Z]{2}\d{7}',str(code)):
   seq=int(row[3])
   if geo=='VI' and code=='DPVI0860001':
    seq=3  # Matrix segment-column typo; table 86 belongs to segment 03
   fields[seq].append((code,row[1]))
 with zipfile.ZipFile(source) as z:
  assert z.testzip() is None
  raw={}
  for seg,layout in fields.items():
   filename=f'{geo.lower()}0000{seg}2020.dp'
   lines=z.read(filename).decode('utf-8').splitlines()
   matched=[line.split('|') for line in lines if line.startswith('DP'+geo+'|'+geo+'|000|'+f'{seg:02}'+'|0000001|')]
   assert len(matched)==1,(geo,seg,len(matched))
   cells=matched[0]
   assert len(cells)==len(layout)+5,(geo,seg,len(cells),len(layout))
   for idx,(code,label) in enumerate(layout,5):
    if code in {'DP'+geo+key for key in metrics.values()}:
     raw[code]={'value':cells[idx],'offset0':idx,'position1':idx+1,'segment':seg,'label':label,'file':filename}
  assert len(raw)==5,(geo,raw)
  for domain,key in metrics.items():
   m=raw['DP'+geo+key]
   print(geo,domain,m,flush=True)
  for domain,key,unit in [('education','0200001','percent'),('unemployment','0510001','percent'),('median_household_income','0630001','USD_2019'),('poverty','0900002','percent_derived')]:
   r=raw['DP'+geo+key]
   assert r['value'].strip() not in ['','-','N','(X)'],(geo,domain,r)
   val=float(r['value'])
   derivation=''
   denom=''
   if domain=='poverty':
    den=raw['DP'+geo+'0900001']
    assert den['value'].isdigit() and float(den['value'])>0
    val=round(100*val/float(den['value']),4)
    denom=den['value']
    derivation='100*DP'+geo+'0900002/DP'+geo+'0900001'
   else:
    derivation='Direct published table value'
   assert 0<=val<=100 if domain!='median_household_income' else val>0
   records.append(dict(jurisdiction=geo,domain=domain,value=val,unit=unit,source_variable='DP'+geo+key,source_label=r['label'],source_raw_value=r['value'],source_denominator_raw=denom,derivation=derivation,source_file=r['file'],source_segment=r['segment'],source_one_based_field_position=r['position1'],source_zero_based_field_offset=r['offset0'],source_archive=str(source.relative_to(root)),source_table_matrix=str(matrix.relative_to(root)),source_archive_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source_matrix_sha256=hashlib.sha256(matrix.read_bytes()).hexdigest(),reference_year='2019 for income and poverty; 2020 census for education and unemployment',comparability_gate='NO_GO_SIX_WAY'))
out=dest/'island_areas_2020_socioeconomic_source_specific.csv'
assert not out.exists(),str(out)+' already exists'
with out.open('w',newline='',encoding='utf-8-sig') as f:
 dw=csv.DictWriter(f,fieldnames=records[0].keys());dw.writeheader();dw.writerows(records)
print('SAVED',out,'RECORDS',len(records),'SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
