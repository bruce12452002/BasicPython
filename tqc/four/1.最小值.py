"""
請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值

範例輸入
23
57
48
2
99
70
9
65
35
88
範例輸出
2
"""

n = None
for i in range(10):
    temp = eval(input("請輸入一個數字:"))
    if n is None or n > temp:
        n = temp
print(n)

'''
# list 配合 min 方法
my_list = []
for i in range(10):
    my_list.append(eval(input("請輸入一個數字:")))
print(min(my_list))
'''
