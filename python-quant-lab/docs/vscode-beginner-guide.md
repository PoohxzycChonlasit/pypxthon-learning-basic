# เปิด Python Quant Lab ใน VS Code

คู่มือนี้ใช้กับ Windows และ macOS. เริ่ม Level 1 ได้ด้วย Python 3.12 และ standard library; ไม่ต้องสร้าง virtual environment หรือติดตั้ง package ก่อน

## 1. Clone หรือเปิดโฟลเดอร์ project

### Windows PowerShell — clone ใหม่

เปิด PowerShell ในโฟลเดอร์ที่จะเก็บ repository:

~~~powershell
git clone https://github.com/PoohxzycChonlasit/pypxthon-learning-basic.git
Set-Location -LiteralPath .\pypxthon-learning-basic\python-quant-lab
code .
~~~

ถ้ามี checkout อยู่แล้ว ให้เปิดโฟลเดอร์ <code>python-quant-lab</code> ซึ่งอยู่ภายใน repository. ใส่ path ที่มีช่องว่างในเครื่องหมายคำพูด:

~~~powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
Get-Location
code .
~~~

### macOS Terminal — clone ใหม่

~~~sh
git clone https://github.com/PoohxzycChonlasit/pypxthon-learning-basic.git
cd ./pypxthon-learning-basic/python-quant-lab
code .
pwd
~~~

หากมี checkout แล้ว ให้เปิดโฟลเดอร์ <code>python-quant-lab</code> ใน VS Code หรือใช้ <code>cd "/path/to/repository/python-quant-lab"</code>. คำสั่ง <code>pwd</code> แสดง current working directory

## 2. เลือก Python interpreter

ใน VS Code กด <strong>Ctrl+Shift+P</strong> บน Windows หรือ <strong>Cmd+Shift+P</strong> บน macOS, เลือก <strong>Python: Select Interpreter</strong>, แล้วเลือก Python 3.12 ที่ติดตั้งไว้แล้ว

ตรวจ interpreter ใน Terminal:

**Windows PowerShell**

~~~powershell
py -3.12 --version
python --version
~~~

**macOS Terminal**

~~~sh
python3.12 --version
python3 --version
~~~

ใช้คำสั่งของ Python 3.12 ในตัวอย่างต่อไป. อย่าเปลี่ยน system Python เพื่อให้ตรงกับคู่มือ; หากไม่มี 3.12 ให้หยุดและเลือก interpreter ที่โครงการรองรับกับเจ้าของโครงการก่อน

## 3. เปิด Terminal ใน VS Code และตรวจตำแหน่ง

เลือกเมนู <strong>Terminal → New Terminal</strong> หรือกด <strong>Ctrl + ปุ่มที่อยู่เหนือ Tab</strong>. Terminal ควรอยู่ที่โฟลเดอร์ <code>python-quant-lab</code> ซึ่งมี <code>practice.py</code> อยู่

**Windows PowerShell**

~~~powershell
Get-Location
Test-Path .\practice.py
~~~

**macOS Terminal**

~~~sh
pwd
test -f practice.py && echo "practice.py found"
~~~

หากไฟล์ไม่พบ ให้เปลี่ยน current directory เข้าโฟลเดอร์ <code>python-quant-lab</code> ก่อนสั่งรัน

## 4. เริ่ม Level 1

**Windows PowerShell**

~~~powershell
py -3.12 -B practice.py list --level 1
py -3.12 -B practice.py open L01-E001
py -3.12 -B practice.py run L01-E001
py -3.12 -B practice.py check L01-E001
~~~

**macOS Terminal**

~~~sh
python3.12 -B practice.py list --level 1
python3.12 -B practice.py open L01-E001
python3.12 -B practice.py run L01-E001
python3.12 -B practice.py check L01-E001
~~~

<code>list</code> แสดงรหัส ชนิดคำตอบ และตำแหน่งส่ง; <code>open</code> เปิด lesson กับไฟล์ส่ง; <code>run</code> ทดลองกรณีแรก; <code>check</code> ตรวจทุกกรณีและบันทึกความคืบหน้า

## 5. แก้ บันทึก และทดลองไฟล์

ไฟล์ที่ <code>open ID</code> ระบุคือไฟล์ที่ต้องแก้. พิมพ์ในตำแหน่ง TODO หรือไฟล์คำตอบที่ lesson บอก จากนั้นบันทึกด้วย <strong>Ctrl+S</strong> บน Windows หรือ <strong>Cmd+S</strong> บน macOS

สำหรับ submission แบบ stdout การกด <strong>Run Python File</strong> ใน VS Code จะรันไฟล์ตรงและแสดง stdout ใน Terminal. แต่ในโจทย์แบบ function ไฟล์อาจเพียงประกาศฟังก์ชันจึงไม่มี output; ใช้ <code>practice.py run ID</code> ให้ course runner เรียกฟังก์ชัน. โจทย์ text_answer ใช้ไฟล์ <code>.txt</code> และ Check ไม่ใช้ Run

## ถ้าไม่มี output

- การกำหนดตัวแปรหรือประกาศ <code>def</code> ไม่แสดงค่าเอง; ใช้ <code>print()</code> เมื่อโจทย์ stdout ต้องการให้แสดง
- <code>practice.py run ID</code> ของ function แสดงผลที่ runner ได้จากการเรียกด้วย input ตัวอย่าง
- สำหรับ text_answer ไม่มี output จากการ Run เป็นพฤติกรรมที่คาดไว้; ใส่คำทำนายใน .txt แล้วใช้ Check
- อ่าน [คำอธิบาย submission types](submission-types.md) หากไม่แน่ใจว่าควร Run หรือ Check

## อ่านก่อนทำ

- [เริ่มต้นหลักสูตร](../README.md#start-here)
- [Level 1 — เรียน Python พื้นฐาน](../lessons/level_01.md)
- [คำตอบ 3 แบบ และ Run/Check](submission-types.md)
- [Data Analysis track](../tracks/data_analysis/README.md) — เป็นเส้นทางเสริมหลัง Level 5
