print("============ 數字 ============")
# b二進制 o八進制 x16進制，大小寫都可以
i = 0b11
# i = 0b5
i = 0o7
i = 0XF

print("============ 浮點數 ============")
# e 是指數，10的幾次方的意思
print(12.345678E2)
print(1234.5678E-2)
print(12.34.is_integer())
print(12.00.is_integer())  # 去掉 0 是否是 int 𡌑態

# round 規則是 ROUND_HALF_DOWN，不是四捨五入
# 假設要取整，如果小數第一位是 5，還要再看第二位之後有沒有數字，有就進位；沒有則不進位
print(round(5.345))  # 捨入到整數
print(round(5.345, 2))  # 捨入到小數第二位
print(round(5.3451, 2))  # 捨入到小數第二位

print("============ 布林 ============")
b = True  # 布林可以和數字運算，False 為 0；True 為 1
print(b + 1, b * 2.0)

print("============ 𡌑態轉換 ============")
# int() float() str() bool() 已介紹過
print(bin(20))
print(oct(20))
print(hex(20))

print("============ 字串 ============")
"""
    find、rfind
    找不到回傳 -1
"""
s = "123" + (3 * "哇哈哈") + "123"
print(s.find("哇哈"))  # 3
print(s.find("哈"))  # 4
print(s.rfind("哈"))  # 11
print(s.find("哇哈", 6))  # 6
print(s.rfind("哇哈", 6, 10))  # 6，注意10是不包括的

"""
    startswith、endswith
    開頭是否是…、結尾是否是…
"""
s = 3 * "abc"
print(s.startswith("ab"))  # True
print(s.endswith("ab"))  # False

"""
    index、rindex
    找不到會報錯
"""
s = 'abcde' * 3
print(s.index("a", 5))  # 5
print(s.rindex("a"))  # 10
print(s.rindex("a", 5, 10))  # 5

'''
    split、rsplit
    第二個參數為分割的次數
    沒找到分割的字串，就是原本的字串
'''
s = "$12$34$56$78$"
print(s.split("$", 2))  # ['12', '34', '56$78']
print(s.rsplit("$", 2))  # ['12$34', '56', '78']

'''
    strip、lstrip、rstrip
'''

'''
    ljust、center、rjust
    左右置中對齊，預設用空格
    zfill：字串左邊放0
'''
s = 'abc'
print(s.rjust(5))  # abc
print(s.rjust(5, 'x'))  # xxabc
print(s.zfill(5))  # 00abc

"""
    join
    字串.join(list)
"""
s = "12$34$56$78"
print(",".join(s.split("$")))

"""
    upper、lower、capitalize、title、swapcase
    swapcase 為大小寫互換
"""
s = "aBc Apple"
print(s.swapcase())

'''
    max、min
    以 ASCII 的數字大小來比較
'''
s = 'abcABC'
print(max(s))
print(min(s))

'''
    isXxx 是否是 xxx，回傳布林值
    
'''
print("123１２３".isdigit())
print(b"9".isdigit())  # bytes 型態，isdecimal 和 isnumeric 會直接報錯
print("123１２３".isdecimal())
print("123壹貳參贰叁一二三１２３ⅠⅱⅲⅣ".isnumeric())

print("123F".isalnum())  # [0-9][A-Z][a-z]
print("Fghi".isalpha())  # [A-Z][a-z]
print("Zz".isascii())

print("abc@".islower())  # 非英文字不影響判斷
print("ABC#".isupper())  # 非英文字不影響判斷
print(" \t　\r\n".isspace())  # 是否是半形空格、全形空格、\r、\n、\t
print("Abc Qoo".istitle())  # 是否每個單字都是開頭大寫，後面小寫
print("abc".isprintable())  # 是否是可見字元，如 \a \b \t \n 都是不可見的
print("print".isidentifier())  # 是否是合法的變數名，如數字開頭就不可以
