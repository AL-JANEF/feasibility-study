# Professional Artifact Output Standard

## Required final deliverables
For standard/investment-grade studies, unless explicitly waived:

1. `<project>-feasibility-study.docx`
2. `<project>-feasibility-study.pdf`
3. `<project>-financial-model.xlsx`

Place in `study/deliverables/`.

## DOCX
Professional report, normally containing:
- cover
- document control/version/date
- executive feasibility conclusion
- project definition
- methodology and evidence basis
- market and demand
- competition/pricing
- sector-specific technical/capacity study
- operations
- regulatory/legal/ESG
- organization/manpower
- implementation
- investment/CAPEX
- OPEX/COGS
- revenue forecast
- working capital and financing
- forecast financial statements
- investment appraisal
- scenarios/sensitivity/stress
- risk register
- red-team findings
- final conditions/kill criteria
- source notes and assumptions

For Arabic, use true RTL paragraph/table behavior and readable Arabic fonts available
on the host system. Do not ship font files.

## PDF
Render the report to PDF. Verify:
- pages are readable;
- Arabic is joined and RTL correctly;
- tables do not overflow;
- charts/figures are not clipped;
- no blank unexpected pages;
- final figures match DOCX and XLSX.

## XLSX
Must be auditable and formula-driven.
Use formulas for derived results; do not hard-code headline outputs.
Separate assumptions from calculations.
Use units and periods consistently.
Include model check cells prominently.

Minimum visible checks:
- BS balance check;
- cash reconciliation check;
- debt roll-forward check;
- sources/uses check;
- scenario-selection check.

## Source traceability
Each material assumption in the workbook should have a Source/Assumption ID.
The report should cite or reference the same evidence base.

## Verification before completion
Confirm:
- all three files exist;
- DOCX opens;
- PDF opens and is visually inspected;
- XLSX opens and formulas are intact;
- key report numbers match workbook outputs;
- no TODO/TBD placeholders remain except explicitly labeled UNKNOWN;
- final decision matches scenario/model evidence.

If the host lacks a PDF/DOCX/XLSX creation capability, do not silently substitute Markdown.
Use an available local artifact tool/library or explicitly report the missing capability.
