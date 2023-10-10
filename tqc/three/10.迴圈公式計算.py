"""
請使用迴圈敘述撰寫一程式，讓使用者輸入正整數n (1 < n)，計算以下公式的總和並顯示結果：
1/根號1+根號2 + 1/根號2+根號3 + 1/根號3+根號4 + 1/根號n-1+根號n
輸出結果至小數點後四位

範例輸入
8
範例輸出
1.8284
"""
n = 8

if 1 < n:
    count = 0
    for i in range(2, n + 1):
        count += 1 / ((i - 1) ** 0.5 + i ** 0.5)
    print("%.4f" % count)
