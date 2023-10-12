"""
請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數

範例輸入
69
48
19
91
83
22
18
37
82
40
範例輸出

Even numbers: 5
Odd numbers: 5
"""
even = 0
odd = 0
for i in range(10):
    n = int(input("請輸入第" + str(i + 1) + "個整數:"))
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers: %d" % even)
print("Odd numbers: %d" % odd)
