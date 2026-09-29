#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from feasibility_study.router import routing_plan
from feasibility_study.study_v2 import init_study, validate_study

def main():
    p=argparse.ArgumentParser(prog="feasibility-v2")
    s=p.add_subparsers(dest="cmd",required=True)

    x=s.add_parser("init")
    x.add_argument("dest")
    x.add_argument("--mode",choices=["rapid","standard","investment-grade"],default="standard")
    x.add_argument("--force",action="store_true")

    x=s.add_parser("route")
    x.add_argument("profile")

    x=s.add_parser("validate")
    x.add_argument("study")

    a=p.parse_args()
    try:
        if a.cmd=="init":
            init_study(a.dest,a.mode,a.force)
            print(f"Initialized V2 {a.mode} study: {Path(a.dest).resolve()}")
        elif a.cmd=="route":
            profile=json.loads(Path(a.profile).read_text(encoding="utf-8"))
            print(json.dumps(routing_plan(profile),ensure_ascii=False,indent=2))
        else:
            issues=validate_study(a.study)
            for level,msg in issues:
                print(f"[{level.lower()}] {msg}")
            errors=[i for i in issues if i[0]=="ERROR"]
            print("study validation: "+("FAIL" if errors else "PASS"))
            raise SystemExit(1 if errors else 0)
    except (ValueError,FileExistsError,json.JSONDecodeError) as e:
        print(f"ERROR: {e}",file=sys.stderr)
        raise SystemExit(2)

if __name__=="__main__":
    main()
