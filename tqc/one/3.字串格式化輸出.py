"""
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、
欄與欄間隔一個空白字元、每列印兩個的方式，
先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

範例輸入

I
enjoy
learning
Python
範例輸出

|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
"""

s1, s2, s3, s4 = 'I', 'enjoy', 'learning', "Python"

right = '|{:>10s} {:>10s}|'
left = '|{:<10s} {:<10s}|'

print(right.format(s1, s2))
print(right.format(s3, s4))
print(left.format(s1, s2))
print(left.format(s3, s4))
