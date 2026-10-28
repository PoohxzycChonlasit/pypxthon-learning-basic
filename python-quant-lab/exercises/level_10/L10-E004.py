# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L10-E004 — แก้ validator OHLC ที่ตรวจไม่ครบ                              │
# │ Level 10: Paper Trading Bot Engineering | Tier 2: ง่าย —                 │
# │ รวมแนวคิดคุ้นเคย                                                         │
# │ ประเภท: แก้โค้ดที่ผิด / stdout | ความรู้ก่อนหน้า: ทบทวน L10-E003 เติม    │
# │ validator ของ paper order                                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: ตรวจ high/low เทียบกับ open/close และ volume                   │
# │ ทำไมสำคัญ: หาสาเหตุของ แก้ validator OHLC ที่ตรวจไม่ครบ ก่อนแก้          │
# │   ช่วยป้องกันบั๊กเดิมเมื่อ input เปลี่ยน.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: ผู้พัฒนา Python                                            │
# │   ที่กำลังฝึกเขียนโปรแกรมให้ทำตามข้อกำหนด.                               │
# │ สถานการณ์: valid_bar(bar) ต้องยืนยันว่าราคาเป็นบวก, high >=              │
# │   max(open, close), low <= min(open, close), low <= high และ volume      │
# │   ไม่ติดลบ โปรแกรมปัจจุบันตรวจเพียง high >= low และ volume แก้ให้ครบ     │
# │ เหตุผล: การฝึก แก้ validator OHLC ที่ตรวจไม่ครบ                          │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: ตรวจ high/low เทียบกับ open/close และ volume            │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '{"open":10,"high":12,"low":9,"close":11,"volume":5}\n'  │
# │ stdout ที่ต้องได้: 'True\n'                                              │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ สถานะและตัวนับ — คำนวณสถานะใหม่จากสถานะเดิมและ event ที่ตรวจแล้ว         │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     state = {"orders": 1}                                                │
# │     state["orders"] += 1                                                 │
# │     print(state["orders"])                                               │
# │ ผลที่คาด: 2                                                              │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: ยอมให้ high     │
# │ ต่ำกว่า close แต่ยังสูงกว่า low                                          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L10-E004                               │
# │ Check: python -B practice.py check L10-E004                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L10-E004 1                           │
# │ Solution: python -B practice.py solution L10-E004                       │
# │ Explain: python -B practice.py explain L10-E004                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def valid_bar(bar):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    import json
    bar = json.loads(input())
    # BUG: high >= low ไม่ได้ตรวจเทียบ open และ close
    valid = bar["high"] >= bar["low"] and bar["volume"] >= 0
    print(valid)
