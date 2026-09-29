#!/usr/bin/env python3
import argparse, zipfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("deliverables")
    p.add_argument("--project")
    a=p.parse_args()
    d=Path(a.deliverables)
    files=list(d.glob("*")) if d.exists() else []
    docx=[x for x in files if x.suffix.lower()==".docx"]
    pdf=[x for x in files if x.suffix.lower()==".pdf"]
    xlsx=[x for x in files if x.suffix.lower()==".xlsx"]
    errors=[]
    if not docx: errors.append("missing DOCX")
    if not pdf: errors.append("missing PDF")
    if not xlsx: errors.append("missing XLSX")
    for f in docx+xlsx:
        try:
            with zipfile.ZipFile(f) as z:
                if z.testzip() is not None: errors.append(f"corrupt zip container: {f.name}")
        except Exception as e: errors.append(f"cannot open {f.name}: {e}")
    for f in pdf:
        try:
            if not f.read_bytes().startswith(b"%PDF-"): errors.append(f"invalid PDF header: {f.name}")
        except Exception as e: errors.append(f"cannot open {f.name}: {e}")
    if errors:
        for e in errors: print("[FAIL]",e)
        raise SystemExit(1)
    print("deliverables validation: PASS")
    for f in docx+pdf+xlsx:
        print(f"{f.name}: {f.stat().st_size} bytes")

if __name__=="__main__":
    main()
