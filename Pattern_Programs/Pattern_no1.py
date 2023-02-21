name = str(input("Enter your name: "))
line = int(input("Enter number of line: "))
count = int(line - 2)
for i in range(1, line + 1):
    blank = 0
    Object = 0

    # ------------Find blank space-----------------

    if i < int(line / 2 + 1):
        blank = int((line / 2 + 1) - i)
    elif i > int(line / 2 + 1):
        blank = int(i - (line / 2))

    # ------------print blank space-----------------

    if i != int(line / 2 + 1):
        for j in range(1, int(blank + 1)):
            print("   ", end='')

    # ------------object number count-----------------

    if i < int(line / 2 + 1):
        Object = i * 2 - 1
    elif i > int(line / 2) + 1:
        Object = count
        count = count - 2
    elif i == int(line / 2 + 1):
        Object = line

    # ------------print object number-----------------

    for j in range(1, Object + 1):
        if j % 2 != 0 and i != int(line / 2 + 1):
            print("\\*/", end='')
        elif j % 2 == 0 and i != int(line / 2 + 1):
            print("/#\\", end='')
        elif j == int(line / 2 + 1) and i == int(line / 2 + 1):
            print(name[0:4], end='')
        elif j != int(line / 2 + 1) and i == int(line / 2 + 1):
            print("|#|", end='')

    # ------------print next line-----------------

    print()
