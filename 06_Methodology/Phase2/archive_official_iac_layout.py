import requests,pathlib,hashlib,openpyxl
base=pathlib.Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
urlbase='https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/'
items=['2020-iac-dpsf-technical-documentation.pdf','2020-iac-american-samoa-table-matrix.xlsx','2020-iac-guam-table-matrix.xlsx','2020-iac-cnmi-table-matrix.xlsx','2020-iac-usvi-table-matrix.xlsx']
for item in items:
 p=base/item
 if not p.exists():
  r=requests.get(urlbase+item,timeout=60);r.raise_for_status();assert (r.content.startswith(b'%PDF') if item.endswith('.pdf') else r.content.startswith(b'PK'))
  p.write_bytes(r.content)
 if item.endswith('.xlsx'):
  w=openpyxl.load_workbook(p,read_only=True,data_only=True)
  print('FILE',item,'SHEETS',[(s.title,s.max_row,s.max_column) for s in w.worksheets],flush=True)
  sh=w.worksheets[0]
  for row in list(sh.iter_rows(min_row=1,max_row=12,values_only=True)):
   print('ROW',str(row[:14])[:280],flush=True)
 print('ARCHIVED',item,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
