# คู่มือไวยากรณ์ Python

คู่มือนี้เรียงจากพื้นฐานไปสู่งานข้อมูลและ Quant ตัวอย่างหลักใช้ Python 3 และ standard library จึงทดลองได้โดยไม่ติดตั้งแพ็กเกจเพิ่ม พิมพ์โค้ดในไฟล์ใหม่แล้วรันด้วย <code>python ชื่อไฟล์.py</code> บรรทัดที่ขึ้นต้นด้วยคำว่า “ผลลัพธ์” เป็นผลที่โปรแกรมแสดง ไม่ใช่โค้ด

## 1. คำสั่งและชนิดข้อมูลพื้นฐาน

### print() และ comments

ใช้ <code>print()</code> แสดงข้อความหรือค่า; ใช้ <code>#</code> เขียนหมายเหตุที่ Python ไม่รัน

~~~python
# แสดงข้อความทักทาย
print("สวัสดี Python")
print(2 + 3)
~~~
ผลลัพธ์:
~~~text
สวัสดี Python
5
~~~
พลาดบ่อย: ลืมเครื่องหมายคำพูดรอบข้อความ หรือใช้ print แทน return ในฟังก์ชันที่ต้องส่งค่ากลับ; JavaScript/TypeScript ใช้ console.log() และ //; ฝึก L01-E001–E006

### Variables และ type()

ตัวแปรเป็นชื่อที่อ้างถึงค่า ตั้งชื่อให้บอกความหมายและกำหนดค่าได้

~~~python
price = 100
print(type(price).__name__)
~~~
ผลลัพธ์: <code>int</code>; พลาดบ่อย: สับสน <code>=</code> (กำหนดค่า) กับ <code>==</code> (เปรียบเทียบ), หรือใช้ชื่อตัวแปรก่อนกำหนด; JS/TS มักประกาศด้วย let/const; ฝึก L01-E003, L01-E007

### int, float, str, bool และ None

ใช้ int สำหรับจำนวนเต็ม, float สำหรับทศนิยม, str สำหรับข้อความ, bool สำหรับจริง/เท็จ และ None แทนการไม่มีค่า

~~~python
quantity = int("3")
price = float("12.5")
label = str(quantity)
available = price > 0
missing = None
print(quantity, price, label, available, missing)
~~~
ผลลัพธ์: <code>3 12.5 3 True None</code>; พลาดบ่อย: <code>bool("False")</code> เป็น True เพราะข้อความไม่ว่าง; ตรวจ None ด้วย <code>value is None</code>; JS/TS ใช้ number, string, boolean และ null; ฝึก L01-E008–E015

### input() และการแปลงชนิด

<code>input()</code> คืน str เสมอ แปลงก่อนคำนวณ

~~~python
raw = "250"  # ในโปรแกรมจริงใช้ input("จำนวนเงิน: ")
amount = int(raw)
print(amount + 50)
~~~
ผลลัพธ์: <code>300</code>; พลาดบ่อย: บวกข้อความกับตัวเลขทำให้ TypeError; <code>int("2.5")</code> ทำให้ ValueError ให้ใช้ float เมื่อรับทศนิยม; ฝึก L01-E008–E011

### Arithmetic, comparison และ logical operators

เครื่องหมายคำนวณ ได้แก่ <code>+ - * / // % **</code>; เครื่องหมายเปรียบเทียบคือ <code>== != < <= > >=</code>; เงื่อนไขรวมใช้ <code>and</code>, <code>or</code>, <code>not</code>

~~~python
print(7 / 2, 7 // 2, 7 % 2, 2 ** 3)
amount = 120
print(amount >= 100 and amount < 500)
~~~
ผลลัพธ์: <code>3.5 3 1 8</code> แล้วตามด้วย <code>True</code>; พลาดบ่อย: / ให้ผลทศนิยม, หารศูนย์ไม่ได้, และ <code>//</code> ใน Python คือหารปัดลง (ใน JS เป็น comment); JS/TS ใช้ &&, ||, !; ฝึก Level 1–2

## 2. เงื่อนไขและการทำซ้ำ

### if, elif, else

ใช้เลือกการทำงานตามเงื่อนไข เครื่องหมาย <code>:</code> และการเยื้อง 4 ช่องเป็นส่วนหนึ่งของไวยากรณ์

~~~python
score = 78
if score >= 80:
    grade = "A"
elif score >= 50:
    grade = "ผ่าน"
else:
    grade = "ทบทวน"
print(grade)
~~~
ผลลัพธ์: <code>ผ่าน</code>; พลาดบ่อย: ลืม colon หรือเรียงเกณฑ์ผิด; JS/TS ใช้ปีกกา; ฝึก Level 2

### for, while และ range()

ใช้ for วนสมาชิกหรือช่วงที่รู้ขนาด; while ทำซ้ำตราบที่เงื่อนไขจริง; <code>range(stop)</code> ไม่รวมค่า stop

~~~python
total = 0
for number in range(1, 4):
    total += number
print(total)
~~~
ผลลัพธ์: <code>6</code>; พลาดบ่อย: คิดว่า range(1, 4) รวม 4 หรือทำ while ที่ไม่มีทางจบ; ฝึก Level 2

### break และ continue

<code>break</code> หยุดลูป; <code>continue</code> ข้ามไปเริ่มรอบถัดไป

~~~python
total = 0
for value in [3, 0, 5]:
    if value == 0:
        continue
    total += value
print(total)
~~~
ผลลัพธ์: <code>8</code>; พลาดบ่อย: ใช้ continue แล้วลืมอัปเดตเงื่อนไขใน while; JS/TS ใช้คำเดียวกัน; ฝึก Level 2

## 3. กลุ่มข้อมูลและการเลือกสมาชิก

### Lists, indexing และ slicing

list เก็บหลายค่าและแก้ไขได้ index เริ่มที่ 0; index -1 คือสมาชิกสุดท้าย; slicing เลือกช่วงโดยไม่รวมตำแหน่ง stop

~~~python
prices = [100, 105, 103, 110]
print(prices[0], prices[-1], prices[1:3], prices[:2])
~~~
ผลลัพธ์: <code>100 110 [105, 103] [100, 105]</code>; พลาดบ่อย: index เกินขนาดทำให้ IndexError และลืมว่า stop ไม่ถูกรวม; JS array ก็เริ่ม index 0 และมี slice(); ฝึก Level 3

### List methods

ใช้ <code>append()</code> เพิ่มหนึ่งค่า, <code>extend()</code> ต่อหลายค่า, <code>pop()</code> เอาค่าออก; <code>sorted()</code> สร้าง list ใหม่ที่เรียงแล้ว

~~~python
items = [2, 1]
items.append(3)
print(sorted(items))
~~~
ผลลัพธ์: <code>[1, 2, 3]</code>; พลาดบ่อย: <code>items.sort()</code> แก้ list เดิมและคืน None; JS ใช้ push() และ sort(); ฝึก Level 3

### Tuples และ sets

tuple เหมาะกับกลุ่มค่าที่ไม่ควรเปลี่ยน เช่น พิกัด; set เก็บสมาชิกไม่ซ้ำและตรวจการเป็นสมาชิกได้

~~~python
point = (2, 5)
symbols = set(["BTC", "ETH", "BTC"])
print(point[0], len(symbols), "BTC" in symbols)
~~~
ผลลัพธ์: <code>2 2 True</code>; พลาดบ่อย: set ไม่มีลำดับที่ควรพึ่งพา; JS มี array/object และ Set; ฝึก L03-E003, L03-E010

### Dictionaries และ methods

dict เก็บคู่ key/value เช่นข้อมูลสินค้า ใช้ <code>get()</code> เมื่อ key อาจไม่มี; <code>keys()</code> อ่าน key และ <code>items()</code> วน key/value

~~~python
item = {"sku": "A1", "price": 25}
print(item["price"], item.get("stock", 0))
~~~
ผลลัพธ์: <code>25 0</code>; พลาดบ่อย: เข้าถึง key ที่ไม่มีด้วย [] ทำให้ KeyError; JS object คล้ายกัน; ฝึก Level 3

### String methods และ list comprehension

string แก้ไขไม่ได้โดยตรง เมธอดจะคืนข้อความใหม่; comprehension สร้าง list จากกฎง่าย ๆ

~~~python
text = "  BTC,ETH  "
print(text.strip().lower().split(","))
positive = [value for value in [-1, 0, 3] if value > 0]
print(positive)
~~~
ผลลัพธ์: <code>['btc', 'eth']</code> แล้วตามด้วย <code>[3]</code>; พลาดบ่อย: ไม่เก็บค่าที่ strip() คืน หรือยัดเงื่อนไขซับซ้อนใน comprehension; JS มี trim()/map()/filter(); ฝึก Level 3 และ 5

## 4. ฟังก์ชันและการแยกโค้ด

### def, parameters, arguments และ return

def สร้างฟังก์ชัน; parameter คือชื่อตัวรับในนิยาม; argument คือค่าที่ส่งตอนเรียก; return ส่งผลกลับและจบฟังก์ชัน

~~~python
def line_total(price, quantity):
    return price * quantity
print(line_total(12, 3))
~~~
ผลลัพธ์: <code>36</code>; พลาดบ่อย: ใช้ print แทน return; JS/TS มี function parameters และ return; ฝึก Level 4

### Default arguments, scope และ function composition

ใช้ค่าเริ่มต้นเมื่อ argument เป็นตัวเลือก ชื่อที่สร้างในฟังก์ชันเป็น local scope โดยทั่วไปให้ส่งค่าที่ต้องใช้ผ่าน parameter

~~~python
def add_fee(amount, rate=0.02):
    return amount + amount * rate
print(add_fee(100))
~~~
ผลลัพธ์: <code>102.0</code>; อย่าใช้ list/dict ที่แก้ไขได้เป็น default; ประกอบฟังก์ชันโดยเรียกฟังก์ชันย่อยให้แต่ละส่วนทำหน้าที่เดียว; JS มี default parameters; ฝึก L04-E011

### Type hints และ lambda

type hint ช่วยคนอ่านและเครื่องมือวิเคราะห์เข้าใจสัญญา แต่ Python ไม่บังคับชนิดให้อัตโนมัติ; lambda ใช้กับฟังก์ชันสั้นที่ส่งเป็นค่า

~~~python
def double(value: float) -> float:
    return value * 2
rows = [("B", 3), ("A", 2)]
print(sorted(rows, key=lambda row: row[1]))
~~~
ผลลัพธ์: จากฟังก์ชันยังไม่มีจนกว่าจะเรียก; sort แสดง <code>[('A', 2), ('B', 3)]</code>; พลาดบ่อย: ซ่อน logic ยาวใน lambda; TS ตรวจชนิดเข้มกว่า; ฝึก Level 4

### import, modules และ packages

module คือไฟล์ Python ที่นำกลับมาใช้; package คือกลุ่ม modules; import ใช้โค้ดหรือไลบรารีที่มีอยู่

~~~python
import math
from statistics import mean
print(math.sqrt(9), mean([2, 4]))
~~~
ผลลัพธ์: <code>3.0 3</code>; พลาดบ่อย: ตั้งชื่อไฟล์ชนกับไลบรารี เช่น statistics.py; JS/TS ใช้ import/export; ฝึก Level 4–5

## 5. ไฟล์ ข้อยกเว้น และการทดสอบ

### try, except, else, finally และ raise

ใช้ try/except จัดการข้อผิดพลาดที่คาดไว้ จับ exception ให้เฉพาะเจาะจง; else ทำเมื่อไม่ผิด; finally ทำเสมอ; raise แจ้ง input ที่ผิดสัญญา

~~~python
def parse_quantity(text):
    try:
        value = int(text)
    except ValueError:
        raise ValueError("จำนวนต้องเป็นจำนวนเต็ม")
    else:
        return value
    finally:
        pass
print(parse_quantity("3"))
~~~
ผลลัพธ์: <code>3</code>; เรียกด้วย abc จะยก ValueError; พลาดบ่อย: ใช้ except เปล่าจนซ่อนบั๊ก; JS/TS ใช้ try/catch/finally; ฝึก Level 5

### with, open(), file reading และ writing

with open เปิดและปิดไฟล์อย่างปลอดภัย ระบุ encoding เพื่อให้ข้อความไทยไม่เสีย

~~~python
with open("note.txt", "w", encoding="utf-8") as file:
    file.write("เรียน Python\n")
with open("note.txt", encoding="utf-8") as file:
    print(file.read().strip())
~~~
ผลลัพธ์: <code>เรียน Python</code>; โค้ดสร้างไฟล์ note.txt ในโฟลเดอร์ทำงาน; พลาดบ่อย: path ผิดหรือเปิดโหมด w แล้วเขียนทับไฟล์เดิม; ฝึก Level 5

### CSV และ JSON

ใช้ csv กับข้อมูลตารางและ json กับ object/list ที่ซ้อนกัน อย่าแยก CSV ด้วย split(",") เพราะช่องข้อมูลอาจมี comma และ quote

~~~python
import csv
import io
rows = list(csv.DictReader(io.StringIO("sku,qty\nA1,2\n")))
print(rows[0]["sku"], int(rows[0]["qty"]))
~~~
ผลลัพธ์: <code>A1 2</code>; JSON อ่านด้วย json.loads(text) และเขียนด้วย json.dumps(data, ensure_ascii=False); พลาดบ่อย: ค่า CSV เป็น string จนกว่าจะ parse; ฝึก Level 5

### Assertions, unittest และ debugging

assert ยืนยันสมมติฐานในตัวอย่าง; unittest จัด test ที่รันซ้ำได้; ใช้ breakpoint หรือ print ชั่วคราวตรวจค่าระหว่างทาง

~~~python
import unittest
def total(price, quantity):
    return price * quantity
class TotalTests(unittest.TestCase):
    def test_two_items(self):
        self.assertEqual(total(5, 2), 10)
if __name__ == "__main__":
    unittest.main()
~~~
ผลลัพธ์เมื่อรัน: <code>Ran 1 test ... OK</code>; พลาดบ่อย: คาด expected จากโค้ดเดียวกับที่ทดสอบ หรือทดสอบแต่ค่าปกติ; JS ใช้ test frameworks เช่นกัน; ฝึก Level 5

## 6. Classes, objects และ environment

### Classes, objects และ constructors

class เป็นแบบของข้อมูลและพฤติกรรม; object คือค่าที่สร้างจาก class; <code>__init__</code> กำหนดสถานะเริ่มต้น

~~~python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
tea = Product("ชา", 20)
print(tea.name, tea.price)
~~~
ผลลัพธ์: <code>ชา 20</code>; พลาดบ่อย: ลืม self หรือสับสน class กับ instance; JS ใช้ class/constructor; ฝึก Level 5 และ 10

### Virtual environments และ pip

virtual environment แยกแพ็กเกจของโครงการจาก Python ส่วนกลาง สร้างใน PowerShell:

~~~powershell
python -m venv .venv
.\\.venv\\Scripts\\python.exe --version
.\\.venv\\Scripts\\python.exe -m pip --version
~~~
pip ติดตั้งแพ็กเกจเข้า interpreter ที่ระบุ รุ่นนี้ไม่ต้องติดตั้งแพ็กเกจเพื่อเรียนแบบฝึกหัดหลัก อย่ารันคำสั่งติดตั้งถ้ายังไม่ต้องใช้; Node ใช้ package managers และ node_modules ในอีกแบบ

## 7. ข้อมูล สถิติ และ Quant

### NumPy

NumPy เพิ่ม array และการคำนวณแบบ vectorized เหมาะกับตัวเลขจำนวนมาก เข้าใจสูตรก่อนใช้ array

~~~python
import numpy as np  # optional: ต้องติดตั้งก่อน
prices = np.array([100.0, 110.0])
print(prices / prices[0] - 1)
~~~
ผลลัพธ์เมื่อมี NumPy: <code>[0.  0.1]</code>; list กับ array มีพฤติกรรมคูณต่างกัน; optional และยังไม่จำเป็นกับ core course; ฝึก Level 6

### pandas: Series, DataFrame, filtering, grouping, missing values และ rolling

Series เป็นคอลัมน์; DataFrame เป็นตาราง; ใช้ read_csv, เลือกแถว, groupby, isna และ rolling เมื่อเหมาะสม

~~~python
import pandas as pd  # optional: ต้องติดตั้งก่อน
frame = pd.DataFrame({"team": ["A", "A", "B"], "sales": [2, 3, 5]})
print(frame.groupby("team")["sales"].sum().to_dict())
~~~
ผลลัพธ์เมื่อมี pandas: <code>{'A': 5, 'B': 5}</code>; พลาดบ่อย: ใช้ rolling แล้วไม่ตรวจว่าหน้าต่างมีข้อมูลครบหรือไม่; optional; ฝึก Level 6

### Matplotlib และ Plotly

Matplotlib ทำกราฟคงที่ในรายงาน; Plotly ทำกราฟโต้ตอบได้ กราฟไม่แก้ข้อมูลผิดและไม่พิสูจน์เหตุ/ผล

~~~python
import matplotlib.pyplot as plt  # optional: ต้องติดตั้งก่อน
plt.plot([1, 2, 3], [4, 2, 5])
plt.xlabel("วัน")
plt.ylabel("ยอดขาย")
plt.show()
~~~
ผลลัพธ์เมื่อมี Matplotlib: เปิดกราฟเส้น 3 จุด; optional; ฝึก Level 6

### Statistics, financial data และ backtesting

ค่าเฉลี่ยคือ sum(values)/len(values); ความแปรปรวนประชากรคือค่าเฉลี่ยของ (x - mean) กำลังสอง; ส่วนเบี่ยงเบนมาตรฐานคือรากที่สองของ variance; สหสัมพันธ์วัดการเคลื่อนที่ร่วมเชิงเส้นและไม่พิสูจน์สาเหตุ

ผลตอบแทนอย่างง่ายคือ next_price / price - 1 เมื่อราคาเริ่มมากกว่าศูนย์; log return ใช้ logarithm ของอัตราส่วนราคา OHLCV ต้องรักษาลำดับเวลาและข้อกำหนดราคา การ backtest ต้องคิด fee, slippage, funding และตรวจ look-ahead bias แยกข้อมูลพัฒนากับ out-of-sample และเทียบ benchmark ผลย้อนหลังไม่ยืนยัน edge หรือรับประกันผลในอนาคต

ข้อมูลในหลักสูตรเป็นข้อมูลสังเคราะห์ ไม่ใช้ราคาตลาดจริงและไม่เชื่อม exchange; ดู [คู่มือ Quant](quant-learning-guide.md); ฝึก Level 7–10

## อ่านต่อ

- [แผนที่หลักสูตร](learning-roadmap.md)
- [วิธีแก้โจทย์](how-to-solve-exercises.md)
- [ข้อผิดพลาดที่พบบ่อย](common-python-errors.md)
- [Python เทียบกับ JavaScript/TypeScript](python-vs-javascript.md)
- [คู่มือ Quant](quant-learning-guide.md)
