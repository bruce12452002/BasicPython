"""
請撰寫一程式，計算費氏數列（Fibonacci numbers），
使用者輸入一正整數num (num>=2)，
並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
F_0=0$$$$F_1 = 1 Fn−Fn−1+Fn−2
​

範例輸入1
10
範例輸出1
0 1 1 2 3 5 8 13 21 34

範例輸入2
20
範例輸出2
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
"""


def compute(n):
    if n > 1:
        return compute(n - 1) + compute(n - 2)
    return n


for i in range(int(input('請輸入一個整數:'))):
    print(compute(i), end=" ")
