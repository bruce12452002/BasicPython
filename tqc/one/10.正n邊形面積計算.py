"""
請撰寫一程式，讓使用者輸入兩個正數n、s，
代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）

範例輸入
8
6

範例輸出
Area = 173.8234
"""

'''
提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下： Area=(n*s**2)/(4*tan(pi/n)) 
提示3：輸出浮點數到小數點後第四位
'''
import math as m

n, s = 8, 6  # 正8邊形，長為6
print("Area = {:.4f}".format(n * s ** 2 / (4 * m.tan(m.pi / n))))
