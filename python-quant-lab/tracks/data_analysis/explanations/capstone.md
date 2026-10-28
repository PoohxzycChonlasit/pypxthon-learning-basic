# คำอธิบาย — Applied analysis

## DA20 — Business KPI

รายได้สุทธิต่อ transaction คือ quantity × unit price × (1 − discount rate) รวม conversions แล้วหารด้วย sessions เพื่อได้ conversion rate; ถ้าไม่มี sessions ให้รายงานว่าไม่มีตัวหารแทนการหารศูนย์ สรุป revenue ตาม segment และ net inventory movement ตาม SKU ตรวจความหมายของแต่ละแถวก่อนรวมและอย่าตีความ correlation เป็นสาเหตุ

## DA21 — ผลตอบแทนและความเสี่ยงแบบออฟไลน์

simple return จากราคา `i` ถึง `i+1` คือ next/current − 1; log return คือ log(next/current) สัญญาณของช่วงนั้นคูณผลตอบแทน แล้วหักค่าธรรมเนียมตาม exposure สร้าง equity ด้วย cumulative product และ drawdown เทียบกับ running peak ตัวอย่างนี้จำลองเท่านั้น ไม่ส่ง order และไม่บอกว่ากลยุทธ์ทำกำไรได้จริง จุดพลาดคือเหลื่อมตำแหน่ง signal/return หรือคิดต้นทุนเป็นเปอร์เซ็นต์โดยไม่ระบุฐาน
