"""
請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，
計算並輸出此正五邊形之面積（Area）

範例輸入
5

範例輸出
Area = 43.0119

"""

'''
提示1：建議使用import math模組的math.pow及math.tan
提示2：正五邊形面積的公式： Area=(5*s**2)/(4*tan(pi/5))
提示3：輸出浮點數到小數點後第四位。
'''
import math as m

s = 5
print("Area = {:.4f}".format(5 * s ** 2 / (4 * m.tan(m.pi / 5))))
