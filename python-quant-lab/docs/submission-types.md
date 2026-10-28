# คำตอบ 3 แบบ และความหมายของ Run / Check

ก่อนแก้โจทย์ ให้ดูชนิดคำตอบในหน้า lesson หรือผลจาก <code>practice.py list</code>. แต่ละแบบใช้ไฟล์และวิธีตรวจต่างกัน

| ชนิด | สิ่งที่แก้ | VS Code: Run Python File | <code>practice.py run ID</code> | <code>practice.py check ID</code> |
|---|---|---|---|---|
| <strong>stdout</strong> | ไฟล์ Python ที่แสดงข้อความด้วย <code>print()</code> | รันไฟล์และแสดง stdout ใน Terminal | รันกรณีตัวอย่างแรกแล้วแสดง output | ตรวจทุกกรณีและบันทึกสถานะ |
| <strong>text_answer</strong> | ไฟล์ข้อความ <code>answers/level_NN/ID.txt</code> ที่มีผลทำนาย | ไม่ใช่ขั้นตอนส่งคำตอบ | บอกว่าไม่ต้องรัน Python และแสดงไฟล์ .txt/คำสั่งตรวจ | เปรียบเทียบข้อความกับคำตอบที่คาดและบันทึกสถานะ |
| <strong>function</strong> | ฟังก์ชันในไฟล์ Python; รับ parameters และคืนค่าด้วย <code>return</code> | อาจไม่แสดงอะไร เพราะการประกาศ <code>def</code> แค่สร้างฟังก์ชัน | เรียกฟังก์ชันด้วย input ตัวอย่างแรกแล้วแสดงค่าที่คืน | เรียกทุกกรณีทดสอบ ตรวจผล และบันทึกสถานะ |

## A — stdout: โปรแกรมพิมพ์ผล

เขียนคำสั่งในไฟล์ Python แล้วใช้ <code>print(value)</code> เพื่อส่งข้อความไปยัง stdout ซึ่งแสดงใน Terminal. หากเพียงกำหนด <code>answer = 5</code> จะยังไม่มีข้อความปรากฏ; ต้องเรียก <code>print(answer)</code> หากโจทย์กำหนดให้แสดงผล

## B — text_answer: ทำนายผลแล้วเขียนข้อความ

อ่านคำสั่ง Python ในโจทย์และคำนวณผลด้วยตนเอง จากนั้นใส่เฉพาะผลที่ทำนายลงไฟล์ <code>.txt</code> ที่ lesson ระบุ. ไม่ต้องสร้างโปรแกรมใหม่และไม่ต้องกด Run เพื่อหาคำตอบ

การกำหนดค่า เช่น <code>ANSWER = 5</code> เก็บค่าไว้ในตัวแปร แต่ไม่ได้สั่งให้ Python แสดงค่า. การแสดงผลต้องเรียก <code>print()</code>; โจทย์นี้ให้ผู้เรียนทำนาย output โดยไม่รัน จึงตรวจด้วย <code>check</code> เท่านั้น

ตัวอย่างคำสั่งตรวจบน Windows PowerShell:

~~~powershell
py -3.12 -B practice.py check L01-E002
~~~

บน macOS Terminal:

~~~sh
python3.12 -B practice.py check L01-E002
~~~

ถ้าเรียก <code>practice.py run ID</code> ในโจทย์ text_answer ระบบจะชี้ไปยังไฟล์ .txt และบอกคำสั่ง Check ที่ควรใช้

## C — function: เขียนฟังก์ชันคืนค่า

ฟังก์ชันรับข้อมูลผ่าน parameters เช่น <code>def add(a, b):</code> แล้วส่งผลกลับด้วย <code>return</code>. การคืนค่าต่างจากการแสดงผล: <code>return</code> มอบผลให้ผู้เรียก ส่วน <code>print</code> แสดงข้อความใน Terminal

ถ้ากด VS Code Run Python File แล้วไฟล์มีเพียงการประกาศฟังก์ชัน อาจไม่มี output ซึ่งเป็นเรื่องปกติ เพราะยังไม่มีใครเรียกฟังก์ชันนั้น. ใช้ <code>practice.py run ID</code> เพื่อให้ runner เรียกฟังก์ชันด้วยกรณีแรก หรือใช้ <code>check</code> เพื่อตรวจทุกกรณี

## วิธีเริ่มจาก project root

เปิด Terminal ในโฟลเดอร์ที่มี <code>practice.py</code>, จากนั้นดู Level 1 และเปิดข้อแรก:

~~~powershell
py -3.12 -B practice.py list --level 1
py -3.12 -B practice.py open L01-E001
py -3.12 -B practice.py run L01-E001
py -3.12 -B practice.py check L01-E001
~~~

macOS ใช้ <code>python3.12</code> แทน <code>py -3.12</code>. หากไม่แน่ใจว่าเปิดไฟล์ใด ให้ใช้ <code>open ID</code>; ระบบจะแสดงชนิดคำตอบและพาธไฟล์จริง

<strong>สรุป:</strong> VS Code Run รันไฟล์ตรง, <code>practice.py run</code> เรียกตัวอย่างแรกของโจทย์ที่รองรับ, และ <code>practice.py check</code> ตรวจทุกกรณี. สามคำสั่งนี้ทำงานคนละอย่าง
