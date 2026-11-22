from pathlib import Path
import csv,zipfile,hashlib,json
import pandas as pd
import pyreadstat

root=Path(r'I:\Territorial-Representation-Research')
source=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'Census'
destination=root/'02_SPSS_Data'/'Phase2'
methods=root/'06_Methodology'/'Phase2'
population={'PR':3285874,'DC':689545,'GU':153836,'VI':87146,'AS':49710,'MP':47329}
names={'PR':'Puerto Rico','DC':'Washington, D.C.','GU':'Guam','VI':'U.S. Virgin Islands','AS':'American Samoa','MP':'Northern Mariana Islands'}
records=[]
for code in ['PR','DC','GU','VI','AS','MP']:
 if code in ('PR','DC'):
  path=source/f'{code}_2020_DHC_original.zip'
  segment=f'{code.lower()}000062020.dhc'
  with zipfile.ZipFile(path) as archive:
   rows=archive.read(segment).decode('utf-8-sig').splitlines()
  first=rows[0].split('|')
  assert first[:5]==['DHCST',code,'000','06','0000001'],(code,first[:5])
  # DHC state file segment 06: first 5 header columns; P10 71 records, P11 73 records;
  # P12 variable 1 therefore begins at zero-based index 5+71+73=149.
  off=149
  total=int(first[off])
  male=int(first[off+1])
  female=int(first[off+25])
  male_age=[int(v) for v in first[off+2:off+25]]
  female_age=[int(v) for v in first[off+26:off+49]]
  assert len(male_age)==23 and len(female_age)==23
  assert sum(male_age)==male and sum(female_age)==female
  under20=sum(male_age[:5])+sum(female_age[:5])
  over65=sum(male_age[17:])+sum(female_age[17:])
  # P12 age entries 65-66 to 85+ are positions 18..23 (0-based 17..22)
  origin='2020 DHC P12, segment 06, state summary'
 else:
  path=source/f'{code}_2020_demographic_profile_original.zip'
  segment=f'{code.lower()}000012020.dp'
  with zipfile.ZipFile(path) as archive:rows=archive.read(segment).decode('utf-8-sig').splitlines()
  first=rows[0].split('|')
  assert first[:5]==['DP'+code,code,'000','01','0000001'],(code,first[:5])
  total=int(first[5])
  male=int(first[24])
  female=int(first[43])
  # DP1 includes 18 five-year groups spanning 0-4 .. 85+
  all_age=[int(x) for x in first[6:24]]
  male_age=[int(x) for x in first[25:43]]
  female_age=[int(x) for x in first[44:62]]
  assert len(all_age)==len(male_age)==len(female_age)==18
  assert sum(all_age)==total and sum(male_age)==male and sum(female_age)==female
  under20=sum(all_age[:4])
  over65=sum(all_age[13:])
  origin='2020 Island Area DP1, segment 01, area summary'
 assert total==population[code],(code,total,population[code])
 assert male+female==total
 assert under20+over65<=total
 rec=dict(geo_code=code,jurisdiction=names[code],population_2020=total,male_2020=male,female_2020=female,under20_2020=under20,age20to64_2020=total-under20-over65,age65plus_2020=over65,male_pct=100*male/total,female_pct=100*female/total,under20_pct=100*under20/total,age65plus_pct=100*over65/total,source_file=path.name,source_segment=segment,source_method=origin)
 records.append(rec)
 print('CHECKED',code,'POP',total,'M',male,'F',female,'<20',under20,'65+',over65,flush=True)
df=pd.DataFrame(records)
assert int(df.population_2020.sum())==4313440
for row in df.to_dict('records'):
 assert abs(row['male_pct']+row['female_pct']-100)<1e-9
 assert row['under20_2020']+row['age20to64_2020']+row['age65plus_2020']==row['population_2020']
df.to_csv(destination/'age_sex_2020_six_jurisdictions.csv',index=False,encoding='utf-8-sig')
labels={
 'geo_code':'US Census jurisdiction code',
 'jurisdiction':'Jurisdiction name',
 'population_2020':'Resident population, 2020 Census',
 'male_2020':'2020 population identified as male',
 'female_2020':'2020 population identified as female',
 'under20_2020':'2020 resident population under age 20',
 'age20to64_2020':'2020 resident population ages 20 to 64',
 'age65plus_2020':'2020 resident population age 65 and older',
 'male_pct':'Male population / total residents times 100',
 'female_pct':'Female population / total residents times 100',
 'under20_pct':'Under 20 population / total residents times 100',
 'age65plus_pct':'Age 65 and over population / total residents times 100',
 'source_file':'Original official ZIP file',
 'source_segment':'Original Census flat-file segment',
 'source_method':'Original Census product and table'
}
pyreadstat.write_sav(df,str(destination/'age_sex_2020_six_jurisdictions.sav'),column_labels=labels)
check,_=pyreadstat.read_sav(str(destination/'age_sex_2020_six_jurisdictions.sav'))
assert len(check)==6
for c in df.columns:
 if pd.api.types.is_numeric_dtype(df[c]):
  assert abs(check[c]-df[c]).max()<1e-8
 else:
  assert (check[c]==df[c]).all()
manifest=root/'01_Government_Sources'/'Phase2_Socioeconomic'/'age_sex_pilot_source_manifest.csv'
with manifest.open('w',encoding='utf-8-sig',newline='') as f:
 columns=['geo_code','population_2020','source_file','source_segment','source_method','sha256']
 w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
 for r in records:
  path=source/r['source_file']
  w.writerow({**{k:r[k] for k in columns if k!='sha256'},'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
print('RESULT',df[['geo_code','male_pct','under20_pct','age65plus_pct']].to_string(index=False),flush=True)
print('SAV_AND_CSV_VALIDATED',len(df),flush=True)
