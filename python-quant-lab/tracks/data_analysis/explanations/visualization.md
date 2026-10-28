# คำอธิบาย — Visualization

## DA18 — เลือกกราฟตามคำถาม

เส้นเหมาะกับการเปลี่ยนตามเวลา; แท่งใช้เปรียบเทียบ category; histogram แสดง distribution ของตัวเลข; scatter แสดงค่าคู่สองตัวแปร ก่อน plot ให้ aggregate ที่ระดับเดียวกันและใส่ชื่อแกนพร้อมหน่วย การทดสอบควรตรวจ x/y data และ labels ของ Matplotlib axes แทนเทียบ pixel เพราะ font และ backend เปลี่ยนภาพได้

## DA19 — OHLCV และ artifact

กราฟนี้ใช้ close line และช่วง low–high พร้อม volume เพื่อให้อ่านราคาและกิจกรรมในเวลาเดียวกัน ตรวจ OHLCV invariants, timestamp order, uniqueness และ volume ก่อนวาด สร้างไฟล์รูปใน temp directory แล้วตรวจว่ามีข้อมูล/label และไฟล์ไม่ว่าง ห้ามเรียกชุดข้อมูลนี้ว่าราคาตลาดจริง

## DA23 — Plotly (ส่วนเสริม)

Plotly สร้าง Figure แบบโต้ตอบและเขียน HTML ที่เปิดใน browser ได้ aggregate sessions กับ conversions ตามวัน/ช่องทางก่อนหาร เพื่อหลีกเลี่ยงค่า conversion แบบเฉลี่ยของค่าเฉลี่ย ตรวจชื่อ trace, ค่า, ชื่อแกนและ artifact ที่บันทึก เส้นทางนี้เป็น optional เพราะ Plotly ต้องติดตั้งแยกใน `.venv`


DA19: reject NaN and infinite OHLCV values before drawing; comparisons alone do not detect them.
