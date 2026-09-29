#!/usr/bin/env python3
import ast, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
errors=[]
required=[
    "SKILL.md","VERSION",
    "references/core/methodology.md",
    "references/core/sector-routing.md",
    "references/core/financial-model-standard.md",
    "references/core/artifact-output-standard.md",
    "references/sectors/digital-services.md",
    "references/sectors/healthcare-life-sciences.md",
    "references/sectors/industrial-resources.md",
    "references/sectors/asset-consumer.md",
    "references/jurisdictions/saudi-arabia-v2.md",
    "schemas/project-profile.schema.json",
    "feasibility_study/router.py",
    "feasibility_study/study_v2.py",
    "scripts/feasibility_v2.py",
    "scripts/check_deliverables.py",
]
for rel in required:
    if not (ROOT/rel).exists():
        errors.append(f"missing {rel}")
if (ROOT/"VERSION").exists() and (ROOT/"VERSION").read_text().strip()!="0.2.0":
    errors.append("VERSION must be 0.2.0")
for p in ROOT.rglob("*.py"):
    try: ast.parse(p.read_text(encoding="utf-8"),filename=str(p))
    except SyntaxError as e: errors.append(f"syntax {p.relative_to(ROOT)}: {e}")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".md",".py",".json",".txt",".yml",".yaml"}:
        txt=p.read_text(encoding="utf-8",errors="ignore")
        for pat in [r"AKIA[0-9A-Z]{16}",r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",r"ghp_[A-Za-z0-9]{30,}"]:
            if re.search(pat,txt): errors.append(f"secret-shaped content in {p.relative_to(ROOT)}")
print("Feasibility Study V2 repository validation")
for e in errors: print("[FAIL]",e)
if errors:
    print(f"validation: FAIL ({len(errors)} errors)")
    raise SystemExit(1)
print("validation: PASS")
