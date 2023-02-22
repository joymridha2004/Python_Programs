num = int(input("Enter integer: "))
temp = num
sum = 0
while temp != 0:
    armstrong = temp % 10
    armstrong = armstrong ** 3
    sum += armstrong
    temp = temp // 10
if num == sum:
    print("Yes")
else:
    print("No")
