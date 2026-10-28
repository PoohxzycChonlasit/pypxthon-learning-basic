income = float(input())
housing = float(input())
food = float(input())
other = float(input())
expenses = housing + food + other
remaining = income - expenses
print(f"Expenses: {expenses:.2f}")
print(f"Remaining: {remaining:.2f}")
