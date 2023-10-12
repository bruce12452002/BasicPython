"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，
將num轉換成十六進位值

範例輸入1
13
範例輸出1
D

範例輸入2
8
範例輸出2
8
"""
n = 0

if n < 0 or n > 15:
    print("輸入錯誤")
elif n >= 10:
    print(chr(n + 55))  # ASCII
else:
    print(n)
