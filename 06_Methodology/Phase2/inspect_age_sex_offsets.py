import zipfile,pathlib,pandas as pd
root=pathlib.Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
m=pd.read_excel(root/'2020-dhc-table-matrix.xlsx',sheet_name='DHC Table_Segments')
print('SEGMENT6',m[m.iloc[:,1].astype(str)=='6'].to_string(index=False))
t=pd.read_excel(root/'2020-dhc-table-matrix.xlsx',sheet_name='DHC Table Matrix',header=None)
for start in list(t.index[t.iloc[:,2].astype(str).str.fullmatch('P0120001')])[:1]:
 print('P12 MATRIX',t.iloc[start:start+55].to_string(index=False,header=False))
for geo in ('DC','PR'):
 z=zipfile.ZipFile(root/f'{geo}_2020_DHC_original.zip')
 print('GEO FILES',[n for n in z.namelist() if 'geo' in n.lower()])
 g=next(n for n in z.namelist() if 'geo' in n.lower())
 for line in z.open(g):
  f=line.decode('utf-8-sig').strip().split('|')
  if '040' in f[:5] or '689545' in f or '3285874' in f:
   print('GEOGRAPHY',geo,f[:21],len(f));break
 seg=f'{geo.lower()}000062020.dhc'
 for line in z.open(seg):
  f=line.decode('utf-8-sig').strip().split('|')
  print('SEG6 HEAD',geo,f[:35],len(f));break
