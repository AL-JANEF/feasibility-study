VALID_SIGNALS={'STRONG','ADEQUATE','WEAK','UNKNOWN'}
VALID_CONF={'HIGH','MEDIUM','LOW','UNKNOWN'}

def derive_state(a):
    dims=a.get('dimensions') or {}; fatal=list(a.get('fatal_blockers') or []); unknowns=list(a.get('critical_unknowns') or [])
    for n,d in dims.items():
        if str(d.get('signal','UNKNOWN')).upper() not in VALID_SIGNALS: raise ValueError(f'{n}: invalid signal')
        if str(d.get('confidence','UNKNOWN')).upper() not in VALID_CONF: raise ValueError(f'{n}: invalid confidence')
    if fatal: return {'state':'NO_GO_CURRENT_FORM','confidence':'HIGH' if a.get('fatal_blocker_verified') else 'MEDIUM','reasons':fatal}
    if str(a.get('technical_readiness','')).upper()=='R&D' and a.get('enabler_outside_horizon'): return {'state':'TOO_EARLY','confidence':a.get('technical_confidence','MEDIUM'),'reasons':['critical enabling technology outside decision horizon']}
    blockers=[n for n,d in dims.items() if d.get('blocker') is True]
    if blockers: return {'state':'NO_GO_CURRENT_FORM','confidence':'MEDIUM','reasons':[f'unresolved blocker: {x}' for x in blockers]}
    weak_high=[n for n,d in dims.items() if str(d.get('signal','')).upper()=='WEAK' and str(d.get('confidence','')).upper()=='HIGH']
    if weak_high: return {'state':'NO_GO_CURRENT_FORM','confidence':'MEDIUM','reasons':[f'high-confidence weak dimension: {x}' for x in weak_high]}
    if unknowns: return {'state':'VALIDATE_FIRST','confidence':'MEDIUM','reasons':unknowns}
    weak=[n for n,d in dims.items() if str(d.get('signal','')).upper()=='WEAK']; low=[n for n,d in dims.items() if str(d.get('confidence','')).upper() in {'LOW','UNKNOWN'}]
    if weak or low: return {'state':'VALIDATE_FIRST','confidence':'LOW' if low else 'MEDIUM','reasons':[*(f'weak: {x}' for x in weak),*(f'low-confidence: {x}' for x in low)]}
    med=[n for n,d in dims.items() if str(d.get('confidence','')).upper()=='MEDIUM']
    if med: return {'state':'CONDITIONAL_GO','confidence':'MEDIUM','reasons':[f'verification remains: {x}' for x in med]}
    return {'state':'GO','confidence':'HIGH','reasons':['no unresolved blocker or critical unknown in supplied assessment']}
