# Exercise — E-commerce Order Processor

## Do this before asking AI

ออกแบบตัวประมวลผลคำสั่งซื้อแบบ in-memory โดยยังไม่เขียน implementation:

1. กำหนด fields ของสินค้าและ order
2. ระบุสัญญาของราคา จำนวนสินค้า สต็อก และยอดรวม
3. เขียน pseudocode สำหรับตรวจทุกบรรทัดก่อนเปลี่ยนสต็อก
4. เลือกว่า order ที่มีสินค้าหนึ่งรายการไม่พอจะ reject ทั้ง order หรือไม่
   แล้วบันทึกเหตุผลของการเลือก
5. เขียน acceptance tests สำหรับ order ว่าง, SKU ไม่รู้จัก, quantity ศูนย์,
   stock ไม่พอ และ order ที่ผ่าน
6. วางแผนแยก validation, calculation และ state update เป็นขั้น

## Constraints

ไม่ทำ payment gateway, database, network calls หรือ retry framework ให้คง
พฤติกรรม offline และกำหนด state change หลัง validation เท่านั้น

## Bounded AI task

หลังเขียน contract และ test cases เองแล้ว ให้ agent implement เฉพาะฟังก์ชัน
คำนวณยอดจากรายการที่ผ่าน validation ห้ามแก้ schema หรือ state transition

## Review

ตรวจ diff, ทดลองอย่างน้อยหนึ่งกรณีที่ reject และยืนยันว่า stock ไม่เปลี่ยน
เมื่อ order ถูกปฏิเสธ
