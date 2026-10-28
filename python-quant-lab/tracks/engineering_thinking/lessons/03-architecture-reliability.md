# 03 — Architecture, Implementation Planning and Reliability

สถาปัตยกรรมเริ่มจากการกำหนดขอบเขตงาน ไม่จำเป็นต้องเริ่มจาก framework
แยกขั้นตอนที่มีเหตุผลต่างกัน แล้วระบุข้อมูลที่แต่ละขั้นรับและส่ง

## Type along: CSV pipeline

```python
raw_rows = ["sku,quantity", "A1,2", "B2,not-a-number"]
header, *rows = raw_rows
print(header, len(rows))
```

สำหรับ CSV analyzer ให้คิดเป็น pipeline: อ่านไฟล์ → ตรวจ header → แยกแถว
ที่ใช้ได้และแถวเสีย → คำนวณสรุป → เขียนรายงาน ตรวจว่าขั้นอ่านไม่แก้ข้อมูล
ต้นฉบับ และผลลัพธ์เรียงลำดับคงที่เพื่อให้รันซ้ำแล้วได้ผลเดิม

## Implementation plan

1. กำหนดรูปแบบ CSV และคอลัมน์ที่ต้องมี
2. สร้าง fixture เล็กที่มีแถวปกติ แถวซ้ำ และแถวผิดรูปแบบ
3. เขียน parser และ validation แยกจากการสรุปผล
4. เขียน summary หลังจากข้อมูลผ่าน validation
5. เพิ่ม output ที่บอกจำนวนแถวรับเข้าและแถวปฏิเสธ

ในแต่ละขั้นระบุ acceptance test ก่อนเริ่ม implementation หากข้อกำหนดด้าน
ความน่าเชื่อถือยังไม่ชัด เช่น จะทำอย่างไรเมื่อไฟล์ว่าง ให้บันทึกเป็นคำถาม

ทำ [CSV data analyzer](../exercises/csv-data-analyzer.md) และวาดเส้นทาง
ข้อมูลตั้งแต่ไฟล์เข้าจนถึงรายงาน
