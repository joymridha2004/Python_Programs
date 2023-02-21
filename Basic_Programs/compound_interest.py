p = float(input("Enter the principal amount: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate: "))
a = p * (1 + (r / 100)) ** t
print("Simple interest: ", a - p)
