"""Phase 2M-E: reproduce source-separated academic figures.

Creates only new Phase2ME output directory files after preflight.
All source data are read-only; no SPSS or Census originals are touched.
Requires matplotlib; Python 3.10+.
"""
from pathlib import Path
import csv
import hashlib
import math
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "02_SPSS_Data" / "Phase2"
OUTPUT = ROOT / "05_Statistical_Graphics" / "Phase2ME"
FIGURES = []

AREAS = {"PR":"Puerto Rico", "DC":"Washington, D.C.", "GU":"Guam",
         "VI":"U.S. Virgin Islands", "AS":"American Samoa", "MP":"Northern Mariana Islands"}
DOMAINS = [
    ("education", "Bachelor's degree or higher (age 25+)", "%"),
    ("unemployment", "Civilian unemployment rate", "%"),
    ("poverty", "Poverty rate (source-defined universe)", "%"),
    ("median_household_income", "Median household income", "$"),
]
PERIODS = [
    ("2019_1yr", "2019 ACS/PRCS one-year", "prdc_2019_acs_one_year_detailed_source_specific.csv", "2019 USD"),
    ("2016_2020_5yr", "2016-2020 ACS/PRCS five-year", "prdc_2020_acs_five_year_detailed_source_specific.csv", "2020 inflation-adjusted USD"),
]

def read_rows(name):
    with (SOURCES / name).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def ensure_new_target():
    if OUTPUT.exists():
        existing = list(OUTPUT.iterdir())
        if existing:
            raise RuntimeError("Refusing to overwrite pre-existing Phase2ME figures: " + str(existing[0]))
    OUTPUT.mkdir(parents=True, exist_ok=True)

def finish(fig, filename, caption, source, period, domain, n, note, values):
    fig.tight_layout(pad=1.8)
    saved=[]
    for ext in ("png","svg"):
        p=OUTPUT / (filename+"."+ext)
        assert not p.exists(), "refusing overwrite: "+str(p)
        fig.savefig(p, dpi=200, bbox_inches="tight", facecolor="white")
        assert p.stat().st_size > 400
        saved.append(p)
    plt.close(fig)
    FIGURES.append(dict(figure=filename,caption=caption,source_family=source,reference_period=period,
                        domain=domain,observations=n,interpretation_note=note,
                        evidence_values=json.dumps(values,sort_keys=True),
                        png_sha256=hashlib.sha256(saved[0].read_bytes()).hexdigest(),
                        svg_sha256=hashlib.sha256(saved[1].read_bytes()).hexdigest()))
    print("FIGURE",filename,"PASS",n,flush=True)

def base_ax(title, xlabel, footnote):
    fig, ax=plt.subplots(figsize=(9.8,5.6))
    ax.set_title(title,loc="left",fontsize=13,fontweight="bold",pad=18)
    ax.set_xlabel(xlabel,fontsize=10)
    ax.grid(axis="x",alpha=.17)
    ax.set_axisbelow(True)
    fig.text(.02,.015,footnote,ha="left",va="bottom",fontsize=8,wrap=True)
    return fig,ax

def labeled_bars(ax, labels, vals, unit):
    y=list(range(len(labels)))
    bars=ax.barh(y,vals,height=.62)
    ax.set_yticks(y,labels)
    ax.invert_yaxis()
    right=max(vals)*1.25 if vals else 1
    ax.set_xlim(0,right)
    for bar,val in zip(bars,vals):
        label=f"${val:,.0f}" if unit=="$" else f"{val:.1f}%"
        ax.text(val+right*.016,bar.get_y()+bar.get_height()/2,label,va="center",fontsize=9)
    return bars

def main():
    population=read_rows("age_sex_2020_six_jurisdictions.csv")
    assert len(population)==6 and {r["geo_code"] for r in population}==set(AREAS)
    assert sum(int(r["population_2020"]) for r in population)==4313440
    islands=read_rows("island_areas_2020_socioeconomic_source_specific.csv")
    assert len(islands)==16
    assert {(r["jurisdiction"],r["domain"]) for r in islands}=={
        (a,d) for a in ("AS","GU","MP","VI") for d,*_ in DOMAINS}
    official=read_rows("../invalid") if False else None
    with (ROOT / "06_Methodology/Phase2/PHASE2I_PUBLISHED_PROFILE_NUMERIC_RECONCILIATION.csv").open(newline="",encoding="utf-8-sig") as f:
        moe_rows=list(csv.DictReader(f))
    assert len(moe_rows)==12
    indexed_moe={(r["jurisdiction"],r["period"],r["domain"]):r for r in moe_rows}
    ensure_new_target()

    # One common 2020 demographic frame: all six jurisdictions, federal district labeled separately.
    sorted_pop=sorted(population,key=lambda r:int(r["population_2020"]),reverse=True)
    names=[r["jurisdiction"]+(" [federal district]" if r["geo_code"]=="DC" else "") for r in sorted_pop]
    values=[int(r["population_2020"]) for r in sorted_pop]
    fig,ax=base_ax("2020 census population | six defined jurisdictions","Population (persons; logarithmic axis)",
                   "2020 decennial DHC (PR/DC); 2020 Island Areas Demographic Profiles (GU/VI/AS/MP). D.C. is not a territory.")
    ax.barh(range(6),values,height=.62)
    ax.set_yticks(range(6),names)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlim(10000,10000000)
    for i,v in enumerate(values):ax.text(v*1.09,i,f"{v:,}",va="center",fontsize=9)
    finish(fig,"01_2020_population_logscale","2020 population by jurisdiction (logarithmic x-axis)",
           "2020 decennial Census jurisdiction-specific products","2020","population",6,
           "Descriptive counts only; log axis clearly labeled; D.C. separate federal district", dict(zip(names,values)))

    fig,ax=plt.subplots(figsize=(10.5,6))
    fig.suptitle("2020 census age structure | six defined jurisdictions",x=.05,ha="left",fontweight="bold",fontsize=13)
    names=[r["jurisdiction"] for r in sorted_pop]
    y=list(range(6))
    palette=plt.rcParams["axes.prop_cycle"].by_key()["color"]
    left=[0.]*6
    by_group={}
    for j,(field,label) in enumerate((("under20_2020","Under 20"),("age20to64_2020","Ages 20-64"),("age65plus_2020","Age 65+"))):
        proportions=[100*int(r[field])/int(r["population_2020"]) for r in sorted_pop]
        by_group[label]=dict(zip(names,proportions))
        ax.barh(y,proportions,left=left,label=label,height=.65,color=palette[j])
        left=[a+b for a,b in zip(left,proportions)]
    assert all(abs(x-100)<1e-8 for x in left)
    ax.set_yticks(y,names)
    ax.invert_yaxis()
    ax.set_xlim(0,100)
    ax.set_xlabel("Share of jurisdiction population (%)")
    ax.legend(loc="lower center",bbox_to_anchor=(.5,-.22),ncol=3,frameon=False)
    fig.text(.02,.01,"2020 decennial Census. Age groups partition each jurisdiction's residents; D.C. is a federal district.",fontsize=8)
    finish(fig,"02_2020_age_structure","Jurisdiction-specific shares for three exhaustive age groups",
           "2020 decennial Census jurisdiction-specific products","2020","age composition",6,
           "Each jurisdiction's age shares sum to 100%; no statistical significance claimed",by_group)

    ia_order=["AS","GU","MP","VI"]
    for dom,title,unit in DOMAINS:
        selected=[next(r for r in islands if r["jurisdiction"]==code and r["domain"]==dom) for code in ia_order]
        values=[float(r["value"]) for r in selected]
        if dom=="poverty":
            for r in selected:
                assert r["unit"]=="percent_derived"
        note=("2019 USD" if unit=="$" else "2020 Island Areas long-form census")
        fig,ax=base_ax(f"Island Areas: {title}",title+(" (2019 USD)" if unit=="$" else " (%)"),
                       "Four Island Areas 2020 Census Demographic Profiles; income/poverty refer to 2019. Guam coverage exclusions apply. No ACS MOEs.")
        labeled_bars(ax,[AREAS[k] for k in ia_order],values,unit)
        finish(fig,f"03_island_areas_{dom}",f"Four Island Areas: {title}",
               "2020 Island Areas Census Demographic Profiles",note,dom,4,
               "Do not pool with ACS/PRCS data or interpret as sample-based ACS uncertainty",
               {r["jurisdiction"]:{'value':r["value"],'unit':r["unit"],'source_variable':r["source_variable"]} for r in selected})

    for period,product,filename,dollars in PERIODS:
        source=read_rows(filename)
        assert len(source)==8
        assert {(r["jurisdiction"],r["domain"]) for r in source} == {(a,d) for a in ("DC","PR") for d,*_ in DOMAINS}
        for dom,title,unit in DOMAINS:
            subset=[next(r for r in source if r["jurisdiction"]==a and r["domain"]==dom) for a in ("DC","PR")]
            values=[float(r["estimate"]) for r in subset]
            if dom=="median_household_income":
                errors=[float(r["margin_of_error"]) for r in subset]
                assert all(e>0 for e in errors)
            else:
                errors=[float(indexed_moe[(r["jurisdiction"],period,dom)]["published_profile_moe90_pp"]) for r in subset]
            assert all(math.isfinite(x) and x>=0 for x in values+errors)
            fig,ax=base_ax(f"{product}: {title}",f"{title} ({dollars if unit=='$' else '%'})",
                           f"{product}. Source-specific 90% published margins of error (error bars); no cross-product inference.")
            ys=[0,1]
            ax.barh(ys,values,height=.54)
            ax.errorbar(values,ys,xerr=errors,fmt="none",ecolor="black",capsize=5,linewidth=1.3)
            ax.set_yticks(ys,["Washington, D.C. [federal district]","Puerto Rico"])
            ax.invert_yaxis()
            ax.set_xlim(0,max(v+e for v,e in zip(values,errors))*1.34)
            for j,(v,e) in enumerate(zip(values,errors)):
                label=f"${v:,.0f} ±${e:,.0f}" if unit=="$" else f"{v:.2f}% ±{e:.1f} pp"
                ax.text(v+e+max(values)*.03,j,label,va="center",fontsize=9)
            finish(fig,f"{'04' if period=='2019_1yr' else '05'}_{period}_{dom}",
                   f"{product}: {title} with published 90% MOEs",
                   "ACS/PRCS survey Detailed Tables; official Data Profile percentage MOEs",product,dom,2,
                   "Two jurisdiction-specific survey estimates and published 90% MOEs; not a significance test",
                   {r["jurisdiction"]:{'estimate':r["estimate"],'published_moe90':e,'unit':r["unit"]} for r,e in zip(subset,errors)})

    index=OUTPUT/"FIGURE_INDEX.csv"
    with index.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=FIGURES[0].keys())
        writer.writeheader()
        writer.writerows(FIGURES)
    assert len(FIGURES)==14,(len(FIGURES),[x["figure"] for x in FIGURES])
    print("PASS",len(FIGURES),"figures 28 PNG/SVG exports, index",index,flush=True)

if __name__=="__main__":
    main()
