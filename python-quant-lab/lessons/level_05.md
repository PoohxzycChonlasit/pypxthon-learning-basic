# Level 5 — Python สำหรับงานจริง

**เป้าหมาย:** อ่านไฟล์ แปลงข้อมูล ตรวจ input ที่ผิด และรายงานปัญหาอย่างควบคุมได้

## พิมพ์ตาม: อ่านและตรวจ CSV ในหน่วยความจำ

### ขั้นที่ 1 — แนวคิด

CSV เก็บข้อมูลเป็นแถวและคอลัมน์ ค่าที่อ่านจาก CSV เป็นข้อความ จึงต้องแปลงชนิดและตรวจแต่ละแถวก่อนใช้ csv module จัดการ quote และ comma ได้ปลอดภัยกว่า split

### ขั้นที่ 2–3 — พิมพ์ตัวอย่างนี้

~~~python
import csv
import io

source = "sku,quantity\nA1,3\nB2,not-a-number\n"
rows = csv.DictReader(io.StringIO(source))
valid = []
rejected = 0

for row in rows:
    try:
        quantity = int(row["quantity"])
    except ValueError:
        rejected = rejected + 1
        continue
    valid.append((row["sku"], quantity))

print(valid)
print(rejected)
~~~

### ขั้นที่ 4 — อ่านทีละส่วน

- csv.DictReader คืนแต่ละแถวเป็น dict
- int แปลงจำนวนจากข้อความ
- try/except จับเฉพาะแถวที่จำนวนไม่ถูกต้อง
- continue ข้ามแถวเสียโดยไม่หยุดประมวลผลไฟล์

### ขั้นที่ 5 — ผลลัพธ์ที่คาด

~~~text
[('A1', 3)]
1
~~~

### ขั้นที่ 6–7 — ทดลองเปลี่ยน

เปลี่ยนค่า not-a-number เป็น 4 แถวที่ถูกต้องจะเพิ่มขึ้นหนึ่งและ rejected จะเป็น 0

### ขั้นที่ 8 — ลองเอง

เพิ่มคอลัมน์ price แล้วตรวจว่าค่าเป็นตัวเลขบวก ก่อนนำไปรายงาน กรณีไฟล์จริงให้เปิดด้วย with open(path, encoding="utf-8", newline="") as file

**แนวคิดของระดับนี้:** ใช้ json สำหรับข้อมูลแบบ object/list, raise เมื่อฟังก์ชันรับค่าที่ไม่ตรงสัญญา และเขียน unittest ครอบคลุมข้อมูลปกติกับข้อมูลเสีย
