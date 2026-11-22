from pathlib import Path
import zipfile,io,openpyxl,re,csv,hashlib,math
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
template=zipfile.ZipFile(base/'2019_1yr_Summary_FileTemplates_original.zip')
needed=['B15003_001']+[f'B15003_{n:03}' for n in range(22,26)]+['B23025_003','B23025_005','B19013_001','B17001_001','B17001_002']
mapping={}
for fn in template.namelist():
 if not re.fullmatch(r'seq\d+\.xlsx',fn):continue
 w=openpyxl.load_workbook(io.BytesIO(template.read(fn)),read_only=True,data_only=True)
 headers=next(w.active.values)
 for pos,value in enumerate(headers):
  if value in needed:
   assert value not in mapping,value
   mapping[value]=(int(fn[3:-5]),pos)
assert set(mapping)==set(needed),(set(needed)-set(mapping))
print('MAPPING',mapping,flush=True)
records=[]
for geo in ['DC','PR']:
 z=zipfile.ZipFile(base/f'{geo}_2019_ACS_1YR_summary_original.zip')
 assert z.testzip() is None
 geographic=list(csv.reader(io.StringIO(z.read(f'g20191{geo.lower()}.csv').decode('latin-1'))))
 stategeo=[r for r in geographic if r[2]=='040' and r[4]=='0000001']
 assert len(stategeo)==1,geo
 values={}
 for var,(seq,pos) in mapping.items():
  for kind in ['e','m']:
   f=f'{kind}20191{geo.lower()}{seq:04}000.txt'
   assert f in z.namelist(),(geo,var,f)
   matches=[r for r in csv.reader(io.StringIO(z.read(f).decode('utf-8'))) if len(r)>5 and r[5]=='0000001']
   assert len(matches)==1,(geo,var,f)
   val=matches[0][pos]
   assert val.strip() not in ['','-','N','(X)','**','***'],(geo,var,kind,val)
   values[(var,kind)]=float(val)
 print('VALUES',geo,values,flush=True)
 def rec(domain,estimate,unit,ref,method,moe=None,moetype='not directly published for derived statistic'):
  records.append(dict(jurisdiction=geo,source_product='2019 ACS/PRCS one-year Summary File Detailed Tables',reference_period='2019 one-year',domain=domain,estimate=round(estimate,4),unit=unit,margin_of_error=moe if moe is not None else '',moe_status='published 90% MOE' if moe is not None else moetype,source_variable_ids=ref,method=method,source_geography='state summary level 040 LOGRECNO 0000001',source_archive=f'01_Government_Sources/Phase2_Socioeconomic/Census/{geo}_2019_ACS_1YR_summary_original.zip',original_archive_sha256=hashlib.sha256((base/f'{geo}_2019_ACS_1YR_summary_original.zip').read_bytes()).hexdigest(),comparability_gate='NO_GO_CROSS_SIX'))
 education_num=sum(values[(f'B15003_{n:03}','e')] for n in range(22,26))
 education_den=values[('B15003_001','e')]
 rec('education',education_num/education_den*100,'percent','B15003_001,B15003_022..025','sum(022..025)/001 * 100; Bachelor degree or higher; numerator component MOEs archived')
 labor=values[('B23025_003','e')]
 rec('unemployment',values[('B23025_005','e')]/labor*100,'percent','B23025_003,B23025_005','B23025_005/B23025_003 * 100; ratio derived; exact MOE not published')
 rec('median_household_income',values[('B19013_001','e')],'2019_USD','B19013_001','direct table estimate',values[('B19013_001','m')])
 poverty_denom=values[('B17001_001','e')]
 rec('poverty',values[('B17001_002','e')]/poverty_denom*100,'percent','B17001_001,B17001_002','B17001_002/B17001_001 * 100; ratio derived; exact MOE not published')
 assert education_den>0 and labor>0 and poverty_denom>0
outfile=root/'02_SPSS_Data'/'Phase2'/'prdc_2019_acs_one_year_detailed_source_specific.csv'
assert not outfile.exists(),outfile
with outfile.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=records[0]);w.writeheader();w.writerows(records)
print('SAVED',outfile,len(records),'SHA256',hashlib.sha256(outfile.read_bytes()).hexdigest(),flush=True)
