list1 = [12, 14, 26, 85, 56, 86, 2, 96]
for i in range(len(list1) // 2):
    font = i;
    back = len(list1) - i - 1;
    list1[font], list1[back] = list1[back], list1[font]
print(list1)
