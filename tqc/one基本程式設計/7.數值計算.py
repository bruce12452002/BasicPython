"""
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。

Tip
總和與平均數皆輸出到小數點後第1位。

範例輸入1
20
40
60
80
100
範例輸出1
20 40 60 80 100
Sum = 300.0
Average = 60.0

範例輸入2
88.7
12
56
132.55
3
範例輸出2
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5
"""
# n1, n2, n3, n4, n5 = 20, 40, 60, 80, 100
n1, n2, n3, n4, n5 = 88.7, 12, 56, 132.55, 3

# 方法一
# print(n1, n2, n3, n4, n5)
#
# summary = n1 + n2 + n3 + n4 + n5
# print("Sum = %.1f" % summary)
# print("Average = %.1f" % (summary / 5))


# 方法二
my_list = []
for i in range(5):
    n = eval(input("請輸入數字："))
    my_list.append(n)

for i in my_list:
    print(i, end=" ")
print()

summary = sum(my_list)
print("Sum = %.1f" % summary)
print("Average = %.1f" % (summary / len(my_list)))
