# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L07-E003 — เติมสูตร population variance                                  │
# │ Level 7: Mathematics and Statistics | Tier 3: ง่ายมาก — แนวคิดเดียว      │
# │ ประเภท: เติมโค้ด / stdout | ความรู้ก่อนหน้า: ทบทวน L07-E002              │
# │ ทำนายค่าเฉลี่ยและมัธยฐาน                                                 │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: คำนวณค่าเฉลี่ยระยะห่างกำลังสองจาก mean                         │
# │ ทำไมสำคัญ: ทำ เติมสูตร population variance ให้ครบ                        │
# │   ช่วยแปลงข้อกำหนดเป็นพฤติกรรมที่ตรวจได้.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: ผู้พัฒนา Python                                            │
# │   ที่กำลังฝึกเขียนโปรแกรมให้ทำตามข้อกำหนด.                               │
# │ สถานการณ์: เติม population_variance(values) ตามนิยามประชากร:             │
# │   หาค่าเฉลี่ยก่อน จากนั้นเฉลี่ยค่า (x - mean) ** 2; คืน None เมื่อ       │
# │   list ว่าง รับตัวเลขคั่นด้วย comma                                      │
# │ เหตุผล: การฝึก เติมสูตร population variance                              │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: คำนวณค่าเฉลี่ยระยะห่างกำลังสองจาก mean                  │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '2,4,4,6\n'                                              │
# │ stdout ที่ต้องได้: '2.0\n'                                               │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Population variance averages squared differences from mean.              │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     values = [1, 3]                                                      │
# │     mean = sum(values) / len(values)                                     │
# │     variance = sum((x-mean)**2 for x in values) / len(values)            │
# │     print(variance)                                                      │
# │ ผลที่คาด: 1.0                                                            │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: หารด้วย n-1     │
# │ ซึ่งเป็น sample variance ทั้งที่โจทย์ขอประชากร                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L07-E003                               │
# │ Check: python -B practice.py check L07-E003                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L07-E003 1                           │
# │ Solution: python -B practice.py solution L07-E003                       │
# │ Explain: python -B practice.py explain L07-E003                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def population_variance(values):
    # TODO: mean แล้วหาค่าเฉลี่ย squared deviations
    raise NotImplementedError("เติมสูตร variance")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    result = population_variance(values)
    print("NONE" if result is None else result)
