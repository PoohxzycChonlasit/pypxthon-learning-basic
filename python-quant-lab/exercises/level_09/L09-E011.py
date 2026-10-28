# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L09-E011 — สร้างสัญญาณตามเกณฑ์                                           │
# │ Level 9: Quant Research and Backtesting | Tier 3: ท้าทาย —               │
# │ เงื่อนไขและกรณีขอบ                                                       │
# │ ประเภท: เขียนโค้ด / function | ความรู้ก่อนหน้า: ทบทวน L09-E010           │
# │ กำหนดขอบเขตช่วงทดสอบ                                                     │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: คืน 1 เมื่อ current/previous-1 > minimum_return มิฉะนั้น 0     │
# │ ทำไมสำคัญ: ฝึก สร้างสัญญาณตามเกณฑ์ ให้ทำซ้ำได้                           │
# │   ช่วยเชื่อมผลลัพธ์กับขั้นตอนถัดไป.                                      │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: นักวิจัยสร้าง long signal เมื่อ simple return                 │
# │   ระหว่างราคาติดกันเกิน threshold                                        │
# │ เหตุผล: การฝึก สร้างสัญญาณตามเกณฑ์                                       │
# │   ช่วยให้ผู้ใช้ตรวจผลและแก้ความผิดพลาดได้ตรงจุด.                         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: คืน 1 เมื่อ current/previous-1 > minimum_return         │
# │   มิฉะนั้น 0                                                             │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ เรียก threshold_signals ด้วย input ตัวอย่าง ([100, 102, 103], 0.01)      │
# │ ผลลัพธ์ตัวอย่าง: [1, 0]                                                  │
# │ เงื่อนไขสำคัญ: Python 3.12; เท่ากับ threshold ไม่ผ่าน; output ยาว n-1;   │
# │ previous<=0 ให้ 0; time series เรียงตามเวลา;                             │
# │ ห้ามใช้ข้อมูลอนาคตสร้างผลในอดีต                                          │
# │ กรณีขอบ: เท่ากับ threshold ไม่ผ่าน; output ยาว n-1; previous<=0 ให้ 0.   │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Compare each return with its threshold to create a signal.               │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     returns = [0.02, -0.01]                                              │
# │     threshold = 0                                                        │
# │     signals = [1 if r > threshold else 0 for r in returns]               │
# │     print(signals)                                                       │
# │ ผลที่คาด: [1, 0]                                                         │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย: เท่ากับ         │
# │ threshold ไม่ผ่าน; output ยาว n-1; previous<=0 ให้ 0                     │
# │ ตรวจลำดับเวลาและขอบเขตของ slice                                          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ threshold_signals ในไฟล์นี้; คงชื่อและ signature ตามโจทย์  │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L09-E011                               │
# │ Check: python -B practice.py check L09-E011                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L09-E011 1                           │
# │ Solution: python -B practice.py solution L09-E011                       │
# │ Explain: python -B practice.py explain L09-E011                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def threshold_signals(prices, minimum_return):
    """TODO: implement the chronological research contract."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เติมโค้ดตามโจทย์")
