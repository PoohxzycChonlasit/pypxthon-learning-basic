# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E005 — จำลอง paper buy/sell พร้อม accounting invariant               │
# │ Level 10: Paper Trading Bot Engineering | Tier 2: ง่าย —                 │
# │ รวมแนวคิดคุ้นเคย                                                         │
# │ ประเภท: โจทย์ประยุกต์ / stdout | ความรู้ก่อนหน้า: ทบทวน L10-E004 แก้     │
# │ validator OHLC ที่ตรวจไม่ครบ                                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ปรับ state จำลองโดยบังคับเงินสด จำนวนหน่วย fee และ             │
# │   notional cap                                                           │
# │ ทำไมสำคัญ: การทำ จำลอง paper buy/sell พร้อม accounting invariant         │
# │   ฝึกประกอบหลายแนวคิดกับข้อมูลและผลลัพธ์ที่กำหนด.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: รับ JSON หนึ่งบรรทัดที่มี state {cash, units}, event          │
# │   {side, quantity, price}, max_order_value และ fee_rate จำลอง buy        │
# │   หรือ sell ในหน่วยความจำเท่านั้น ปฏิเสธข้อมูลผิด, buy                   │
# │   ที่ใช้เงินเกิน, notional เกิน cap และ sell ที่ขายเกินจำนวนที่ถือ       │
# │   แสดง accepted, cash, units และ live_trading=False                      │
# │ เหตุผล: การเข้าใจ จำลอง paper buy/sell พร้อม accounting invariant        │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ปรับ state จำลองโดยบังคับเงินสด จำนวนหน่วย fee และ      │
# │   notional cap                                                           │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '{"state":{"cash":100,"units":0},"event":{"side":"buy"," │
# │ quantity":1,"price":10},"max_order_value":25,"fee_rate":0.001}\n'        │
# │ stdout ที่ต้องได้: 'accepted=True cash=89.99 units=1.00                  │
# │ live_trading=False\n'                                                    │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ json.dumps() — บันทึก event เป็นบรรทัดข้อมูลที่อ่านกลับได้               │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     import json                                                          │
# │     event = {"side": "buy"}                                              │
# │     print(json.dumps(event, sort_keys=True))                             │
# │ ผลที่คาด: {"side": "buy"}                                                │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ อัปเดตเงินสดก่อนตรวจวงเงิน หรือยอมให้ units ติดลบเมื่อขายเกิน            │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E005                               │
# │ Check: python -B practice.py check L10-E005                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E005 1                           │
# │ Solution: python -B practice.py solution L10-E005                       │
# │ Explain: python -B practice.py explain L10-E005                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def paper_step(state, event, max_order_value, fee_rate):
    raise NotImplementedError("TODO: validate then update paper state")

if __name__ == "__main__":
    import json
    payload = json.loads(input())
    result = paper_step(payload["state"], payload["event"], payload["max_order_value"], payload["fee_rate"])
    print(f"accepted={result['accepted']} cash={result['cash']:.2f} units={result['units']:.2f} live_trading={result['live_trading']}")
