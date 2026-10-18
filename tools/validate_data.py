#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1];d=json.loads((r/'data/research.json').read_text());bad=[]
for key in ['companies','sources','opportunities','problems','architecture','playbook']:
 if key not in d or not isinstance(d[key],list):bad.append('Missing dataset '+key)
for key in ['companies','sources','opportunities','problems']:
 ids=[x.get('id') for x in d[key]]
 if len(ids)!=len(set(ids)):bad.append('Duplicate IDs in '+key)
sids={x['id'] for x in d['sources']}
for x in [*d['problems'],*d['opportunities']]:
 for sid in x.get('evidence',[]):
  if sid not in sids:bad.append(f"Missing source {sid} on {x['id']}")
for c in d['companies']:
 for key in ['name','description','category','confidence']:
  if not c.get(key):bad.append(f"Missing {key} on {c.get('id')}")
 for key in ('site','source'):
  if c.get(key) and not re.match(r'^https?://',c[key]):bad.append(f"Invalid URL {key} for {c['id']}")
if d['meta']['counts']['companies']!=len(d['companies']):bad.append('Company count mismatch')
for f in ['index.html','app.js','styles.css','data/research-base.js','AGENTS.md']:
 if not (r/f).exists():bad.append('Missing site artifact: '+f)
print(('INVALID: '+str(bad[:40])) if bad else f"PASS: {len(d['companies'])} companies, {len(d['sources'])} sources, {len(d['opportunities'])} opportunities")
sys.exit(1 if bad else 0)