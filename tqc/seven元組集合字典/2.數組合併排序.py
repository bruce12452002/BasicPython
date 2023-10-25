"""
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）
將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列

輸入與輸出會交雜如下，輸出的部份以粗體字表示
**Create tuple1:**
9
0
-1
3
8
-9999

**Create tuple2:**
28
16
39
56
78
88
-9999

Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
"""
my_list1 = []
my_list2 = []

i = 0
while i < 2:
    print(f"Create tuple{i + 1}:")
    n = int(input('請輸入整數:'))

    if n == -9999:
        if i == 1:
            break
        i += 1
        continue

    if i == 0:
        my_list1.append(n)
    if i == 1:
        my_list2.append(n)

my_list1.extend(my_list2)
print("Combined tuple before sorting:{}".format(tuple(my_list1)))
my_list1.sort()
print("Combined list after sorting:{}".format(my_list1))
