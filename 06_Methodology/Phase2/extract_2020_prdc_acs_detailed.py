from pathlib import Path
import zipfile,io,openpyxl,re,csv,hashlib
root=Path(r'I:\Territorial-Representation-Research')
base=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
template=zipfile.ZipFile(base/'2020_5yr_Summary_FileTemplates_original.zip')
needed=['B15003_001']+[f'B15003_{n:03}' for n in range(22,26)]+['B23025_003','B23025_005','B19013_001','B17001_001','B17001_002']
mapping={}
for fn in template.namelist():
 name=fn.split('/')[-1]
 if not re.fullmatch(r'seq\d+\.xlsx',name):continue
 w=openpyxl.load_workbook(io.BytesIO(template.read(fn)),read_only=True,data_only=True)
 header=next(w.active.values)
 for pos,value in enumerate(header):
  if value in needed:
   assert value not in mapping,value
   mapping[value]=(int(name[3:-5]),pos)
assert set(mapping)==set(needed),(set(needed)-set(mapping))
rows=[]
components=[]
for geo in ['DC','PR']:
 values={}
 for var,(seq,pos) in mapping.items():
  archive=base/f'{geo}_2020_ACS_5YR_seq{seq:04}_original.zip'
  with zipfile.ZipFile(archive) as z:
   assert z.testzip() is None
   for kind in ['e','m']:
    filename=f'{kind}20205{geo.lower()}{seq:04}000.txt'
    assert filename in z.namelist()
    matches=[r for r in csv.reader(io.StringIO(z.read(filename).decode('latin-1'))) if len(r)>5 and r[5]=='0000001']
    assert len(matches)==1,(geo,var,filename)
    val=matches[0][pos]
    assert val.strip() not in ('','-','N','(X)','**','***'),(geo,var,kind,val)
    values[(var,kind)]=float(val)
    components.append(dict(jurisdiction=geo,reference_period='2016-2020 ACS/PRCS 5-year',table_variable=var,component_type='estimate' if kind=='e' else 'published_90pct_MOE',value=float(val),original_source_archive=archive.name,original_source_file=filename,sequence=seq,zero_based_column_offset=pos,logical_record_number='0000001',source_sha256=hashlib.sha256(archive.read_bytes()).hexdigest()))
 print('COMPONENTS',geo,values,flush=True)
 def add(domain,val,unit,variables,method,moe=None):
  rows.append(dict(jurisdiction=geo,source_product='2016-2020 ACS/PRCS 5-year Summary File Detailed Tables',reference_period='2016-2020 five-year',domain=domain,estimate=round(val,4),unit=unit,margin_of_error=moe if moe is not None else '',moe_status='Published table 90% MOE' if moe is not None else 'Derived ratio has no directly published MOE; underlying component MOEs archived',source_variable_ids=variables,method=method,source_geography='state summary level 040 LOGRECNO 0000001',source_archives=';'.join(sorted({f"{geo}_2020_ACS_5YR_seq{mapping[v][0]:04}_original.zip" for v in variables.replace('..025',',B15003_023,B15003_024,B15003_025').split(',')})),comparability_gate='NO_GO_CROSS_SIX'))
 edu=sum(values[(f'B15003_{n:03}','e')] for n in range(22,26))/values[('B15003_001','e')]*100
 unemployment=values[('B23025_005','e')]/values[('B23025_003','e')]*100
 poverty=values[('B17001_002','e')]/values[('B17001_001','e')]*100
 add('education',edu,'percent','B15003_001,B15003_022..025','Sum bachelor/master/professional/doctorate over age 25+ total')
 add('unemployment',unemployment,'percent','B23025_003,B23025_005','Unemployed divided by civilian labor force')
 add('median_household_income',values[('B19013_001','e')],'USD_2020_inflation_adjusted','B19013_001','Direct median household income table value',values[('B19013_001','m')])
 add('poverty',poverty,'percent','B17001_001,B17001_002','Below poverty count over population for whom status determined')
outdir=root/'02_SPSS_Data'/'Phase2'
files=[(outdir/'prdc_2020_acs_five_year_detailed_source_specific.csv',rows),(outdir/'prdc_2020_acs_five_year_raw_components_with_moe.csv',components)]
for path,data in files:
 assert not path.exists(),path
 with path.open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=data[0]);w.writeheader();w.writerows(data)
 print('SAVED',path,len(data),'SHA256',hashlib.sha256(path.read_bytes()).hexdigest(),flush=True)
