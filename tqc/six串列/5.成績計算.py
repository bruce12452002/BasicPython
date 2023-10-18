"""
請撰寫一程式，讓使用者輸入十個成績，
接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果
平均值輸出到小數點後第二位

範例輸入
89
78
67
80
75
98
77
89
76
60
範例輸出
631
78.88
"""

# low, high, count = 0, 0, 0
# loop = 10
# my_list = []
# for i in range(loop):
#     n = int(input("請輸入整數:"))
#     my_list.append(n)
#
#     if i == 0:
#         low = n
#         high = n
#
#     if low > n:
#         low = n
#
#     if high < n:
#         high = n
#
#     count += n
#
# count -= low + high
# avg = count / (loop - 2)
# print(count)
# print(f"{avg:.2f}")

print('========== 使用內鍵方法 =========')
loop = 10
my_list = []
for i in range(loop):
    n = int(input("請輸入整數:"))
    my_list.append(n)

count = sum(my_list) - max(my_list) - min(my_list)
print(count)
print(f"{count / (loop - 2):.2f}")
