# int float str
print("============ 基本型態 ============")
print(1)  # 數字和浮點數可用底線隔開，但最後面和最後面不能加底線，浮點數的.前後也不行
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
# + - * / //(商) %(餘) **(次方)
print(2 ** 5)
print(1 + 1.2, type(1 + 1.2))  # int 自動轉 float
# print("a" + 1) # 型態不同，無法 +
print("a" + "b")
print("a" "b")
print(2 * "a" + 3 * "b")

print("============ 型態轉換 ============")
print(int(9.6), type(int(9.6)))
# print(int("a"))  # 執行期錯誤
print(float(8), type(float(8)))
print(str(7788), type(str(7788)))

print("============ 宣告變數 ============")
# 命名規則
# 中英文_數字
# 數字不開頭
# 不可用關鍵字
# https://docs.python.org/zh-tw/3/reference/lexical_analysis.html#identifiers
# = += -= *= /= //= %= **=，python 沒有 ++ -- 語法
a = 2
a += 5
print(a)
x, y, z = 1, 2.3, "ooo"
print(x, y, z)
del a  # 刪除 a 變數
# print(a)

print("============ 宣告字串的三種方式 ============")
a = 'a'
b = "b"
# 三個"和三個'是一樣意思
c = """
abc
    123
    """  # 注意 """ 左邊的空格
d = "\"yeah\""  # 跳脫字元 \
print(a, b, c, d)

print("============ 註解 ============")
#

"""
和字串一樣，也可用三個'
"""

print("============ 字串格式化一 ============")
# %d %s %f 為 digit(數字) string(字串) float(浮點數)
# 格式為 "%s" % (取代 %s 的字串)，如果只有一個要取代，圓括可不寫
# %s 什麼都可以接收；%d 和 %f 只能傳數字，否則報錯
# %d 給浮點數會無條件括去小數；%f 給整數會自動將後面 .0
print("Hello! %s")
# print("Hello! %" % ("world"))
print("Hello! %s" % ("%"))  # 只有一個參數可省略圓括號

e = "Hello! %s" % "world"
print(e)
f = "%s %s" % ("Haha!", e)
print(f)
g = "is %f %d" % (9.5, 10 + 1)  # 圓括裡可運算
print(g)

# %d %f 可以限制長度
# m.n：m 包括整數、小數加起來的位數(不包括小數點)，n 只有小數的位數
# %3d %3.2f %.2f，整數超過會失效；小數超過會四捨五入
h = "n1=%d n2=%.2f n3=%3.2f n4=%10.2f" % (1.55, 2.567, 1234.789, 1234.678)
print(h)

print("============ 字串格式化二 ============")
i = "haha"
j = 1.111
k = 56
print(F"hello {i}, {j} {k}, {type(k)}")  # 變數裡可運算

# 多行可用 \ 換行
print(f"abc{i}, \
      def {j} \
jkl {k}"
      )

print("============ 字串格式化一二，可一起使用 ============")
xxx = "nine"
ooo = 9
print(f"{xxx} is %3d" % ooo)

print("============ 字串格式化三 ============")
# 參考 https://docs.python.org/zh-tw/3/library/stdtypes.html#str.format
print('1.{1} and {0} and {0}'.format('aaa', 'bbb'))
print('2.{fa} and {fb} and {0} or {fa}'.format("ccc", fa='aaa', fb='bbb'))

# :開頭，如果傳進來的參數位數 > 設定的位數，設定會失效，不會報錯
print('{:<9}'.format(12.3))  # 靠左對齊
print('{:^9}'.format(12.3))  # 置中，如果無法置中會往左一格
print('{:>9}'.format(12.3))  # 靠右對齊，這是預設，也就是不寫 > 也是這樣的結果
print('{0:>9}'.format(12.3))  # 第 0 個參數有 9 格，靠右對齊

print("============ 字串格式化三-數字補滿 ============")
print('{:0>7d}'.format(987))
print('{:#<7d}'.format(987))
print('{:x<7.1f}'.format(987.2))

print("============ 字串格式化三-正負號 ============")
# 9 和上面一樣，佔 9 位，預設靠右對齊
print('{:+9} {:+9}'.format(12.3, -12.3))  # 正負數前面都會顯示 +-
print('{:-} {:-}'.format(12.3, -12.3))  # 正數不會顯示 +；負數會顯示 -，這是預設值，也就是「-」可以不用打
print('{: } {: }'.format(12.3, -12.3))  # 正數前會有空格；負數會顯示 -

# 小數位數
print('{:.2f} {:7.0f} {:0d}'.format(12.3, -12.3, -99))  # 保留幾位小數，「.0f」會四捨五入

print("============ 字串格式化三-進制 ============")
print('{:b}'.format(324))
print('{:d}'.format(324))
print('{:o}'.format(324))
print('{:x}'.format(324))
print('{:#x}'.format(324))
print('{:#X}'.format(324))

# 其他
print('{:2%} {:2e}'.format(987.245, 789.1234))
print('{:,}'.format(12_3456.7891113))  # 整數位三位一個逗號，只能打逗號；小數位沒有

print("============ 字串格式化三-資料結構 ============")
# {0[xxx]} 裡的 0 表示第一個參數
abc = {'a': 111, 'b': 222, 'c': 333.7}
print('{0[c]:f} {0[a]:d} ' '{0[b]:d}'.format(abc))
print('{c:f} {a:d} {b:d}'.format(**abc))

my_list = ['s', 'ss']
print("{0[0]} {0[1]}".format(my_list))

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
print(my_string3.strip("ab"))  # 整個字串裡，有 a 或 b 都會清除
