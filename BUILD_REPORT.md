# Feasibility Study v0.1.0 — Build Report

## Result

- Repository validation: PASS
- Unit tests: 24/24 PASS
- Python bytecode compile: PASS
- Financial engine smoke: PASS
- Standard study scaffold: PASS
- Study validator smoke: PASS
- Installer dry-run (Claude + Codex): PASS
- Installer isolated-home install (Claude + Codex): PASS
- Installer doctor (Claude + Codex): PASS

## Security posture

- Standard-library Python only
- No bundled network client
- No subprocess execution in bundled Python
- No secret-shaped content detected by repository validator
- Installer refuses unmanaged destinations unless `--force` is explicit
- Uninstall refuses unmanaged installations
- Live web research remains under the host agent's authorized tools

## Architecture

- 16-stage feasibility state machine
- Evidence ledger with FACT / ESTIMATE / ASSUMPTION / JUDGMENT
- Bottom-up market sizing discipline
- Separate demand, technical, operational and regulatory feasibility
- Driver-based financial engine with NPV / IRR / break-even / LTV:CAC / DSCR where inputs support them
- Scenario multipliers and sensitivity protocol
- Risk + pre-mortem + kill criteria
- Four-lens independent red team
- Non-averaged decision engine
- Saudi Arabia jurisdiction research profile
- Safe Claude + Codex personal-skill installer

## Important boundary

`investment-grade` describes diligence depth, not an audit, tax opinion, legal opinion,
fairness opinion, licensed valuation, or assurance engagement.
