def sum_at_or_below_limit(values, limit):
    # TODO: วน values และคืนผลรวมที่ผ่านเงื่อนไข
    raise NotImplementedError("เติมลูป")

if __name__ == "__main__":
    limit = int(input())
    values = [int(value) for value in input().split()]
    print(sum_at_or_below_limit(values, limit))
