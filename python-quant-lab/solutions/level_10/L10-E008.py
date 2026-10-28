def market_event_symbol(event):
    return str(event.get("symbol") or "").strip().upper()
