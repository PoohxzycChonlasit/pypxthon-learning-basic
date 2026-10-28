def compare_oos(strategy_returns, benchmark_returns):
    if len(strategy_returns) != len(benchmark_returns):
        return None
    strategy_net = sum(strategy_returns)
    benchmark_net = sum(benchmark_returns)
    excess = strategy_net - benchmark_net
    return {"strategy_net": strategy_net, "benchmark_net": benchmark_net, "excess": excess, "beats": excess > 0}

if __name__ == "__main__":
    import json
    strategy = json.loads(input())
    benchmark = json.loads(input())
    result = compare_oos(strategy, benchmark)
    if result is None:
        print("INVALID")
    else:
        print(f"strategy={result['strategy_net']:.4f} benchmark={result['benchmark_net']:.4f} excess={result['excess']:.4f} beats={result['beats']}")
