import openpyxl,pathlib,re,zipfile
b=pathlib.Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
names={'AS':'american-samoa','GU':'guam','MP':'cnmi','VI':'usvi'}
for g,name in names.items():
 w=openpyxl.load_workbook(b/f'2020-iac-{name}-table-matrix.xlsx',read_only=True,data_only=True)
 v={s:[] for s in range(1,5)}
 for i,row in enumerate(w.worksheets[0].values,1):
  if row[2] and re.fullmatch(r'DP[A-Z]{2}\d{7}',str(row[2])) and str(row[3]) in ['1','2','3','4']:
   v[int(row[3])].append((row[2],row[1],i))
 print(g,[(s,len(rows),rows[:2],rows[-2:]) for s,rows in v.items()],flush=True)
 z=zipfile.ZipFile(b/f'{g}_2020_demographic_profile_original.zip')
 for s,rows in v.items():
  line=z.read(f'{g.lower()}0000{s}2020.dp').decode('utf-8').splitlines()[0].split('|')
  print('SEGMENT',s,'CELL_COUNT',len(line)-5,'MATRIX_COUNT',len(rows),'MATCH',len(line)-5==len(rows),flush=True)
