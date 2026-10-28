# ชุดข้อมูลสังเคราะห์สำหรับฝึกออฟไลน์

ไฟล์ทั้งหมดเป็นข้อมูลสังเคราะห์ที่สร้างในเครื่อง ไม่มีข้อมูลลูกค้าจริง ไม่มีราคาตลาดจริง และไม่มีการเชื่อมต่อ exchange ชื่อ `synthetic_` หมายถึงตัวเลขจำลองเท่านั้น

## ชุดข้อมูลที่มี

| ไฟล์ | แถวข้อมูล | ใช้ฝึก |
|---|---:|---|
| `sales.csv` | 6 | CSV เริ่มต้นและยอดขายต่อสินค้า |
| `customers.csv` | 6 | อ่าน segment และ region |
| `inventory.csv` | 4 | สต็อกและระดับสั่งซื้อซ้ำ |
| `expenses.csv` | 5 | จัดกลุ่มค่าใช้จ่าย |
| `employee_hours.csv` | 4 | ชั่วโมงทำงานและค่าแรงตัวอย่าง |
| `website_traffic.csv` | 6 | conversion rate แบบเริ่มต้น |
| `paper_trades.csv` | 4 | ผลเทรดจำลองหลังค่าธรรมเนียม |
| `synthetic_btc_ohlcv.csv` | 8 | อ่าน schema OHLCV ขนาดเล็ก |
| `synthetic_eth_ohlcv.csv` | 8 | อ่าน schema OHLCV ขนาดเล็ก |
| `ecommerce_transactions.csv` | 1,200 | รายได้ สินค้า ส่วนลด segment และการจัดกลุ่ม |
| `ecommerce_transactions_dirty.csv` | 66 | missing, duplicate, วันที่และตัวเลขผิดรูปแบบ, ค่าติดลบ และส่วนลดเกินช่วง |
| `customer_segments.csv` | 400 | segment, region, orders และ distribution ของมูลค่าลูกค้า |
| `inventory_movements.csv` | 800 | movement ตามวัน, SKU และผลรวมสต็อก |
| `employee_time_records.csv` | 260 | ชั่วโมงทำงานและการคำนวณค่าแรงตามกฎตัวอย่าง |
| `website_sessions.csv` | 1,825 | visits, conversions, ช่องทาง และแนวโน้มรายวัน |
| `monthly_business_expenses.csv` | 240 | รายจ่ายแยกเดือน หมวด และหน่วยงาน |
| `synthetic_btc_ohlcv_daily.csv` | 727 | OHLCV หลายวันสำหรับ returns, volatility และกราฟราคา |
| `synthetic_eth_ohlcv_daily.csv` | 727 | OHLCV สังเคราะห์แยกชุดและมีช่องว่างในวันที่ |
| `synthetic_paper_trades.csv` | 500 | trade log จำลองสำหรับ fee และสรุปผล paper |

## สร้างซ้ำ

ตัวสร้างใช้ `random.Random` กับ seed คงที่และ standard library เท่านั้น ไม่อ่านอินเทอร์เน็ต ไม่ติดตั้งแพ็กเกจ ให้เปิด PowerShell ที่โฟลเดอร์ `python-quant-lab/` แล้วรัน:

~~~powershell
python -B data\generate_synthetic_datasets.py
~~~

การทดสอบตรวจว่าการสร้างสองครั้งให้ไฟล์เหมือนกันทุก byte ตรวจจำนวนแถว และตรวจข้อกำหนด OHLCV

## การใช้ชุดสะอาดและชุดมีปัญหา

ใช้ `ecommerce_transactions.csv` เป็นตัวอย่างที่ควรผ่าน schema และกฎพื้นฐาน ส่วน `ecommerce_transactions_dirty.csv` ตั้งใจใส่ duplicate, missing value, วันที่ผิด, จำนวนที่แปลงไม่ได้, quantity ติดลบ และ discount เกิน 100% เพื่อฝึกแยกแถวที่รับได้กับแถวที่ปฏิเสธ อย่านำไฟล์ dirty ไปใช้แทนไฟล์ clean ในงานสรุปผลที่สมมติว่าข้อมูลผ่านการตรวจแล้ว

ข้อมูลการเงินแยกเป็นชุดสะอาดเสมอ ค่า open/high/low/close เป็นบวก, volume ไม่ติดลบ, timestamp ไม่ซ้ำและเรียงจากเก่าไปใหม่ ทุกแถวเป็นจริงว่า `high >= max(open, close)` และ `low <= min(open, close)` ช่องว่างบางวันเป็นข้อมูลเวลาที่ตั้งใจให้ฝึก resampling; ไม่ได้เพิ่มแถวราคาที่ผิดกฎ

## เส้นทาง Data Analysis

เริ่มจาก [Data Analysis Practice Track](../tracks/data_analysis/README.md) หลังผ่านพื้นฐาน Level 5 ชุดฝึกใช้ NumPy, pandas และ Matplotlib ใน virtual environment ของโครงการเมื่อได้รับอนุมัติการติดตั้ง รายงานแถวที่ถูกปฏิเสธและเหตุผลแทนการลบข้อมูลเงียบ ๆ
