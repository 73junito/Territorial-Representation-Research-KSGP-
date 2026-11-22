from pathlib import Path
import requests,pandas as pd
root=Path(r'I:\Territorial-Representation-Research')
folder=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
base='https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/complete-tech-docs/demographic-and-housing-characteristics-file-and-demographic-profile/'
for name in ['2020-dhc-table-matrix.xlsx','2020-dp1-table.xlsx','sl-sequence-list-dhc-state-ph.xlsx','geoheader-2020-dhc-state.xlsx']:
 p=folder/name
 r=requests.get(base+name,timeout=20);r.raise_for_status();p.write_bytes(r.content)
 book=pd.ExcelFile(p)
 print('FILE',name,'SIZE',len(r.content),'SHEETS',book.sheet_names,flush=True)
 for sheet in book.sheet_names[:2]:
  frame=pd.read_excel(p,sheet_name=sheet,header=None)
  print('HEAD',sheet,frame.shape,frame.head(8).to_string(index=False,header=False)[:1300],flush=True)
  mask=frame.astype(str).apply(lambda s:s.str.contains(r'P12|SEX BY AGE|Male|Female',case=False,regex=True)).any(axis=1)
  print('MATCHES',frame[mask].head(8).to_string(index=False,header=False)[:1400],flush=True)
