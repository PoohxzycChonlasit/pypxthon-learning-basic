# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L07-E007 — ผลคาดหมายต่อรายการ                                            │
# │ Level 7: Mathematics and Statistics | Tier 3: ปานกลาง — หลายขั้นตอน      │
# │ ประเภท: ทำนายผล / function | ความรู้ก่อนหน้า: ทบทวน L07-E006 อัตราค่าบวก │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: รับ win_probability, average_win, average_loss; คำนวณ          │
# │   p*win + (1-p)*loss; loss เป็นค่าลบ                                     │
# │ ทำไมสำคัญ: ทำนายผลก่อนรันในโจทย์ ผลคาดหมายต่อรายการ                      │
# │   ช่วยฝึกติดตามลำดับคำสั่งและตรวจวิธีคิด.                                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: นักวิจัยคำนวณผลคาดหมายต่อรายการจากโอกาสชนะและผลเฉลี่ย.        │
# │   เขียน expected_trade_result(win_probability, average_win,              │
# │   average_loss) ให้ใช้ input ทั้งสามค่าและคืน expected value             │
# │ เหตุผล: การฝึก ผลคาดหมายต่อรายการ                                        │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: รับ win_probability, average_win, average_loss; คำนวณ   │
# │   p*win + (1-p)*loss; loss เป็นค่าลบ                                     │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก expected_trade_result ด้วย input ตัวอย่าง (0.6, 10, -5)            │
# │ ผลลัพธ์ตัวอย่าง: 4.0                                                     │
# │ เงื่อนไขสำคัญ: Python 3.12; p อยู่ระหว่าง 0 ถึง 1; p=0 คืน average_loss; │
# │ p=1 คืน average_win; ใช้ข้อมูลตามรูปแบบที่ระบุในโจทย์; output            │
# │ ต้องตรงทั้งชนิดและลำดับ                                                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Expected value = p * win + (1 - p) * loss.                               │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     p = 0.6                                                              │
# │     win = 2; loss = -1                                                   │
# │     expected = p*win + (1-p)*loss                                        │
# │     print(round(expected, 1))                                            │
# │ ผลที่คาด: 0.8                                                            │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: p อยู่ระหว่าง 0 │
# │ ถึง 1; p=0 คืน average_loss; p=1 คืน average_win                         │
# │ ตรวจชนิดข้อมูลและลำดับผลลัพธ์ก่อน return                                 │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ expected_trade_result ในไฟล์นี้; คงชื่อและ signature       │
# │ ตามโจทย์                                                                 │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L07-E007                               │
# │ Check: python -B practice.py check L07-E007                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L07-E007 1                           │
# │ Solution: python -B practice.py solution L07-E007                       │
# │ Explain: python -B practice.py explain L07-E007                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def expected_trade_result(win_probability, average_win, average_loss):
    """TODO: calculate the probability-weighted result per trade."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เติมสูตร expected value")
