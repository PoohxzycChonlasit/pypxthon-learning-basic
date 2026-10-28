# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L08-E003 — เติมการคำนวณขนาดสถานะจากวงเงินเสี่ยง                          │
# │ Level 8: Financial Analysis and Risk | Tier 3: ง่ายมาก — แนวคิดเดียว     │
# │ ประเภท: เติมโค้ด / stdout | ความรู้ก่อนหน้า: ทบทวน L08-E002              │
# │ ทำนายกำไรสุทธิหลังค่าธรรมเนียม                                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: แปลง risk budget เป็นจำนวนหน่วยโดยหารระยะ stop                 │
# │ ทำไมสำคัญ: ทำ เติมการคำนวณขนาดสถานะจากวงเงินเสี่ยง ให้ครบ                │
# │   ช่วยแปลงข้อกำหนดเป็นพฤติกรรมที่ตรวจได้.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: เติม risk_based_quantity(equity, risk_percent,                │
# │   stop_distance) ให้คืน (equity * risk_percent / 100) /                  │
# │   stop_distance; ถ้า equity ไม่บวก, risk_percent ติดลบ หรือ              │
# │   stop_distance ไม่บวก ให้คืน 0 รับค่าทีละบรรทัดและแสดงสองตำแหน่ง        │
# │ เหตุผล: การเข้าใจ เติมการคำนวณขนาดสถานะจากวงเงินเสี่ยง                   │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: แปลง risk budget เป็นจำนวนหน่วยโดยหารระยะ stop          │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '1000\n1\n5\n'                                           │
# │ stdout ที่ต้องได้: '2.00\n'                                              │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Divide risk budget by distance; guard zero distance.                     │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     distance = abs(10 - 8)                                               │
# │     if distance == 0: quantity = 0                                       │
# │     else: quantity = 20 / distance                                       │
# │     print(quantity)                                                      │
# │ ผลที่คาด: 10.0                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ ใช้เปอร์เซ็นต์เป็น 1 แทน 0.01 โดยทั้งที่โจทย์ระบุว่า 1                   │
# │ หมายถึงหนึ่งเปอร์เซ็นต์                                                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L08-E003                               │
# │ Check: python -B practice.py check L08-E003                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L08-E003 1                           │
# │ Solution: python -B practice.py solution L08-E003                       │
# │ Explain: python -B practice.py explain L08-E003                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def risk_based_quantity(equity, risk_percent, stop_distance):
    # TODO: ตรวจค่าก่อนหารและคืนขนาดหน่วย
    raise NotImplementedError("เติมสูตร position sizing")

if __name__ == "__main__":
    equity = float(input())
    risk_percent = float(input())
    stop_distance = float(input())
    print(f"{risk_based_quantity(equity, risk_percent, stop_distance):.2f}")
