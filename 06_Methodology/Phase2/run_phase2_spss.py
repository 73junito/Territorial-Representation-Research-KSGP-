"""Run Phase 2 SPSS syntax in an isolated SPSS Python backend; preserve .sav."""
from pathlib import Path
import hashlib
import sys
import spss
root = Path(r"I:\Territorial-Representation-Research")
data = root / "02_SPSS_Data" / "Phase2" / "age_sex_2020_six_jurisdictions.sav"
syntax = root / "03_SPSS_Syntax" / "Phase2" / "01_age_sex_2020_descriptive.sps"
out = root / "04_SPSS_Output" / "Phase2" / "01_age_sex_2020_descriptive.spv"
if out.exists():
    raise RuntimeError("Output already exists, refusing to overwrite")
before = hashlib.sha256(data.read_bytes()).hexdigest()
text = syntax.read_text(encoding="utf-8-sig")
if "SAVE OUTFILE" in text.upper():
    raise RuntimeError("Syntax appears to save data; abort")
spss.StartSPSS()
try:
    spss.Submit("OUTPUT NEW.\n" + text + "\nOUTPUT SAVE OUTFILE='" + out.as_posix() + "'.")
finally:
    spss.StopSPSS()
assert out.exists() and out.stat().st_size > 500, "SPSS did not create output"
assert hashlib.sha256(data.read_bytes()).hexdigest() == before, "Source .sav changed"
print("SPSS_PRODUCED",out, out.stat().st_size,flush=True)
print("SAV_UNCHANGED",before,flush=True)
