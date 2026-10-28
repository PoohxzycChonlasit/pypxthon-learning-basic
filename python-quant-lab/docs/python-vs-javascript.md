# Python เทียบกับ JavaScript และ TypeScript

พื้นฐานการเขียนโปรแกรมจาก JavaScript/TypeScript ใช้ต่อได้ เช่น ตัวแปร เงื่อนไข ลูป ฟังก์ชัน และการแยกปัญหา จุดที่ต้องปรับคือรูปแบบไวยากรณ์และรายละเอียดของชนิดข้อมูล

| แนวคิด | Python | JavaScript/TypeScript |
|---|---|---|
| จบคำสั่ง | โดยมากใช้ขึ้นบรรทัดใหม่และเยื้องเพื่อบอกบล็อก | ใช้ `{}` บอกบล็อก มักใช้ `;` |
| ตัวแปร | `price = 100` ไม่ประกาศชนิดซ้ำ | `let price = 100`, `const price = 100` |
| บล็อกเงื่อนไข | `if price > 0:` แล้วเยื้องบรรทัดถัดไป | `if (price > 0) { ... }` |
| ฟังก์ชัน | `def total(price, count):` และ `return` | `function total(price, count) { return ... }` หรือ arrow function |
| Boolean | `True`, `False`, `None` | `true`, `false`, `null` |
| ไม่มีค่า | `None` | มักใช้ `null` หรือ `undefined` ซึ่งมีความหมายแยกกัน |
| list | `items = ["tea", "rice"]` | `const items = ["tea", "rice"]` |
| dict | `item["price"]` | object property เช่น `item.price` หรือ `item["price"]` |
| ความเท่ากัน | `==` เทียบค่า, `is` ตรวจ identity | `===` เทียบค่าและชนิดในหลายกรณี |
| การวน | `for item in items:` | `for (const item of items)` |
| ช่วงตัวเลข | `range(3)` ให้ 0, 1, 2 | ใช้ลูปแบบ index หรือ helper |
| string | `f"ยอด {total}"` | `` `ยอด ${total}` `` |
| การนำเข้า | `from math import sqrt` | `import { sqrt } from "..."` |
| ข้อยกเว้น | `try: ... except ValueError:` | `try { ... } catch (error) { ... }` |
| ค่าว่างในเงื่อนไข | มี truthiness แต่ควรตรวจชนิด/ความหมายตรง ๆ | มี truthiness เช่นกัน แต่ coercion ต่างกัน |

## ตัวอย่างเทียบรูปแบบ

Python:

~~~python
def final_price(price, discount):
    if price < 0 or discount < 0:
        raise ValueError("ค่าต้องไม่ติดลบ")
    return price * (1 - discount / 100)

print(final_price(200, 10))
~~~

ผลลัพธ์:

~~~text
180.0
~~~

รูปแบบใกล้เคียงใน TypeScript:

~~~typescript
function finalPrice(price: number, discount: number): number {
  if (price < 0 || discount < 0) {
    throw new Error("ค่าต้องไม่ติดลบ");
  }
  return price * (1 - discount / 100);
}

console.log(finalPrice(200, 10));
~~~

## จุดที่ควรระวังเมื่อย้ายภาษา

- Python ใช้การเยื้องเป็นส่วนหนึ่งของโครงสร้างโปรแกรม ถ้าเยื้องผิดโปรแกรมอาจไม่ทำงาน
- `input()` คืนข้อความเสมอ ต้องแปลงชนิดก่อนคำนวณ
- `and`, `or`, `not` ใช้แทน `&&`, `||`, `!`
- ใช้ `is None` เมื่อตรวจว่าไม่มีค่า ไม่ใช้ `== None`
- `list.sort()` แก้รายการเดิมและคืน `None`; `sorted(list)` สร้างรายการใหม่
- `dict` เป็น mapping สำหรับ key/value; JSON object มักแปลงเป็น dict
- Python ไม่มี `null`; ค่าไม่มีข้อมูลคือ `None`
- ชื่อตัวแปรแยกตัวพิมพ์เล็กใหญ่เหมือน JavaScript

ไม่ต้องท่องเทียบทุกคำสั่ง ให้ใช้แนวคิดเดิมแล้วดู handbook เมื่อต้องการไวยากรณ์ Python: [คู่มือไวยากรณ์](python-syntax-handbook.md)
