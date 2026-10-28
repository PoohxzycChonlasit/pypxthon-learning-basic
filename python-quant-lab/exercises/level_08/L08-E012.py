# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L08-E012 — สัดส่วนเงินที่เปิดรับความเสี่ยง                               │
# │ Level 8: Financial Analysis and Risk | Tier 2: ท้าทาย —                  │
# │ เงื่อนไขและกรณีขอบ                                                       │
# │ ประเภท: ทำนายผล / function | ความรู้ก่อนหน้า: ทบทวน L08-E011 เงินคงเหลือ │
# │ paper หลังเทรด                                                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: fraction = price*quantity/equity; คืน None เมื่อ equity        │
# │   เป็น 0                                                                 │
# │ ทำไมสำคัญ: ทำนายผลก่อนรันในโจทย์ สัดส่วนเงินที่เปิดรับความเสี่ยง         │
# │   ช่วยฝึกติดตามลำดับคำสั่งและตรวจวิธีคิด.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: นักวิเคราะห์วัด notional exposure เทียบกับ equity             │
# │   ปัจจุบัน                                                               │
# │ เหตุผล: การเข้าใจ สัดส่วนเงินที่เปิดรับความเสี่ยง                        │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: fraction = price*quantity/equity; คืน None เมื่อ equity │
# │   เป็น 0                                                                 │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก exposure_fraction ด้วย input ตัวอย่าง (10, 2, 100)                 │
# │ ผลลัพธ์ตัวอย่าง: 0.2                                                     │
# │ เงื่อนไขสำคัญ: Python 3.12; fraction เกิน 1 หมายถึง exposure มากกว่า     │
# │ equity; ไม่จำกัดอัตโนมัติ; ไม่มีการเชื่อมต่อ exchange หรือคำสั่งเงินจริง │
# │ กรณีขอบ: fraction เกิน 1 หมายถึง exposure มากกว่า equity;                │
# │ ไม่จำกัดอัตโนมัติ.                                                       │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Exposure fraction = exposure / equity; handle zero equity.               │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     equity = 100; exposure = 25                                          │
# │     fraction = exposure / equity if equity else None                     │
# │     print(fraction)                                                      │
# │ ผลที่คาด: 0.25                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: fraction เกิน 1 │
# │ หมายถึง exposure มากกว่า equity; ไม่จำกัดอัตโนมัติ                       │
# │ ตรวจว่าต้นทุนและสัดส่วนใช้ฐานคำนวณถูกต้อง                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ exposure_fraction ในไฟล์นี้; คงชื่อและ signature ตามโจทย์  │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L08-E012                               │
# │ Check: python -B practice.py check L08-E012                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L08-E012 1                           │
# │ Solution: python -B practice.py solution L08-E012                       │
# │ Explain: python -B practice.py explain L08-E012                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def exposure_fraction(price, quantity, equity):
    """TODO: implement the paper-only contract in the exercise."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เติมโค้ดตามโจทย์")
