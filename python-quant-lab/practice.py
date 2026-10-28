"""Python Quant Lab: offline exercise runner (Python 3.12, stdlib only)."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CURRICULUM = ROOT / "curriculum.json"
PROGRESS = ROOT / "progress.json"


def catalog():
    return json.loads(CURRICULUM.read_text(encoding="utf-8"))


def read_progress():
    try:
        value = json.loads(PROGRESS.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {"exercises": {}}


def save_progress(p):
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    tmp = PROGRESS.with_suffix(".tmp")
    tmp.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, PROGRESS)


def ex_path(ex, kind):
    return ROOT / kind / f"level_{ex['level']:02d}" / f"{ex['id']}.py"


def find_ex(cid=None):
    all_ex = catalog()
    p = read_progress()
    if cid is None:
        cid = p.get("current") or all_ex[0]["id"]
    for ex in all_ex:
        if ex["id"] == cid:
            return ex
    raise ValueError(f"ไม่พบรหัส {cid}")


def state(p, ex):
    return p.setdefault("exercises", {}).setdefault(ex["id"], {
        "status": "NOT_STARTED", "attempts": 0, "hints": [], "solution_viewed": False
    })


def unlocked(ex, all_ex, p):
    ix = all_ex.index(ex)
    if ix == 0:
        return True
    prev = all_ex[ix - 1]
    prev_status = state(p, prev)["status"]
    if ex["level"] > prev["level"]:
        return prev_status == "PASSED_INDEPENDENTLY"
    return prev_status in ("PASSED_INDEPENDENTLY", "PASSED_WITH_HELP")


def show_lesson(ex):
    print(f"บทเรียน {ex['id']} — {ex['title']}\nเป้าหมาย: {ex['objective']}\n")
    print(ex["lesson"])
    print(f"\nตัวอย่าง\n{ex['example']}\n\nข้อผิดพลาดที่พบบ่อย: {ex['pitfall']}")
    print(f"\nโจทย์: {ex['problem']}\nข้อมูลตัวอย่าง: {ex['sample']}\nผลที่คาดหวัง: {ex['expected']}\nข้อจำกัด: {ex['constraints']}")
    print(f"\nไฟล์คำตอบ: {ex_path(ex, 'exercises')}")


def run_check(ex, p):
    if not unlocked(ex, catalog(), p):
        print("ยังล็อกอยู่: ผ่านแบบทดสอบก่อนหน้าก่อน")
        return
    file = ex_path(ex, "exercises")
    st = state(p, ex)
    st["attempts"] += 1
    st["status"] = "IN_PROGRESS"
    save_progress(p)
    harness = r'''import importlib.util,json,sys
spec=importlib.util.spec_from_file_location("student",sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
cases=json.loads(sys.stdin.read()); fn=getattr(m,sys.argv[2])
def norm(x):
    if isinstance(x,tuple): return [norm(v) for v in x]
    if isinstance(x,list): return [norm(v) for v in x]
    if isinstance(x,dict): return {str(k):norm(v) for k,v in x.items()}
    return x
for i,c in enumerate(cases,1):
    got=norm(fn(*c["args"],**c.get("kwargs",{}))); expected=norm(c["expected"])
    if isinstance(expected,float) and isinstance(got,(int,float)):
        assert abs(got-expected) <= float(c.get("tolerance",1e-8)), f"case {i}: expected {expected}, got {got}"
    else: assert got==expected, f"case {i}: expected {expected!r}, got {got!r}"
print("PASS",len(cases))
'''
    try:
        result = subprocess.run([sys.executable, "-I", "-c", harness, str(file), ex["function"]], input=json.dumps(ex["cases"]), text=True, capture_output=True, timeout=4, cwd=ROOT)
    except subprocess.TimeoutExpired:
        result = None
    passed = result is not None and result.returncode == 0
    print(f"แบบฝึกหัด: {ex['id']} — {ex['title']}")
    if passed:
        assisted = st["solution_viewed"] or bool(st["hints"])
        st["status"] = "PASSED_WITH_HELP" if assisted else "PASSED_INDEPENDENTLY"
        st.setdefault("results", []).append({"passed": True, "tests": len(ex["cases"])})
        print(f"ผล: ผ่าน {len(ex['cases'])} กรณี ({st['status']})")
    else:
        st["status"] = "NEEDS_REVIEW"
        st.setdefault("results", []).append({"passed": False})
        print("ผล: ยังไม่ผ่าน — ตรวจข้อผิดพลาดแล้วลองใหม่")
        if result is None:
            print("โปรแกรมใช้เวลาเกิน 4 วินาที")
        elif result.stderr:
            print(result.stderr[-2000:])
    save_progress(p)


def main():
    ap = argparse.ArgumentParser(description="Python Quant Lab — ฝึก Python แบบออฟไลน์")
    ap.add_argument("command", nargs="?", default="help", choices="help start lesson open next list status run check hint solution explain retry reset-progress".split())
    ap.add_argument("id", nargs="?")
    ap.add_argument("detail", nargs="?")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()
    all_ex = catalog(); p = read_progress()
    if args.command == "help":
        print("คำสั่ง: start, lesson, open, next, list, status, run, check, hint [ID [1-3]], solution [ID] [--yes], explain [ID], retry ID, reset-progress")
        return
    if args.command == "list":
        for ex in all_ex:
            print(ex["id"], state(p, ex)["status"], ex["title"])
        return
    if args.command == "status":
        print("แบบฝึกหัดปัจจุบัน:", p.get("current", all_ex[0]["id"]))
        for k in ("NOT_STARTED", "IN_PROGRESS", "PASSED_INDEPENDENTLY", "PASSED_WITH_HELP", "NEEDS_REVIEW"):
            print(k, sum(state(p, x)["status"] == k for x in all_ex))
        return
    if args.command == "reset-progress":
        if args.yes or input("ล้างเฉพาะ progress.json (ไม่ลบงานเขียน) หรือไม่? พิมพ์ YES: ") == "YES":
            save_progress({"exercises": {}}); print("ล้างความคืบหน้าแล้ว")
        return
    ex = find_ex(args.id)
    if args.command in ("start", "lesson"):
        p["current"] = ex["id"]; save_progress(p); show_lesson(ex)
    elif args.command == "run":
        file=ex_path(ex,"exercises")
        harness='import importlib.util,sys,json; s=importlib.util.spec_from_file_location("student",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); f=getattr(m,sys.argv[2]); c=json.loads(sys.stdin.read())[0]; print(repr(f(*c["args"])))'
        try:
            result=subprocess.run([sys.executable,"-I","-c",harness,str(file),ex["function"]],input=json.dumps(ex["cases"]),text=True,capture_output=True,timeout=4,cwd=ROOT)
            print("ผลทดลอง:", result.stdout.strip() if result.returncode==0 else result.stderr[-1500:])
        except subprocess.TimeoutExpired:
            print("โปรแกรมใช้เวลาเกิน 4 วินาที")
    elif args.command == "open":
        path=ex_path(ex,"exercises")
        try:
            subprocess.Popen(["code","-r",str(path)],cwd=ROOT)
            print("เปิดไฟล์:",path)
        except OSError:
            print("เปิดไฟล์นี้ใน VS Code:",path)
    elif args.command == "check": run_check(ex, p)
    elif args.command == "next":
        ix = all_ex.index(ex)
        if ix + 1 == len(all_ex): print("จบหลักสูตรแล้ว")
        elif not unlocked(all_ex[ix + 1], all_ex, p): print("ผ่านแบบฝึกหัดนี้ก่อนจึงจะปลดล็อกข้อถัดไป")
        else:
            ex = all_ex[ix + 1]; p["current"] = ex["id"]; save_progress(p); show_lesson(ex)
    elif args.command == "retry":
        p["current"] = ex["id"]; save_progress(p); print("เปิดไฟล์เดิมเพื่อแก้ไข:", ex_path(ex, "exercises"))
    elif args.command == "hint":
        n = int(args.detail or (len(state(p, ex)["hints"]) + 1)); n = min(max(n, 1), 3)
        print(f"คำใบ้ {n}: {ex['hints'][n-1]}"); st = state(p, ex); st["hints"] = sorted(set(st["hints"] + [n])); save_progress(p)
    elif args.command in ("solution", "explain"):
        st = state(p, ex)
        if not st["solution_viewed"] and not (args.yes or input("เนื้อหานี้มีเฉลยเต็ม ต้องการดูหรือไม่? พิมพ์ YES: ") == "YES"):
            print("ยกเลิก"); return
        st["solution_viewed"] = True; save_progress(p)
        if args.command == "solution": print(ex_path(ex, "solutions").read_text(encoding="utf-8"))
        else: print((ROOT / "explanations" / f"{ex['id']}.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
