# int float str
print("============ 基本型態 ============")
print(1)  # 數字和浮點數可用底線隔開，但最前面和最後面不能加底線，浮點數的.前後也不行
print(1.0)
print(123, "456")
print(123, "456", sep='--')
print(123, "456", end=' ')
print("abc")

print("============ 查看型態 ============")
print(type(1))
print(type(1.0))
print(type("abc"))

print("============ 運算 ============")
# + - * / //(商) %(餘) **(次方)，只要其中一個是浮點數，就會回傳浮數；但 / 只會回傳浮點數
print(2 ** 5)
print(2 ** 3 ** 2)  # 512，寫法不好，易造成誤解
print(2 ** (3 ** 2))  # 512
print((2 ** 3) ** 2)  # 64
print(1 + 1.2, type(1 + 1.2))  # int 自動轉 float
# print("a" + 1) # 型態不同，無法 +
print("a" + "b")
print("a" "b")  # 不可是變數
print(2 * "a" + 3 * "b")

print("============ 型態轉換 ============")
print(int(9.6), type(int(9.6)))  # 第二個參數預設是 10，表示是 10 進位
print(int('55', 16))  # 85
# print(int("a"))  # 執行期錯誤
print(float(8), type(float(8)))
print(str(7788), type(str(7788)))

print("============ 宣告變數 ============")
# 命名規則
# 中英文_數字
# 數字不開頭
# 不可用關鍵字
# 不要使用內鍵名稱
# https://docs.python.org/zh-tw/3/reference/lexical_analysis.html#identifiers
# = += -= *= /= //= %= **=，python 沒有 ++ -- 語法
a = 2
a *= 5  # a = a * 5
print(a)
x, y, z = 1, 2.3, "ooo"
print(x, y, z)
# print = 3
# print(print)
# del a  # 刪除 a 變數
# print(a)

print("============ 宣告字串的四種方式 ============")
a = 'a'
b = "b"
# 三個"和三個'是一樣意思
c = """
abc
    123
    """  # 注意 """ 左邊的空格
d = '"yeah"'  # 跳脫字元 \
print(a, b, c, d)

print("============ 註解 ============")
#

"""
和字串一樣，也可用三個'
"""

print("============ 布林 ============")
# ==  !=  >  <  >=  <=
print(True)
print(False)
print(type(True))

print("============ 轉布林 ============")
print(bool(0.0))
print(bool(0))
print(bool(""))  # bool("False") 仍然是 True
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))
print("以上都是 False，其他都是 True")
print(bool({None: None}))  # True，bool({False, False})、bool({"", ""}) 也算 True

print("============ 字串常用方法 ============")
# 字串是不可變的
my_string = "abc apple"

# 大小寫
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title(), my_string.istitle())  # 多個 capitalize，如果是就是 True
print(my_string)

print(my_string[-1])
print(my_string[0])
print(my_string.index("a"))
print(my_string.count("a"))
new_my_string = my_string.replace("a", "A")  # 將所有 a 變大寫
print(my_string)
print(new_my_string)

my_string_list = my_string.split(" ")
print(my_string_list, type(my_string_list))
print(my_string_list[1])
print(len(my_string_list))

print("============ 清除前後特定字串 ============")
my_string2 = " 　 abaac  apple 　  "  # 注意裡面有全形空格
print(my_string2.strip())  # 全形空格也能清除
print(my_string2.strip(""))  # 什麼都沒發生，所以不要用空字串來清除

my_string3 = "abaac  appleba"
print(my_string3.strip("ab"))  # 整個字串裡，最前和最後有 a 或 b 都會清除
print(my_string3.removeprefix("ab"))  # 字串開頭是 ab 會刪除
print(my_string3.removesuffix("ab"))  # 字串結尾是 ab 會刪除

print("============ Unicode Code ============")
a = ord('一')
print(a, '{:x}'.format(a), chr(a))

print("============ 運算元優先級 ============")
# https://docs.python.org/zh-tw/3/reference/expressions.html#operator-precedence

print("============ 複數 ============")
c1 = 1.5 - 0.5j  # 最後的 j 固定寫死，大小寫皆可
c2 = complex(3, 4.5)
print(c1.real, c1.imag)  # 1.5 實數 -0.5 虛數，imaginary
print(c2.real, c2.imag)  # 3.0 實數 4.5 虛數
complex('1+2j')  # 裡面可以放字串，但不能有空格

print("============ 複數-四則運算 ============")
# 複數沒有 // % **
# 加減都是 實+實；虛+虛
print(c1 + c2)  # (4.5+4j)
print(c1 - c2)  # (-1.5-5j)

# 乘法公式：(a+b) * (c+d) => 實：(ac - bd)； 虛：(ad+bc)
# 實 => 直線相乘再相減； 虛 => 交叉相乘再相加
# 實 => (1.5*3.0)-(-0.5*4.5) => 4.5 -(-2.25)； 虛 => (3.0*-0.5) + (1.5*4.5) => -1.5+6.75
print(c1 * c2)  # (6.75+5.25j)

# 除法公式：a+b/c+d => 實：(ac+bd) / (c**2 + d**2)； 虛：(bc-ad) / (c**2 + d**2)
# 實 => 直線相乘再相加/(第二個複數)實平方+虛平方
# 虛 => 交叉相乘再相減(右上~左下-左上~右上)/(第二個複數)實平方+虛平方
# 實 => (1.5*3.0)+(-0.5*4.5)/3**2+4.5**2 => 4.5+(-2.25)/9+20.25 => 2.25/29.25
# 虛 => (-0.5*3.0)-(1.5*4.5)/29.25 => -1.5-6.75/29.25 => -8.25/29.25
print(c1 / c2)  # (0.07692307692307693-0.28205128205128205j)

# c3 = 2+4j
# c4 = 3+1j
c3 = complex(2, 4)
c4 = complex(3, 1)
print(c3 / c4)  # (0.9999999999999999+1j)，應該是 1+1j，有誤差
