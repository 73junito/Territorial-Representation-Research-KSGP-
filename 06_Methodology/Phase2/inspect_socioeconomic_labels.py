from pathlib import Path
import json
base=Path(r'I:\Territorial-Representation-Research\01_Government_Sources\Phase2_Socioeconomic\Census')
keys=['DP2_0012C','DP2_0013C','DP2_0014C','DP2_0015C','DP2_0016C','DP2_0017C','DP3_0001C','DP3_0003C','DP3_0004C','DP3_0005C','DP3_0006C','DP3_0104C','DP3_0139C','DP3_0158C']
for loc in ['AS','GU','MP','VI']:
 v=json.loads((base/f'{loc}_DP_variables.json').read_text())['variables']
 print('\nGEO',loc,flush=True)
 for k in keys:print(k, v.get(k,{}).get('label','ABSENT')[:190],flush=True)
 for family in ['DP2','DP3']:
  matches=[(k,item.get('label','')) for k,item in v.items() if k.startswith(family) and any(t in item.get('label','').lower() for t in ["bachelor's degree or higher","unemployment rate","median household income","all people","percent below poverty level"])]
  print('CANDIDATES',family,matches[:12],flush=True)
