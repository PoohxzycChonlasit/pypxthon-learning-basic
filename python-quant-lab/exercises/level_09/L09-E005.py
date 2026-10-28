# M005 EXERCISE BOX — UTF-8
# ┌─ EXERCISE ───────────────────────────────────────────────────────────────┐
# │ L09-E005 — เปรียบเทียบผล OOS กับ benchmark                               │
# │ Level 9: Quant Research and Backtesting | Tier 3: ง่าย —                 │
# │ รวมแนวคิดคุ้นเคย                                                         │
# │ ประเภท: โจทย์ประยุกต์ / stdout | ความรู้ก่อนหน้า: ทบทวน L09-E004 แก้     │
# │ look-ahead ในค่าเฉลี่ยย้อนหลัง                                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ LEARNING OBJECTIVE ─────────────────────────────────────────────────────┐
# │ เรียนรู้: สรุปผลตอบแทน net นอกตัวอย่างและตรวจว่า benchmark               │
# │   ถูกเอาชนะหรือไม่                                                       │
# │ ทำไมสำคัญ: การทำ เปรียบเทียบผล OOS กับ benchmark                         │
# │   ฝึกประกอบหลายแนวคิดกับข้อมูลและผลลัพธ์ที่กำหนด.                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ REAL-WORLD SCENARIO ────────────────────────────────────────────────────┐
# │ ผู้ใช้/บทบาท: นักวิจัย Quant ที่ทดสอบสูตรกับข้อมูลสังเคราะห์ออฟไลน์.     │
# │ สถานการณ์: รับ JSON array ของผลตอบแทนกลยุทธ์และอีกบรรทัดเป็น             │
# │   benchmark returns จากช่วง out-of-sample ที่แยกไว้ก่อนแล้ว              │
# │   คืนผลรวมแต่ละชุด, excess และ beats; ถ้าความยาวไม่เท่ากันให้แสดง        │
# │   INVALID ห้ามใช้ผลชุดนี้ปรับกลยุทธ์ย้อนหลัง                             │
# │ เหตุผล: การเข้าใจ เปรียบเทียบผล OOS กับ benchmark                        │
# │   ช่วยให้เห็นต้นทุนหรือข้อจำกัดก่อนใช้ผลจำลอง.                           │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ TASK CHECKLIST ─────────────────────────────────────────────────────────┐
# │ ☐ ทำตามข้อกำหนด: สรุปผลตอบแทน net นอกตัวอย่างและตรวจว่า benchmark        │
# │   ถูกเอาชนะหรือไม่                                                       │
# │ ☐ รักษารูปแบบ input/output และกรณีขอบตามโจทย์                            │
# │ ☐ รัน check จนผ่านทุกกรณี; แก้เฉพาะ TODO(student)                        │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ INPUT AND OUTPUT ───────────────────────────────────────────────────────┐
# │ stdin ตัวอย่าง: '[0.02,-0.01,0.03]\n[0.01,0.0,0.01]\n'                   │
# │ stdout ที่ต้องได้: 'strategy=0.0400 benchmark=0.0200 excess=0.0200       │
# │ beats=True\n'                                                            │
# │ ข้อจำกัด: ใช้ Python 3.12 และ standard library; ห้ามแก้ tests,           │
# │ curriculum หรือไฟล์เฉลย; ตัวอย่างการเทรดเป็น paper-only                  │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ SYNTAX REFERENCE ───────────────────────────────────────────────────────┐
# │ math.prod(1 + r for r in returns) - 1 compounds simple returns.
# │ ตัวอย่างสั้น (ฝึก syntax ไม่ใช่คำตอบโจทย์):                              │
# │     import math                                                          │
# │     returns = [0.1, 0.2]                                                 │
# │     net = math.prod(1 + r for r in returns) - 1                          │
# │     print(round(net, 4))                                                 │
# │ ผลที่คาด: 0.32                                                           │
# │ อ่านต่อ: docs/python-syntax-handbook.md; จุดที่พลาดบ่อย:                 │
# │ เปรียบเทียบผลรวมของช่วงเวลาต่างกัน หรือเลือกพารามิเตอร์จาก OOS ซ้ำ       │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ IMPLEMENTATION ─────────────────────────────────────────────────────────┐
# │ เขียนหรือแก้โค้ดตรง TODO ด้านล่าง; แสดงเฉพาะ stdout ที่โจทย์กำหนด        │
# │ แก้เฉพาะ TODO; อย่าลบชื่อฟังก์ชันหรือแก้ไฟล์ grader/solution             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ VERIFICATION ───────────────────────────────────────────────────────────┐
# │ Run in the project folder (same folder as practice.py).                 │
# │ Run:   python -B practice.py run L09-E005                               │
# │ Check: python -B practice.py check L09-E005                             │
# └───────────────────────────────────────────────────────────────────────────┘
# ┌─ HELP AND COMPLETION ────────────────────────────────────────────────────┐
# │ Hint:   python -B practice.py hint L09-E005 1                           │
# │ Solution: python -B practice.py solution L09-E005                       │
# │ Explain: python -B practice.py explain L09-E005                         │
# │ Help is recorded; checking afterwards marks PASSED_WITH_HELP.           │
# │ Finish when check passes; an independent E015 pass unlocks next.        │
# └───────────────────────────────────────────────────────────────────────────┘

# TODO(student): write or repair the program below.
def compare_oos(strategy_returns, benchmark_returns):
    raise NotImplementedError("TODO: เทียบผล OOS")

if __name__ == "__main__":
    import json
    strategy = json.loads(input())
    benchmark = json.loads(input())
    result = compare_oos(strategy, benchmark)
    if result is None:
        print("INVALID")
    else:
        print(f"strategy={result['strategy_net']:.4f} benchmark={result['benchmark_net']:.4f} excess={result['excess']:.4f} beats={result['beats']}")
