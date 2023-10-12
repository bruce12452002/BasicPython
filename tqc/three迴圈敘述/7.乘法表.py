"""
(1) 請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數n（n<10），顯示n*n乘法表
(2) 每項運算式需進行格式化排列整齊，每個運算子及運算元輸出的欄寬為2，
而每項乘積輸出的欄寬為4，皆靠左對齊不跳行

範例輸入1
3
範例輸出1
1 * 1 = 1   2 * 1 = 2   3 * 1 = 3
1 * 2 = 2   2 * 2 = 4   3 * 2 = 6
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9

範例輸入2
5
範例輸出2
1 * 1 = 1   2 * 1 = 2   3 * 1 = 3   4 * 1 = 4   5 * 1 = 5
1 * 2 = 2   2 * 2 = 4   3 * 2 = 6   4 * 2 = 8   5 * 2 = 10
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9   4 * 3 = 12  5 * 3 = 15
1 * 4 = 4   2 * 4 = 8   3 * 4 = 12  4 * 4 = 16  5 * 4 = 20
1 * 5 = 5   2 * 5 = 10  3 * 5 = 15  4 * 5 = 20  5 * 5 = 25
"""
n = 5

if n < 10:
    print("===== for-for =====")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("{:<2d}* {:<2d}= {:<4d}".format(j, i, i * j), end="")
        print()

    print("===== while-while =====")
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print("{:<2d}* {:<2d}= {:<4d}".format(j, i, i * j), end="")
            j += 1
        print()
        i += 1

    print("===== for-while =====")
    for i in range(1, n + 1):
        j = 1
        while j <= n:
            print("{:<2d}* {:<2d}= {:<4d}".format(j, i, i * j), end="")
            j += 1
        print()

    print("===== while-for =====")
    i = 1
    while i <= n:
        for j in range(1, n + 1):
            print("{:<2d}* {:<2d}= {:<4d}".format(j, i, i * j), end="")
        print()
        i += 1
