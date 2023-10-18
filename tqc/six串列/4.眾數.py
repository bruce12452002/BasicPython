"""
請撰寫一程式，讓使用者輸入十個整數作為樣本數，
輸出眾數（樣本中出現最多次的數字）及其出現的次數
假設樣本中只有一個眾數

範例輸入
34
18
22
32
18
29
30
38
42
18
範例輸出
18
3
"""
my_dict = {}

for i in range(10):
    n = int(input("請輸入整數:"))
    if n in my_dict:
        my_dict[n] += 1
    else:
        my_dict[n] = 1

for k, v in my_dict.items():
    if v == max(my_dict.values()):
        print(k)
        print(v)
