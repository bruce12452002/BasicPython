"""
請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，
此函式將回傳x和y的乘積

範例輸入
56
11
範例輸出
616
"""


def compute(a, b):
    return a * b


x = int(input("請輸入一個整數:"))
y = int(input("請再輸入一個整數:"))
print(compute(x, y))
