"""Write Level 1 artifacts; expected outputs below are authored fixtures, not solution output."""
import json
from pathlib import Path
from level_01_content import ITEMS

ROOT = Path(__file__).resolve().parent


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_student(path, text):
    """Replace only the known untouched generated stubs; thereafter preserve edits."""
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if "PYQL_L1_STARTER" in current or "TODO: implement the behavior in the exercise instructions." not in current:
            return False
    write(path, "# PYQL_L1_STARTER\n" + text)
    return True


def normalize_console(value):
    """Use Windows code-page-safe arithmetic glyphs in text printed by the CLI."""
    if isinstance(value, str):
        return value.replace("×", "*").replace("÷", "/").replace("−", "-")
    if isinstance(value, list):
        return [normalize_console(x) for x in value]
    if isinstance(value, dict):
        return {k: normalize_console(v) for k, v in value.items()}
    return value


def main():
    curriculum_path = ROOT / "curriculum.json"
    catalog = json.loads(curriculum_path.read_text(encoding="utf-8"))
    positions = {e["id"]: i for i, e in enumerate(catalog)}
    for item in ITEMS:
        item = normalize_console(item)
        if item["id"] == "L01-E013":
            item["lesson"] += " ฟังก์ชัน `abs(x)` คืนค่าขนาดที่ไม่ติดลบของ x จึงใช้คิดค่าธรรมเนียมได้แม้ gross เป็นขาดทุน"
        if item["id"] == "L01-E015":
            item["variants"]["B"] = [
                {"name": "budget transfer positive", "stdin": "1000\n100\n50\n25\n", "expected_stdout": "Expenses: 175.00\nRemaining: 825.00\n"},
                {"name": "budget transfer overspend", "stdin": "100\n80\n30\n10\n", "expected_stdout": "Expenses: 120.00\nRemaining: -20.00\n"},
            ]
            item["variant_solutions"]["B"] = "income = float(input())\nhousing = float(input())\nfood = float(input())\nother = float(input())\nexpenses = housing + food + other\nremaining = income - expenses\nprint(f\"Expenses: {expenses:.2f}\")\nprint(f\"Remaining: {remaining:.2f}\")\n"
            item["variant_prompts"] = {
                "A": item["problem"],
                "B": "โจทย์ประเมินชุดใหม่: อ่านรายรับ ค่าที่พัก ค่าอาหาร และค่าใช้จ่ายอื่น คนละบรรทัด แล้วแสดง `Expenses: ...` และ `Remaining: ...` เป็นทศนิยมสองตำแหน่ง ค่าใช้จ่ายรวมคือค่าที่พัก + อาหาร + อื่น และเงินคงเหลือคือรายรับ − ค่าใช้จ่ายรวม",
            }
            item["variant_prompts"] = normalize_console(item["variant_prompts"])
            item["variant_samples"] = {"A": "100, 110, 0.1, 1", "B": "1000, 100, 50, 25"}
            item["variant_expected"] = {"A": item["expected"], "B": "Expenses = housing + food + other; Remaining = income - Expenses; both have two decimal places"}
        prediction_prompts = {
            "L01-E002": "ยังไม่ต้องรันโค้ด ให้เขียนผลลัพธ์สองบรรทัดลงไฟล์คำตอบ .txt โดยหนึ่งผลลัพธ์ต่อบรรทัด สำหรับ print(8 + 2 * 3) และ print((8 + 2) * 3)",
            "L01-E007": "ทายผลลัพธ์ของโค้ดในโจทย์ แล้วเขียนค่าที่แสดงลงไฟล์คำตอบ .txt โดยหนึ่งผลลัพธ์ต่อบรรทัด",
            "L01-E012": "ทายค่าที่ print แสดงจาก amount = 80, percent = 10, print(amount * percent / 100) แล้วเขียนค่าหนึ่งบรรทัดลงไฟล์คำตอบ .txt",
        }
        prediction_explanations = {
            "L01-E002": "บรรทัดแรกคูณก่อน: 2×3 ได้ 6 แล้วบวก 8 จึงได้ 14 บรรทัดที่สองคำนวณวงเล็บก่อน: 8+2 ได้ 10 แล้วคูณ 3 จึงได้ 30 ส่งคำตอบเป็นข้อความสองบรรทัดในไฟล์ .txt โดยไม่ต้องเขียน Python",
            "L01-E007": "ค่าของ coins คือ 2 และ price คือ 3 จึงคูณกันได้ 6 คำสั่ง print ถัดไปแสดง BTC ในบรรทัดใหม่ ส่งผลทั้งสองบรรทัดลงไฟล์ข้อความคำตอบ",
            "L01-E012": "แทนค่าตัวแปรในนิพจน์ได้ 80×10÷100 การคูณและหารมีลำดับเดียวกันและคำนวณซ้ายไปขวา ผลทางคณิตศาสตร์คือ 8 แต่ Python ใช้ / จึงแสดงเป็น 8.0 ส่งข้อความนี้ลงไฟล์คำตอบ",
        }
        if item["id"] in prediction_prompts:
            item["problem"] = prediction_prompts[item["id"]]
            item["sample"] = "เขียนผลลัพธ์ที่คาดลงไฟล์ข้อความคำตอบตามจำนวนบรรทัดของ stdout"
            item["explanation"] = normalize_console(prediction_explanations[item["id"]])
        if item["id"] in ("L01-E002", "L01-E007"):
            item["expected"] = item["expected"].replace("\\n", "\n")
            item["cases"][0]["expected"] = item["cases"][0]["expected"].replace("\\n", "\n")
        ex = catalog[positions[item["id"]]]
        ex.update({k: item[k] for k in ("title", "category", "objective", "lesson", "example", "problem", "sample", "expected", "pitfall", "hints", "assessment") if k in item})
        ex["explanation"] = item["explanation"]
        ex["difficulty"] = "เริ่มต้น" if item["id"] != "L01-E015" else "ท้าทาย"
        ex["prerequisites"] = [] if item["id"] == "L01-E001" else [f"L01-E{int(item['id'][-3:])-1:03d}"]
        ex["submission_mode"] = item["mode"]
        ex["function"] = None
        ex["signature"] = None
        ex["constraints"] = "Python 3.12; ใช้เฉพาะแนวคิดที่สอนถึงข้อนี้; การเทรดเป็นการจำลอง paper-only"
        if item["id"] == "L01-E013":
            ex["constraints"] += "; gross อาจเป็นบวกหรือลบ และ fee_percent ต้องไม่ติดลบ"
        if item["id"] in ("L01-E014", "L01-E015"):
            ex["constraints"] += "; ราคาซื้อ/ขายและจำนวนต้องไม่ติดลบ; fee_percent ต้องไม่ติดลบ"
        ex["lesson_file"] = f"lessons/{item['id']}.md"
        if item.get("variant_samples"):
            ex["variant_samples"] = item["variant_samples"]
        if item.get("assessment"):
            ex["variant_samples"] = {"A": "100, 110, 0.1, 1", "B": "250, 275, 0.2, 0.4"}
            if item.get("variant_prompts"):
                ex["variant_prompts"] = item["variant_prompts"]
                ex["variant_samples"] = item["variant_samples"]
                ex["variant_expected"] = item["variant_expected"]
        ex["cases"] = item["cases"]
        ex.pop("solution_source", None)
        level_dir = ROOT / "exercises" / "level_01"
        if item["mode"] == "text_answer":
            ex["answer_file"] = f"answers/level_01/{item['id']}.txt"
            student_source = f"# Prediction exercise. Submit your predicted output in {ex['answer_file']}\n"
            write_student(level_dir / f"{item['id']}.py", student_source)
            answer_path = ROOT / ex["answer_file"]
            if not answer_path.exists():
                write(answer_path, item["answer_starter"])
            write(ROOT / "solutions" / "level_01" / f"{item['id']}.txt", item["answer_solution"] + "\n")
        else:
            ex.pop("answer_file", None)
            write_student(level_dir / f"{item['id']}.py", item["starter"])
            write(ROOT / "solutions" / "level_01" / f"{item['id']}.py", item["solution"])
        write(ROOT / "explanations" / f"{item['id']}.md", f"# {item['id']} — {item['title']}\n\n{item['explanation']}\n")
        write(ROOT / "hints" / f"{item['id']}.json", json.dumps(item["hints"], ensure_ascii=False, indent=2) + "\n")
        write(ROOT / "tests" / f"{item['id']}.json", json.dumps(item["cases"], ensure_ascii=False, indent=2) + "\n")
        if item.get("assessment"):
            for variant, cases in item["variants"].items():
                write(ROOT / "tests" / "assessment" / f"{item['id']}-{variant}.json", json.dumps(cases, ensure_ascii=False, indent=2) + "\n")
                solution = item["solution"] if variant == "A" else item["variant_solutions"][variant]
                write(ROOT / "solutions" / "assessment" / f"{item['id']}-{variant}.py", solution)
        write(ROOT / "lessons" / f"{item['id']}.md", f"# {item['id']} — {item['title']}\n\n## เป้าหมาย\n\n{item['objective']}\n\n## แนวคิด\n\n{item['lesson']}\n\n## ตัวอย่าง\n\n```python\n{item['example']}\n```\n\n## โจทย์\n\n{item['problem']}\n\n## รูปแบบ input/output\n\n{item['sample']}\n\nผลที่ต้องการ: {item['expected']}\n\nข้อควรระวัง: {item['pitfall']}\n")
    write(ROOT / "curriculum.json", json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    intro = "# Level 1 — Python พื้นฐาน\n\nระดับนี้ฝึก print, arithmetic, variables, strings, input, type conversion และการจัดรูปแบบข้อความตามลำดับ แบบทำนายผลให้ส่งคำตอบในตัวแปร `ANSWER` ของไฟล์โจทย์ ส่วนข้อเขียน/แก้/เติม/ประยุกต์ให้แก้ไฟล์ `.py` ตามโจทย์\n\n"
    write(ROOT / "lessons" / "level_01.md", intro + "\n".join(f"- [{i['id']} — {i['title']}]({i['id']}.md)" for i in ITEMS) + "\n")
    print(f"Materialized {len(ITEMS)} Level 1 exercises and authored fixtures.")


if __name__ == "__main__":
    main()
