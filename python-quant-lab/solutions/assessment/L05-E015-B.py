def final_parsing_assessment(text):
    region, item, quantity = [part.strip() for part in text.strip().split("-")]
    return {"region": region.upper(), "item": item.lower(), "quantity": int(quantity)}
