num = int(input("Enter integer: "))
for i in range(1, num + 1):
    print("*", end='')
    obj = 0
    if i == 1 or i == num:
        obj = 1
    for j in range(1, num - 1):
        if obj == 1:
            print("*", end='')
        else:
            print(" ", end='')
    print("*")
