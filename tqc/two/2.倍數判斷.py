"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，
顯示【x is a multiple of 3.】或【x is a multiple of 5.】；
若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；
如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，
將使用者輸入的數值代入x

範例輸入1
55
範例輸出1
55 is a multiple of 5.

範例輸入2
36
範例輸出2
36 is a multiple of 3.

範例輸入3
92
範例輸出3
92 is not a multiple of 3 or 5.

範例輸入4
15
範例輸出4
15 is a multiple of 3 and 5.
"""
x = int(input("請輸入一個正整數:"))
if x % 3 == 0 and x % 5 == 0:
    print("x is a multiple of 3 and 5.")
elif x % 3 == 0:
    print("x is a multiple of 3.")
elif x % 5 == 0:
    print("x is a multiple of 5.")
else:
    print("x is not a multiple of 3 or 5.")
