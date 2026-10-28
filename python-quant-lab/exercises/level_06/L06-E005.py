# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L06-E005 — สรุปรายได้แยกตามสินค้า                                        │
# │ Level 6: Data Analysis | Tier 4: ง่าย — รวมแนวคิดคุ้นเคย                 │
# │ ประเภท: โจทย์ประยุกต์ / stdout | ความรู้ก่อนหน้า: ทบทวน L06-E004         │
# │ แก้การเติม missing ด้วยค่าก่อนหน้า                                       │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: จัดกลุ่มแถวขายตาม product แล้วรวม quantity คูณ unit_price      │
# │ ทำไมสำคัญ: การทำ สรุปรายได้แยกตามสินค้า                                  │
# │   ฝึกประกอบหลายแนวคิดกับข้อมูลและผลลัพธ์ที่กำหนด.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: รับ CSV ที่มี header product,quantity,unit_price จาก          │
# │   standard input รวมรายได้ของแต่ละสินค้าและแสดง                          │
# │   product:ยอดสองตำแหน่ง เรียงตามชื่อสินค้า หากไม่มีแถวให้แสดง NONE       │
# │ เหตุผล: การเข้าใจ สรุปรายได้แยกตามสินค้า                                 │
# │   ช่วยแยกข้อมูลพร้อมใช้จากแถวที่ต้องตรวจ.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: จัดกลุ่มแถวขายตาม product แล้วรวม quantity คูณ          │
# │   unit_price                                                             │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง:                                                          │
# │ 'product,quantity,unit_price\ntea,2,30\nrice,1,25\ntea,1,30\n'           │
# │ stdout ที่ต้องได้: 'rice:25.00\ntea:90.00\n'                             │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ DictReader reads named columns; a dict can group totals.                 │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     import csv                                                           │
# │     from io import StringIO                                              │
# │     raw = "symbol,amount\nA,2\nA,3\n"                                    │
# │     reader = csv.DictReader(StringIO(raw))                               │
# │     totals = {}                                                          │
# │     for row in reader:                                                   │
# │         key = row["symbol"]                                              │
# │         totals[key] = totals.get(key, 0) + float(row["amount"])          │
# │     print(totals["A"])                                                   │
# │ ผลที่คาด: 5.0                                                            │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ รวมจำนวนชิ้นแทนรายได้ หรือแสดงสินค้าในลำดับที่ขึ้นกับการพบ               │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L06-E005                               │
# │ Check: python -B practice.py check L06-E005                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L06-E005 1                           │
# │ Solution: python -B practice.py solution L06-E005                       │
# │ Explain: python -B practice.py explain L06-E005                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def revenue_by_product(rows):
    raise NotImplementedError("TODO: รวมรายได้ตาม product")

if __name__ == "__main__":
    import csv
    import sys
    rows = list(csv.DictReader(sys.stdin))
    report = revenue_by_product(rows)
    if not report:
        print("NONE")
    else:
        for product in sorted(report):
            print(f"{product}:{report[product]:.2f}")
