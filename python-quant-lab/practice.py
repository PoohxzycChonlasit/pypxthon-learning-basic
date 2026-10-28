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
        if not isinstance(value, dict):
            return {"exercises": {}}
    except (OSError, json.JSONDecodeError):
        return {"exercises": {}}
    exercises = value.setdefault("exercises", {})
    assessment = exercises.get("L01-E015")
    migrated = False
    if assessment:
        for key, default in (("assessment_variant", "A"), ("revealed_assessments", ["A"] if assessment.get("solution_viewed") else []), ("hinted_assessments", ["A"] if assessment.get("hints") else []), ("assessment_results", {})):
            if key not in assessment:
                assessment[key] = default
                migrated = True
        if assessment.get("status") == "PASSED_INDEPENDENTLY" and "assessment_verified" not in assessment:
            assessment["legacy_assessment_pending"] = True
            assessment["assessment_verified"] = False
            migrated = True
        else:
            if "assessment_verified" not in assessment:
                assessment["assessment_verified"] = False
                migrated = True
    if migrated:
        save_progress(value)
    return value


def save_progress(p):
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    tmp = PROGRESS.with_suffix(".tmp")
    tmp.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, PROGRESS)


def ex_path(ex, kind):
    if ex.get("submission_mode") == "text_answer":
        if kind == "exercises":
            return ROOT / ex["answer_file"]
        if kind == "solutions":
            return ROOT / "solutions" / f"level_{ex['level']:02d}" / f"{ex['id']}.txt"
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
    st = p.setdefault("exercises", {}).setdefault(ex["id"], {
        "status": "NOT_STARTED", "attempts": 0, "hints": [], "solution_viewed": False
    })
    if ex.get("assessment"):
        st.setdefault("assessment_variant", "A")
        st.setdefault("revealed_assessments", [])
        st.setdefault("hinted_assessments", [])
        st.setdefault("assessment_results", {})
        st.setdefault("assessment_verified", False)
    return st


def unlocked(ex, all_ex, p):
    ix = all_ex.index(ex)
    if ix == 0:
        return True
    prev = all_ex[ix - 1]
    prev_state = state(p, prev)
    prev_status = prev_state["status"]
    if ex["level"] > prev["level"]:
        if prev["id"] == "L01-E015" and (not prev_state.get("assessment_verified") or prev_state.get("legacy_assessment_pending")):
            return False
        return prev_status == "PASSED_INDEPENDENTLY"
    return prev_status in ("PASSED_INDEPENDENTLY", "PASSED_WITH_HELP")


def show_lesson(ex):
    variant = None
    problem = ex["problem"]
    sample = ex["sample"]
    expected = ex["expected"]
    if ex.get("assessment"):
        variant = state(read_progress(), ex)["assessment_variant"]
        problem = ex.get("variant_prompts", {}).get(variant, problem)
        sample = ex.get("variant_samples", {}).get(variant, sample)
        expected = ex.get("variant_expected", {}).get(variant, expected)
    print(f"บทเรียน {ex['id']} — {ex['title']}\nเป้าหมาย: {ex['objective']}\n")
    lesson_path = ROOT / "lessons" / f"{ex['id']}.md"
    if not lesson_path.is_file():
        lesson_path = ROOT / ex["lesson_file"]
    if lesson_path.is_file():
        print(f"บทเรียนแบบพิมพ์ตาม: {lesson_path}\n")
        print(lesson_path.read_text(encoding="utf-8"))
    if variant:
        print(f"Assessment variant {variant}; ตัวอย่าง input: {sample}")
    print(ex["lesson"])
    print(f"\nตัวอย่าง\n{ex['example']}\n\nข้อผิดพลาดที่พบบ่อย: {ex['pitfall']}")
    if ex.get("submission_mode") == "text_answer" or ex.get("assessment"):
        print(f"\nโจทย์: {problem}\nข้อมูลตัวอย่าง: {sample}\nข้อจำกัด: {ex['constraints']}")
        print("ซ่อนผลลัพธ์ตัวอย่างไว้ เพื่อให้คุณตรวจความเข้าใจด้วยตนเอง")
    else:
        print(f"\nโจทย์: {problem}\nข้อมูลตัวอย่าง: {sample}\nผลลัพธ์ตัวอย่าง: {expected}\nข้อจำกัด: {ex['constraints']}")
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
    cases = ex["cases"]
    variant = None
    if ex.get("assessment"):
        variant = st["assessment_variant"]
        cases = json.loads((ROOT / "tests" / "assessment" / f"{ex['id']}-{variant}.json").read_text(encoding="utf-8"))
    else:
        fixture_path = ROOT / "tests" / f"{ex['id']}.json"
        if fixture_path.is_file():
            cases = json.loads(fixture_path.read_text(encoding="utf-8"))
    if ex.get("submission_mode") in ("stdout", "literal", "text_answer"):
        failures = []
        passed_count = 0
        for number, case in enumerate(cases, 1):
            try:
                if ex["submission_mode"] == "text_answer":
                    actual = file.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n")
                    expected = case["expected"]
                    success = actual == expected
                    detail = "คำตอบยังไม่ตรงกับผลที่ทำนายไว้ ตรวจลำดับและบรรทัดว่างอีกครั้ง"
                elif ex["submission_mode"] == "literal":
                    harness = 'import json,runpy,sys; ns=runpy.run_path(sys.argv[1]); actual=ns.get("ANSWER"); expected=json.loads(sys.stdin.read()); assert actual==expected, f"expected {expected!r}, got {actual!r}"'
                    result = subprocess.run([sys.executable, "-X", "utf8", "-I", "-c", harness, str(file)], input=json.dumps(case["expected"]), text=True, encoding="utf-8", capture_output=True, timeout=4, cwd=ROOT)
                    success = result.returncode == 0
                    detail = result.stderr.strip()
                else:
                    result = subprocess.run([sys.executable, "-X", "utf8", "-I", str(file)], input=case.get("stdin", ""), text=True, encoding="utf-8", capture_output=True, timeout=4, cwd=ROOT)
                    actual = result.stdout.replace("\r\n", "\n")
                    expected = case["expected_stdout"]
                    success = result.returncode == 0 and actual == expected
                    detail = result.stderr.strip() if result.returncode else f"expected stdout {expected!r}; got {actual!r}"
                if success:
                    passed_count += 1
                    print(f"Test {number} — {case['name']}: PASS")
                else:
                    failures.append(detail or "คำตอบไม่ตรงกับที่กำหนด")
                    print(f"Test {number} — {case['name']}: FAIL")
                    if detail and not ex.get("assessment"):
                        print(detail[-1200:])
            except subprocess.TimeoutExpired:
                failures.append("โปรแกรมใช้เวลาเกิน 4 วินาที")
                print(f"Test {number} — {case['name']}: TIMEOUT")
        passed = not failures and len(cases) > 0
        print(f"ผล: {passed_count}/{len(cases)} กรณีผ่าน")
        if ex.get("assessment"):
            assisted = variant in st["revealed_assessments"] or variant in st["hinted_assessments"]
            st["assessment_results"][variant] = "PASSED_WITH_HELP" if passed and assisted else ("PASSED_INDEPENDENTLY" if passed else "NEEDS_REVIEW")
            if passed and not assisted:
                st["assessment_verified"] = True
                st.pop("legacy_assessment_pending", None)
        else:
            assisted = st["solution_viewed"] or bool(st["hints"])
        if passed:
            st["status"] = "PASSED_WITH_HELP" if assisted else "PASSED_INDEPENDENTLY"
        else:
            st["status"] = "NEEDS_REVIEW"
        st.setdefault("results", []).append({"passed": passed, "tests": len(cases), "variant": variant})
        print(f"สถานะ: {st['status']}")
        save_progress(p)
        return
    harness = r'''import importlib.util,json,sys
spec=importlib.util.spec_from_file_location("student",sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
cases=json.loads(sys.stdin.read()); fn=getattr(m,sys.argv[2])
def norm(x):
    if isinstance(x,tuple): return [norm(v) for v in x]
    if isinstance(x,list): return [norm(v) for v in x]
    if isinstance(x,dict): return {str(k):norm(v) for k,v in x.items()}
    return x
def matches(got, expected, tolerance=1e-8):
    if isinstance(expected, dict):
        return isinstance(got, dict) and set(got) == set(expected) and all(matches(got[k], expected[k], tolerance) for k in expected)
    if isinstance(expected, list):
        return isinstance(got, list) and len(got) == len(expected) and all(matches(a, b, tolerance) for a, b in zip(got, expected))
    if isinstance(expected, float) and isinstance(got, (int, float)):
        return abs(got - expected) <= tolerance
    return got == expected
for i,c in enumerate(cases,1):
    got=norm(fn(*c["args"],**c.get("kwargs",{}))); expected=norm(c["expected"])
    assert matches(got, expected, float(c.get("tolerance",1e-8))), f"case {i}: expected {expected!r}, got {got!r}"
print("PASS",len(cases))
'''
    try:
        result = subprocess.run([sys.executable, "-X", "utf8", "-I", "-c", harness, str(file), ex["function"]], input=json.dumps(cases), text=True, encoding="utf-8", capture_output=True, timeout=4, cwd=ROOT)
    except subprocess.TimeoutExpired:
        result = None
    passed = result is not None and result.returncode == 0
    print(f"แบบฝึกหัด: {ex['id']} — {ex['title']}")
    if passed:
        if ex.get("assessment"):
            assisted = variant in st["revealed_assessments"] or variant in st["hinted_assessments"]
            st["assessment_results"][variant] = "PASSED_WITH_HELP" if assisted else "PASSED_INDEPENDENTLY"
            if not assisted:
                st["assessment_verified"] = True
                st.pop("legacy_assessment_pending", None)
        else:
            assisted = st["solution_viewed"] or bool(st["hints"])
        st["status"] = "PASSED_WITH_HELP" if assisted else "PASSED_INDEPENDENTLY"
        st.setdefault("results", []).append({"passed": True, "tests": len(cases), "variant": variant})
        print(f"ผล: ผ่าน {len(cases)} กรณี ({st['status']})")
    else:
        if ex.get("assessment"):
            st["assessment_results"][variant] = "NEEDS_REVIEW"
        st["status"] = "NEEDS_REVIEW"
        st.setdefault("results", []).append({"passed": False, "tests": len(cases), "variant": variant})
        print("ผล: ยังไม่ผ่าน — ตรวจข้อผิดพลาดแล้วลองใหม่")
        print("สถานะ: NEEDS_REVIEW")
        if result is None:
            print("โปรแกรมใช้เวลาเกิน 4 วินาที")
        elif result.stderr and not ex.get("assessment"):
            print(result.stderr[-2000:])
        elif ex.get("assessment"):
            print("ซ่อนผลที่คาดไว้สำหรับ assessment; ตรวจขั้นตอนและกรณีขอบแล้วลองอีกครั้ง")
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
        if ex.get("submission_mode") in ("literal", "text_answer"):
            print("ข้อนี้เป็นการทำนายผล: กรอกผลลัพธ์ในไฟล์คำตอบ แล้วใช้ check เพื่อตรวจ")
            return
        harness='import importlib.util,sys,json; s=importlib.util.spec_from_file_location("student",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); f=getattr(m,sys.argv[2]); c=json.loads(sys.stdin.read())[0]; print(repr(f(*c["args"])))'
        try:
            if ex.get("submission_mode") == "stdout":
                case=ex["cases"][0]
                result=subprocess.run([sys.executable,"-X","utf8","-I",str(file)],input=case.get("stdin",""),text=True,encoding="utf-8",capture_output=True,timeout=4,cwd=ROOT)
            else:
                result=subprocess.run([sys.executable,"-X","utf8","-I","-c",harness,str(file),ex["function"]],input=json.dumps(ex["cases"]),text=True,encoding="utf-8",capture_output=True,timeout=4,cwd=ROOT)
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
        st = state(p, ex)
        current_variant = st.get("assessment_variant", "A")
        exposed = current_variant in st.get("revealed_assessments", []) or current_variant in st.get("hinted_assessments", [])
        if ex.get("assessment") and (st["attempts"] > 0 or exposed):
            st["assessment_variant"] = "B" if st["assessment_variant"] == "A" else "A"
            st["status"] = "IN_PROGRESS"
            print("เริ่ม assessment variant ใหม่:", st["assessment_variant"])
        p["current"] = ex["id"]; save_progress(p); print("เปิดไฟล์เดิมเพื่อแก้ไข:", ex_path(ex, "exercises"))
        if ex.get("assessment"):
            show_lesson(ex)
    elif args.command == "hint":
        n = int(args.detail or (len(state(p, ex)["hints"]) + 1)); n = min(max(n, 1), 3)
        print(f"คำใบ้ {n}: {ex['hints'][n-1]}"); st = state(p, ex); st["hints"] = sorted(set(st["hints"] + [n]))
        if ex.get("assessment"):
            st["hinted_assessments"] = sorted(set(st["hinted_assessments"] + [st["assessment_variant"]]))
        save_progress(p)
    elif args.command in ("solution", "explain"):
        st = state(p, ex)
        if not st["solution_viewed"] and not (args.yes or input("เนื้อหานี้มีเฉลยเต็ม ต้องการดูหรือไม่? พิมพ์ YES: ") == "YES"):
            print("ยกเลิก"); return
        st["solution_viewed"] = True
        if ex.get("assessment"):
            st["revealed_assessments"] = sorted(set(st["revealed_assessments"] + [st["assessment_variant"]]))
        save_progress(p)
        if args.command == "solution":
            solution_path = ex_path(ex, "solutions")
            if ex.get("assessment"):
                solution_path = ROOT / "solutions" / "assessment" / f"{ex['id']}-{st['assessment_variant']}.py"
            print(solution_path.read_text(encoding="utf-8"))
        else: print((ROOT / "explanations" / f"{ex['id']}.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
