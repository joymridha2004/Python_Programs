def rotation(list, length, rotation):
    for j in range(rotation):
        temp = list[0]
        for i in range(0, length - 1):
            list[i] = list[i + 1]
        list[length - 1] = temp


list1 = [1, 2, 3, 4, 5, 6, 7]
rotation(list1, len(list1), 2)
print(list1)
