"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，
判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。
例如：a為英文字母、9為數字、$為其它字元

範例輸入1
P
範例輸出1
P is an alphabet.

範例輸入2
@
範例輸出2
@ is a symbol.

範例輸入3
7
範例輸出3
7 is a number.
"""
a = input("請輸入一個字元:")
unicode = ord(a)

if 48 <= unicode <= 57:  # a.isdigit()
    print(f"{a} is a number.")
elif (65 <= unicode <= 90) or (97 <= unicode <= 122):  # a.isalpha()
    print(f"{a} is an alphabet.")
else:
    print(f"{a} is a symbol.")
