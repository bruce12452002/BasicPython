"""
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，
此函式回傳x和y的最大公因數

範例輸入1
12,8
範例輸出1
4

範例輸入2
4,6
範例輸出2
2
"""

"""
一直循環到兩個數最小的那一個，只要兩個都可以整除，
迴圈的最後一個就是最大公因數
"""


# def compute(x, y):
#     if x > y:
#         x, y = y, x
#
#     result = 1
#     for i in range(2, x + 1):
#         if (x % i == 0) and (y % i == 0):
#             result = i
#     return result
#
#
# print(compute(int(input("請輸入一個整數:")),
#               int(input("請再輸入一個整數:"))))

"""
輾轉相除法
40 % 16 = 8
16 % 8 = 0
餘數=0，8 就是最大公因數
"""


def compute2(x, y):
    if x > y:
        x, y = y, x

    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x


print(compute2(int(input("請輸入一個整數:")),
               int(input("請再輸入一個整數:"))))
