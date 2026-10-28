# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L09-E004 — แก้ look-ahead ในค่าเฉลี่ยย้อนหลัง                            │
# │ Level 9: Quant Research and Backtesting | Tier 2: ง่าย —                 │
# │ รวมแนวคิดคุ้นเคย                                                         │
# │ ประเภท: แก้โค้ดที่ผิด / stdout | ความรู้ก่อนหน้า: ทบทวน L09-E003         │
# │ เติมค่าเฉลี่ยจากข้อมูลก่อน index                                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ตรวจและตัดข้อมูลปัจจุบันออกจาก window ก่อนหน้า                 │
# │ ทำไมสำคัญ: หาสาเหตุของ แก้ look-ahead ในค่าเฉลี่ยย้อนหลัง ก่อนแก้        │
# │   ช่วยป้องกันบั๊กเดิมเมื่อ input เปลี่ยน.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: ผู้พัฒนา Python                                            │
# │   ที่กำลังฝึกเขียนโปรแกรมให้ทำตามข้อกำหนด.                               │
# │ สถานการณ์: trailing_mean(values, index, window)                          │
# │   ต้องคำนวณค่าเฉลี่ยจาก window ค่า ก่อน index เท่านั้น                   │
# │   โค้ดปัจจุบันรวม values[index] ด้วย                                     │
# │   แก้ให้ไม่ใช้ข้อมูลของแท่งที่กำลังตัดสินใจและไม่อ่านค่าหลัง index       │
# │ เหตุผล: การเข้าใจ แก้ look-ahead ในค่าเฉลี่ยย้อนหลัง                     │
# │   ช่วยแยกข้อมูลพร้อมใช้จากแถวที่ต้องตรวจ.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ตรวจและตัดข้อมูลปัจจุบันออกจาก window ก่อนหน้า          │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '100,104,200\n2\n2\n'                                    │
# │ stdout ที่ต้องได้: '102.0\n'                                             │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Flag feature_time >= decision_time; it is not yet available.             │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     feature_time = 5; decision_time = 4                                  │
# │     leaks = feature_time >= decision_time                                │
# │     print(leaks)                                                         │
# │ ผลที่คาด: True                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ ทดสอบแต่ข้อมูลที่ค่าปัจจุบันใกล้กับ mean จนไม่เห็นผล look-ahead          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L09-E004                               │
# │ Check: python -B practice.py check L09-E004                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L09-E004 1                           │
# │ Solution: python -B practice.py solution L09-E004                       │
# │ Explain: python -B practice.py explain L09-E004                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def trailing_mean(values, index, window):
    raise NotImplementedError("ดู look-ahead ใน main")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    # BUG: รวมค่าปัจจุบันและหารด้วย window + 1
    section = values[index - window:index + 1]
    print(sum(section) / len(section) if len(section) == window + 1 else "NONE")
