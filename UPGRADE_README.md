# Feasibility Study V2 Replacement Package

This package is intended to replace the reasoning layer of the installed `feasibility-study`
skill after copying it into the repository.

## What V2 changes
- mandatory sector/subsector classification;
- dynamic sector-pack synthesis for uncovered industries;
- sector-specific demand/capacity/technical/operating logic;
- integrated three-statement financial-model standard;
- explicit working-capital and financing schedules;
- coherent scenario/sensitivity/stress testing;
- required professional DOCX + PDF + XLSX deliverables;
- Arabic/RTL report requirements;
- V2 router, study scaffold, validation and deliverable checks.

## Important
The current V1 financial engine is not deleted by this package. V2 does not treat its
simple `free_cash_flow_proxy` as the final financial model. The final model is expected to
be built in the XLSX deliverable and must satisfy the V2 financial-model standard.

## Installation into repository
Copy this package over the repository root, preserving directories, then run the V2
validation/tests. After verification, commit and install the skill.

The repository's existing installer already includes:
`SKILL.md`, `VERSION`, `references`, `schemas`, `scripts`, and `feasibility_study`,
so these V2 files will be installed into Claude Code and Codex.
