def two_item_moving_averages(items):
    return [(a+b)/2 for a,b in zip(items,items[1:])]
