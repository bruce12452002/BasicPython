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
    以 ASCII 的數字大小來回傳
'''
a = 'abcABC'
print(max(a))
print(min(a))
