---
name: feasibility-study
description: >
  Evidence-first feasibility and investment decision support for business ideas,
  startups, SaaS, marketplaces, services, industrial/manufacturing projects,
  expansions, and market-entry decisions. Use for feasibility studies, business
  viability, investment cases, factory feasibility, market validation, go/no-go
  analysis, financial feasibility, market sizing, regulatory feasibility,
  scenario analysis, or whether a project is worth pursuing.
---

# Feasibility Study

**Decision discipline for ideas before capital is committed.**

Feasibility Study is not a generic business-plan writer. It is a staged feasibility
system that converts a decision question into a traceable evidence base, financial
model, risk case, independent challenge, and a human-owned decision.

## Non-negotiable rules

1. **Decision first.** Define the decision, owner, horizon, geography, capital at risk,
   and success threshold before research.
2. **Evidence before narrative.** Never let a polished report outrun the evidence.
3. **No invented numbers.** Every material number is a Fact, Estimate, or Assumption
   and carries a source/basis.
4. **Bottom-up sizing is load-bearing.** Top-down market figures corroborate; they do
   not anchor the model.
5. **Demand is not market size.** Validate willingness-to-pay, switching behavior,
   budget, and current substitutes separately.
6. **Financials are a model, not prophecy.** State drivers, formulas, uncertainty,
   scenario logic, and sensitivity.
7. **Regulation is a feasibility dimension.** Permits, ownership restrictions,
   localization requirements, tax treatment, or sector rules can block a project.
8. **Technical and operational feasibility are separate.** "Can be built" does not
   mean "can be operated economically".
9. **Red-team before verdict.** A final decision cannot issue until challenge findings
   are reconciled or explicitly carried forward.
10. **The human owns the decision.** The system produces an evidence-backed decision
    state and conditions; it does not silently choose for the user.

## Study modes

| Mode | Use | Required depth |
|---|---|---|
| `rapid` | Early screen / many ideas | Core evidence, demand, rough economics, blockers, next validation |
| `standard` | Serious founder/operator decision | Full market, technical, operational, regulatory, financial, scenarios, risk |
| `investment-grade` | Capital allocation / lender / IC depth | Standard + source redundancy, independent verification, sensitivity, red-team, reconciliation |

`investment-grade` means depth of diligence, not audited financial statements,
legal/tax opinion, fairness opinion, or assurance engagement.

## State machine

Run stages in order. Resume from persisted artifacts; do not re-derive settled work.

```text
00 Decision Frame
01 Evidence Plan
02 Market & Demand
03 Competition & Positioning
04 Technical Feasibility
05 Operational Feasibility
06 Regulatory & Jurisdiction
07 Business Model
08 Financial Model
09 Scenarios & Sensitivity
10 Risk & Pre-Mortem
11 Resources & Implementation
12 Validation Experiments
13 Independent Red Team
14 Evidence Reconciliation
15 Decision & Final Report
```

## Mandatory gates

- **Gate A — Scope:** Stage 00 complete before external research.
- **Gate B — Evidence:** no load-bearing claim without an evidence/assumption record.
- **Gate C — Market:** category boundary, demand evidence, and bottom-up sizing reconciled.
- **Gate D — Finance:** model inputs trace to assumption/evidence registers.
- **Gate E — Blockers:** technical, operational, and regulatory blockers resolved,
  conditioned, or retained.
- **Gate F — Red team:** all `BLOCKER` objections resolved or carried into the decision.
- **Gate G — Reconciliation:** report, model, scenarios, and evidence ledger agree.

## Loading map

Do not load every reference at once. Read only what the active stage needs.

| Stage | Read |
|---|---|
| 00–01 | `references/decision-frame.md`, `references/evidence-standard.md` |
| 02 | `references/research-protocol.md`, `references/market-demand.md` |
| 03 | `references/competition-positioning.md` |
| 04 | `references/technical-feasibility.md` |
| 05 | `references/operational-feasibility.md` |
| 06 | `references/regulatory-feasibility.md` + jurisdiction profile |
| 07 | `references/business-model.md` |
| 08 | `references/financial-model.md` |
| 09 | `references/scenarios-sensitivity.md` |
| 10 | `references/risk-premortem.md` |
| 11 | `references/implementation.md` |
| 12 | `references/validation-experiments.md` |
| 13 | `references/red-team.md` |
| 14–15 | `references/decision-engine.md`, `references/reporting-standard.md` |

For Saudi Arabia also read `references/jurisdictions/saudi-arabia.md`.

## Research discipline

When live web/research tools exist:

- Prefer official/primary sources for regulation, statistics, tax, licenses, filings,
  pricing, and company facts.
- Pull the current page; do not rely on model memory for time-sensitive rules.
- Record access date and data/reference period.
- Cross-check load-bearing numbers with an independent source where practical.
- If two sources disagree materially, preserve the range and explain the boundary
  or methodology difference.
- If a required fact is unavailable, write `UNKNOWN`; never manufacture a point estimate.

If live research is unavailable, do not pretend to have completed a current market or
regulatory study. Continue only with clearly labelled assumptions/proxies and lower confidence.

## Output contract

A standard or investment-grade study maintains:

```text
study/
  STUDY.json
  PROGRESS.md
  00-decision-frame.md
  01-evidence-plan.md
  02-market-demand.md
  03-competition-positioning.md
  04-technical-feasibility.md
  05-operational-feasibility.md
  06-regulatory-feasibility.md
  07-business-model.md
  08-financial-model.md
  09-scenarios-sensitivity.md
  10-risk-premortem.md
  11-implementation.md
  12-validation-experiments.md
  13-red-team.md
  14-reconciliation.md
  15-final-decision.md
  evidence.jsonl
  assumptions.jsonl
  sources.md
  financial-input.json
  financial-output.json
```

Create a study with:

```bash
python3 scripts/feasibility.py init <study-dir> --mode standard
```

## Decision states

The final state is one of:

- `GO`
- `CONDITIONAL_GO`
- `VALIDATE_FIRST`
- `PIVOT`
- `NO_GO_CURRENT_FORM`
- `TOO_EARLY`

Never derive the state from an average score. A single verified fatal blocker can dominate
many positive dimensions. Confidence in the state is reported separately.

## Dimension language

Signal: `STRONG / ADEQUATE / WEAK / UNKNOWN`.

Confidence: `HIGH / MEDIUM / LOW / UNKNOWN`.

A dimension may be `STRONG` with `LOW` confidence: promising signal, weak evidence.

## Financial tooling

```bash
python3 scripts/feasibility.py finance study/financial-input.json \
  --output study/financial-output.json
```

The bundled engine computes mechanical outputs only from supplied inputs: revenue/cost
summaries, free-cash-flow proxy, NPV, IRR where solvable, break-even, cumulative cash,
LTV/CAC when supported, and DSCR when supported.

A correct calculation from invented inputs is still a bad study. Evidence-gate inputs first.

## Validation

```bash
python3 scripts/feasibility.py validate study/
```

For repository self-validation:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Stop conditions

Stop and surface the issue instead of continuing when:

- the decision question is materially ambiguous;
- current regulation is required but cannot be verified;
- a load-bearing market number is unsupported;
- financial inputs are internally inconsistent;
- the revenue identity is not the business the user described;
- a red-team blocker remains unresolved;
- the final report contradicts the model or evidence ledger.

The purpose is not to finish every study. The purpose is to prevent weak evidence from
masquerading as a confident decision.
