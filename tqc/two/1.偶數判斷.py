"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）

範例輸入1
56
範例輸出1
56 is an even number.

範例輸入2
21
範例輸出2
21 is not an even number.
"""
n = 21
if n % 2 == 0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is not an even number.")
