# Python Quant Lab

สภาพแวดล้อมฝึก Python แบบ local สำหรับ Python 3.12 ทำงานโดยไม่ต่ออินเทอร์เน็ตและไม่ต้องติดตั้งแพ็กเกจเพิ่ม แบบฝึกหัดด้านตลาดใช้ข้อมูลตัวอย่างที่กำหนดในโจทย์เพื่อการศึกษาเท่านั้น ระบบนี้ไม่มีการเชื่อมต่อ exchange กระเป๋าเงิน หรือส่งคำสั่งซื้อขายจริง

## เปิดโครงการและเริ่มเรียน

1. เปิด VS Code แล้วเลือก **File → Open Folder...**
2. เลือกโฟลเดอร์ `python-quant-lab`
3. เปิดเมนู **Terminal → New Terminal**
4. ตรวจ Python ด้วย `python --version` (ควรเป็น Python 3.12)
5. เริ่มบทเรียนแรก:

```powershell
python practice.py start
```

ระบบจะแสดงบทเรียนสั้น โจทย์ ตัวอย่าง และตำแหน่งไฟล์คำตอบ จากนั้นเปิดไฟล์ด้วย:

```powershell
python practice.py open
```

เขียนคำตอบใน `exercises/level_01/L01-E001.py` ตรงตำแหน่ง TODO อย่าแก้ไฟล์ใน `tests/`, `solutions/`, `curriculum.json` หรือ `practice.py` เพื่อให้การตรวจสะท้อนคำตอบจริง

## วงจรฝึก

```powershell
python practice.py lesson
python practice.py run
python practice.py check
```

ระบุรหัสได้ เช่น `python practice.py check L01-E001` คำสั่ง `run` ทดลองเรียกฟังก์ชันด้วยข้อมูลตัวอย่างหนึ่งชุด ส่วน `check` รันทดสอบทุกกรณีของข้อนั้นใน subprocess ที่จำกัดเวลา 4 วินาที ระบบแสดงข้อผิดพลาด Python ใน terminal เมื่อมีปัญหา

```powershell
python practice.py hint
python practice.py hint L01-E001 2
python practice.py solution L01-E001
python practice.py solution L01-E001 --yes
python practice.py explain L01-E001
python practice.py retry L01-E001
python practice.py next
```

คำใบ้มี 3 ระดับและบันทึกระดับที่เปิดดู เฉลยและคำอธิบายจะเตือนก่อนเปิด และบันทึกการดูเฉลยโดยไม่เขียนทับไฟล์นักเรียน การผ่านหลังเปิดคำใบ้หรือเฉลยจะแสดง `PASSED_WITH_HELP`; ถ้าไม่เคยเปิด จะบันทึก `PASSED_INDEPENDENTLY` การผ่านแบบช่วยเหลือไม่ถูกนับเป็นหลักฐานผ่านอิสระเพื่อปลดล็อก Level ถัดไป

## ความคืบหน้าและคำสั่ง

```powershell
python practice.py help
python practice.py start
python practice.py lesson [ID]
python practice.py open [ID]
python practice.py run [ID]
python practice.py check [ID]
python practice.py hint [ID [1-3]]
python practice.py solution [ID] [--yes]
python practice.py explain [ID]
python practice.py next
python practice.py list
python practice.py status
python practice.py retry ID
python practice.py reset-progress
```

ความคืบหน้าอยู่ใน `progress.json` และอยู่ต่อหลังปิด VS Code ได้ `reset-progress` ขอให้พิมพ์ `YES` เพื่อยืนยัน หรือใช้ `--yes`; คำสั่งนี้ลบเฉพาะความคืบหน้าและไม่ลบไฟล์คำตอบ สำรองไฟล์คำตอบได้โดยคัดลอกโฟลเดอร์ `exercises/` ไว้ต่างหาก

## หลักสูตร

มี 10 ระดับ ระดับละ 15 ข้อ รวม 150 ข้อ ตั้งแต่พื้นฐาน การควบคุมลำดับและโครงสร้างข้อมูล ไปจนถึงสถิติ การวิเคราะห์ความเสี่ยง การวิจัยกลยุทธ์ และ paper trading แบบออฟไลน์ ข้อ E015 ในแต่ละระดับเป็น assessment และต้องผ่านแบบอิสระก่อนเริ่มระดับถัดไป เนื้อหาปัจจุบันเป็นแบบฝึกหัดฟังก์ชันพร้อมข้อมูล deterministic; แต่ละข้อมีตัวอย่างบทเรียน hints เฉลย คำอธิบาย และ test cases แยกไฟล์

ตัวอย่างทางการเงินไม่ได้พิสูจน์ว่ากลยุทธ์มี edge หรือทำกำไรได้ และไม่ใช้ข้อมูลตลาดจริง การทดสอบของ grader ตรวจ input/output ไม่ได้ประเมินความเข้าใจเชิงแนวคิดทั้งหมด

## VS Code Tasks

เปิด **Terminal → Run Task...** เพื่อเลือก Start Learning, Open Current Exercise, Check Current Exercise, Show Hint, Show Solution, Explain Solution, Show Progress หรือ Next Exercise

## Dependencies และข้อจำกัด

ระดับทั้งหมดเริ่มใช้งานได้ด้วย standard library ไม่จำเป็นต้องติดตั้ง NumPy, pandas, Matplotlib, Plotly หรือ vectorbt `requirements.txt` ตั้งใจเว้นไว้เพื่อให้เพิ่มแพ็กเกจภายหลังเมื่อถึงเนื้อหานั้น

ตัวตรวจรันโค้ดผู้เรียนใน subprocess ที่จำกัดเวลา แต่ process isolation นี้ **ไม่ใช่ sandbox เพื่อความปลอดภัยที่แข็งแรง** จึงควรตรวจโค้ดก่อนรัน โครงการนี้ไม่มีการเข้าถึงบัญชี exchange, wallet, private key หรือ live trading API
