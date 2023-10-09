"""
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

Tip

提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

範例輸入1  10
範例輸出1

Radius = 10.00
Perimeter = 62.83
Area = 314.16


範例輸入2   2.5
範例輸出2

Radius = 2.50
Perimeter = 15.71
Area = 19.63
"""

# 周長=半徑*2*PI
# 面積=半徑*半徑*PI

import math as m

n = 10  # 2.5
print("Radius = {:.2f}".format(n))
print("Perimeter = {:.2f}".format(n * 2 * m.pi))
print("Area = {:.2f}".format(n ** 2 * m.pi))
