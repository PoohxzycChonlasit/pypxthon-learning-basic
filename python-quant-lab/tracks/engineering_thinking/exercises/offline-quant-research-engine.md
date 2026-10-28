# Exercise — Offline Quant Research Engine

## Do this before asking AI

ออกแบบ pipeline ทดลองกลยุทธ์จากข้อมูลสังเคราะห์ โดยไม่เชื่อมตลาดจริง:

1. เขียนสมมติฐานและเงื่อนไขที่ทำให้สมมติฐานผิด
2. กำหนด schema ของ time, price และ signal พร้อม validation
3. ระบุการเรียงเวลาและแบ่งช่วงพัฒนา/ทดสอบตามเวลา
4. เขียน pseudocode ที่ใช้เฉพาะข้อมูลที่ทราบ ณ เวลาของ signal
5. กำหนด benchmark, fee/slippage assumptions และผลตอบแทนสุทธิ
6. เลือก metrics และระบุข้อจำกัดของจำนวน observations
7. เขียน tests สำหรับราคาไม่ถูกต้อง, ข้อมูลไม่เรียง, ช่วงทดสอบว่าง,
   transaction costs และผลตอบแทนที่คำนวณจากมือ

## Architecture boundary

แยก load/validate, signal, portfolio calculation และ report ออกจากกัน
ข้อมูลทั้งหมดต้องเป็น local synthetic fixtures และการประเมินต้องทำซ้ำได้

## Bounded AI task

หลังเขียนกติกาและ pseudocode เอง ให้ agent เพิ่ม test สำหรับการแยกช่วงเวลา
ห้ามให้ agent เลือกพารามิเตอร์จากผล out-of-sample หรืออ้างว่า backtest
พิสูจน์ผลตอบแทนในอนาคต

## Review

ตรวจว่าไม่มี future data leakage, benchmark ใช้ช่วงเวลาเดียวกัน และต้นทุนที่
กำหนดถูกหักก่อนสรุปผล
