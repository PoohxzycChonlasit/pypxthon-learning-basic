raw = input().strip()
values = [] if not raw else [None if x == "NA" else float(x) for x in raw.split(",")]
# BUG: every missing observation is replaced with zero.
clean = [0 if value is None else value for value in values]
print(clean)
