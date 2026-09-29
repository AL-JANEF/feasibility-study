# Feasibility Study

Maintained by **AL-JANEF**.

**Decision discipline for ideas before capital is committed.**

Evidence-first feasibility for startups, SaaS, marketplaces, services,
industrial/manufacturing projects, expansions and market entry.

Core capabilities:

- decision framing and evidence ledger
- market/demand and competitive intelligence
- technical, operational and regulatory feasibility
- driver-based financial model
- downside/base/upside scenarios and sensitivity
- risk register, pre-mortem and kill criteria
- independent red team and reconciliation
- decision states: GO / CONDITIONAL_GO / VALIDATE_FIRST / PIVOT /
  NO_GO_CURRENT_FORM / TOO_EARLY

## Install for Claude + Codex

```bash
python3 scripts/install.py install --target both --dry-run
python3 scripts/install.py install --target both
python3 scripts/install.py doctor --target both
```

## Create a study

```bash
python3 scripts/feasibility.py init ~/Documents/my-study --mode standard
```

Modes: `rapid`, `standard`, `investment-grade`.

## Validate

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Saudi Arabia

`references/jurisdictions/saudi-arabia.md` is a live-research map. It deliberately
avoids hardcoding tax rates, localization percentages, fees, ownership limits or
permit timelines; those must be verified from the current competent authority.

## License

MIT — © 2026 AL-JANEF.
