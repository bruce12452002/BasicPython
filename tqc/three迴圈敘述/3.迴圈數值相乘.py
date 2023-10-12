"""
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），
然後以三角形的方式依序輸出此數的相乘結果
輸出欄寬為4，且需靠右對齊

範例輸入1
5
範例輸出1
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25

範例輸入2
12
範例輸出2
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144
"""
n = 5

if n < 100:
    print("===== while-while =====")
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("{:>4d}".format(i * j), end="")
            j += 1
        i += 1
        print()

    print("===== for-for =====")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("{:>4d}".format(i * j), end="")
        print()

    print("===== while-for =====")
    i = 1
    while i <= n:
        for j in range(1, i + 1):
            print("{:>4d}".format(i * j), end="")
        i += 1
        print()

    print("===== for-while =====")
    for i in range(1, n + 1):
        j = 1
        while j <= i:
            print("{:>4d}".format(i * j), end="")
            j += 1
        print()
