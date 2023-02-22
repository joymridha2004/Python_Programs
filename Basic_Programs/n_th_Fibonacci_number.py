num = int(input("Enter integer: "))
a = 0
b = 1
if num < 0:
    print("Incorrect Number ")
elif num == 0:
    print(a)
elif num == 1:
    print(b)
else:
    for i in range(2, num):
        temp = a + b
        a = b
        b = temp
    print(b)
