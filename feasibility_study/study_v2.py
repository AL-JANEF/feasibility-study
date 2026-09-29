from pathlib import Path
import json
from .router import routing_plan

STAGES = [
    "00-project-classification.md",
    "01-sector-pack.md",
    "02-decision-evidence.md",
    "03-market-demand.md",
    "04-sales-revenue-engine.md",
    "05-technical-capacity.md",
    "06-operations.md",
    "07-regulatory-legal-esg.md",
    "08-organization-manpower.md",
    "09-implementation.md",
    "10-capex.md",
    "11-opex-cogs.md",
    "12-working-capital.md",
    "13-financing.md",
    "14-integrated-financial-model.md",
    "15-investment-appraisal.md",
    "16-scenarios.md",
    "17-sensitivity-switching.md",
    "18-stress-tests.md",
    "19-risk-premortem.md",
    "20-red-team.md",
    "21-final-feasibility.md",
]

def init_study(dest, mode="standard", force=False):
    if mode not in {"rapid","standard","investment-grade"}:
        raise ValueError(f"invalid mode: {mode}")
    d=Path(dest)
    if d.exists() and any(d.iterdir()) and not force:
        raise FileExistsError(f"{d} is not empty; use --force")
    d.mkdir(parents=True, exist_ok=True)
    (d/"deliverables").mkdir(exist_ok=True)
    for name in STAGES:
        title=name[:-3].replace("-"," ").title()
        (d/name).write_text(f"# {title}\n\n", encoding="utf-8")
    profile={
        "project_name":"",
        "description":"",
        "sector":"",
        "subsector":"",
        "business_model":"",
        "customer_type":"MIXED",
        "jurisdiction":"",
        "stage":"",
        "financing_type":"",
        "study_mode":mode,
        "currency":"SAR",
        "language":"ar",
        "decision_question":"",
    }
    (d/"PROJECT_PROFILE.json").write_text(json.dumps(profile, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (d/"PROGRESS.md").write_text("# Progress\n\nCurrent stage: 00\n", encoding="utf-8")
    (d/"evidence.jsonl").touch()
    (d/"assumptions.jsonl").touch()
    (d/"sources.md").write_text("# Sources\n\n", encoding="utf-8")

def validate_study(dest):
    d=Path(dest)
    issues=[]
    if not d.exists():
        return [("ERROR",f"study directory not found: {d}")]
    for name in STAGES:
        if not (d/name).exists():
            issues.append(("ERROR",f"missing required artifact: {name}"))
    profile_path=d/"PROJECT_PROFILE.json"
    if not profile_path.exists():
        issues.append(("ERROR","missing PROJECT_PROFILE.json"))
    else:
        try:
            profile=json.loads(profile_path.read_text(encoding="utf-8"))
            routing_plan(profile)
        except Exception as e:
            issues.append(("ERROR",f"invalid/incomplete PROJECT_PROFILE.json: {e}"))
    for name in ["evidence.jsonl","assumptions.jsonl","sources.md","PROGRESS.md"]:
        if not (d/name).exists():
            issues.append(("ERROR",f"missing {name}"))
    return issues
