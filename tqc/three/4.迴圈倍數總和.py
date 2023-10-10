"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，
利用迴圈計算從1到a之間，所有5之倍數數字總和

範例輸入
21
範例輸出
50
"""
n = int(input("請輸入一個正整數:"))

count = 0
if n >= 5:
    # while
    # i = 5
    # while i <= n:
    #     count += i
    #     i += 5

    # for
    for i in range(5, n + 1, 5):
        count += i
print(count)
