# Exercise — Offline Paper Trading Bot

## Do this before asking AI

ออกแบบตัวจำลองคำสั่งซื้อขายที่รับ event ในไฟล์และไม่ส่งคำสั่งออกนอกเครื่อง:

1. กำหนด fields ของ event และ state: cash, position และ event history
2. นิยามกติกา accept/reject สำหรับ side, quantity, price และเงิน/position
3. เขียน pseudocode ให้ validation เสร็จก่อนเปลี่ยน state
4. ระบุ invariants: cash และ position ไม่ติดลบ; rejected event ไม่เปลี่ยนยอด
5. ออกแบบ event log ที่ทำซ้ำและตรวจย้อนหลังได้
6. เขียน tests สำหรับ buy ผ่าน, sell เกิน position, ราคาไม่ถูกต้อง,
   event ซ้ำ และ input ที่ไม่ใช่ dict
7. วาง implementation เป็น validate → calculate → apply → log

## Hard boundary

ใช้เฉพาะ input และ output ใน local test ไม่มี exchange/broker API, socket,
wallet, private key, signing หรือ live order ใด ๆ

## Bounded AI task

ให้ agent implement เฉพาะ pure function ที่ตรวจ event และคืนผลตาม contract
ห้ามให้ agent เพิ่ม network, credentials หรือ side effects

## Review

ตรวจ diff, ทดสอบ state หลัง event ที่ถูกปฏิเสธ และคำนวณ expected result ด้วย
มือก่อนรัน test ห้ามตีความผล paper ว่าเป็นผลการเทรดจริง
