def compare_oos(strategy_returns, benchmark_returns):
    if len(strategy_returns) != len(benchmark_returns):
        return None
    from math import prod
    strategy_net = prod(1 + value for value in strategy_returns) - 1
    benchmark_net = prod(1 + value for value in benchmark_returns) - 1
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
