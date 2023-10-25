"""
請撰寫一程式，依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中
接著回答：set2是否為set1的子集合（subset）？
set3是否為set1的超集合（superset）？

輸入與輸出會交雜如下，輸出的部份以粗體字表示
**Input to set1:**
3
28
-2
7
39

**Input to set2:**
2
77
0

**Input to set3:**
3
28
12
99
39
7
-1
-2
65

set2 is subset of set1: False
set3 is superset of set1: True
"""
set1 = set()
set2 = set()
set3 = set()

for i in range(1, 17 + 1):
    if i <= 5:
        if i == 1:
            print("Input to set1:")
        set1.add(int(input()))
    elif i <= 8:
        if i == 6:
            print("Input to set2:")
        set2.add(int(input()))
    else:
        if i == 9:
            print("Input to set3:")
        set3.add(int(input()))

print("set2 is subset of set1: {}".format(set2.issubset(set1)))
print("set3 is superset of set1: {}".format(set3.issuperset(set1)))
