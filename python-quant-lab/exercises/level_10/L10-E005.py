def paper_step(state, event, max_order_value, fee_rate):
    raise NotImplementedError("TODO: validate then update paper state")

if __name__ == "__main__":
    import json
    payload = json.loads(input())
    result = paper_step(payload["state"], payload["event"], payload["max_order_value"], payload["fee_rate"])
    print(f"accepted={result['accepted']} cash={result['cash']:.2f} units={result['units']:.2f} live_trading={result['live_trading']}")
