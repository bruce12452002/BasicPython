# 1.給一個整數，如給 5，結果為 1*2*3*4*5
num = 5
s = 1
for i in range(1, num + 1):
    s *= i
print(s)
print()

# 2.給一個整數，如給 5，結果為 1+11+111+1111+11111 的總合
num = 9
sum = 0
for i in range(1, num + 1):
    temp = "1"
    j = 1
    while j < i:
        temp = temp + "1"
        j += 1
    # print(temp)
    sum += int(temp)
print(sum)
print()

# 3.輸出9*9乘法表，乘完後的數字靠右對齊
num = 9
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{i} X {j} = %2d" % (i * j))
    print()
print()

""" 4.用迴圈印出以下星星
*****
*****
*****
*****
*****
"""
n = 8

# 方法一
# for i in range(n):
#     print(n * "*")

# 方法二
for i in range(1, n + 1):
    for j in range(n):
        print("*", end="")
    print()

print()

""" 5.用迴圈印出以下數字
11111
22222
33333
44444
55555
"""

# 方法一
# for i in range(1, n + 1):
#     print(str(i) * n)

# 方法二
for i in range(1, n + 1):
    for j in range(n):
        print(i, end="")
    print()

print()

""" 6.用迴圈印出以下數字
12345
12345
12345
12345
12345
"""

for i in range(1, n + 1):
    j = 1
    while j < n + 1:
        print(j, end="")
        j += 1
    print()

print()

""" 7.用迴圈印出以下數字
55555
44444
33333
22222
11111
"""

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(i, end="")
    print()

print()

""" 8.用迴圈印出以下數字
54321
54321
54321
54321
54321
"""

for i in range(n, 0, -1):
    j = n
    while j > 0:
        print(j, end="")
        j -= 1
    print()

print()

""" 9.用迴圈印出以下星星
*
**
***
****
*****
"""
# line

max_num = 5
for i in range(1, max_num + 1):
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()

print()

""" 10.用迴圈印出以下星星
*****
****
***
**
*
"""
# max_num - line + 1

for i in range(1, max_num + 1):
    j = 1
    while j <= max_num - i + 1:
        print("*", end="")
        j += 1
    print()

print()

""" 11.用迴圈印出以下星星
    *
   **
  ***
 ****
*****
"""
# space： max_num - line
# star ： line

for i in range(1, max_num + 1):
    j = 1
    while j <= max_num - i:
        print(" ", end="")
        j += 1

    k = 1
    while k <= i:
        print("*", end="")
        k += 1

    print()

print()

""" 12.用迴圈印出以下星星
*****
 ****
  ***
   **
    *
"""
# space： max_num - line
# star ： line

for i in range(1, max_num + 1):
    j = 1
    while j <= i - 1:
        print(" ", end="")
        j += 1

    k = 1
    while k <= max_num - i + 1:
        print("*", end="")
        k += 1

    print()

print()
