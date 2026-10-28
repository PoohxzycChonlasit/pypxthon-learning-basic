# Level 8 — การเงินและความเสี่ยง

**เป้าหมาย:** คำนวณผลตอบแทนหลังต้นทุน และตรวจความเสี่ยงก่อนตีความกำไร

**ทำไมสำคัญ:** ส่วนต่างราคาขั้นต้นไม่รวมค่าธรรมเนียมหรือความเสี่ยงของขนาดสถานะ

**ก่อนเริ่ม:** ทบทวนสถิติและการจัดการข้อมูลตามเวลาใน Level 7

**แนวคิดหลัก:** ผลตอบแทน gross/net · ค่าธรรมเนียม · ขนาดสถานะและ exposure · drawdown

## ตัวอย่างสั้นที่ทำตามได้

ตัวอย่างนี้ใช้ข้อมูลคนละชุดกับแบบฝึกหัด ให้ทำนายผลก่อนอ่านบรรทัดผลลัพธ์

~~~python
entry = 100.0
exit_price = 108.0
quantity = 2
fee_rate = 0.001
gross = (exit_price - entry) * quantity
fees = (entry + exit_price) * quantity * fee_rate
net = gross - fees
print(round(net, 3))
~~~

**อ่านทีละขั้น:**
1. คำนวณส่วนต่างราคาแล้วคูณจำนวน
2. คิด fee จากมูลค่าตอนเข้าและออก
3. หัก fee ออกจาก gross เพื่อได้ net

ผลของตัวอย่าง:

~~~text
15.584
~~~

## แบบฝึกหัดทั้ง 15 ข้อ

ทำตามลำดับที่แสดง; แต่ละแถวพาไปยังบทเรียนรายข้อและไฟล์ส่งคำตอบจริง

1. [L08-E001 — กำไรขั้นต้นสถานะซื้อ](L08-E001.md) — function · Tier 1 · gross profit = (exit-entry)*quantity; quantity ไม่ติดลบ — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E001.py)
2. [L08-E002 — ทำนายกำไรสุทธิหลังค่าธรรมเนียม](L08-E002.md) — text_answer · Tier 1 · แยก gross profit, fee และ net profit — [ไฟล์ส่งคำตอบ](../answers/level_08/L08-E002.txt)
3. [L08-E003 — เติมการคำนวณขนาดสถานะจากวงเงินเสี่ยง](L08-E003.md) — stdout · Tier 3 · แปลง risk budget เป็นจำนวนหน่วยโดยหารระยะ stop — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E003.py)
4. [L08-E004 — แก้สูตรที่บวก fee เข้ากำไร](L08-E004.md) — stdout · Tier 2 · ตรวจเครื่องหมายของต้นทุนและผลเมื่อราคาไม่เปลี่ยน — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E004.py)
5. [L08-E005 — ตรวจ exposure รวมของพอร์ตจำลอง](L08-E005.md) — stdout · Tier 2 · รวมมูลค่าสถานะและเทียบกับสัดส่วนเพดานของ equity — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E005.py)
6. [L08-E006 — กำไรสุทธิหลังค่าธรรมเนียม](L08-E006.md) — function · Tier 2 · net = (exit-entry)*quantity - (entry+exit)*quantity*0.001 — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E006.py)
7. [L08-E007 — กำไรขั้นต้นสถานะขายชอร์ต](L08-E007.md) — function · Tier 2 · gross profit = (entry-exit)*quantity — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E007.py)
8. [L08-E008 — ปรับราคาขายด้วย slippage](L08-E008.md) — function · Tier 2 · รับ exit_price และ slippage_rate; คืน exit_price*(1-slippage_rate) — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E008.py)
9. [L08-E009 — ระยะความเสี่ยง](L08-E009.md) — function · Tier 2 · total risk = abs(entry-stop)*quantity — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E009.py)
10. [L08-E010 — อัตราผลตอบแทนต่อความเสี่ยง](L08-E010.md) — function · Tier 4 · ratio = abs(target-entry)/abs(entry-stop); ถ้า stop distance เป็น 0 คืน None — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E010.py)
11. [L08-E011 — เงินคงเหลือ paper หลังเทรด](L08-E011.md) — function · Tier 4 · equity = 100 + gross long profit - round-trip fee — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E011.py)
12. [L08-E012 — สัดส่วนเงินที่เปิดรับความเสี่ยง](L08-E012.md) — function · Tier 2 · fraction = price*quantity/equity; คืน None เมื่อ equity เป็น 0 — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E012.py)
13. [L08-E013 — สัดส่วนการลดลง](L08-E013.md) — function · Tier 3 · คืน max(0,(peak-current)/peak); หาก peak ไม่บวกคืน 0 — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E013.py)
14. [L08-E014 — จำนวนหน่วยตามระยะขาดทุน](L08-E014.md) — function · Tier 3 · quantity = risk_budget/abs(entry-stop); ถ้าระยะเป็น 0 คืน 0 — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E014.py)
15. [L08-E015 — ประเมินความเสี่ยง paper](L08-E015.md) — function · Tier 5 · คำนวณผลตอบแทนและผลลัพธ์ด้านความเสี่ยงตาม prompt ของ variant ที่เลือก — [ไฟล์ส่งคำตอบ](../exercises/level_08/L08-E015.py)

## วิธีเรียนและเกณฑ์จบระดับ

1. เปิดบทเรียนรายข้อ อ่านตัวอย่าง แล้วแก้เฉพาะไฟล์ส่งคำตอบที่ลิงก์ไว้
2. ใช้ Run ทดลอง และใช้ Check ตรวจทุกกรณี; โจทย์ text_answer ให้พิมพ์ผลที่ทำนายลง .txt แล้ว Check โดยไม่รันไฟล์ Python
3. ทำ L08-E015 ตาม prompt ที่ระบบเลือก; อ่านบทเรียนของข้อนั้นก่อนเริ่ม
4. ดูสถานะด้วย py -3.12 -B practice.py list --level 8 และ py -3.12 -B practice.py status

ผ่านแบบฝึกหัดเมื่อ Check ผ่านกรณีทั้งหมด. สถานะที่ใช้ hint หรือ solution จะแยกจากการผ่านด้วยตนเอง

ก่อนหน้า: [Level 7 overview](level_07.md)
ถัดไป: [Level 9 overview](level_09.md)

## ตัวอย่างฝึกเพิ่มเติม

**เป้าหมาย:** คำนวณผลตอบแทนสุทธิและประเมินความเสี่ยงก่อนดูผลกำไรขั้นต้น

## พิมพ์ตาม: คิดกำไร paper trade หลัง fee

### ขั้นที่ 1 — แนวคิด

ราคาออกสูงกว่าราคาเข้าไม่ได้แปลว่ากำไรสุทธิเท่ากับส่วนต่างทั้งหมด ต้องคิดจำนวนหน่วยและ fee ทั้งตอนเข้าและออก

### ขั้นที่ 2–3 — พิมพ์ตัวอย่างนี้

~~~python
entry = 100.0
exit_price = 108.0
quantity = 2
fee_rate = 0.001

gross = (exit_price - entry) * quantity
fees = (entry + exit_price) * quantity * fee_rate
net = gross - fees
print(round(gross, 3))
print(round(fees, 3))
print(round(net, 3))
~~~

### ขั้นที่ 4 — อ่านทีละส่วน

- gross คือส่วนต่างราคาคูณจำนวน
- fee คิดทั้งมูลค่าซื้อและขาย
- net คือผลหลังหักต้นทุน
- ข้อมูลทั้งหมดเป็นตัวเลขตัวอย่าง ไม่ส่งคำสั่งตลาดจริง

### ขั้นที่ 5 — ผลลัพธ์ที่คาด

~~~text
16.0
0.416
15.584
~~~

### ขั้นที่ 6–7 — ทดลองเปลี่ยน

เพิ่ม fee_rate เป็น 0.002 ค่า fee จะเพิ่มเป็นสองเท่าและกำไร net ลดลง แต่ gross คงเดิม

### ขั้นที่ 8 — ลองเอง

คำนวณผลสุทธิเมื่อ exit_price ต่ำกว่า entry และตรวจว่าค่าธรรมเนียมยังลดผลลัพธ์ลงอีก วางเพดานขาดทุนก่อนทดลองเพิ่มขนาดสถานะ

**แนวคิดของระดับนี้:** drawdown วัดการลดลงจากจุดสูงสุด; exposure บอกมูลค่าที่เสี่ยงอยู่; Sharpe และ profit factor สรุปผลบางส่วนแต่ไม่รับประกันอนาคต
