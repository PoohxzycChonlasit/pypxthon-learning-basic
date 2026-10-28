# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E014 — บันทึกเหตุการณ์แบบมีโครงสร้าง                                 │
# │ Level 10: Paper Trading Bot Engineering | Tier 2: ประยุกต์ขั้นสูง —      │
# │ ใช้ความรู้เดิมกับโจทย์ใหม่                                               │
# │ ประเภท: เติมโค้ด / function | ความรู้ก่อนหน้า: ทบทวน L10-E013            │
# │ กู้คืนยอดเงินสด                                                          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: คืน dict event=id, side=side, paper_only=True                  │
# │ ทำไมสำคัญ: ทำ บันทึกเหตุการณ์แบบมีโครงสร้าง ให้ครบ                       │
# │   ช่วยแปลงข้อกำหนดเป็นพฤติกรรมที่ตรวจได้.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: ระบบ log เก็บข้อมูลสำคัญของ event พร้อมป้าย paper_only        │
# │ เหตุผล: การเข้าใจ บันทึกเหตุการณ์แบบมีโครงสร้าง                          │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: คืน dict event=id, side=side, paper_only=True           │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก structured_event_log ด้วย input ตัวอย่าง ({'id': 'a', 'side':      │
# │ 'buy'},)                                                                 │
# │ ผลลัพธ์ตัวอย่าง: {'event': 'a', 'side': 'buy', 'paper_only': True}       │
# │ เงื่อนไขสำคัญ: Python 3.12; field ที่หายคืน None; paper_only ต้อง        │
# │ boolean True; ไม่มีการเชื่อมต่อ exchange หรือ wallet                     │
# │ กรณีขอบ: field ที่หายคืน None; paper_only ต้อง boolean True.             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ A dict literal records named fields in one structured value.             │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     event = {"id": "A1", "side": "buy"}                                  │
# │     record = {"event": event["id"]}                                      │
# │     print(record["event"])                                               │
# │ ผลที่คาด: A1                                                             │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: field ที่หายคืน │
# │ None; paper_only ต้อง boolean True ห้ามแปลงงานจำลองเป็นคำสั่งเงินจริง    │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ structured_event_log ในไฟล์นี้; คงชื่อและ signature        │
# │ ตามโจทย์                                                                 │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E014                               │
# │ Check: python -B practice.py check L10-E014                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E014 1                           │
# │ Solution: python -B practice.py solution L10-E014                       │
# │ Explain: python -B practice.py explain L10-E014                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def structured_event_log(event):
    """TODO: implement the behavior in the exercise instructions."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เขียนฟังก์ชันนี้")
