from copy import deepcopy
from math import isfinite

class FinancialInputError(ValueError): pass

def _num(v,name,allow_negative=False):
    if not isinstance(v,(int,float)) or isinstance(v,bool) or not isfinite(float(v)): raise FinancialInputError(f'{name} must be finite number')
    x=float(v)
    if not allow_negative and x<0: raise FinancialInputError(f'{name} must be >= 0')
    return x

def validate_input(data):
    for k in ('currency','initial_investment','discount_rate','years'):
        if k not in data: raise FinancialInputError(f'missing required field: {k}')
    _num(data['initial_investment'],'initial_investment')
    if _num(data['discount_rate'],'discount_rate',True)<=-1: raise FinancialInputError('discount_rate must be > -1')
    if not isinstance(data['years'],list) or not data['years']: raise FinancialInputError('years must be non-empty list')
    for i,y in enumerate(data['years']):
        for k in ('revenue','cogs','opex'):
            if k not in y: raise FinancialInputError(f'years[{i}] missing {k}')
            _num(y[k],f'years[{i}].{k}')
        for k in ('taxes','capex','debt_service'):
            if k in y: _num(y[k],f'years[{i}].{k}')
        if 'working_capital_change' in y: _num(y['working_capital_change'],f'years[{i}].working_capital_change',True)

def npv(cashflows,r): return sum(cf/((1+r)**t) for t,cf in enumerate(cashflows))

def irr(cashflows):
    if not cashflows or not(any(x<0 for x in cashflows) and any(x>0 for x in cashflows)): return None
    lo,hi=-.9999,10.0; flo,fhi=npv(cashflows,lo),npv(cashflows,hi)
    if flo*fhi>0: return None
    for _ in range(250):
        mid=(lo+hi)/2; fm=npv(cashflows,mid)
        if abs(fm)<1e-10: return mid
        if flo*fm<=0: hi,fhi=mid,fm
        else: lo,flo=mid,fm
    return (lo+hi)/2

def run_model(data):
    validate_input(data)
    initial=float(data['initial_investment']); opening=float(data.get('opening_cash',0)); financing=float(data.get('financing',0)); dr=float(data['discount_rate'])
    cumulative=opening+financing-initial; fcf=[-initial]; years=[]
    for y in data['years']:
        rev=float(y['revenue']); cogs=float(y['cogs']); opex=float(y['opex']); taxes=float(y.get('taxes',0)); capex=float(y.get('capex',0)); wc=float(y.get('working_capital_change',0)); debt=float(y.get('debt_service',0))
        gp=rev-cogs; ocf=gp-opex-taxes; free=ocf-capex-wc; cumulative+=free-debt; fcf.append(free)
        cads=float(y.get('cads',ocf)); dscr=None if debt<=0 else cads/debt
        years.append({'year':y.get('year'),'revenue':rev,'cogs':cogs,'gross_profit':gp,'gross_margin':None if rev==0 else gp/rev,'opex':opex,'taxes':taxes,'operating_cash_flow_proxy':ocf,'capex':capex,'working_capital_change':wc,'free_cash_flow_proxy':free,'debt_service':debt,'dscr':dscr,'cumulative_cash_after_debt_service':cumulative})
    unit=data.get('unit_economics') or {}; u={}
    if all(k in unit for k in ('price','variable_cost_per_unit','annual_fixed_costs')):
        p=float(unit['price']); v=float(unit['variable_cost_per_unit']); f=float(unit['annual_fixed_costs']); c=p-v
        u['contribution_per_unit']=c; u['break_even_units']=None if c<=0 else f/c; u['break_even_revenue']=None if c<=0 else (f/c)*p
    if all(k in unit for k in ('cac','monthly_arpu','gross_margin','monthly_churn')):
        cac=float(unit['cac']); arpu=float(unit['monthly_arpu']); gm=float(unit['gross_margin']); churn=float(unit['monthly_churn']); ltv=None if churn<=0 else arpu*gm/churn
        u['ltv']=ltv; u['ltv_cac']=None if ltv is None or cac<=0 else ltv/cac; u['cac_payback_months']=None if arpu*gm<=0 else cac/(arpu*gm)
    return {'currency':data['currency'],'initial_investment':initial,'discount_rate':dr,'years':years,'cashflows_for_npv_irr':fcf,'npv':npv(fcf,dr),'irr':irr(fcf),'ending_cumulative_cash_after_debt_service':cumulative,'unit_economics':u,'method_note':'Mechanical decision-support calculations from supplied inputs; not audited statements or forecasts.'}

def apply_multipliers(data,multipliers):
    out=deepcopy(data); allowed={'revenue','cogs','opex','taxes','capex','working_capital_change','debt_service'}
    for key,mult in multipliers.items():
        if key not in allowed: raise FinancialInputError(f'unsupported scenario driver: {key}')
        _num(mult,f'multiplier.{key}')
        for y in out['years']: y[key]=float(y.get(key,0))*float(mult)
    return out
