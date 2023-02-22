num = int(input("Enter integer: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num, " is prime number")
else:
    print(num, " is not prime number")
