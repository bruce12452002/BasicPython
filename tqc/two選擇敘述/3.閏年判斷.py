"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，
然後判斷它是否為閏年（leap year）或平年。
其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

範例輸入1
1992
範例輸出1
1992 is a leap year.

範例輸入2
2010
範例輸出2
2010 is not a leap year.
"""
n = 2010
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")
