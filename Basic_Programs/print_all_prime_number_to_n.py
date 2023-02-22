num = int(input("Enter integer: "))
i = 0
for j in range(2, num + 1):
    count = 0
    for i in range(1, j + 1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(j, " ", end='')
