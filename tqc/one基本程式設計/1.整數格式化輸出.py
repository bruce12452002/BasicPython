"""
請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、
欄與欄間隔一個空白字元，再以每列印兩個的方式，
先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

範例輸入

85
4
299
478
範例輸出

|   85     4|
|  299   478|
|85    4    |
|299   478  |
"""

n1, n2, n3, n4 = 85, 4, 299, 478
# n1 = int(input("n1:"))

right: str = '|{:>5d} {:>5d}|'
left: str = '|{:<5d} {:<5d}|'

print(right.format(n1, n2))
print(right.format(n3, n4))
print(left.format(n1, n2))
print(left.format(n3, n4))
