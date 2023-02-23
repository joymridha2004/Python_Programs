num = int(input("Enter integer: "))
a = 0
b = 1
flag = 0
if num == 0:
    print("Yes")
elif num == 1:
    print("Yes")
else:
    for i in range(num + 3):
        temp = a + b
        a = b
        b = temp
        if b == num:
            print("Yes")
            flag = 1
            break
if flag == 0:
    print("No")
