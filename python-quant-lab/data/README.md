# ชุดข้อมูลฝึกออฟไลน์

ไฟล์ทั้งหมดในโฟลเดอร์นี้เป็นข้อมูลสังเคราะห์ที่สร้างขึ้นเพื่อการเรียน ไม่มีชื่อ ที่อยู่ เบอร์โทร หรือข้อมูลลูกค้าจริง และไม่มีราคาตลาดจริง วันที่เป็นวันตัวอย่างเพื่อฝึกเรียงเวลา ไม่ใช่การอ้างอิงเหตุการณ์ในตลาด

| ไฟล์ | คอลัมน์หลัก | ใช้ฝึก |
|---|---|---|
| sales.csv | order_id, date, product, quantity, unit_price | รวมยอดขาย แยกสินค้า และตรวจ CSV |
| customers.csv | customer_id, segment, region, orders | จัดกลุ่มและนับระเบียนสังเคราะห์ |
| inventory.csv | sku, product, quantity, reorder_level, unit_cost | แจ้งเตือนสต็อกและคำนวณมูลค่า |
| expenses.csv | date, category, amount, note | รวมค่าใช้จ่ายและตรวจข้อมูล |
| employee_hours.csv | employee_id, date, hours, hourly_rate | คำนวณชั่วโมงและค่าแรงตัวอย่าง |
| website_traffic.csv | date, visits, signups | คำนวณ conversion rate และดูแนวโน้ม |
| synthetic_btc_ohlcv.csv | timestamp, open, high, low, close, volume | ฝึกตรวจ OHLCV และคำนวณผลตอบแทนบนข้อมูลสังเคราะห์ |
| synthetic_eth_ohlcv.csv | timestamp, open, high, low, close, volume | ฝึกเหมือนกันโดยมีชุดข้อมูลแยก |
| paper_trades.csv | trade_id, side, entry, exit, quantity, fee_rate | คำนวณกำไรขาดทุนจำลองหลัง fee |

## กติกาข้อมูล OHLCV

ชื่อไฟล์ขึ้นต้นด้วย synthetic เพื่อย้ำว่าไม่ใช่ประวัติราคาจริง เวลาเรียงจากเก่าไปใหม่; ทุกแถวมีราคาเป็นบวกและ volume ไม่ติดลบ; ต้องเป็นจริงว่า high >= max(open, close), low <= min(open, close) และ low <= high อย่าใช้ข้อมูลจากแถวอนาคตคำนวณสัญญาณของแถวก่อนหน้า

## วิธีเปิด

รันคำสั่งจากโฟลเดอร์รากของโครงการ แล้วใช้ path เช่น data/sales.csv เปิดไฟล์ด้วย encoding UTF-8 และ newline="" เมื่อใช้ csv module เพื่อจัดการบรรทัดและ quote อย่างถูกต้อง
