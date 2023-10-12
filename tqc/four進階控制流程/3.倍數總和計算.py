"""
請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），
輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）
以及倍數之個數、總和

範例輸入1
5
55
範例輸出1
8   9   12  16  18  20  24  27  28  32
36  40  44  45  48  52  54
17
513

範例輸入2
4
9
範例輸出2
4   8   9
3
21
"""
a = int(input("請輸入一個正整數:"))
b = int(input("請再輸入一個正整數:"))

count = 0  # 個數
summary = 0  # 總合
if a <= b:
    for i in range(a, b + 1):
        if i % 4 == 0 or i % 9 == 0:
            if count != 0 and count % 10 == 0:
                print()
            print("{:<4}".format(i), end="")
            count += 1
            summary += i
    print()
    print(count)
    print(summary)
