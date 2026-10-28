# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L04-E004 — แก้การตรวจหารด้วยศูนย์                                        │
# │ Level 4: Functions and Modules | Tier 2: ง่าย — รวมแนวคิดคุ้นเคย         │
# │ ประเภท: แก้โค้ดที่ผิด / stdout | ความรู้ก่อนหน้า: ทบทวน L04-E003         │
# │ เติมฟังก์ชันแปลงหน่วยค่าใช้จ่าย                                          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ตรวจว่าเงื่อนไข safe division ตรวจตัวหาร ไม่ใช่ตัวตั้ง         │
# │ ทำไมสำคัญ: หาสาเหตุของ แก้การตรวจหารด้วยศูนย์ ก่อนแก้                    │
# │   ช่วยป้องกันบั๊กเดิมเมื่อ input เปลี่ยน.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: ผู้พัฒนา Python                                            │
# │   ที่กำลังฝึกเขียนโปรแกรมให้ทำตามข้อกำหนด.                               │
# │ สถานการณ์: ฟังก์ชัน safe_division(numerator, denominator) ควรคืน         │
# │   None เมื่อ denominator เป็นศูนย์ แต่โค้ดปัจจุบันตรวจตัวแปรผิดตัว       │
# │   แก้บั๊กและให้โปรแกรมแสดง NONE เมื่อไม่มีผลหาร                          │
# │ เหตุผล: การฝึก แก้การตรวจหารด้วยศูนย์                                    │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ตรวจว่าเงื่อนไข safe division ตรวจตัวหาร ไม่ใช่ตัวตั้ง  │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '10\n2\n'                                                │
# │ stdout ที่ต้องได้: '5.0\n'                                               │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Check divisor == 0 before dividing; return a safe value.                 │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     divisor = 0                                                          │
# │     if divisor == 0: result = None                                       │
# │     else: result = 10 / divisor                                          │
# │     print(result)                                                        │
# │ ผลที่คาด: None                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: คืน None เมื่อ  │
# │ numerator เป็นศูนย์                                                      │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L04-E004                               │
# │ Check: python -B practice.py check L04-E004                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L04-E004 1                           │
# │ Solution: python -B practice.py solution L04-E004                       │
# │ Explain: python -B practice.py explain L04-E004                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def safe_division(numerator, denominator):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    numerator = float(input())
    denominator = float(input())
    # BUG: ตรวจ numerator แทน denominator
    if numerator == 0:
        result = None
    else:
        result = numerator / denominator
    print("NONE" if result is None else result)
