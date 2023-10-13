"""
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
此函式接收兩個參數a、b，並回傳從a連加到b的和

範例輸入

33
66
範例輸出

1683
"""


def compute(a, b):
    count = 0
    for i in range(a, b + 1):
        count += i
    print(count)


compute(33, 66)
