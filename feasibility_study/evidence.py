from dataclasses import dataclass
import json
from pathlib import Path

KINDS={"FACT","ESTIMATE","ASSUMPTION","JUDGMENT"}
TIERS={"PRIMARY","AUTHORITATIVE_SECONDARY","REPUTABLE_SECONDARY","COMMUNITY","UNKNOWN"}
CONFIDENCE={"HIGH","MEDIUM","LOW","UNKNOWN"}
STATUS={"CURRENT","SUPERSEDED","RETRACTED","OPEN"}

@dataclass
class Issue:
    level:str
    message:str
    record_id:str|None=None

def load_jsonl(path):
    p=Path(path)
    if not p.exists(): return []
    out=[]
    for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try: obj=json.loads(line)
        except json.JSONDecodeError as e: raise ValueError(f"{p}:{n}: invalid JSON: {e}") from e
        if not isinstance(obj,dict): raise ValueError(f"{p}:{n}: record must be object")
        out.append(obj)
    return out

def validate_record(r):
    issues=[]; rid=r.get('id'); kind=str(r.get('kind','')).upper(); tier=str(r.get('source_tier','UNKNOWN')).upper(); conf=str(r.get('confidence','UNKNOWN')).upper(); status=str(r.get('status','CURRENT')).upper()
    if not rid: issues.append(Issue('ERROR','missing id'))
    if kind not in KINDS: issues.append(Issue('ERROR',f'invalid kind: {kind or "<missing>"}',rid))
    if not str(r.get('statement','')).strip(): issues.append(Issue('ERROR','missing statement',rid))
    if tier not in TIERS: issues.append(Issue('ERROR',f'invalid source_tier: {tier}',rid))
    if conf not in CONFIDENCE: issues.append(Issue('ERROR',f'invalid confidence: {conf}',rid))
    if status not in STATUS: issues.append(Issue('ERROR',f'invalid status: {status}',rid))
    if kind=='FACT' and not str(r.get('source','')).strip(): issues.append(Issue('ERROR','FACT requires source',rid))
    if kind=='ESTIMATE' and not str(r.get('formula','')).strip() and not r.get('depends_on'): issues.append(Issue('ERROR','ESTIMATE requires formula or depends_on',rid))
    if kind=='ASSUMPTION' and conf=='HIGH': issues.append(Issue('WARN','ASSUMPTION marked HIGH confidence; verify justification',rid))
    if r.get('value') is not None and not r.get('unit'): issues.append(Issue('WARN','numeric value has no unit',rid))
    if tier=='COMMUNITY' and conf=='HIGH': issues.append(Issue('WARN','community-only evidence should rarely be HIGH confidence',rid))
    if tier=='UNKNOWN' and conf=='HIGH': issues.append(Issue('ERROR','HIGH confidence cannot use UNKNOWN source tier',rid))
    return issues

def validate_ledger(records):
    rows=list(records); issues=[]; ids=set()
    for r in rows:
        rid=r.get('id')
        if rid in ids: issues.append(Issue('ERROR','duplicate id',rid))
        if rid: ids.add(rid)
        issues.extend(validate_record(r))
    for r in rows:
        for dep in r.get('depends_on',[]) or []:
            if dep not in ids: issues.append(Issue('ERROR',f'depends_on references missing id {dep}',r.get('id')))
    return issues
