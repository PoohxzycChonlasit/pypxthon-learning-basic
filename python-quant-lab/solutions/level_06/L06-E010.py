def compute_range(values):
    return max(v for v in values if v is not None)-min(v for v in values if v is not None) if any(v is not None for v in values) else None
