# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L08-E005 — ตรวจ exposure รวมของพอร์ตจำลอง                                │
# │ Level 8: Financial Analysis and Risk | Tier 2: ง่าย — รวมแนวคิดคุ้นเคย   │
# │ ประเภท: โจทย์ประยุกต์ / stdout | ความรู้ก่อนหน้า: ทบทวน L08-E004         │
# │ แก้สูตรที่บวก fee เข้ากำไร                                               │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: รวมมูลค่าสถานะและเทียบกับสัดส่วนเพดานของ equity                │
# │ ทำไมสำคัญ: การทำ ตรวจ exposure รวมของพอร์ตจำลอง                          │
# │   ฝึกประกอบหลายแนวคิดกับข้อมูลและผลลัพธ์ที่กำหนด.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: ผู้ดูแล paper portfolio มี equity                             │
# │   และมูลค่าสถานะตามสินทรัพย์ ตรวจ exposure รวมเทียบ max_fraction ของ     │
# │   equity ถ้าค่าเป็นลบ, equity ไม่บวก หรือ max_fraction นอกช่วง 0 ถึง     │
# │   1 ให้แสดง INVALID มิฉะนั้นรายงาน exposure และ allowed                  │
# │ เหตุผล: การเข้าใจ ตรวจ exposure รวมของพอร์ตจำลอง                         │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: รวมมูลค่าสถานะและเทียบกับสัดส่วนเพดานของ equity         │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '100\n{"BTC":20,"ETH":15}\n0.5\n'                        │
# │ stdout ที่ต้องได้: 'exposure=35.00 limit=50.00 allowed=True\n'           │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ ตรวจ invariant — ยืนยันเงื่อนไขบัญชีด้วยค่าจริงหลังคำนวณ                 │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     cash_before = 100                                                    │
# │     spent = 25                                                           │
# │     print(cash_before - spent >= 0)                                      │
# │ ผลที่คาด: True                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: คิดว่า position │
# │ สองรายการแต่ละรายการผ่าน limit แล้วผลรวมก็ต้องผ่าน                       │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L08-E005                               │
# │ Check: python -B practice.py check L08-E005                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L08-E005 1                           │
# │ Solution: python -B practice.py solution L08-E005                       │
# │ Explain: python -B practice.py explain L08-E005                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def exposure_report(equity, positions, max_fraction):
    raise NotImplementedError("TODO: ตรวจและรวม exposure")

if __name__ == "__main__":
    import json
    equity = float(input())
    positions = json.loads(input())
    max_fraction = float(input())
    report = exposure_report(equity, positions, max_fraction)
    if report is None:
        print("INVALID")
    else:
        limit = equity * max_fraction
        print(f"exposure={report['exposure']:.2f} limit={limit:.2f} allowed={report['allowed']}")
