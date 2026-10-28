"""โครงเริ่มโปรเจกต์ paper bot: เติม TODO โดยคงการทำงานออฟไลน์เท่านั้น."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "synthetic_btc_ohlcv.csv"
STARTING_CASH = 100.0
MAX_ORDER_VALUE = 25.0
MAX_UNITS = 0.2
FEE_RATE = 0.001


def load_bars(path):
    """อ่าน CSV และคืน list ของ OHLCV dictionaries; ปฏิเสธข้อมูลผิดรูปแบบ."""
    raise NotImplementedError("TODO: อ่าน header, แปลงชนิด และตรวจ invariant ของข้อมูล")


def signal_for(closes, index, window=2):
    """คืน buy/sell/hold โดยใช้ข้อมูลที่เกิดก่อน index เท่านั้น."""
    raise NotImplementedError("TODO: คำนวณค่าอ้างอิงจาก closes ก่อน index")


def run_paper_bot(bars):
    """จำลองคำสั่งในหน่วยความจำ คืน report พร้อม event log."""
    raise NotImplementedError("TODO: ใช้เงินสดจำลอง บังคับ risk limits และรวม fee")


if __name__ == "__main__":
    bars = load_bars(DATA_FILE)
    report = run_paper_bot(bars)
    print(report)
