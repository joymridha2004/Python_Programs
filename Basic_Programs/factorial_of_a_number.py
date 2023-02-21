num = int(input("Enter integer : "))
fact = int(1)
for i in range(1, num + 1):
    fact *= i
print(num, "factorial is: ", fact)
