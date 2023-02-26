list1 = [12, 14, 26, 85, 56]
MAX = list1[0]
for i in range(len(list1)):
    if MAX < list1[i]:
        MAX = list1[i]
print(MAX)
