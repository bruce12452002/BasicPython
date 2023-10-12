"""
請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，
計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。

Tip
輸出浮點數到小數點後第二位。

範例輸入
23.5
19
範例輸出

Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50

"""
# 周長 = (長+寬)*2
height = 23.5
width = 19

print("Height = %.2f" % height)
print("Width = %.2f" % width)
print("Perimeter = {:.2f}".format((height + width) * 2))
print("Area = {:.2f}".format(height * width))
