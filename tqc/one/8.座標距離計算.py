"""
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，
分別代表兩個點的座標(x1, y1)、(x2, y2)。
計算並輸出這兩點的座標與其歐式距離。

歐式距離 = (x1-x2) ** 2 + (y1-y2) ** 2，全部的開根號
兩座標的歐式距離，輸出到小數點後第4位

範例輸入
2
1
5.5
8

範例輸出
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262
"""
x1, y1, x2, y2 = 2, 1, 5.5, 8
execute = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("( %s , %s )" % (x1, y1))
print("( %s , %s )" % (x2, y2))
print("Distance = {:.4f}".format(execute))
