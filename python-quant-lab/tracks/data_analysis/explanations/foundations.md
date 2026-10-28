# คำอธิบาย — Data Analysis foundations

## DA01 — รู้จัก dataset และตรวจคุณภาพเบื้องต้น

แถวหนึ่งแทน record และ key เป็นคอลัมน์/field ที่บอก schema การนับ missing ต้องแยก `None` หรือข้อความว่างจากเลขศูนย์ ส่วน duplicate row คือ record ซ้ำทั้งแถว ไม่ใช่เพียง SKU ซ้ำ อัลกอริทึมคืออ่าน schema จากแถวแรก แล้วไล่ทุกแถวเพื่อสะสม missing cells และ marker ของแถวที่เคยพบ ข้อผิดพลาดที่พบบ่อยคือเปรียบเทียบ `dict` โดยตรงกับ set ซึ่งเก็บค่า hash ไม่ได้ หรือถือ 0 เป็น missing

## DA02 — อ่าน CSV ด้วย schema

`csv.DictReader` ผูกชื่อหัวตารางกับค่าของแต่ละแถวและจัดการ comma/quote ได้ ข้อมูลที่อ่านได้ยังเป็น string จึงค่อยแปลงตามกฎของงาน ระบุ `encoding="utf-8"` และ `newline=""` เพื่ออ่านไฟล์ไทยและ CSV อย่างถูกต้อง CSV มีโครงสร้างแบบแถว/คอลัมน์แต่ไม่มีชนิดข้อมูลบังคับ ข้อผิดพลาดที่พบบ่อยคือใช้ `split(",")` และทำให้ comma ภายใน quoted field กลายเป็นคอลัมน์ใหม่

## DA03 — JSON และ validation

JSON ใช้แทน list และ object ที่ซ้อนได้ `json.load()` อ่านไฟล์เป็นชนิดข้อมูล Python ต้องตรวจ outer shape และชนิดของแต่ละ record ก่อนใช้งาน ถ้ารูปแบบไม่ตรง schema ให้แจ้ง `ValueError` แทนการเดาค่า ข้อผิดพลาดที่พบบ่อยคือสมมติว่า object ทุกตัวมี key เดียวกันหรือวน dict โดยคิดว่าได้ value ทั้งแถว

## DA04 — SQLite

`sqlite3` อยู่ใน standard library จึง query ฐานข้อมูลออฟไลน์ได้โดยไม่ติดตั้ง package ตัวอย่างใช้ `substr(order_date, 1, 7)` จัดกลุ่มเป็นเดือน แล้ว `SUM(quantity * unit_price)` รวมยอด ผลต้อง sort ตามเดือนเพื่อให้เปรียบเทียบซ้ำได้ ตรวจ schema ก่อนรัน SQL และอย่าใช้ SQLite date grouping กับรูปแบบวันที่ที่ไม่สม่ำเสมอ

## DA05 — Clean และ quarantine

แถวรับเข้าได้เมื่อ ID ไม่ซ้ำ วันที่ parse ได้ quantity เป็นจำนวนเต็มบวก ราคาไม่ติดลบ และ discount อยู่ระหว่าง 0–1 ส่งแถวที่ไม่ผ่านไป `rejected` พร้อมเหตุผล แทนการลบทิ้งเงียบ ๆ ทำสำเนา record ก่อน normalize เพื่อไม่แก้ input ต้นฉบับ จุดพลาดคือบันทึก duplicate หลังแถว invalid อย่างไม่ชัดเจน และแปลง numeric ก่อนจับ `ValueError`


DA01: missing_cells includes None/empty values and absent values in columns from the first row.
DA02: reject missing, blank, or duplicate CSV header names before returning records.
DA05: unit prices must be finite and nonnegative; reject infinity as invalid input.
