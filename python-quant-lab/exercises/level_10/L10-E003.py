# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E003 — เติม validator ของ paper order                                │
# │ Level 10: Paper Trading Bot Engineering | Tier 3: ง่ายมาก — แนวคิดเดียว  │
# │ ประเภท: เติมโค้ด / stdout | ความรู้ก่อนหน้า: ทบทวน L10-E002              │
# │ ทำนายบัญชีเงินสดหลังซื้อแบบ paper                                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ตรวจ side, ราคา, จำนวน, เงินสด และ notional limit              │
# │   ก่อนรับคำสั่ง                                                          │
# │ ทำไมสำคัญ: ทำ เติม validator ของ paper order ให้ครบ                      │
# │   ช่วยแปลงข้อกำหนดเป็นพฤติกรรมที่ตรวจได้.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: เติม order_allowed(cash, quantity, price,                     │
# │   max_order_value) ให้คืน bool เท่านั้น อนุญาตเมื่อ cash ไม่ติดลบ,       │
# │   quantity/price เป็นบวก, notional ไม่เกิน max_order_value               │
# │   และไม่เกิน cash โปรแกรมรับค่าทีละบรรทัด                                │
# │ เหตุผล: การเข้าใจ เติม validator ของ paper order                         │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ตรวจ side, ราคา, จำนวน, เงินสด และ notional limit       │
# │   ก่อนรับคำสั่ง                                                          │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '100\n1\n10\n25\n'                                       │
# │ stdout ที่ต้องได้: 'True\n'                                              │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Validate supplied fields; there is no side field in this input.          │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     cash = 30; quantity = 2; price = 10; max_value = 25                  │
# │     notional = quantity * price                                          │
# │     allowed = cash >= 0 and quantity > 0 and price > 0                   │
# │     allowed = allowed and notional <= max_value and notional <= cash     │
# │     print(allowed)                                                       │
# │ ผลที่คาด: True                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ เช็กแค่เงินสดแล้วไม่ตรวจ notional limit หรือราคาศูนย์                    │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E003                               │
# │ Check: python -B practice.py check L10-E003                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E003 1                           │
# │ Solution: python -B practice.py solution L10-E003                       │
# │ Explain: python -B practice.py explain L10-E003                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def order_allowed(cash, quantity, price, max_order_value):
    # TODO: ตรวจ invariant ทุกข้อก่อนอนุญาต
    raise NotImplementedError("เติม risk check")

if __name__ == "__main__":
    cash = float(input())
    quantity = float(input())
    price = float(input())
    max_order_value = float(input())
    print(order_allowed(cash, quantity, price, max_order_value))
