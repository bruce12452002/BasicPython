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

    match s:
        case 'J' | 'K' | 'L' | 'j' | 'k' | 'l':
            j = ord(s) - 63
        case 'A' | 'a':
            j = 1
        case _:
            j = int(s)
    summary += j
print(summary)
