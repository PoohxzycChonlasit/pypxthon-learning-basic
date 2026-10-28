# Python Quant Lab — เรียน Python ด้วยการลงมือทำ

Python Quant Lab เป็นหลักสูตรภาษาไทยสำหรับฝึก Python ตั้งแต่พื้นฐานไปจนถึงการวิเคราะห์ข้อมูล การเงินเชิงปริมาณ และการจำลอง paper trading แบบออฟไลน์ คุณไม่จำเป็นต้องรู้ Python มาก่อน ผู้ที่เคยใช้ JavaScript/TypeScript สามารถต่อยอดแนวคิดเดิมได้ ดู [ความแตกต่างระหว่าง Python กับ JavaScript](docs/python-vs-javascript.md)

Python เป็นภาษาโปรแกรมที่อ่านง่ายและมีเครื่องมือหลากหลาย คนใช้เขียนสคริปต์อัตโนมัติ จัดการไฟล์ ทำรายงาน เว็บ และวิเคราะห์ข้อมูล ในงาน Quant เราใช้ Python เตรียมข้อมูล คำนวณสถิติและทดสอบสมมติฐาน ส่วน trading bot คือโปรแกรมที่อ่านข้อมูลและทำตามกฎที่กำหนด หลักสูตรนี้ใช้การจำลองออฟไลน์เท่านั้น ไม่มี exchange, wallet หรือคำสั่งซื้อขายจริง ผล backtest ไม่พิสูจน์ว่ามีกำไรหรือรับประกันผลในอนาคต

## เริ่มต้นบน Windows และ VS Code

### 1. เปิดโฟลเดอร์โครงการ

เปิด VS Code แล้วเลือก **File → Open Folder...** เลือกโฟลเดอร์ <code>python-quant-lab</code> จากนั้นเลือก **Terminal → New Terminal** terminal คือช่องพิมพ์คำสั่งที่ทำงานอยู่ในโฟลเดอร์หนึ่ง ๆ

ตรวจโฟลเดอร์ปัจจุบันและเปิดโครงการจาก PowerShell ได้ด้วย:

~~~powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
Get-Location
~~~

ใช้ <code>-LiteralPath</code> และใส่ path ในเครื่องหมายคำพูด เพราะชื่อโฟลเดอร์มีช่องว่าง

### 2. ตรวจ Python และเลือก interpreter

~~~powershell
python --version
~~~

โครงการเตรียมไว้สำหรับ Python 3.12 หากคำสั่ง <code>python</code> ใช้ไม่ได้ ให้ลอง:

~~~powershell
py -3.12 --version
~~~

ใน VS Code กด **Ctrl+Shift+P**, เลือก **Python: Select Interpreter**, แล้วเลือก Python 3.12 ที่ต้องการ หากสร้าง virtual environment ตามขั้นตอนถัดไป ให้เลือก <code>.venv\Scripts\python.exe</code>

### 3. สร้าง virtual environment ของโครงการ

virtual environment เป็นพื้นที่แยกสำหรับแพ็กเกจของโครงการนี้ ไม่เปลี่ยน Python ส่วนกลาง:

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe --version
~~~

ไม่จำเป็นต้อง activate environment ใน PowerShell; เรียก interpreter ด้วย path เต็มได้โดยตรง ระดับหลักสูตรปัจจุบันใช้ standard library จึงยังไม่ต้องติดตั้งแพ็กเกจเพิ่ม

### 4. เริ่มระบบและอ่านบทเรียน

~~~powershell
python practice.py start
python practice.py lesson
~~~

เริ่มข้อแรกหรือข้อที่บันทึกไว้ ระบบแสดงโจทย์และพาธไฟล์ที่ต้องแก้ หาก VS Code เปิดไฟล์ไม่ได้ ให้ใช้คำสั่ง open แล้วเปิดพาธที่แสดง:

~~~powershell
python practice.py open
~~~

### 5. พิมพ์และรันคำตอบ

แก้เฉพาะไฟล์คำตอบของข้อปัจจุบัน แล้วบันทึกด้วย **Ctrl+S** คำสั่ง run ทดลองกรณีตัวอย่างแรก:

~~~powershell
python practice.py run
~~~

### 6. ตรวจคำตอบและทำความเข้าใจผล

~~~powershell
python practice.py check
python practice.py check L01-E003
~~~

หากตรวจไม่ผ่าน อ่านชื่อ test และ traceback แล้วแก้สาเหตุ ใช้ [คู่มือแก้โจทย์](docs/how-to-solve-exercises.md) และ [ข้อผิดพลาด Python ที่พบบ่อย](docs/common-python-errors.md)

### 7. ขอ hint หรือเปิด solution

~~~powershell
python practice.py hint
python practice.py hint L01-E003 2
python practice.py solution L01-E003
python practice.py explain L01-E003
~~~

ระบบจะถามก่อนเปิด solution หรือคำอธิบายฉบับเต็ม ตอบ <code>YES</code> เพื่อยืนยัน หรือใช้ <code>--yes</code> ต่อท้ายเมื่อคุณตัดสินใจแล้ว เช่น <code>python practice.py solution L01-E003 --yes</code> การเปิด solution ไม่เขียนทับไฟล์นักเรียน แต่จะบันทึกว่าเคยดูไว้ และการผ่านภายหลังจะเป็นการผ่านแบบช่วยเหลือ

### 8. ไปข้อถัดไปและดูความคืบหน้า

~~~powershell
python practice.py next
python practice.py status
python practice.py list
python practice.py retry L01-E003
~~~

## ทำความเข้าใจไฟล์ในโครงการ

| ไฟล์หรือโฟลเดอร์ | ใช้ทำอะไร | ผู้เรียนควรแก้หรือไม่ |
|---|---|---|
| <code>README.md</code> | คู่มือเริ่มต้นและดัชนีบทเรียน | อ่าน; ไม่จำเป็นต้องแก้ |
| <code>practice.py</code> | โปรแกรมนำทาง ตรวจคำตอบ และบันทึกความคืบหน้า | ไม่ควรแก้ระหว่างเรียน |
| <code>curriculum.json</code> | โจทย์ เป้าหมาย ตัวอย่าง และกรณีทดสอบของระบบ | ไม่ควรแก้ |
| <code>lessons/</code> | บทเรียนแบบพิมพ์ตามและตัวอย่างก่อนทำโจทย์ | อ่านและพิมพ์ตัวอย่างลงไฟล์ทดลอง |
| <code>exercises/</code> | ไฟล์ Python สำหรับส่งคำตอบ | แก้ไฟล์ของข้อที่กำลังทำ |
| <code>answers/</code> | คำตอบข้อความสำหรับข้อทำนายผล | แก้เฉพาะไฟล์ที่คำสั่ง open ระบุ |
| <code>solutions/</code> | คำตอบอ้างอิง | เปิดผ่านคำสั่ง solution หลังลองทำ |
| <code>explanations/</code> | คำอธิบายหลังเฉลย | เปิดผ่านคำสั่ง explain หลังลองทำ |
| <code>hints/</code> | ใบ้สามระดับสำหรับแต่ละข้อ | อ่านผ่านคำสั่ง hint |
| <code>tests/</code> | ตัวอย่างข้อมูลที่ grader ใช้ตรวจ | ไม่ควรแก้ |
| <code>data/</code> | ชุดข้อมูลฝึกออฟไลน์และข้อมูลสังเคราะห์ | อ่าน; เก็บข้อมูลทดลองแยกไฟล์ |
| <code>progress.json</code> | สถานะ attempts, hints, solution reveals และผลผ่าน | อย่าแก้หรือลบทิ้ง |
| <code>requirements.txt</code> | รายการ dependency ของโครงการ | ไม่ต้องติดตั้งแพ็กเกจเพื่อเริ่ม |

ไฟล์ <code>.py</code> คือโปรแกรม Python; <code>.md</code> คือเอกสาร Markdown; <code>.txt</code> ใช้เก็บคำตอบข้อความหรือข้อมูลธรรมดา; <code>.json</code> เก็บข้อมูลแบบมีโครงสร้าง; CSV เก็บข้อมูลเป็นแถวและคอลัมน์; dependency คือไลบรารีที่โปรแกรมอื่นเขียนไว้และโครงการอาจเรียกใช้; test คือการตรวจว่าโปรแกรมทำตามข้อกำหนดในกรณีที่เลือกไว้

### คำศัพท์พื้นฐาน

- **ตัวแปร (variable):** ชื่อที่เก็บหรืออ้างถึงค่า เช่น <code>price = 100</code>
- **ฟังก์ชัน (function):** ชุดคำสั่งที่ตั้งชื่อ เรียกใช้ซ้ำ และรับข้อมูลผ่าน parameters
- **ข้อยกเว้น (exception):** สัญญาณที่ Python ใช้บอกว่าเกิดปัญหา เช่น แปลงข้อความเป็นตัวเลขไม่ได้
- **ไลบรารี (library):** โค้ดที่เขียนไว้ให้เรียกใช้ เช่น <code>csv</code> ใน standard library
- **เทอร์มินัล (terminal):** ช่องสั่งให้คอมพิวเตอร์รันโปรแกรม โดยคำสั่งทำงานจากโฟลเดอร์ปัจจุบัน
- **ตัวทดสอบ (test):** ตัวอย่าง input และผลที่คาดไว้ ใช้ตรวจพฤติกรรมของโปรแกรม

โครงการไม่สร้าง <code>progress.json</code> จนกว่าจะมีการบันทึกการเรียนครั้งแรก หากมีไฟล์นี้แล้ว อย่าลบหรือ reset เพื่อทดลอง ใช้สำเนาโครงการชั่วคราวแทน

## วงจรการเรียน

**อ่านบทเรียน → พิมพ์ตัวอย่างเอง → ทดลองเปลี่ยนค่า → ทำโจทย์ → ตรวจ → แก้ข้อผิดพลาด → อ่านคำอธิบาย → สรุปด้วยคำของตนเอง → ทำข้อต่อไป**

อย่าจำโค้ดโดยไม่เข้าใจ ลองทำนายผลก่อนรัน อธิบายว่าแต่ละบรรทัดทำอะไร และสร้างกรณีทดสอบใหม่เพื่อดูว่าความเข้าใจยังใช้ได้เมื่อข้อมูลเปลี่ยนหรือไม่

## แผนที่หลักสูตร

| ระดับ | เนื้อหาและเหตุผลที่ใช้ได้จริง |
|---|---|
| 1 — Python พื้นฐาน | print, ตัวแปร, ข้อความ, ตัวเลข, input, การแปลงชนิด และสูตรสั้น ๆ |
| 2 — เงื่อนไขและลูป | เปรียบเทียบค่า เลือกกฎ วนซ้ำ และหยุดเมื่อถึงเงื่อนไข |
| 3 — โครงสร้างข้อมูล | list, tuple, set, dict และการจัดการรายการ/ระเบียน |
| 4 — ฟังก์ชันและโมดูล | แยกขั้นตอนเป็นชิ้นที่เรียกซ้ำและดูแลได้ |
| 5 — Python สำหรับงานจริง | ไฟล์ CSV/JSON การตรวจข้อมูล exception และ unit test |
| 6 — วิเคราะห์ข้อมูล | ทำความสะอาด คัดกรอง สรุป และแสดงข้อมูลตามเวลา |
| 7 — คณิตศาสตร์และสถิติ | ค่าเฉลี่ย การกระจาย ความน่าจะเป็น และความไม่แน่นอน |
| 8 — การเงินและความเสี่ยง | ผลตอบแทนสุทธิ ต้นทุน ขนาดสถานะ exposure และ drawdown |
| 9 — วิจัย Quant | สมมติฐาน benchmark backtest และการตรวจ overfitting/data leakage |
| 10 — บอท paper ออฟไลน์ | replay ข้อมูล สัญญาณ การจำลองคำสั่ง บัญชี และขีดจำกัดความเสี่ยง |

อ่าน prerequisites, งานตัวอย่าง และเกณฑ์จบแต่ละระดับใน [แผนที่การเรียนฉบับเต็ม](docs/learning-roadmap.md) บทเรียนแบบพิมพ์ตามอยู่ในดัชนีด้านล่าง

## ดัชนีไฟล์แบบฝึกหัด

- [Level 1 starters](exercises/level_01/) · [คำอธิบายข้อแรก](explanations/L01-E001.md)
- [Level 2 starters](exercises/level_02/) · [คำอธิบายข้อแรก](explanations/L02-E001.md)
- [Level 3 starters](exercises/level_03/) · [คำอธิบายข้อแรก](explanations/L03-E001.md)
- [Level 4 starters](exercises/level_04/) · [คำอธิบายข้อแรก](explanations/L04-E001.md)
- [Level 5 starters](exercises/level_05/) · [คำอธิบายข้อแรก](explanations/L05-E001.md)
- [Level 6 starters](exercises/level_06/) · [คำอธิบายข้อแรก](explanations/L06-E001.md)
- [Level 7 starters](exercises/level_07/) · [คำอธิบายข้อแรก](explanations/L07-E001.md)
- [Level 8 starters](exercises/level_08/) · [คำอธิบายข้อแรก](explanations/L08-E001.md)
- [Level 9 starters](exercises/level_09/) · [คำอธิบายข้อแรก](explanations/L09-E001.md)
- [Level 10 starters](exercises/level_10/) · [คำอธิบายข้อแรก](explanations/L10-E001.md)

## ความคืบหน้าและการประเมิน

- <code>NOT_STARTED</code> — ยังไม่เริ่มส่งคำตอบ
- <code>IN_PROGRESS</code> — เริ่มตรวจแล้วแต่ยังไม่ผ่าน
- <code>PASSED_INDEPENDENTLY</code> — ผ่านกรณีทดสอบโดยยังไม่เปิด hint หรือ solution ของข้อนั้น
- <code>PASSED_WITH_HELP</code> — ผ่านหลังเปิด hint หรือ solution
- <code>NEEDS_REVIEW</code> — มีกรณีทดสอบไม่ผ่าน ต้องอ่าน feedback และแก้ไข

การผ่าน test หมายความว่าคำตอบตรงกับกรณีที่ระบบตรวจ ไม่ได้พิสูจน์ว่าผู้เรียนเข้าใจทุกกรณีหรือทำงานจริงได้ อธิบายวิธีคิดและทดสอบ input เพิ่มเองเสมอ

ข้อ E015 เป็น assessment ท้ายระดับ ทุกระดับมีโจทย์ variant A/B คนละบริบทและใช้ grader แยกชุดทดสอบ หากเปิด hint หรือ solution ของ variant ที่กำลังทำแล้วผ่าน ระบบจะนับเป็น assisted; การผ่าน variant ใหม่โดยไม่เปิดความช่วยเหลือจึงใช้เป็นหลักฐานประเมินซ้ำได้ ผลทดสอบยืนยันเฉพาะกรณีที่กำหนด ไม่ได้พิสูจน์ความเข้าใจทั้งหมด

## FAQ

**ต้องจำ syntax ทั้งหมดไหม?** ไม่ต้อง จำแนวคิดและรู้วิธีเปิดคู่มืออ้างอิงสำคัญกว่า

**ควร copy โค้ดไหม?** พิมพ์ตัวอย่างเองได้ แต่ต้องทำนายผลก่อนรันและเปลี่ยนค่าเพื่อทดลอง

**ถ้าแก้โจทย์ไม่ได้ควรทำอย่างไร?** อ่านโจทย์แยก input/process/output ลองตัวอย่างเล็ก ๆ แล้วขอ hint ทีละระดับ

**เมื่อไรจึงควรเปิด solution?** หลังจากพยายามอย่างจริงจังและใช้ hint แล้วยังติด อ่านเพื่อเรียนรู้วิธีคิด ไม่ใช่เพื่อคัดลอกผ่าน

**ถ้าโค้ดให้ผลต่างกันแต่ดูถูกต้องล่ะ?** ตรวจ output ที่โจทย์กำหนด ชนิดข้อมูล ลำดับ และกรณีขอบ ถ้าพบข้อกำหนดกำกวม ให้จด input และผลที่คาดพร้อมเหตุผล

**ทำไม test ไม่ผ่าน?** อาจคำนวณผิด ลืมขอบเขต คืนค่าผิดชนิด พิมพ์ข้อความเพิ่ม หรือจัดรูปแบบไม่ตรง อ่านชื่อ test และ expected/actual

**รู้ได้อย่างไรว่าตนเข้าใจ Python?** อธิบายโค้ดได้ เขียนใหม่โดยไม่มองต้นฉบับ และปรับให้ทำงานในโจทย์บริบทใหม่ได้

**พร้อมเรียน NumPy เมื่อไร?** เมื่อเข้าใจ list, loop, function, การคำนวณพื้นฐาน และความหมายของข้อมูล NumPy เป็น optional dependency

**พร้อมเริ่ม Quant เมื่อไร?** หลังเขียนฟังก์ชันและจัดการข้อมูลได้ เข้าใจเปอร์เซ็นต์และสถิติพื้นฐาน จากนั้นค่อยศึกษาต้นทุนและความเสี่ยง

**ต้องเก่งคณิตศาสตร์ไหม?** เริ่มจากบวก ลบ คูณ หาร และเปอร์เซ็นต์ได้ ค่อยเรียนความหมายของสถิติพร้อมตัวอย่าง

**ใช้ AI ช่วยได้ไหม?** ใช้ถามคำถามและขอคำอธิบายได้ แต่ให้พิมพ์และตรวจคำตอบเอง อย่าเชื่อโค้ดที่สร้างให้จนกว่าจะอ่าน test และเข้าใจข้อสมมติ

**ถ้าติดนานควรทำอย่างไร?** ลดโจทย์เป็น input เล็กลง เขียนผลที่คาดด้วยมือ ใช้ debugger หรือพักแล้วกลับมาอ่าน traceback อีกครั้ง

## ดัชนีบทเรียนและเอกสาร

- [Level 1 — พื้นฐาน Python](lessons/level_01.md) และบทเรียนรายข้อใน [โฟลเดอร์ lessons](lessons/)
- [Level 2 — เงื่อนไขและลูป](lessons/level_02.md)
- [Level 3 — โครงสร้างข้อมูล](lessons/level_03.md)
- [Level 4 — ฟังก์ชันและโมดูล](lessons/level_04.md)
- [Level 5 — Python สำหรับงานจริง](lessons/level_05.md)
- [Level 6 — วิเคราะห์ข้อมูล](lessons/level_06.md)
- [Level 7 — คณิตศาสตร์และสถิติ](lessons/level_07.md)
- [Level 8 — การเงินและความเสี่ยง](lessons/level_08.md)
- [Level 9 — วิจัย Quant](lessons/level_09.md)
- [Level 10 — Paper bot ออฟไลน์](lessons/level_10.md)
- [คู่มือไวยากรณ์ Python](docs/python-syntax-handbook.md)
- [แผนที่หลักสูตร](docs/learning-roadmap.md)
- [วิธีแก้โจทย์](docs/how-to-solve-exercises.md)
- [ข้อผิดพลาดที่พบบ่อย](docs/common-python-errors.md)
- [Python เทียบกับ JavaScript/TypeScript](docs/python-vs-javascript.md)
- [คู่มือ Quant](docs/quant-learning-guide.md)
- [ชุดข้อมูลออฟไลน์](data/README.md)
- [โปรเจกต์จบ: บอท paper แบบออฟไลน์](projects/offline-paper-bot/README.md)

## คำสั่งระบบ

~~~powershell
python practice.py help
python practice.py start
python practice.py lesson [ID]
python practice.py open [ID]
python practice.py run [ID]
python practice.py check [ID]
python practice.py hint [ID [1-3]]
python practice.py solution [ID] [--yes]
python practice.py explain [ID] [--yes]
python practice.py next
python practice.py list
python practice.py status
python practice.py retry ID
~~~

run ทดลองกรณีแรก; check ตรวจทุกกรณีของข้อ; hint แสดงใบ้ระดับที่ระบุ; solution แสดงโค้ดอ้างอิง; explain แสดงเหตุผล; retry เริ่มทำข้อเดิมหรือ assessment variant ใหม่ตามความสามารถของข้อนั้น

## Dependencies และขอบเขตการใช้งาน

แบบฝึกหัดหลักใช้ Python standard library; <code>requirements.txt</code> ไม่ติดตั้งแพ็กเกจภายนอก ตัวอย่าง NumPy, pandas, Matplotlib และ Plotly เป็นส่วนเสริม และจะทำงานเมื่อแพ็กเกจนั้นอยู่ใน interpreter ที่เลือก หากต้องการติดตั้ง ให้ใช้ virtual environment <code>.venv</code> ของโครงการและคำสั่งนี้:

~~~powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-optional.txt
~~~

รายการเสริมมี NumPy, pandas, Matplotlib และ Plotly; vectorbt ไม่ได้รวมไว้และไม่จำเป็นกับหลักสูตรนี้ อย่ารันคำสั่งติดตั้งถ้าต้องการเรียนเฉพาะส่วน standard library

grader ใช้ subprocess และจำกัดเวลา แต่ไม่ได้เป็น sandbox ที่ปลอดภัยสำหรับรันโค้ดที่ไม่น่าเชื่อถือ ใช้ไฟล์นี้เพื่อเรียนในเครื่องของตนเอง ตรวจโค้ดก่อนรัน และอย่าใส่ credential หรือข้อมูลส่วนตัวลงในชุดฝึก
