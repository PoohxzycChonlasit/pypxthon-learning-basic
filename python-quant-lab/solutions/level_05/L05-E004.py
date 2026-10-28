import csv

def csv_field_count(line):
    return len(next(csv.reader([line])))

if __name__ == "__main__":
    line = input()
    print(csv_field_count(line))
