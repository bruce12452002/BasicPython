"""
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和
J、Q、K以及A分別代表11、12、13以及1

範例輸入
5
10
K
3
A
範例輸出
32
"""
summary = 0
for i in range(5):
    s = input("請輸入樸克牌號:")

    if s.lower() == 'j':
        summary += 11
    elif s.lower() == 'q':
        summary += 12
    elif s.lower() == 'k':
        summary += 13
    elif s.lower() == 'a':
        summary += 1
    else:
        summary += int(s)
print(summary)
