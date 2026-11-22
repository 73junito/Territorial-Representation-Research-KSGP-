"""Generate and validate the Phase 1 SPSS file from the documented Census CSV."""
from pathlib import Path
import csv
import pandas as pd
import pyreadstat

base = Path(r"I:\Territorial-Representation-Research")
source = base / "02_SPSS_Data" / "population_2010_2020_source.csv"
dest = base / "02_SPSS_Data" / "population_2010_2020.sav"
csv_dest = base / "02_SPSS_Data" / "population_2010_2020_derived.csv"
with source.open("r", encoding="utf-8-sig", newline="") as f:
    records = list(csv.DictReader(f))
assert len(records) == 6, "Expected six jurisdictions"
assert len({r["geo_code"] for r in records}) == 6, "Duplicate geography"
df = pd.DataFrame(records)
for col in ["population_2010", "population_2020", "house_final_vote_members", "senate_members"]:
    df[col] = pd.to_numeric(df[col], errors="raise").astype("int64")
assert (df[["population_2010", "population_2020"]] > 0).all().all()
assert (df["house_final_vote_members"] == 0).all()
assert (df["senate_members"] == 0).all()
assert df["population_2020"].sum() == 4313440, "Population checksum mismatch"
df["population_change"] = df["population_2020"] - df["population_2010"]
df["population_change_pct"] = 100 * df["population_change"] / df["population_2010"]
labels = {
    "geo_code": "Census jurisdiction code",
    "jurisdiction": "Jurisdiction name",
    "jurisdiction_type": "Territory or federal district",
    "population_2010": "Resident population, April 1 2010",
    "population_2020": "Resident population, April 1 2020",
    "house_final_vote_members": "Members with final-passage House vote",
    "senate_members": "Voting U.S. senators",
    "source_id": "Official source register identifier",
    "population_change": "2010 to 2020 numeric change",
    "population_change_pct": "2010 to 2020 percentage change",
}
pyreadstat.write_sav(df, str(dest), column_labels=labels)
df.to_csv(csv_dest, index=False, encoding="utf-8-sig")
check, meta = pyreadstat.read_sav(str(dest))
assert len(check) == 6
assert int(check["population_2020"].sum()) == 4313440
assert all(abs(check["population_change_pct"] - df["population_change_pct"]) < 1e-8)
print(f"SPSS validated: {dest}")
print(f"Rows={len(check)} 2010={int(check.population_2010.sum())} 2020={int(check.population_2020.sum())}")
print(df[["geo_code","population_change","population_change_pct"]].to_string(index=False))
