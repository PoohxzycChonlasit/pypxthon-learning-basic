# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E007 — มูลค่าสถานะ paper                                             │
# │ Level 10: Paper Trading Bot Engineering | Tier 2: ปานกลาง — หลายขั้นตอน  │
# │ ประเภท: ทำนายผล / function | ความรู้ก่อนหน้า: ทบทวน L10-E006             │
# │ หยุดเมื่อเงินถึงขีดจำกัด                                                 │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: คืน quantity*price โดย field ที่หายใช้ 0                       │
# │ ทำไมสำคัญ: ทำนายผลก่อนรันในโจทย์ มูลค่าสถานะ paper                       │
# │   ช่วยฝึกติดตามลำดับคำสั่งและตรวจวิธีคิด.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: ผู้ดูแลพอร์ตสรุป notional exposure ของคำสั่ง paper            │
# │ เหตุผล: การเข้าใจ มูลค่าสถานะ paper                                      │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: คืน quantity*price โดย field ที่หายใช้ 0                │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก paper_exposure ด้วย input ตัวอย่าง ({'quantity': 2, 'price': 10},) │
# │ ผลลัพธ์ตัวอย่าง: 20                                                      │
# │ เงื่อนไขสำคัญ: Python 3.12; quantity หรือ price ศูนย์ให้ exposure 0;     │
# │ ไม่มีการเชื่อมต่อ exchange หรือ wallet                                   │
# │ กรณีขอบ: quantity หรือ price ศูนย์ให้ exposure 0.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Notional exposure = quantity * price.                                    │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     quantity = 2; price = 10                                             │
# │     exposure = quantity * price                                          │
# │     print(exposure)                                                      │
# │ ผลที่คาด: 20                                                             │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: quantity หรือ   │
# │ price ศูนย์ให้ exposure 0 ห้ามแปลงงานจำลองเป็นคำสั่งเงินจริง             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ paper_exposure ในไฟล์นี้; คงชื่อและ signature ตามโจทย์     │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E007                               │
# │ Check: python -B practice.py check L10-E007                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E007 1                           │
# │ Solution: python -B practice.py solution L10-E007                       │
# │ Explain: python -B practice.py explain L10-E007                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def paper_exposure(event):
    """TODO: implement the behavior in the exercise instructions."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เขียนฟังก์ชันนี้")
