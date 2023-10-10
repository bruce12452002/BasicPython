"""
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），
利用迴圈計算從a開始連加到b的總和。
例如：輸入a=1、b=100，則輸出結果為5050（1 + 2 + … + 100 = 5050）

範例輸入
66
666

範例輸出
219966
"""
a = int(input("請輸入開始的正整數:"))
b = int(input("請輸入結束的正整數:"))

if a < b:
    # for
    count = 0
    for i in range(a, b + 1):
        count += i
    print(count)

    # while
    count = 0
    while a <= b:
        count += a
        a += 1
    print(count)
