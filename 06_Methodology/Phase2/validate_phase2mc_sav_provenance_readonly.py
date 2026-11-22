"""TRR Phase 2M-C read-only SPSS SAV archival provenance audit.

No data writes, no SAV regeneration, no SPSS execution, no network, no Git mutations.
Only the current repository tree and tracked Git history are inspected.
"""
from pathlib import Path
import csv
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[2]
TARGET = "02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.sav"
CSV = "02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv"
EARLIER = "300e5b3379435508d373416e70481032461173bb12ca99c6d913aafa6469b7d8"
CURRENT = "15c1bdb12e6202eb61944e2f794113aa2449914ee006d5de0750013043ae5def"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], stderr=subprocess.DEVNULL)


def main() -> None:
    current = ROOT / TARGET
    assert current.is_file()
    data = current.read_bytes()
    observed = hashlib.sha256(data).hexdigest()
    assert observed == CURRENT, f"STOP: original SAV changed: {observed}"
    assert len(data) == 4126
    git_bytes = git("show", f"HEAD:{TARGET}")
    assert git_bytes == data, "STOP: tracked Git bytes differ from working copy"
    print("PASS current SAV sha256", observed)
    print("PASS tracked Git blob equals current SAV exactly; size", len(data))

    history = git("log", "--all", "--format=%H", "--", TARGET).decode().splitlines()
    print("SAV_GIT_HISTORY_COMMITS", len(history))
    assert history, "SAV is not tracked"
    candidate_digests = [(commit, hashlib.sha256(git("show", f"{commit}:{TARGET}")).hexdigest()) for commit in history]
    for commit, digest in candidate_digests:
        print("GIT_HISTORICAL_BLOB", commit, digest)
    has_old_git_blob = any(digest == EARLIER for _, digest in candidate_digests)
    assert not has_old_git_blob, "EARLIER SAV FOUND IN HISTORY; requires manual read-only comparison"

    candidates = sorted(
        (p for p in ROOT.rglob("*")
         if p.is_file()
         and ".git" not in p.parts
         and p.name.lower().endswith((".sav", ".sav.bak", ".sav.old", ".bak", ".7z", ".zip", ".tar", ".gz"))
         and ("age_sex" in p.name.lower() or p.name.lower().endswith(".sav"))),
        key=lambda p: str(p),
    )
    print("REPOSITORY_SAV_ARCHIVE_CANDIDATES", len(candidates))
    for item in candidates:
        print("CANDIDATE", item.relative_to(ROOT), item.stat().st_size)
    matches = [p for p in candidates if hashlib.sha256(p.read_bytes()).hexdigest() == EARLIER]
    print("EARLIER_HASH_MATCHED_WORKSPACE_CANDIDATES", len(matches))

    with (ROOT / CSV).open(encoding="utf-8-sig", newline="") as f:
        csv_rows = list(csv.DictReader(f))
    assert len(csv_rows) == 6 and len(csv_rows[0]) == 15
    assert {r["geo_code"] for r in csv_rows} == {"PR", "DC", "GU", "VI", "AS", "MP"}
    assert sum(int(r["population_2020"]) for r in csv_rows) == 4313440
    print("PASS canonical CSV dimensions 6x15 and population 4313440")
    print("NOTE: SAV-to-CSV per-cell equivalence separately established in PHASE2F_SAV_HASH_FORENSIC.md")
    print("DECISION: HISTORICAL_BYTE_CAUSALITY_UNRESOLVED_WITH_REPOSITORY_EVIDENCE")
    print("PRESERVE: earlier hash", EARLIER, "current hash", observed)


if __name__ == "__main__":
    main()
