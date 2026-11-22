from pathlib import Path
import requests,zipfile,openpyxl,io,re,hashlib
b=Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
p=b/'2020_5yr_Summary_FileTemplates_original.zip'
if not p.exists():
 r=requests.get('https://www2.census.gov/programs-surveys/acs/summary_file/2020/data/2020_5yr_Summary_FileTemplates.zip',timeout=60);r.raise_for_status();p.write_bytes(r.content)
with zipfile.ZipFile(p) as z:
 assert z.testzip() is None
 needed=['B15003_001']+[f'B15003_{i:03}' for i in range(22,26)]+['B23025_003','B23025_005','B19013_001','B17001_001','B17001_002']
 mapping={}
 for f in z.namelist():
  fname=f.split('/')[-1]
  if not re.fullmatch(r'seq[0-9]+\.xlsx',fname):continue
  header=next(openpyxl.load_workbook(io.BytesIO(z.read(f)),read_only=True,data_only=True).active.values)
  for idx,k in enumerate(header):
   if k in needed:mapping[k]=(int(fname[3:-5]),idx)
 assert set(mapping)==set(needed),(set(needed)-set(mapping))
 print('2020_5YR_TEMPLATE',p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),'MAPPING',mapping,flush=True)
 seqs=sorted({x[0] for x in mapping.values()})
 for geo,name in [('DC','DistrictOfColumbia'),('PR','PuertoRico')]:
  for seq in seqs:
   fn=f'20205{geo.lower()}{seq:04}000.zip'
   dest=b/f'{geo}_2020_ACS_5YR_seq{seq:04}_original.zip'
   if not dest.exists():
    u=f'https://www2.census.gov/programs-surveys/acs/summary_file/2020/data/5_year_seq_by_state/{name}/All_Geographies_Not_Tracts_Block_Groups/{fn}'
    res=requests.get(u,timeout=60);res.raise_for_status()
    assert res.content.startswith(b'PK')
    dest.write_bytes(res.content)
   with zipfile.ZipFile(dest) as zi:
    assert zi.testzip() is None
    print('SOURCE',geo,seq,dest.stat().st_size,zi.namelist()[:5],hashlib.sha256(dest.read_bytes()).hexdigest(),flush=True)
