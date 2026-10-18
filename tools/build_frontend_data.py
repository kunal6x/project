#!/usr/bin/env python3
"""Generate dependency-free JS data bundles from the canonical research.json."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/research.json').read_text(encoding='utf-8'))
companies=data.pop('companies')
counts={}
for c in companies:counts[c['category']]=counts.get(c['category'],0)+1
data['meta']['counts']={'companies':len(companies),'sources':len(data['sources']),'opportunities':len(data['opportunities']),'problemSignals':len(data['problems']),'categories':counts}
# Persist recomputed metadata in the canonical data
canonical={**data,'companies':companies}
(ROOT/'data/research.json').write_text(json.dumps(canonical,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'data/research-base.js').write_text('window.INFRA_DATA='+json.dumps({**data,'companies':[]},ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
for i in range(0,len(companies),55):
 chunk=companies[i:i+55]
 (ROOT/'data'/f'companies-{i//55+1}.js').write_text('window.INFRA_DATA.companies.push(...'+json.dumps(chunk,ensure_ascii=False,separators=(',',':'))+');\n',encoding='utf-8')
print('Generated',1+(len(companies)+54)//55,'JS data bundles; companies:',len(companies))