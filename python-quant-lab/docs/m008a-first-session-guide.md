# คู่มือเริ่ม Python Quant Lab: L01-E001–E003

เป้าหมายคือเริ่มจากโจทย์แรก เรียนรู้ว่าไฟล์ใดต้องแก้ และใช้ Run กับ Check ให้ถูกประเภท โจทย์และคำตอบไม่ได้ทำแทนไว้ในคู่มือนี้

## เจ้าของเครื่องตรวจ checkout ก่อน

ใน Terminal ของ VS Code ที่เปิด checkout ที่ผู้เรียนจะใช้ รันคำสั่งอ่านอย่างเดียวเหล่านี้ก่อนแก้ไฟล์:

~~~powershell
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --short
$repoRoot = (git rev-parse --show-toplevel).Trim()
Test-Path (Join-Path $repoRoot "python-quant-lab\README.md")
Test-Path (Join-Path $repoRoot "python-quant-lab\docs\m008a-first-session-guide.md")
py -0p
py -3.12 --version
py -3.12 -c "import sys; print(sys.executable)"
~~~

Remote ที่คาดไว้คือ `https://github.com/PoohxzycChonlasit/pypxthon-learning-basic.git`; โครงการเรียนอยู่ในโฟลเดอร์ `python-quant-lab` และใช้ Python 3.12. ตรวจ interpreter ที่แถบสถานะของ VS Code ด้วย; ถ้าแสดง Python 3.15.2 หรือไม่ตรงกับ Python 3.12 ที่ตรวจด้วยคำสั่งด้านบน ให้หยุดก่อนใช้ Run. หาก remote, interpreter หรือไฟล์โครงการไม่ตรง หรือ checkout นี้ไม่ใช่ที่ต้องการ อย่า pull, reset, clean หรือคัดลอกทับไฟล์ ให้หยุดและให้เจ้าของตรวจ checkout ก่อน เพราะ M008 ยังเป็นงาน local ที่ไม่ได้ commit หรือ push.

## เริ่มบทเรียน

หลังเจ้าของยืนยัน checkout แล้ว ให้เปิด Terminal ที่โฟลเดอร์ `python-quant-lab` ซึ่งมี `practice.py`:

~~~powershell
py -3.12 -B practice.py list --level 1
py -3.12 -B practice.py lesson L01-E001
~~~

### L01-E001 — แสดงข้อความ

อ่าน [บทเรียน L01-E001](../lessons/L01-E001.md). เพิ่มคำสั่งใน `exercises/level_01/L01-E001.py` ใต้ comment คำแนะนำ แล้วทดลองและตรวจงาน:

~~~powershell
py -3.12 -B practice.py run L01-E001
py -3.12 -B practice.py check L01-E001
~~~

### L01-E002 — ทายผลลัพธ์

อ่าน [บทเรียน L01-E002](../lessons/L01-E002.md). นี่เป็นโจทย์ทำนายผล: เขียนเฉพาะผลที่คุณคำนวณได้ลง `answers/level_01/L01-E002.txt` ตามรูปแบบที่บทเรียนระบุ แล้วใช้ Check. อย่ารันไฟล์ Python หรือใช้ `practice.py run` กับข้อนี้:

~~~powershell
py -3.12 -B practice.py check L01-E002
~~~

### L01-E003 — ใช้ตัวแปรคำนวณ

อ่าน [บทเรียน L01-E003](../lessons/L01-E003.md). เติมเฉพาะ TODO ใน `exercises/level_01/L01-E003.py`, จากนั้นใช้ Run และ Check:

~~~powershell
py -3.12 -B practice.py run L01-E003
py -3.12 -B practice.py check L01-E003
~~~

ถ้า Check ไม่ผ่าน ให้อ่านข้อความที่แสดงและกลับไปดูข้อกำหนดในบทเรียนก่อนแก้ ห้ามลบหรือ reset `progress.json`; Check ใช้บันทึกความคืบหน้า

## บันทึกผลผู้เรียนจริง

หลังเรียนจบ เจ้าของหลักสูตรค่อยบันทึกความเข้าใจและจุดที่สับสนใน [checklist การยอมรับ](m008-real-learner-acceptance.md). สถานะยังเป็น **NOT_VERIFIED** จนกว่าจะมีผู้เรียนจริงทดลองและให้ feedback.
