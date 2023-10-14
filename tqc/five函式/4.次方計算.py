"""
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
此函式接收兩個參數a、b，並回傳a^b的值

範例輸入

14
3
範例輸出

2744
"""


def compute(a, b):
    return a ** b


result = compute(int(input("請輸入一個整數:")), int(input("請再輸入一個整數:")));
input(result)
