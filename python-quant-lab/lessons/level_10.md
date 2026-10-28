# Level 10 — วิศวกรรม paper bot ออฟไลน์

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
