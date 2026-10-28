# Level 10 — วิศวกรรม paper bot ออฟไลน์

**เป้าหมาย:** ตรวจ event และจำลองการเปลี่ยนสถานะบัญชีแบบออฟไลน์

**ทำไมสำคัญ:** การตรวจ input ก่อนเปลี่ยนสถานะช่วยให้ event ที่ถูกปฏิเสธไม่ทำให้บัญชีเสียความสอดคล้อง

**ก่อนเริ่ม:** ทบทวนฟังก์ชัน การจัดการไฟล์ สถิติ และต้นทุนจาก Levels 4–9

**แนวคิดหลัก:** event และ state · validation ก่อน mutation · บัญชี paper · การบันทึกและ replay · ขีดจำกัดความเสี่ยง

## ตัวอย่างสั้นที่ทำตามได้

ตัวอย่างนี้ใช้ข้อมูลคนละชุดกับแบบฝึกหัด ให้ทำนายผลก่อนอ่านบรรทัดผลลัพธ์

~~~python
event = {"side": "buy", "quantity": 2}
if event["quantity"] > 0:
    print("รับ event สำหรับการจำลอง")
~~~

**อ่านทีละขั้น:**
1. event เก็บ field แบบมีชื่อ
2. เงื่อนไขตรวจ quantity ก่อนทำงานต่อ
3. ไม่มีการเชื่อมต่อ broker หรือส่งคำสั่งจริง

ผลของตัวอย่าง:

~~~text
รับ event สำหรับการจำลอง
~~~

## แบบฝึกหัดทั้ง 15 ข้อ

ทำตามลำดับที่แสดง; แต่ละแถวพาไปยังบทเรียนรายข้อและไฟล์ส่งคำตอบจริง

1. [L10-E001 — ตรวจคำสั่ง paper](L10-E001.md) — function · Tier 1 · True เมื่อ event เป็น dict, side ถูกต้อง, quantity/price finite และบวก, cash finite ไม่ติดลบ; buy ต้องไม่เกิน cash — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E001.py)
2. [L10-E002 — ทำนายบัญชีเงินสดหลังซื้อแบบ paper](L10-E002.md) — text_answer · Tier 1 · คำนวณ notional, fee และเงินสดโดยไม่ส่งคำสั่งจริง — [ไฟล์ส่งคำตอบ](../answers/level_10/L10-E002.txt)
3. [L10-E003 — เติม validator ของ paper order](L10-E003.md) — stdout · Tier 3 · ตรวจ side, ราคา, จำนวน, เงินสด และ notional limit ก่อนรับคำสั่ง — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E003.py)
4. [L10-E004 — แก้ validator OHLC ที่ตรวจไม่ครบ](L10-E004.md) — stdout · Tier 2 · ตรวจ high/low เทียบกับ open/close และ volume — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E004.py)
5. [L10-E005 — จำลอง paper buy/sell พร้อม accounting invariant](L10-E005.md) — stdout · Tier 2 · ปรับ state จำลองโดยบังคับเงินสด จำนวนหน่วย fee และ notional cap — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E005.py)
6. [L10-E006 — หยุดเมื่อเงินถึงขีดจำกัด](L10-E006.md) — function · Tier 2 · คืน True เมื่อ cash <= risk_floor; ถ้าไม่มี floor ให้ใช้ 0 — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E006.py)
7. [L10-E007 — มูลค่าสถานะ paper](L10-E007.md) — function · Tier 2 · คืน quantity*price โดย field ที่หายใช้ 0 — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E007.py)
8. [L10-E008 — ปรับรูปแบบสัญลักษณ์ตลาด](L10-E008.md) — function · Tier 2 · คืน symbol แบบ string ที่ตัดช่องว่างแล้วทำ uppercase — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E008.py)
9. [L10-E009 — ใช้ค่าธรรมเนียมเริ่มต้น](L10-E009.md) — function · Tier 3 · คืน fee หากเป็น finite number >=0 และไม่ใช่ bool; มิฉะนั้น 0.0 — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E009.py)
10. [L10-E010 — บันทึกผลคำสั่ง](L10-E010.md) — function · Tier 2 · คืน dict ที่มี id จาก event, status="paper", live=False — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E010.py)
11. [L10-E011 — ปรับปรุงจำนวนสถานะ](L10-E011.md) — function · Tier 3 · buy คืน +quantity; sell คืน -quantity; side อื่นหรือ quantity ไม่ถูกต้องคืน 0 — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E011.py)
12. [L10-E012 — หยุดเมื่อขาดทุนรายวันถึงขีดจำกัด](L10-E012.md) — function · Tier 4 · คืน True เมื่อ day_pnl <= -abs(loss_limit) — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E012.py)
13. [L10-E013 — กู้คืนยอดเงินสด](L10-E013.md) — function · Tier 2 · คืน cash ถ้าเป็น finite number >=0 มิฉะนั้นคืน 100.0 — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E013.py)
14. [L10-E014 — บันทึกเหตุการณ์แบบมีโครงสร้าง](L10-E014.md) — function · Tier 2 · คืน dict event=id, side=side, paper_only=True — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E014.py)
15. [L10-E015 — ประเมินบอทออฟไลน์](L10-E015.md) — function · Tier 5 · ตรวจ event จำลองและคำนวณ state ใหม่ตาม prompt ของ variant ที่เลือก โดยทำงาน offline — [ไฟล์ส่งคำตอบ](../exercises/level_10/L10-E015.py)

## วิธีเรียนและเกณฑ์จบระดับ

1. เปิดบทเรียนรายข้อ อ่านตัวอย่าง แล้วแก้เฉพาะไฟล์ส่งคำตอบที่ลิงก์ไว้
2. ใช้ Run ทดลอง และใช้ Check ตรวจทุกกรณี; โจทย์ text_answer ให้พิมพ์ผลที่ทำนายลง .txt แล้ว Check โดยไม่รันไฟล์ Python
3. ทำ L10-E015 ตาม prompt ที่ระบบเลือก; อ่านบทเรียนของข้อนั้นก่อนเริ่ม
4. ดูสถานะด้วย py -3.12 -B practice.py list --level 10 และ py -3.12 -B practice.py status

ผ่านแบบฝึกหัดเมื่อ Check ผ่านกรณีทั้งหมด. สถานะที่ใช้ hint หรือ solution จะแยกจากการผ่านด้วยตนเอง

ก่อนหน้า: [Level 9 overview](level_09.md)
นี่คือระดับสุดท้ายของหลักสูตร; ทบทวนข้อที่ต้องการหรือเลือกเส้นทางเสริมใน tracks/

## ตัวอย่างฝึกระดับเพิ่มเติม

เนื้อหาฝึกเดิมของระดับนี้ยังคงไว้เพื่อใช้ทบทวน

**เป้าหมาย:** เชื่อมข้อมูลกับกฎจำลองและรักษาบัญชีให้สอดคล้อง โดยไม่ส่งคำสั่งเงินจริง

## พิมพ์ตาม: ตรวจความเสี่ยงก่อนจำลองการซื้อ

### ขั้นที่ 1 — แนวคิด

ระบบจำลองควรปฏิเสธราคาหรือจำนวนที่ไม่ถูกต้อง ตรวจวงเงินก่อนลดเงินสด และคงกฎเดียวกันทุกครั้งที่ replay ข้อมูล

### ขั้นที่ 2–3 — พิมพ์ตัวอย่างนี้

~~~python
def simulate_buy(cash, quantity, price, max_order_value):
    if quantity <= 0 or price <= 0:
        return cash, "rejected: invalid size or price"

    order_value = quantity * price
    if order_value > max_order_value or order_value > cash:
        return cash, "rejected: risk limit"

    cash_after = cash - order_value
    return cash_after, "paper order accepted"

cash, status = simulate_buy(100.0, 2, 10.0, 25.0)
print(cash)
print(status)
~~~

### ขั้นที่ 4 — อ่านทีละส่วน

- ตรวจข้อมูลก่อนคำนวณ
- order_value เป็นมูลค่าจำลองของคำสั่ง
- เงื่อนไขจำกัดมูลค่าต่อรายการและเงินสด
- ฟังก์ชันคืนเงินสดใหม่และสถานะ โดยไม่เชื่อมต่อบริการภายนอก

### ขั้นที่ 5 — ผลลัพธ์ที่คาด

~~~text
80.0
paper order accepted
~~~

### ขั้นที่ 6–7 — ทดลองเปลี่ยน

ลด max_order_value เป็น 15 คำสั่งต้องถูกปฏิเสธและ cash คงเป็น 100

### ขั้นที่ 8 — ลองเอง

ออกแบบการบันทึก order id เพื่อไม่ให้ replay เดิมนับคำสั่งซ้ำ เพิ่ม log ที่อธิบายการปฏิเสธ และทดสอบว่า cash + มูลค่าสินทรัพย์ตรงกับมูลค่าพอร์ตตามสูตรที่กำหนด

**โปรเจกต์จบ:** [ข้อกำหนดบอท paper ออฟไลน์](../projects/offline-paper-bot/README.md) ใช้ข้อมูลสังเคราะห์จาก data/ ทดสอบซ้ำได้ และห้ามเพิ่ม live exchange/API
