"""
請撰寫一程式，讓使用者輸入一個整數x，並將x傳遞給名為compute()的函式，
此函式將回傳x是否為質數（Prime number）的布林值，接著再將判斷結果輸出。
如輸入值為質數顯示【Prime】，否則顯示【Not Prime】

範例輸入1
3
範例輸出1
Prime

範例輸入2
6
範例輸出2
Not Prime

範例輸入3
1
範例輸出3
Not Prime

範例輸入4
0
範例輸出4
Not Prime

範例輸入5
-5
範例輸出5
Not Prime
"""


def compute(n):
    if n == 0 or n == 1:
        return False

    if n < 0:
        n *= -1

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if compute(-7):
    print('Prime')
else:
    print('Not Prime')
