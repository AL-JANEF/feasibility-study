#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from feasibility_study.finance import run_model,apply_multipliers,FinancialInputError
from feasibility_study.study import init_study,validate_study
from feasibility_study.decision import derive_state

def main():
 p=argparse.ArgumentParser(prog='feasibility-study'); s=p.add_subparsers(dest='cmd',required=True)
 x=s.add_parser('init'); x.add_argument('dest'); x.add_argument('--mode',choices=['rapid','standard','investment-grade'],default='standard'); x.add_argument('--force',action='store_true')
 x=s.add_parser('validate'); x.add_argument('study')
 x=s.add_parser('finance'); x.add_argument('input'); x.add_argument('--multipliers'); x.add_argument('--output')
 x=s.add_parser('decide'); x.add_argument('input')
 a=p.parse_args()
 try:
  if a.cmd=='init': init_study(a.dest,ROOT/'templates/study',a.mode,a.force); print(f'Initialized {a.mode} study: {Path(a.dest).resolve()}')
  elif a.cmd=='validate':
   issues=validate_study(a.study); [print(f'[{l.lower():5}] {m}') for l,m in issues]; e=[x for x in issues if x[0]=='ERROR']; print('study validation: '+('FAIL' if e else 'PASS')); raise SystemExit(1 if e else 0)
  elif a.cmd=='finance':
   data=json.loads(Path(a.input).read_text(encoding='utf-8'))
   if a.multipliers: data=apply_multipliers(data,json.loads(Path(a.multipliers).read_text(encoding='utf-8')))
   out=json.dumps(run_model(data),indent=2,ensure_ascii=False)
   if a.output: Path(a.output).write_text(out+'\n',encoding='utf-8'); print(f'Wrote: {Path(a.output).resolve()}')
   else: print(out)
  else: print(json.dumps(derive_state(json.loads(Path(a.input).read_text(encoding='utf-8'))),indent=2,ensure_ascii=False))
 except (ValueError,FileExistsError,FinancialInputError,json.JSONDecodeError) as e: print(f'ERROR: {e}',file=sys.stderr); raise SystemExit(2)
if __name__=='__main__': main()
