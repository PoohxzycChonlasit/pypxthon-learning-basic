# คำอธิบาย — NumPy

## DA06 — Array และ dtype

`ndarray` เก็บตัวเลขให้มีรูปร่างและ dtype ชัดเจน `np.asarray(..., dtype=float)` ทำให้ค่าจำนวนเต็มและทศนิยมใช้กฎเดียวกัน รูปร่าง `(n,)` หมายถึงหนึ่งมิติ ยอมรับ array ว่างที่มี shape `(0,)` แต่ปฏิเสธ input หลายมิติ งานจริงควรตรวจ dtype และ shape ก่อนทำ arithmetic เพราะการคูณ list ของ Python ไม่เท่ากับการคูณ array

## DA07 — Indexing และ slicing

คอลัมน์ OHLC คือ open/high/low/close จึงอยู่ index 3 เมื่อเริ่ม index ที่ศูนย์ `matrix[start:stop, 3]` เลือกช่วงแถวแบบไม่รวม stop คืนสำเนาเพื่อลด side effect กับข้อมูลต้นฉบับ ตรวจ start/stop และจำนวนคอลัมน์ก่อนเลือก จุดพลาดคือคิดว่า stop รวมอยู่ในผล หรือเลือกคอลัมน์ high แทน close

## DA08 — Vectorization และ broadcasting

เมื่อ matrix มี shape `(จำนวนแถว, จำนวนคอลัมน์)` และ weight มีความยาวเท่าจำนวนคอลัมน์ NumPy ขยาย weight ให้แต่ละแถวได้โดยไม่เขียน loop การตรวจ shape ทำให้ error เข้าใจง่าย ผลควรเป็น array ใหม่และมีค่าเดิมคูณ weight ประจำคอลัมน์ อย่าใช้ `.T` โดยเดา เพราะทำให้มิติกลับด้าน

## DA09 — Aggregation และสถิติ

sum, mean, min และ max สรุปข้อมูลหนึ่งมิติ ส่วน `np.std(ddof=0)` คือ population standard deviation ตามข้อกำหนดนี้ หากใช้ `ddof=1` จะเป็น sample estimate และได้ค่าไม่เท่ากัน ตรวจ input ว่าง, NaN และ infinity ก่อนสรุป ค่าทางสถิติช่วยอธิบายชุดข้อมูล แต่ไม่บอกสาเหตุของการเปลี่ยนแปลง
