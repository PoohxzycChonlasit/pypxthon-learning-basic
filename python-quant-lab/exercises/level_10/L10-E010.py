# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E010 — บันทึกผลคำสั่ง                                                │
# │ Level 10: Paper Trading Bot Engineering | Tier 2: ท้าทาย —               │
# │ เงื่อนไขและกรณีขอบ                                                       │
# │ ประเภท: โจทย์ประยุกต์ / function | ความรู้ก่อนหน้า: ทบทวน L10-E009       │
# │ ใช้ค่าธรรมเนียมเริ่มต้น                                                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: คืน dict ที่มี id จาก event, status="paper", live=False        │
# │ ทำไมสำคัญ: การทำ บันทึกผลคำสั่ง                                          │
# │   ฝึกประกอบหลายแนวคิดกับข้อมูลและผลลัพธ์ที่กำหนด.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: ระบบ audit บันทึกผลคำสั่งเป็น event ที่ยืนยันว่าเป็น          │
# │   paper                                                                  │
# │ เหตุผล: การเข้าใจ บันทึกผลคำสั่ง                                         │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: คืน dict ที่มี id จาก event, status="paper", live=False │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก record_order_result ด้วย input ตัวอย่าง ({'id': 'O-1'},)           │
# │ ผลลัพธ์ตัวอย่าง: {'id': 'O-1', 'status': 'paper', 'live': False}         │
# │ เงื่อนไขสำคัญ: Python 3.12; id หายคืน None; live เป็น boolean False      │
# │ เสมอ; ไม่มีการเชื่อมต่อ exchange หรือ wallet                             │
# │ กรณีขอบ: id หายคืน None; live เป็น boolean False เสมอ.                   │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Return a dict containing the requested order-result fields.              │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     order_id = "A1"                                                      │
# │     result = {"id": order_id, "status": "paper"}                         │
# │     print(result["status"])                                              │
# │ ผลที่คาด: paper                                                          │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: id หายคืน None; │
# │ live เป็น boolean False เสมอ ห้ามแปลงงานจำลองเป็นคำสั่งเงินจริง          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ record_order_result ในไฟล์นี้; คงชื่อและ signature         │
# │ ตามโจทย์                                                                 │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E010                               │
# │ Check: python -B practice.py check L10-E010                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E010 1                           │
# │ Solution: python -B practice.py solution L10-E010                       │
# │ Explain: python -B practice.py explain L10-E010                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def record_order_result(event):
    """TODO: implement the behavior in the exercise instructions."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เขียนฟังก์ชันนี้")
