from pathlib import Path
import zipfile, re, hashlib
import pyreadstat
root=Path(r"I:\Territorial-Representation-Research")
for n in ["population_2010_2020.sav","population_2010_2021.sav"]:
 p=root/"02_SPSS_Data"/n
 df,meta=pyreadstat.read_sav(str(p))
 print("FILE",n,"sha256",hashlib.sha256(p.read_bytes()).hexdigest(),"rows",len(df),"columns",list(df.columns))
 print(df.to_string(index=False))
p=root/"04_SPSS_Output"/"01_population_comparison.spv"
print("SPV sha256",hashlib.sha256(p.read_bytes()).hexdigest(),"zip",zipfile.is_zipfile(p))
if zipfile.is_zipfile(p):
 with zipfile.ZipFile(p) as z:
  for item in z.infolist():
   print("SPV_ENTRY",item.filename,item.file_size)
   if item.filename.lower().endswith((".xml",".txt",".htm",".html")) and item.file_size<500000:
    t=z.read(item).decode("utf-8",errors="replace")
    s=re.sub(r"<[^>]*>"," ",t)
    s=re.sub(r"\s+"," ",s)
    print("TEXT",s[:6000])
