# Integrated Financial Model Standard

## Objective
Convert evidenced market, capacity, operating, implementation, regulatory, and financing
assumptions into auditable cash flows and investment metrics.

## Required workbook architecture
Recommended sheets:
- Cover
- Assumptions
- Sources
- Timeline
- Demand
- Capacity
- Sales
- Revenue
- COGS
- Headcount_Payroll
- OPEX
- CAPEX
- Depreciation
- Working_Capital
- Tax_Zakat_VAT
- Debt
- Equity
- P&L
- Balance_Sheet
- Cash_Flow
- FCFF_FCFE
- KPIs
- Break_Even
- Scenarios
- Sensitivity
- Stress_Tests
- Risk
- Dashboard

Use only relevant sheets; do not add decorative sheets without purpose.

## Time horizon
Default new venture:
- Month 1-36 monthly.
- Years 4-5+ annual.
Use full useful/project life when economics require it: real estate, hotels, plants,
energy, mining, PPP/concessions.

## Revenue
Build from operational drivers, not market CAGR.
Separate, where relevant:
- contracts/bookings;
- invoices/billings;
- accounting revenue;
- cash collections.

Subscription example:
new contracts -> implementation/go-live -> active recurring base -> renewal/expansion/churn.
Annual prepayment may increase cash and deferred revenue before revenue recognition.

## Costs
Separate:
- COGS/direct variable cost;
- payroll;
- fixed/semi-variable OPEX;
- CAPEX;
- depreciation/amortization;
- financing cost;
- tax/zakat;
- noncash items.

## Working capital
Model applicable:
AR, inventory, AP, accrued expenses, prepayments, deposits, deferred revenue/contract
liabilities, retention receivables/payables, tax/VAT timing, minimum cash.

## Financing
Sources and uses must balance.
Debt schedule:
opening debt + drawdown - principal repayment = closing debt.
Interest uses the stated debt convention.
Model fees, grace periods, balloon payments, leases, covenants if relevant.

## Three-statement hard gates
P&L, Balance Sheet, and Cash Flow must reconcile.

Hard checks:
- Assets = Liabilities + Equity.
- Closing cash from cash flow = Balance Sheet cash.
- Opening cash + CFO + CFI + CFF = Closing cash.
- Closing retained earnings = opening RE + net income - dividends.
- Closing PPE = opening PPE + CAPEX - disposals - depreciation.
- Debt schedule = Balance Sheet debt.
- Revenue schedule = P&L revenue.
- depreciation schedule = P&L depreciation and BS accumulated depreciation.
- working-capital schedules = BS balances and CFO changes.

## Cash-flow appraisal
Use the correct cash flow:
- Project/unlevered FCFF for project economics and WACC-based NPV.
- Equity/levered FCFE for equity-return analysis.
Do not mix debt cash flows into an unlevered project IRR.

Generic FCFF:
EBIT × (1 - cash tax rate) + D&A - CAPEX - change in operating NWC

Generic FCFE:
Net income + D&A - CAPEX - change in operating NWC + net borrowing

Adapt for sector and accounting reality.

## Metrics
Use only relevant metrics:
NPV, project IRR, equity IRR, MIRR, payback, discounted payback, profitability index,
ROI/ROIC, break-even, DSCR, ICR, LLCR, runway, peak funding gap, minimum cash.

## Scenarios
Base/Downside/Upside must change drivers coherently.
Examples: launch timing, utilization, price, conversion, yield, payroll timing, collection
days, CAPEX, FX, rates, churn.

## Sensitivity
Test decision-critical independent variables and switching values.
When justified, use probabilistic simulation and report assumptions, distribution choices,
P50/P90 or equivalent.

## Failure conditions
The model is not complete if:
- it does not balance;
- revenue is unconstrained by demand/capacity;
- negative cash has no financing source;
- inputs have no basis;
- scenarios modify outputs directly instead of drivers;
- report numbers differ from workbook outputs.
