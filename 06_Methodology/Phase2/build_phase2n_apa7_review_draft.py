"""Create a separate editorial APA-7 review manuscript; preserve Phase 2M-D unchanged."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/"08_Final_Report/Phase2MD_Integrated_Academic_Manuscript_Review_Draft.md"
target=ROOT/"08_Final_Report/Phase2N_APA7_Cited_Academic_Manuscript_Review_Draft.md"
assert source.is_file() and not target.exists()
s=source.read_text(encoding="utf-8")
s=s.replace("**Phase 2M-D — Academic manuscript, working draft for external faculty review**",
            "**Phase 2N — APA 7 citation and editorial review draft (based on Phase 2M-D)**")
s=s.replace("**Status:** Internal evidence QA only; not independently peer-reviewed, accepted, or authorized for final publication.",
            "**Status:** Source-linked editorial draft. Census publication-year suffixes are provisionally assigned; faculty APA and methods approval still pending. Not an approved publication.")
assert "## Introduction and geographic scope" in s
s=s.replace("The uninhabited or nonpermanently inhabited U.S. Minor Outlying Islands and other U.S.-claimed small islands are outside the analysis because the selected jurisdiction-level data sources do not supply equivalent socioeconomic profiles.",
            "The uninhabited or nonpermanently inhabited U.S. Minor Outlying Islands and other U.S.-claimed small islands are outside the analysis because the selected jurisdiction-level data sources do not supply equivalent socioeconomic profiles (U.S. Census Bureau, 2022c).")
s=s.replace("This is a **descriptive, nonexperimental secondary-data** study using aggregated U.S. Census Bureau material.",
            "This is a **descriptive, nonexperimental secondary-data** study using aggregated U.S. Census Bureau material (U.S. Census Bureau, 2020a, 2022a, 2022c).")
s=s.replace("1. **2020 Island Areas Census Demographic Profile** — AS, GU, MP, VI.",
            "1. **2020 Island Areas Census Demographic Profile** — AS, GU, MP, VI (U.S. Census Bureau, 2022b, 2022c).")
s=s.replace("2. **2019 one-year ACS/PRCS** — DC, PR;",
            "2. **2019 one-year ACS/PRCS** — DC, PR (U.S. Census Bureau, 2020a);")
s=s.replace("3. **2016–2020 five-year ACS/PRCS** — DC, PR;",
            "3. **2016–2020 five-year ACS/PRCS** — DC, PR (U.S. Census Bureau, 2022a);")
s=s.replace("The Phase 2D government acquisition manifest inventories **17 original files** with source URLs, size and SHA-256 hash.",
            "The project-archived Phase 2D government acquisition manifest inventories **17 original files** with source URLs, size and SHA-256 hash; this is a project verification result, not a figure published by the Census Bureau.")
s=s.replace("*Note.* Values are the archived 2020 decennial demographic pilot.",
            "*Note.* Values are the archived 2020 decennial demographic pilot, extracted from source-specific DHC and Island Areas records (U.S. Census Bureau, 2022c; repository provenance: `02_SPSS_Data/Phase2/age_sex_2020_six_jurisdictions.csv`).")
s=s.replace("*Note.* Four Island Areas source products; not sample-based ACS figures.",
            "*Note.* Four Island Areas source products (U.S. Census Bureau, 2022b, 2022c); not sample-based ACS figures.")
s=s.replace("*Note.* Survey estimates and corresponding 90% MOEs. Uncertainty intervals are source-specific; see Table 5.",
            "*Note.* Survey estimates and corresponding 90% MOEs (U.S. Census Bureau, 2020a, 2020b). Uncertainty intervals are source-specific; see Table 5.")
s=s.replace("*Note.* Pooled five-year survey estimates are not a second independent year-2020 measurement,",
            "*Note.* Pooled five-year survey estimates (U.S. Census Bureau, 2022a) are not a second independent year-2020 measurement,")
s=s.replace("For ACS/PRCS results, the standard reported margin of error is associated with a **90% confidence level**.",
            "For ACS/PRCS results, the standard reported margin of error is associated with a **90% confidence level** (U.S. Census Bureau, 2020b).")
s=s.replace("*Note.* These are the **published 90% percentage MOEs**, not MOEs recomputed from category counts.",
            "*Note.* These are the **published 90% percentage MOEs**, not MOEs recomputed from category counts (U.S. Census Bureau, 2020a, 2022a; archived direct Data Profile API JSON in Phase 2I).")
s=s.replace("The four median-household-income MOEs come directly from source `B19013_001`",
            "The four median-household-income MOEs come directly from source `B19013_001` (U.S. Census Bureau, 2020a, 2022a)")
s=s.replace("The decennial population and age/sex evidence can be aggregated for the **six explicitly selected jurisdictions**,",
            "The decennial population and age/sex evidence can be aggregated for the **six explicitly selected jurisdictions** (U.S. Census Bureau, 2022c),")
s=s.replace("The Island Areas Census profiles differ from D.C. and Puerto Rico ACS/PRCS survey operations,",
            "The Island Areas Census profiles differ from D.C. and Puerto Rico ACS/PRCS survey operations (U.S. Census Bureau, 2020b, 2022b, 2022c),")
start=s.index("## References — provisional APA 7 entries for faculty verification")
end=s.index("## Evidence and reproducibility appendix",start)
replacement="""## References — APA 7 editorial draft, bibliographic verification pending

The year-letter designations below follow **alphabetical order by title** for multiple works by the same corporate author published in the same year. The release years of the 2019 ACS and 2016–2020 ACS sources were independently checked against official Census Bureau release notices. The 2020 Island Areas technical-documentation date is supported by its official directory listing, not a complete title-page publication-history review. Faculty should verify exact titles, retrieval locations, square-bracket descriptors, and final APA disambiguation before submission.

U.S. Census Bureau. (2020a). *2019 American Community Survey 1-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2019/release.html

U.S. Census Bureau. (2020b). *Understanding and using American Community Survey data: What all data users need to know* [Handbook]. https://www.census.gov/programs-surveys/acs/library/handbooks/general.html

U.S. Census Bureau. (2022a). *2016–2020 American Community Survey 5-year estimates* [Data set]. https://www.census.gov/programs-surveys/acs/news/data-releases/2020/release.html

U.S. Census Bureau. (2022b). *2020 Island Areas Censuses (IAC) demographic profile summary file: Technical documentation* [Technical documentation]. https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/2020-iac-dpsf-technical-documentation.pdf

U.S. Census Bureau. (2022c). *2020 Island Areas Censuses: Demographic profile summary file* [Data set]. https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html

**Verification links for release chronology:** [2019 one-year release (September 17, 2020)](https://www.census.gov/newsroom/press-releases/2020/acs-1year.html); [2016–2020 five-year release (March 17, 2022)](https://www.census.gov/newsroom/press-releases/2022/acs-5-year-estimates.html); [official Island Areas technical-documentation directory](https://www2.census.gov/programs-surveys/decennial/2020/technical-documentation/island-areas-tech-docs/demographic_profile/); [2020 ACS general handbook listing](https://www.census.gov/programs-surveys/acs/library/handbooks/general.html).

**Citation convention:** The five citations above are source families, not field-level citations for each archived value. Tables 1–5 also require the accompanying repository field and extraction provenance described below. The document's review remains provisional and does not imply faculty or institutional approval.

"""
s=s[:start]+replacement+s[end:]
# ensure all cited institutional author-year suffixes defined
from re import findall
used=set(findall(r"U\.S\. Census Bureau, (202[02][abc])",s[:s.index("## References")]))
defined=set(findall(r"U\.S\. Census Bureau\. \((202[02][abc])\)",s[s.index("## References"):]))
assert used<=defined,(used,defined)
assert s.count("### Table ")==5
assert "NO-GO" in s and "historical cause" in s
target.write_text(s,encoding="utf-8")
print("CREATED",target,"bytes",target.stat().st_size)
print("CITATION_YEAR_SUFFIXES_USED",sorted(used),"DEFINED",sorted(defined))
