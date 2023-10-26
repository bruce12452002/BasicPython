"""
請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），代表有k筆測試資料
每一筆測試資料是一串數字，每個數字之間以一空白區隔，
請找出此串列數字中最大值和最小值之間的差
差值輸出到小數點後第二位。

輸入與輸出會交雜如下，輸出的部份以粗體字表示
4
94 52.9 3.14 77 46
**90.86**
-2 0 1000.34 -14.4 89 50
**1014.74**
87.78 33333 29.3
**33303.70**
9998 9996 9999
**3.00**
"""
n = int(input("請輸入測試次數: "))
if 1 <= n <= 100:
    for i in range(n):
        st = input("請輸入測試資料，數字之間以空白隔開: ")
        maxi = 0
        mini = 0
        first = True
        for s in st.split(" "):
            num = float(s)
            if first:
                maxi = num
                mini = num
                first = False
            if maxi < num:
                maxi = num
            if mini > num:
                mini = num
        print(f"{maxi - mini:.2f}")
