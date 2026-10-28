# คำอธิบาย — pandas

## DA10 — Series และ missing values

Series เป็นคอลัมน์ที่มี index และ dtype `isna()` หา missing ส่วน `dropna()` ช่วยคำนวณเฉพาะข้อมูลที่มีค่า เลขศูนย์ยังเป็นข้อมูลจริง ถ้าทุกค่าหายไป mean/median ไม่มีคำตอบ จึงคืน `None` ตามข้อกำหนด จุดพลาดคือถือ `0` เป็น missing หรือคำนวณค่าเฉลี่ยของ Series ว่าง

## DA11 — สำรวจ DataFrame ก่อนสรุป

`read_csv()` สร้าง DataFrame; `head()` แสดงตัวอย่างแถว; `info()` สรุป schema และ non-null counts; `describe()` แสดงสถิติของตัวเลข ฟังก์ชัน `info()` พิมพ์ลง buffer และคืน `None` อย่าตัดสินใจจากชื่อไฟล์อย่างเดียว ให้ดู dtype และ missing counts ก่อน

## DA12 — loc, iloc, filter และ sort

`loc` เลือกด้วยเงื่อนไข label/boolean mask; `iloc` เลือกด้วยตำแหน่งจำนวนเต็ม คำนวณ revenue ต่อแถวก่อนกรอง แล้ว sort พร้อม tie-breaker ที่คงที่ จุดพลาดคือใช้ threshold แบบ strict ทั้งที่โจทย์ระบุ inclusive หรือคูณ string โดยยังไม่แปลงเป็นตัวเลข

## DA13 — ทำความสะอาดเหตุการณ์

อ่าน raw columns เป็น string และแปลงวันที่/ตัวเลขด้วย `errors="coerce"`; ค่าที่แปลงไม่ได้กลายเป็น missing เพื่อให้ตรวจได้ ตรวจ duplicate ID และข้อกำหนดช่วงค่าก่อนนำเข้า accepted list เก็บ rejected พร้อมเหตุผลที่ตรวจย้อนกลับได้ อย่าใช้ `dropna()` แล้วทิ้งแถวโดยไม่มีหลักฐาน

## DA14 — groupby และ merge

merge transactions กับ catalog ด้วย `product_id` แล้วตรวจว่า relationship เป็น many-to-one และไม่มี unmatched ID หลังจากนั้นคำนวณ gross revenue และ groupby category เพื่อรวมจำนวนรายการและรายได้ จุดพลาดคือ join ที่ทำให้แถว transaction เพิ่มขึ้นโดยไม่รู้ตัว จึงควรใช้ `validate=` และทดสอบจำนวนแถว

## DA15 — เวลา, resampling และ rolling

แปลง timestamp แล้วเรียงก่อนตั้งเป็น index `resample("D").last()` เพิ่มวันปฏิทินที่ไม่มี record โดยให้ close เป็น missing; `shift(1)` ใช้ close ก่อนหน้า และ `pct_change(fill_method=None)` ไม่เติมช่องว่างให้เอง rolling window ที่กำหนด `min_periods=window` ป้องกันค่าเฉลี่ยจากหน้าต่างไม่ครบ จุดพลาดสำคัญคือ forward-fill ราคาโดยไม่กำหนดความหมาย หรือใช้ข้อมูลอนาคต

## DA16 — แบ่ง train/test ตามเวลา

เรียงตาม timestamp แล้วแบ่งด้วยจุดตัดเดียวกันทุกครั้ง training ต้องอยู่ก่อน test ทั้งชุด ห้ามสุ่มแถวเพราะจะเปิดทางให้อนาคตรั่วเข้า train ตรวจ timestamp สูงสุดของ train เทียบกับต่ำสุดของ test ก่อนส่งผล

## DA17 — Exploratory Data Analysis

เริ่มด้วย describe และ quality counts จากนั้นดู distribution, category mean และ trend ตามเดือน IQR ใช้ Q1−1.5×IQR และ Q3+1.5×IQR เพื่อ flag ค่าที่ควรตรวจ ไม่ได้ยืนยันว่าเป็นข้อมูลเสีย correlation บอกความสัมพันธ์เชิงเส้น ไม่ได้พิสูจน์สาเหตุ

## DA22 — Export

`to_csv(index=False, encoding="utf-8")` เขียนตารางโดยไม่เพิ่ม index เป็นคอลัมน์ซ้ำ อ่านไฟล์กลับเพื่อตรวจ schema และจำนวนแถว ถ้าสร้าง report ในโปรแกรม ให้เขียนลง path ที่ระบุและอย่าแก้ไฟล์ input


DA13: quarantine non-finite numeric values alongside missing, unparseable and negative values.
