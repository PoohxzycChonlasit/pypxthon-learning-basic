# L09-E005 — เปรียบเทียบผล OOS กับ benchmark
# Level 9 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L09-E005
# macOS: python3.12 -B practice.py check L09-E005
# อ่านก่อนทำ: lessons/L09-E005.md

def compare_oos(strategy_returns, benchmark_returns):
    raise NotImplementedError("TODO: เทียบผล OOS")

if __name__ == "__main__":
    import json
    strategy = json.loads(input())
    benchmark = json.loads(input())
    result = compare_oos(strategy, benchmark)
    if result is None:
        print("INVALID")
    else:
        print(f"strategy={result['strategy_net']:.4f} benchmark={result['benchmark_net']:.4f} excess={result['excess']:.4f} beats={result['beats']}")
