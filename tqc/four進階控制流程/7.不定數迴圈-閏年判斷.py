"""
(1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，
然後判斷它是否為閏年（leap year）或平年。
其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈

輸入與輸出會交雜如下，輸出的部份以粗體字表示
2017
2017 is not a leap year.
2000
2000 is a leap year.
2016
2016 is a leap year.
2009
2009 is not a leap year.
2018
2018 is not a leap year.
-9999
"""
while True:
    n = int(input("請輸入西元年:"))
    if n == -9999:
        break

    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(f"{n} is a leap year.")
    else:
        print(f"{n} is not a leap year.")
