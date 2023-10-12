"""
請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，
然後找出其最小值，並輸出最小值

範例輸入
29
100
948
377
-28
0
-388
9999
範例輸出
-388
"""

n = None
while True:
    temp = eval(input("請輸入一個數字:"))
    if temp == 9999:
        break
    if n is None or n > temp:
        n = temp
print(n)

# list 配合 min 方法
'''
# my_list = []
while True:
    temp = eval(input("請輸入一個數字:"))
    if temp == 9999:
        break
    my_list.append(temp)
print(min(my_list))
'''
