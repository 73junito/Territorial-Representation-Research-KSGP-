from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
root=Path(r'I:\Territorial-Representation-Research')
data=pd.read_csv(root/'02_SPSS_Data'/'Phase2'/'age_sex_2020_six_jurisdictions.csv')
plot=data.sort_values('under20_pct')
fig,ax=plt.subplots(figsize=(10,5.5))
ax.barh(plot.jurisdiction,plot.under20_pct)
for i,n in enumerate(plot.under20_pct):ax.text(n+0.6,i,f'{n:.1f}%',va='center',fontsize=9)
ax.set_xlim(0,46)
ax.set_xlabel('Percent of total resident population under age 20')
ax.set_title('Residents under 20 by jurisdiction — 2020 Census')
fig.text(.01,.015,'Source: U.S. Census Bureau 2020 DHC P12 / Island Areas DP1; broad age categories harmonized.',fontsize=8)
fig.tight_layout(rect=(0,.04,1,1))
out=root/'05_Statistical_Graphics'/'Phase2'/'01_2020_under20_share.png'
fig.savefig(out,dpi=170)
plt.close(fig)
print('CREATED',out,out.stat().st_size)
