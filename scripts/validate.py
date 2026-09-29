#!/usr/bin/env python3
import ast,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; errors=[]
required=['SKILL.md','VERSION','LICENSE','NOTICE.md','references/decision-frame.md','references/evidence-standard.md','references/market-demand.md','references/financial-model.md','references/red-team.md','references/decision-engine.md','references/jurisdictions/saudi-arabia.md','scripts/feasibility.py','scripts/install.py','feasibility_study/evidence.py','feasibility_study/finance.py','feasibility_study/decision.py','feasibility_study/study.py']
for rel in required:
 if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
if 'name: feasibility-study' not in (ROOT/'SKILL.md').read_text(encoding='utf-8'): errors.append('SKILL.md frontmatter name mismatch')
for p in ROOT.rglob('*.py'):
 try: ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
 except SyntaxError as e: errors.append(f'syntax {p.relative_to(ROOT)}: {e}')
 txt=p.read_text(encoding='utf-8')
 for b in ['requests','httpx','urllib.request','socket','paramiko']:
  if re.search(rf'(^|\n)\s*(import|from)\s+{re.escape(b)}',txt): errors.append(f'network-capable import {b} in {p.relative_to(ROOT)}')
 if re.search(r'subprocess\.(run|Popen|call|check_call|check_output)',txt): errors.append(f'subprocess execution in {p.relative_to(ROOT)}')
for p in ROOT.rglob('*'):
 if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.txt','.yml','.yaml'}:
  txt=p.read_text(encoding='utf-8',errors='ignore')
  for pat in [r'AKIA[0-9A-Z]{16}',r'-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----',r'ghp_[A-Za-z0-9]{30,}']:
   if re.search(pat,txt): errors.append(f'secret-shaped content in {p.relative_to(ROOT)}')
print('Feasibility Study repository validation')
for x in errors: print('[FAIL]',x)
if errors: print(f'validation: FAIL ({len(errors)} errors)'); raise SystemExit(1)
print('validation: PASS')
