"""
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，
檢查這三個邊長是否可以組成一個三角形。
若可以，則輸出該三角形之周長；否則顯示【Invalid】

範例輸入1
5
6
13
範例輸出1
Invalid

範例輸入2
1
1
1
範例輸出2
3
"""
# 檢查方法 = 任意兩個邊長之總和大於第三邊長。

a, b, c = 5, 6, 13
# a, b, c = 1, 1, 1

if a + b > c and a + c > b and b + c > a:
    print(a + b + c)
else:
    print("Invalid")
