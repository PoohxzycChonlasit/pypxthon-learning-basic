# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L06-E015 — ประเมินและทำความสะอาดข้อมูล                                   │
# │ Level 6: Data Analysis | Tier 3: ประยุกต์ขั้นสูง —                       │
# │ ใช้ความรู้เดิมกับโจทย์ใหม่                                               │
# │ ประเภท: โจทย์ประยุกต์ / function | ความรู้ก่อนหน้า: ทบทวน L06-E014       │
# │ โจทย์: อ่าน prompt ของ variant ปัจจุบันใน lesson; A/B อาจต่างกัน         │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เป้าหมาย: ใช้แนวคิดระดับนี้กับ input และ output ของ variant ปัจจุบัน     │
# │ เหตุผล: ฝึกแปลงข้อกำหนดเป็นขั้นตอนและผลลัพธ์ที่ตรวจสอบได้                │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: ผู้เรียนฝึกนำแนวคิด Python ไปใช้กับข้อมูลใหม่              │
# │ สถานการณ์: ใช้ prompt ของ variant ปัจจุบันใน lesson เป็น contract        │
# │ ตรวจ input, output และกรณีขอบก่อนแก้โปรแกรมหรือฟังก์ชัน                  │
# │ เหตุผล: การทดสอบตาม contract ช่วยเผยข้อผิดพลาดก่อนใช้งาน                 │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ อ่าน prompt ของ variant ปัจจุบัน; ข้อกำหนด A/B อาจต่างกัน              │
# │ ☐ ทำตาม input, output และกรณีขอบ; ห้าม hardcode คำตอบ                    │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ รูปแบบส่ง: function; assessment A/B — ใช้ prompt ปัจจุบันใน lesson       │
# │ ตัวอย่าง input และ output: ดู lesson ของ variant ที่ระบบเลือก            │
# │ ผลคาดหวังถูกซ่อนไว้; check จะแสดงชื่อกรณีที่ไม่ผ่าน                      │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ Use is None for missing values; count and filter separately.             │
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     values = [1, None]                                                   │
# │     clean = [x for x in values if x is not None]                         │
# │     missing = sum(x is None for x in values)                             │
# │     result = {"clean": clean, "missing": missing}                        │
# │     print(result)                                                        │
# │ ผลที่คาด: {'clean': [1], 'missing': 1}                                   │
# │ อ่านต่อ: docs/python-syntax-handbook.md; ใช้ syntax นี้ตาม prompt        │
# │ ตรวจ input และกรณีขอบตาม variant ปัจจุบันก่อนจบ                          │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เติม body ของ final_data_cleaning_assessment ในไฟล์นี้; คงชื่อและ        │
# │ signature ตามโจทย์                                                       │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L06-E015                               │
# │ Check: python -B practice.py check L06-E015                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L06-E015 1                           │
# │ Solution: python -B practice.py solution L06-E015                       │
# │ Explain: python -B practice.py explain L06-E015                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

def final_data_cleaning_assessment(values):
    """TODO: implement the behavior in the exercise instructions."""
    # TODO(student): implement the boxed requirements.
    raise NotImplementedError("เขียนฟังก์ชันนี้")
