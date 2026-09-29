from pathlib import Path
import json,shutil
from .evidence import load_jsonl,validate_ledger

STAGES=[f'{i:02d}-{n}.md' for i,n in enumerate(['decision-frame','evidence-plan','market-demand','competition-positioning','technical-feasibility','operational-feasibility','regulatory-feasibility','business-model','financial-model','scenarios-sensitivity','risk-premortem','implementation','validation-experiments','red-team','reconciliation','final-decision'])]
REQ={'rapid':set([STAGES[i] for i in [0,1,2,7,8,10,12,15]]),'standard':set(STAGES),'investment-grade':set(STAGES)}

def init_study(dest,template_root,mode='standard',force=False):
    if mode not in REQ: raise ValueError(f'invalid mode: {mode}')
    d=Path(dest)
    if d.exists() and any(d.iterdir()) and not force: raise FileExistsError(f'{d} is not empty; use --force')
    d.mkdir(parents=True,exist_ok=True); t=Path(template_root)
    for src in t.glob('*.md'): shutil.copy2(src,d/src.name)
    (d/'evidence.jsonl').touch(); (d/'assumptions.jsonl').touch(); (d/'sources.md').write_text('# Sources\n\n',encoding='utf-8'); (d/'financial-input.json').write_text('{}\n',encoding='utf-8'); (d/'financial-output.json').write_text('{}\n',encoding='utf-8')
    (d/'STUDY.json').write_text(json.dumps({'product':'Feasibility Study','study_version':'0.1.0','mode':mode,'current_stage':'00'},indent=2)+'\n',encoding='utf-8')

def validate_study(dest):
    d=Path(dest); issues=[]
    if not d.exists(): return [('ERROR',f'study directory not found: {d}')]
    try: meta=json.loads((d/'STUDY.json').read_text(encoding='utf-8')); mode=meta.get('mode','standard')
    except Exception as e: issues.append(('ERROR',f'invalid/missing STUDY.json: {e}')); mode='standard'
    required=REQ.get(mode)
    if required is None: issues.append(('ERROR',f'invalid mode: {mode}')); required=REQ['standard']
    for name in sorted(required):
        if not (d/name).exists(): issues.append(('ERROR',f'missing required artifact: {name}'))
    if not (d/'PROGRESS.md').exists(): issues.append(('ERROR','missing PROGRESS.md'))
    if not (d/'evidence.jsonl').exists(): issues.append(('ERROR','missing evidence.jsonl'))
    else:
        try:
            for i in validate_ledger(load_jsonl(d/'evidence.jsonl')): issues.append((i.level,f'evidence {i.record_id or ""}: {i.message}'.strip()))
        except Exception as e: issues.append(('ERROR',f'evidence parse failed: {e}'))
    if mode=='investment-grade' and (d/'13-red-team.md').exists():
        txt=(d/'13-red-team.md').read_text(encoding='utf-8')
        if 'BLOCKER' in txt and 'OPEN' in txt: issues.append(('ERROR','investment-grade study has OPEN red-team BLOCKER'))
    return issues
