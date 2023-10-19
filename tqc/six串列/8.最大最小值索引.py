"""
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），
接著輸出矩陣最大值與最小值的索引

範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
"""
outer_list = []
maxi = 0
mini = 0
flag = True
r = 3
c = 3
for row in range(r):
    inner_list = []
    for column in range(c):
        n = int(input())
        if flag:
            maxi, mini = n, n
            flag = False

        if mini > n:
            mini = n

        if maxi < n:
            maxi = n

        inner_list.append(n)
    outer_list.append(inner_list)
# print(outer_list)

max_index = ()
min_index = ()
for a, o in enumerate(outer_list):
    for b, i in enumerate(o):
        if i == maxi:
            max_index = (a, b)
        if i == mini:
            min_index = (a, b)

print(f"Index of the largest number {maxi} is: {max_index}")
print(f"Index of the smallest number {mini} is: {min_index}")
