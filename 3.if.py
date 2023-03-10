import operator

# https://docs.python.org/zh-tw/3/library/operator.html#mapping-operators-to-functions
# and、or(邏輯運算)   &、|(算術運算)
# is、is not(比較記憶體)   ==、!=(比較值)
# 一般工作都是用 and or == !=
print("============ 算術運算不等於邏輯運算 ============")
aaa = 15
bbb = 10
# is is not 在比較 list tuple dict 才看得出來
# print(aaa is bbb)
# print(aaa is not bbb)
print(not True)  # 沒有「!」寫法

# aaa & bbb 等於 10 為True；
# (aaa == 15) & (bbb == 10) 為 True；
# True & 奇數為 1；True & 偶數為 0，只看個為數； False & 數字都是 0
if aaa == 15 & bbb == 10:  # 0 != 10
    print("yes")
else:
    print("no")

if aaa == 15 and bbb == 10:
    print("yes")
else:
    print("no")

print("============ if 一 ============")
# 用空格控制
# 可以寫多行
apple = 30
if operator.gt(apple, 25):  # apple > 25
    print("too expensive")
    print("too expensive")
print("非 if 區塊")

print("============ if 二 ============")
if apple > 50:
    print("too expensive")
    print("too expensive")
else:
    print("too cheap")
    print("too cheap")
print("非 if 區塊")

print("============ if 三 ============")
score = int(input("input score:"))
if score > 90:
    print("A class")
elif score > 80:
    print("B class")
elif score > 60:
    print("C class")
# else:
#     print("D class")
print("非 if 區塊")

print("============ __matmul__ ============")
# 矩陣相乘
# __matmul__ 和 @ 一樣

import numpy

# 以下都不支援 __matmul__
matmul = '__matmul__'
print(matmul in dir(False))
print(matmul in dir(1))
print(matmul in dir(2.3))
print(matmul in dir(""))
print(matmul in dir(()))
print(matmul in dir([]))
print(matmul in dir({}))
print(matmul in dir(set()))

a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6], [7, 8]])
# 不會影響原本的
# [0][0]=1*5+2*7  [0][1]=1*6+2*8
# [1][0]=3*5+4*7  [1][1]=3*6+4*8

print(a @ b)
print(a.__matmul__(b))

# 剩下的和 java 一樣，參考我的 blog
# https://javabruce.blogspot.com/2019/08/blog-post.html
