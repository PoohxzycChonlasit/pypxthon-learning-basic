# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L07-E004 — แก้เศษส่วน conversion rate                                    │
# │ Level 7: Mathematics and Statistics | Tier 2: ง่าย — รวมแนวคิดคุ้นเคย    │
# │ ประเภท: แก้โค้ดที่ผิด / stdout | ความรู้ก่อนหน้า: ทบทวน L07-E003         │
# │ เติมสูตร population variance                                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ตรวจลำดับ numerator/denominator                                │
# │   และกรณีจำนวนผู้เข้าชมเป็นศูนย์                                         │
# │ ทำไมสำคัญ: หาสาเหตุของ แก้เศษส่วน conversion rate ก่อนแก้                │
# │   ช่วยป้องกันบั๊กเดิมเมื่อ input เปลี่ยน.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท:                                                            │
# │   นักวิเคราะห์ข้อมูลธุรกิจที่สรุปพฤติกรรมลูกค้าและเว็บไซต์.              │
# │ สถานการณ์: ฟังก์ชัน conversion_rate(signups, visits) ต้องคืน signups     │
# │   / visits หรือ None เมื่อ visits เป็นศูนย์                              │
# │   โค้ดปัจจุบันกลับด้านเศษส่วนและตรวจ signup แทนตัวหาร แก้ให้ถูกต้อง      │
# │ เหตุผล: การฝึก แก้เศษส่วน conversion rate                                │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ตรวจลำดับ numerator/denominator                         │
# │   และกรณีจำนวนผู้เข้าชมเป็นศูนย์                                         │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '4\n100\n'                                               │
# │ stdout ที่ต้องได้: '0.04\n'                                              │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ A fraction is part / whole; guard a zero denominator.                    │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     part = 2; whole = 5                                                  │
# │     fraction = part / whole if whole else None                           │
# │     print(fraction)                                                      │
# │ ผลที่คาด: 0.4                                                            │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: หาร visits ด้วย │
# │ signups เพราะลำดับ parameter อ่านยาก                                     │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L07-E004                               │
# │ Check: python -B practice.py check L07-E004                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L07-E004 1                           │
# │ Solution: python -B practice.py solution L07-E004                       │
# │ Explain: python -B practice.py explain L07-E004                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def conversion_rate(signups, visits):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    signups = float(input())
    visits = float(input())
    # BUG: เศษส่วนกลับด้านและตรวจตัวตั้ง
    rate = None if signups == 0 else visits / signups
    print("NONE" if rate is None else rate)
