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
