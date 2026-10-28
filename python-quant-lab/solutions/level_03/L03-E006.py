def frequency_table(items):
    return {x:items.count(x) for x in set(items)}
