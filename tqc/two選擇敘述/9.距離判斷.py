"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，
判斷此點是否與點(5, 6)的距離小於或等於15，
如距離小於或等於15顯示【Inside】，反之顯示【Outside】

範例輸入1
7
20
範例輸出1
Inside

範例輸入2
30
35
範例輸出2
Outside
"""

x = 7
y = 20
d = (((5 - x) ** 2) + ((6 - y) ** 2)) ** 0.5
print(d)
if d <= 15:
    print("Inside")
else:
    print("Outside")
