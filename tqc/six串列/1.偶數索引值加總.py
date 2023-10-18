"""
請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。
顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果
輸出每一個數字欄寬設定為3，每3個一列，靠右對齊

範例輸入
56
45
43
22
3
1
39
20
93
18
44
83
範例輸出
 56 45 43
 22  3  1
 39 20 93
 18 44 83
278
"""
n = 12
my_list = []
for i in range(n):
    my_list.append(int(input("請輸入整數:")))

summary = 0
for i in range(len(my_list)):
    print("{:>3}".format(my_list[i]), end=" ")
    if (i + 1) % 3 == 0:
        print()

    if i % 2 == 0:
        summary += my_list[i]
print(summary)
