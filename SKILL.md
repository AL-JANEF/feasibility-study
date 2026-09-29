---
name: feasibility-study
description: >
  Sector-adaptive, evidence-driven feasibility-study system for real commercial,
  industrial, healthcare, technology, real-estate, agriculture, energy, mining,
  infrastructure, services, and regulated projects. It researches the exact sector
  and jurisdiction, builds a bottom-up demand/capacity model, an integrated financial
  model, scenarios and risks, and produces professional Word, PDF, and Excel deliverables.
---

# Feasibility Study V2

A feasibility study is not a generic report template.

It is an integrated investment decision model in which:

**Demand -> Capacity -> Operations -> Investment -> Financing -> Financial Statements -> Cash -> Return -> Risk -> Decision**

Evidence and red-team review are controls over that chain; they are not substitutes for it.

## Primary objective

When the user asks for a feasibility study, behave like a senior feasibility-study team:
market analyst + sector specialist + operations/technical analyst + regulatory researcher +
financial modeler + risk reviewer + report designer.

The default end-product for a `standard` or `investment-grade` study is not only Markdown.
Unless the user explicitly asks otherwise, produce:

1. `deliverables/<project>-feasibility-study.docx`
2. `deliverables/<project>-feasibility-study.pdf`
3. `deliverables/<project>-financial-model.xlsx`

The Word and PDF are the professional study report. The Excel workbook is the auditable,
formula-driven financial model. Verify all three before declaring completion.

## Non-negotiable principles

1. **Classify before researching.**
   Determine sector, subsector, business model, customer type, jurisdiction, project stage,
   capital intensity, regulatory intensity, financing type, and the investment decision.
2. **No one-size-fits-all feasibility study.**
   A hospital, medical device, factory, hotel, mine, SaaS company, restaurant, and real-estate
   development must not receive the same technical, operating, regulatory, or financial model.
3. **Build or load the correct sector pack first.**
   Read `references/core/sector-routing.md`, then only the relevant sector references.
   If the subsector is not covered precisely, create a project-specific sector pack from
   authoritative sources before proceeding.
4. **Research current facts.**
   For market size, regulation, licenses, tax, prices, technical standards, sector KPIs,
   and competitor facts, use live authoritative research tools when available.
5. **Evidence before narrative.**
   Material numbers are FACT / ESTIMATE / ASSUMPTION / JUDGMENT / UNKNOWN and carry a basis.
6. **Market size is not demand.**
   The commercial forecast must be bottom-up and constrained by realistic acquisition,
   capacity, timing, pricing, conversion, utilization, retention, or absorption drivers.
7. **Capacity must constrain revenue.**
   A factory cannot sell beyond effective production capacity; a hospital beyond service
   capacity; a hotel beyond room nights; a SaaS team beyond realistic implementation/sales
   capacity; a logistics operation beyond fleet/warehouse capacity.
8. **Profit is not cash.**
   Model revenue recognition, collections, working capital, CAPEX, debt service, tax,
   financing, and minimum cash separately.
9. **Three statements for full studies.**
   Standard/investment-grade work requires a linked Income Statement, Balance Sheet,
   and Cash Flow Statement unless the project is at a stage where such statements would
   be knowingly artificial; in that case explain and use a stage-appropriate model.
10. **No final NPV/IRR from unsupported cash flows.**
11. **Scenarios change causes, not just percentages.**
   A downside case changes coherent operating drivers: schedule, price, conversion,
   utilization, churn, collection days, costs, capacity, etc.
12. **Use sector-appropriate investment metrics.**
   NPV/IRR are not the only metrics. Apply DSCR/LLCR, RevPAR, OEE, occupancy, AISC,
   LCOE, CAC payback, NOI/cap rate, or other metrics only where relevant.
13. **Regulation can kill feasibility.**
   Identify competent regulators, required approvals, timelines, professional licenses,
   ownership/localization restrictions, data/privacy, environment, safety, clinical,
   product, import/export, and tax obligations as applicable.
14. **Do not fabricate missing information.**
   Use UNKNOWN, ranges, scenario bands, or explicit assumptions.
15. **A polished report is not completion.**
   The financial model, report, citations, scenarios, and final conclusion must reconcile.

## Study modes

- `rapid`: early screen; no claim of bankability; concise evidence, economics, blockers.
- `standard`: complete management/founder feasibility study with integrated financial model.
- `investment-grade`: standard + deeper source redundancy, sector-specialist research,
  financing analysis, stress tests, red team, reconciliations, and professional deliverables.

`investment-grade` means diligence depth, not an audit, licensed valuation, legal opinion,
tax opinion, engineering stamp, clinical opinion, or lender approval.

## Required workflow

### 00 Project classification
Create `PROJECT_PROFILE.json` containing:
- project name and description
- sector / subsector
- business model
- B2B / B2C / B2G
- geography / jurisdiction
- current stage
- revenue mechanism
- financing type
- study mode
- language and currency
- decision being made

### 01 Sector-pack selection or synthesis
Read `references/core/sector-routing.md`.

Load the exact sector pack. If none fits the project precisely:
- identify the competent regulator(s);
- identify authoritative sector/technical standards;
- identify sector-specific demand and capacity drivers;
- identify sector-specific CAPEX/OPEX and working-capital mechanics;
- identify the sector's core KPIs and failure modes;
- write `01-sector-pack.md`;
- do not continue until the sector pack is adequate.

### 02 Decision frame and evidence plan
Define decision owner, alternatives, horizon, capital at risk, return threshold, constraints,
unknowns, and research plan.

### 03 Market and demand
Research:
- addressable customers/users/population;
- historical/current demand;
- demand drivers;
- segmentation;
- willingness to pay;
- procurement/buying process;
- substitution and switching;
- competition;
- pricing;
- bottom-up obtainable demand;
- TAM/SAM/SOM only as supporting outputs.

### 04 Sales/revenue engine
Build the sector-appropriate driver tree.

Examples:
- SaaS: leads -> opportunities -> wins -> implementation -> active ARR -> renewals/expansion/churn.
- Hotel: rooms x available nights x occupancy x ADR + F&B/other.
- Hospital: clinics/beds/rooms x utilization x payer/reimbursement mix.
- Factory: effective capacity x utilization x yield x sell-through x unit price.
- Real estate: units/GFA x absorption x price/rent x collection schedule.
- Marketplace: active supply x demand x match/fill rate x GMV x take rate.
- Contracting: tender pipeline x bid rate x win rate x backlog x execution curve.

### 05 Technical/capacity feasibility
Use the selected sector pack. Define design basis, capacity, process/technology, equipment,
infrastructure, site, utilities, quality, safety, maintenance, scalability, and bottlenecks.

### 06 Operations
Define operating model, staffing, shifts, suppliers, inventory/logistics, service delivery,
support, quality systems, maintenance, resilience, and operating controls.

### 07 Regulatory / legal / ESG
Research current rules in the jurisdiction. Record regulator, requirement, applicability,
evidence/source, approval timeline, cost, dependency, and blocker status.

### 08 Organization and manpower
Build headcount by role, hire date, loaded payroll, productivity/capacity link, training,
professional licensing, and critical-person dependencies.

### 09 Implementation schedule
Create a dependency-aware schedule including licensing, procurement, construction/development,
validation/commissioning, hiring, sales ramp, launch, and contingency.

### 10 Investment and CAPEX
Model land/site, construction, equipment, fit-out, technology, vehicles, professional fees,
pre-operating costs, startup inventory, capitalized development if justified, contingency,
interest during construction if relevant, replacement and sustaining CAPEX.

### 11 OPEX and COGS
Model direct costs, materials, utilities/cloud, payroll, support, maintenance, rent, logistics,
commissions, sales/marketing, insurance, professional services, compliance, G&A, and other
sector-specific costs.

### 12 Working capital
Model AR, AP, inventory, deposits, deferred revenue/contract liabilities, retentions,
VAT/tax timing, prepayments, and minimum operating cash where applicable.

### 13 Financing
Model sources and uses, equity timing, debt drawdown, interest, fees, grace period,
principal repayment, leases, grants, covenants, and refinancing where applicable.

### 14 Integrated financial model
Read `references/core/financial-model-standard.md`.

For a full study, build:
- Income Statement
- Balance Sheet
- Cash Flow Statement
- CAPEX/depreciation schedule
- working-capital schedule
- debt/equity schedule
- tax/zakat/VAT schedule where applicable
- FCFF and FCFE where meaningful

Default time granularity:
- monthly for the first 24-36 months;
- annual thereafter to at least year 5;
- longer/full project life for real estate, energy, mining, infrastructure, concessions,
  and other long-lived assets.

### 15 Investment appraisal
Use applicable metrics:
NPV, IRR, MIRR, discounted payback, payback, profitability index, ROI/ROIC, break-even,
DSCR/LLCR/ICR, project IRR/equity IRR, economic NPV/EIRR, risk-adjusted NPV, or
sector-specific metrics.

### 16 Scenarios
At minimum Base / Downside / Upside. Each scenario changes coherent causal drivers.

### 17 Sensitivity and switching values
Test the variables that can reverse the decision. Calculate, where meaningful, the value
at which NPV becomes zero, liquidity fails, DSCR breaches, or break-even becomes unreachable.

### 18 Stress tests
Use project-specific shocks: delayed launch, slower demand, price compression, cost overrun,
lower yield/utilization, collection delays, churn, FX/rates, key supplier/customer loss,
regulatory delay, commodity price shock, or construction delay.

### 19 Risk and pre-mortem
Probability x impact x trigger x mitigation x owner x residual risk.
Define explicit kill criteria.

### 20 Independent red team
Attack:
- demand;
- pricing;
- technical design/capacity;
- operating assumptions;
- schedule;
- CAPEX/OPEX;
- working capital;
- regulation;
- financing/liquidity;
- scenario logic;
- conclusion.

### 21 Reconciliation and final decision
Reconcile evidence, Excel, report, scenarios, and risk findings.

Decision states:
- GO
- CONDITIONAL_GO
- VALIDATE_FIRST
- RESCOPE
- PHASE
- DELAY
- PIVOT
- NO_GO_CURRENT_FORM
- TOO_EARLY

Never average scores into a verdict.

## Financial model requirements

For full studies, the following identities are hard gates:

- `Revenue schedule = reported revenue`
- `Closing cash = opening cash + CFO + CFI + CFF`
- `Balance-sheet cash = cash-flow closing cash`
- `Assets = Liabilities + Equity`
- `Closing debt = opening debt + drawdowns - principal repayments`
- `Closing PPE = opening PPE + CAPEX - disposals - depreciation`
- `Closing retained earnings = opening retained earnings + net income - dividends`

For subscription/contract businesses, explicitly distinguish where applicable:

**Bookings != Billings != Revenue != Cash Collections**

For SaaS, prepaid contracts may create cash before accounting revenue; deferred revenue /
contract liabilities must be modeled when material.

## Professional deliverables

Read `references/core/artifact-output-standard.md`.

A standard/investment-grade study is not complete until:
- DOCX exists and is readable;
- PDF exists and visually matches the DOCX content;
- XLSX exists, opens, contains formulas/schedules, and reconciles;
- report numbers match the workbook;
- citations/source register exists;
- assumptions register exists;
- no material placeholder such as TODO/TBD remains without explicit UNKNOWN status.

When the user's language is Arabic:
- produce Arabic report by default;
- use RTL formatting in DOCX/PDF;
- keep technical acronyms where clearer;
- make tables readable right-to-left;
- Excel may use English sheet names for interoperability, but labels should be Arabic-friendly.

## Research standard

Prefer, in order:
1. law/regulator/official statistics/official registries;
2. audited filings / official company pricing and documents;
3. recognized multilateral/standards/industry bodies;
4. reputable sector research;
5. credible expert/industry evidence;
6. secondary commentary only as support.

For changing facts, record access date and reference period.
For critical regulatory or financial claims, seek primary evidence.
If live research is unavailable, do not claim a current investment-grade study.

## Stop conditions

Stop and surface the problem if:
- sector/subsector is materially ambiguous;
- the project-specific sector pack is missing;
- current regulation is required and cannot be verified;
- a load-bearing demand input is unsupported;
- revenue exceeds realistic capacity without explicit expansion;
- financial statements fail reconciliation;
- cash becomes negative without a financing source;
- a scenario changes outputs without changing underlying drivers;
- a red-team blocker remains unresolved;
- final report contradicts the workbook.

## Working files

Maintain:

```text
study/
  PROJECT_PROFILE.json
  PROGRESS.md
  00-project-classification.md
  01-sector-pack.md
  02-decision-evidence.md
  03-market-demand.md
  04-sales-revenue-engine.md
  05-technical-capacity.md
  06-operations.md
  07-regulatory-legal-esg.md
  08-organization-manpower.md
  09-implementation.md
  10-capex.md
  11-opex-cogs.md
  12-working-capital.md
  13-financing.md
  14-integrated-financial-model.md
  15-investment-appraisal.md
  16-scenarios.md
  17-sensitivity-switching.md
  18-stress-tests.md
  19-risk-premortem.md
  20-red-team.md
  21-final-feasibility.md
  evidence.jsonl
  assumptions.jsonl
  sources.md
  deliverables/
```

The working Markdown is audit trail. The user's primary deliverables are DOCX, PDF, and XLSX.
