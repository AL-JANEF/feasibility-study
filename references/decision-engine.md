# Decision Engine

Do not average dimensions into one score.

For market, competition, technical, operational, regulatory, business model, financial, execution/resources,
and risk report signal `STRONG/ADEQUATE/WEAK/UNKNOWN`, confidence `HIGH/MEDIUM/LOW/UNKNOWN`, blockers,
critical assumptions, evidence IDs and what would change the finding.

Decision states:
- `GO`: no unresolved fatal blocker and evidence supports threshold.
- `CONDITIONAL_GO`: viable if named measurable conditions are met before irreversible commitment.
- `VALIDATE_FIRST`: critical unknown can flip decision and is cheap to test relative to capital at risk.
- `PIVOT`: current form weak, but evidence supports a specific adjacent form worth re-evaluating.
- `NO_GO_CURRENT_FORM`: verified structural blocker or unattractive economics under plausible scenarios.
- `TOO_EARLY`: enabling technology/regulation/ecosystem/timing is outside the horizon.

Decision confidence is separate from attractiveness. High confidence can support NO-GO.
The human decision owner makes the actual commit/pause/pivot/stop choice.
