# Exercise — CSV Data Analyzer

## Do this before asking AI

วางแผนเครื่องมือ offline ที่อ่าน CSV ยอดขายและสรุปยอดตามสินค้า:

1. ระบุ encoding, delimiter, header และ columns ที่ต้องมี
2. กำหนด data model หลัง parse และชนิดข้อมูลของแต่ละ field
3. ตัดสินว่าแถวผิดรูปแบบจะถูก reject พร้อมเหตุผลอย่างไร
4. เขียน pseudocode ตั้งแต่เปิดไฟล์จนถึง summary และ error report
5. วาด boundary ระหว่าง read, validate, summarize และ report
6. เขียน tests สำหรับไฟล์ว่าง, header ซ้ำ, จำนวนคอลัมน์ไม่ตรง, ราคาเสีย
   และไฟล์ที่ถูกต้อง
7. ระบุวิธีทำให้ผลเรียงลำดับเดิมเมื่อรันซ้ำ
8. วางแผน Git checkpoint: branch ที่จะใช้, ไฟล์ที่เปลี่ยน และ commit ที่
   แยก parser ออกจาก report

## Implementation plan

ให้แต่ละงานแก้ได้และตรวจได้แยกกัน: parser → validator → summary → report
เริ่มจาก fixture ขนาดเล็กก่อนใช้ dataset จริง

## Bounded AI task

ให้ agent เพิ่ม parser เฉพาะรูปแบบที่กำหนดไว้ ห้ามเพิ่ม dependency, เปลี่ยน
รูปแบบ input, ลบแถวเสียเงียบ ๆ หรือแตะไฟล์อื่นนอกขอบเขต

## Review

ตรวจ diff และกรณี rejected row ด้วยตนเอง รัน tests แล้วเทียบผลกับค่าที่
คำนวณมือจาก fixture เล็ก
