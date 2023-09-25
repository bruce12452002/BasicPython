"""
    find、rfind
    找不到回傳 -1
"""
a = "123" + (3 * "哇哈哈") + "123"
print(a.find("哇哈"))  # 3
print(a.find("哈"))  # 4
print(a.rfind("哈"))  # 11
print(a.find("哇哈", 6))  # 6
print(a.rfind("哇哈", 6, 10))  # 6，注意10是不包括的

"""
    startswith、endswith
    開頭是否是…、結尾是否是…
"""
a = 3 * "abc"
print(a.startswith("ab"))  # True
print(a.endswith("ab"))  # False

"""
    index、rindex
    找不到會報錯
"""
a = 'abcde' * 3
print(a.index("a", 5))  # 5
print(a.rindex("a"))  # 10
print(a.rindex("a", 5, 10))  # 5

'''
    split、rsplit
    第二個參數為分割的次數
    沒找到分割的字串，就是原本的字串
'''
a = "$12$34$56$78$"
print(a.split("$", 2))  # ['12', '34', '56$78']
print(a.rsplit("$", 2))  # ['12$34', '56', '78']

'''
    strip、lstrip、rstrip
'''

'''
    ljust、center、rjust
    左右置中對齊，預設用空格
    zfill：字串左邊放0
'''
a = 'abc'
print(a.rjust(5))  # abc
print(a.rjust(5, 'x'))  # xxabc
print(a.zfill(5))  # 00abc

"""
    join
    字串.join(list)
"""
a = "12$34$56$78"
print(",".join(a.split("$")))

"""
    upper、lower、capitalize、title、swapcase
    swapcase 為大小寫互換
"""
a = "aBc Apple"
print(a.swapcase())

'''
    max、min
    以 ASCII 的數字大小來比較
'''
a = 'abcABC'
print(max(a))
print(min(a))

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
