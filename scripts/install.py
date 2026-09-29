#!/usr/bin/env python3
import argparse,hashlib,json,shutil,tempfile
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; NAME='feasibility-study'; VERSION=(ROOT/'VERSION').read_text().strip(); MARKER='.feasibility-study-managed.json'
TARGETS={'claude':Path.home()/'.claude/skills'/NAME,'codex':Path.home()/'.codex/skills'/NAME}; INCLUDE=['SKILL.md','VERSION','LICENSE','NOTICE.md','references','templates','schemas','scripts','feasibility_study']
def files():
 for rel in INCLUDE:
  p=ROOT/rel
  if p.is_file(): yield p,Path(rel)
  elif p.is_dir():
   for f in sorted(p.rglob('*')):
    if f.is_file() and '__pycache__' not in f.parts: yield f,f.relative_to(ROOT)
def digest():
 h=hashlib.sha256()
 for src,rel in files(): h.update(str(rel).encode()); h.update(b'\0'); h.update(src.read_bytes()); h.update(b'\0')
 return h.hexdigest()
def managed(p):
 try:return json.loads((p/MARKER).read_text()).get('product')==NAME
 except:return False
def install(k,dry=False,force=False):
 dest=TARGETS[k]
 if dest.exists() and not managed(dest) and not force: raise RuntimeError(f'refusing unmanaged destination: {dest}')
 if dry: print(f'DRY RUN [{k}] -> {dest}'); return
 dest.parent.mkdir(parents=True,exist_ok=True); backup=None
 if dest.exists():
  backup=dest.with_name(dest.name+'.backup.'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')); shutil.move(dest,backup)
 tmp=Path(tempfile.mkdtemp(prefix=NAME+'-',dir=str(dest.parent)))
 try:
  for src,rel in files(): out=tmp/rel; out.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,out)
  (tmp/MARKER).write_text(json.dumps({'product':NAME,'version':VERSION,'digest':digest()},indent=2)+'\n'); tmp.rename(dest)
 except Exception:
  shutil.rmtree(tmp,ignore_errors=True)
  if backup and backup.exists() and not dest.exists(): shutil.move(backup,dest)
  raise
 print(f'installed [{k}] {VERSION}: {dest}');
 if backup: print(f'backup: {backup}')
def doctor(k):
 d=TARGETS[k]; ok=d.exists() and managed(d) and (d/'SKILL.md').exists() and (d/'references').is_dir(); print(f'[{k}] {"OK" if ok else "NOT OK"}: {d}'); return ok
def uninstall(k):
 d=TARGETS[k]
 if not d.exists(): print(f'[{k}] already absent'); return
 if not managed(d): raise RuntimeError(f'refusing to remove unmanaged destination: {d}')
 shutil.rmtree(d); print(f'removed [{k}]: {d}')
def targets(x): return ['claude','codex'] if x=='both' else [x]
def main():
 p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True)
 x=s.add_parser('install'); x.add_argument('--target',choices=['claude','codex','both'],default='both'); x.add_argument('--dry-run',action='store_true'); x.add_argument('--force',action='store_true')
 x=s.add_parser('doctor'); x.add_argument('--target',choices=['claude','codex','both'],default='both')
 x=s.add_parser('uninstall'); x.add_argument('--target',choices=['claude','codex','both'],default='both'); a=p.parse_args()
 try:
  if a.cmd=='install': [install(k,a.dry_run,a.force) for k in targets(a.target)]
  elif a.cmd=='doctor': raise SystemExit(0 if all(doctor(k) for k in targets(a.target)) else 1)
  else: [uninstall(k) for k in targets(a.target)]
 except RuntimeError as e: print(f'ERROR: {e}'); raise SystemExit(2)
if __name__=='__main__': main()
