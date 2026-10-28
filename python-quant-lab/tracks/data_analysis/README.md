# Data Analysis Practice Track

เส้นทางเสริมนี้ต่อจาก Level 5 มี 23 งานใน **6 ไฟล์โจทย์ร่วมกัน**. เริ่มจาก [DA01](lessons/DA01.md) และเปิดหน้าบทเรียนของข้อที่จะทำก่อนแก้ไฟล์ module

ข้อมูลการเงินและตลาดทั้งหมดเป็นข้อมูลสังเคราะห์สำหรับฝึกออฟไลน์ ไม่มีการเชื่อมต่อ exchange, wallet, broker หรือคำสั่งซื้อขายจริง

## วิธีทำงาน

1. เปิดโฟลเดอร์ <code>python-quant-lab</code> ใน VS Code และเปิด integrated Terminal
2. เปิดบทเรียนตามรหัสในดัชนีด้านล่าง
3. เปิดไฟล์โจทย์ที่บทเรียนระบุ แล้วค้นหา function name; แต่ละ module มีหลายข้อ ให้แก้เฉพาะฟังก์ชันของรหัสนั้น
4. บันทึกไฟล์ แล้วรัน grader ของข้อจาก project root
5. อ่าน test ที่ไม่ผ่าน แก้สาเหตุ และตรวจซ้ำ

Windows PowerShell — เมื่อ Terminal อยู่ที่ project root:

~~~powershell
py -3.12 --version
py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_foundations.py -k DA01 -v
~~~

macOS Terminal ใช้ <code>python3.12</code> แทน <code>py -3.12</code>. <code>-k DA01</code> เลือกเฉพาะ test ที่มีรหัส DA01; เอา <code>-k DA01</code> ออกถ้าต้องการรันทั้งไฟล์ grader. Grader ใช้ input ชั่วคราวและไม่แก้ submission/progress ของ core course.

## ไฟล์โจทย์ที่ใช้ร่วมกัน

| Python module | ข้อ | แนวคิด | Package ที่ต้องมีอยู่แล้ว |
|---|---|---|---|
| <code>foundations.py</code> | DA01–DA05 | Standard library: list/dict, CSV, JSON, SQLite และ validation | Python 3.12 standard library |
| <code>numpy_practice.py</code> | DA06–DA09 | NumPy: array shape, indexing, broadcasting และสถิติ | NumPy |
| <code>pandas_practice.py</code> | DA10–DA17 และ DA22 | pandas/NumPy: Series, CSV/DataFrame, cleaning, joins, time series, EDA และ export | pandas + NumPy |
| <code>visualization.py</code> | DA18–DA19 | Matplotlib/pandas: charts และ OHLCV validation | Matplotlib + pandas |
| <code>capstone.py</code> | DA20–DA21 | pandas/NumPy: business KPI และ offline financial metrics | pandas + NumPy |
| <code>plotly_extension.py</code> | DA23 | Plotly/pandas: optional interactive chart | Plotly + pandas |


DA01–DA05 ใช้ standard library จึงเริ่มได้ทันที. DA06 ขึ้นไปต้องมี package ตามตารางใน interpreter ที่เลือกอยู่แล้ว. ถ้ายังไม่มี ให้ทำ standard-library group ก่อน; อย่าติดตั้ง dependency ผ่านคู่มือนี้. DA23 เป็นส่วนเสริมและข้ามได้.

## ดัชนี DA01–DA23

- [DA01 — สำรวจโครงสร้างและคุณภาพ dataset](lessons/DA01.md) · <code>tracks/data_analysis/exercises/foundations.py</code> → <code>dataset_profile()</code>
- [DA02 — อ่าน CSV และตรวจชื่อหัวคอลัมน์](lessons/DA02.md) · <code>tracks/data_analysis/exercises/foundations.py</code> → <code>load_csv_records()</code>
- [DA03 — อ่าน JSON และตรวจรูปแบบข้อมูล](lessons/DA03.md) · <code>tracks/data_analysis/exercises/foundations.py</code> → <code>load_json_records()</code>
- [DA04 — รวมรายได้รายเดือนจาก SQLite](lessons/DA04.md) · <code>tracks/data_analysis/exercises/foundations.py</code> → <code>monthly_revenue()</code>
- [DA05 — ตรวจธุรกรรมและเก็บเหตุผลรายการที่ปฏิเสธ](lessons/DA05.md) · <code>tracks/data_analysis/exercises/foundations.py</code> → <code>clean_transaction_rows()</code>
- [DA06 — สร้าง NumPy array ชนิด float](lessons/DA06.md) · <code>tracks/data_analysis/exercises/numpy_practice.py</code> → <code>make_price_array()</code>
- [DA07 — เลือกคอลัมน์ close ด้วย index และ slice](lessons/DA07.md) · <code>tracks/data_analysis/exercises/numpy_practice.py</code> → <code>select_close_window()</code>
- [DA08 — คูณแต่ละคอลัมน์ด้วยน้ำหนัก](lessons/DA08.md) · <code>tracks/data_analysis/exercises/numpy_practice.py</code> → <code>apply_column_weights()</code>
- [DA09 — สรุปสถิติตัวเลขด้วย NumPy](lessons/DA09.md) · <code>tracks/data_analysis/exercises/numpy_practice.py</code> → <code>numeric_summary()</code>
- [DA10 — นับ missing และสรุป pandas Series](lessons/DA10.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>series_profile()</code>
- [DA11 — สำรวจ CSV ด้วย read_csv, head, info, describe](lessons/DA11.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>csv_overview()</code>
- [DA12 — กรองและเรียงยอดขายด้วย loc และ iloc](lessons/DA12.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>filter_sort_sales()</code>
- [DA13 — ทำความสะอาดเหตุการณ์และแยกแถวผิด](lessons/DA13.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>clean_event_csv()</code>
- [DA14 — รวมยอดตามหมวดด้วย groupby และ merge](lessons/DA14.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>sales_by_category()</code>
- [DA15 — สร้าง daily series, lag, return และ rolling mean](lessons/DA15.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>daily_price_features()</code>
- [DA16 — แบ่ง train/test ตามเวลาโดยไม่สลับแถว](lessons/DA16.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>time_based_split()</code>
- [DA17 — ทำ EDA และแยกข้อสังเกตจากข้อสรุป](lessons/DA17.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>eda_summary()</code>
- [DA18 — เลือกกราฟให้ตรงคำถามธุรกิจ](lessons/DA18.md) · <code>tracks/data_analysis/exercises/visualization.py</code> → <code>business_charts()</code>
- [DA19 — วาด OHLCV สังเคราะห์พร้อมตรวจข้อมูล](lessons/DA19.md) · <code>tracks/data_analysis/exercises/visualization.py</code> → <code>ohlcv_chart()</code>
- [DA20 — สรุป KPI จากธุรกรรม ผู้เข้าชม และสต็อก](lessons/DA20.md) · <code>tracks/data_analysis/exercises/capstone.py</code> → <code>business_kpis()</code>
- [DA21 — คำนวณ returns, fees และ drawdown แบบออฟไลน์](lessons/DA21.md) · <code>tracks/data_analysis/exercises/capstone.py</code> → <code>financial_metrics()</code>
- [DA22 — ส่งออก DataFrame เป็น CSV แล้วอ่านกลับ](lessons/DA22.md) · <code>tracks/data_analysis/exercises/pandas_practice.py</code> → <code>export_analysis()</code>
- [DA23 — สร้างกราฟ conversion แบบโต้ตอบ (ส่วนเสริม)](lessons/DA23.md) · <code>tracks/data_analysis/exercises/plotly_extension.py</code> → <code>interactive_conversion_chart()</code>


## ข้อมูลฝึกและการตรวจ

ดู [คู่มือชุดข้อมูลสังเคราะห์](../../data/README.md) สำหรับ CSV ที่ใช้ฝึกเอง. Grader บางข้อสร้างไฟล์ input สั้น ๆ ใน temporary directory เพื่อทดสอบ schema และกรณีขอบ; รายละเอียดจริงอยู่ในหน้าบทเรียนแต่ละข้อ. ถ้ายังเห็น <code>raise NotImplementedError</code> grader จะไม่ผ่านจนกว่าจะทำฟังก์ชัน.

| กลุ่ม | Windows PowerShell — project root |
|---|---|
| DA01–DA05 | <code>py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_foundations.py -v</code> |
| DA06–DA17, DA22 | <code>py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_numpy_pandas.py -v</code> |
| DA18–DA19 | <code>py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_visualization.py -v</code> |
| DA20–DA21 | <code>py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_capstone.py -v</code> |
| DA23 optional | <code>py -3.12 -B -m unittest discover -s tracks/data_analysis/tests -p grade_plotly_optional.py -v</code> |

Financial examples are offline education only; no grader places orders or contacts an external service.
