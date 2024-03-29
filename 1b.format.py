# https://docs.python.org/3/tutorial/introduction.html#text
print("============ 字串格式化一 printf style ============")
# %d %s %f 為 digital(數字) string(字串) float(浮點數), %d 等同 %i
# 格式為 "%s" % (取代 %s 的字串)，如果只有一個要取代，圓括可不寫
# %s 什麼都可以接收；%d 和 %f 只能傳數字，否則報錯
# %d 給浮點數會無條件括去小數；%f 給整數會自動將後面 .0
# %f 預設小數 6 位，如果想將後面的 0 去掉，可用 %g
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

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

print("============ 字串格式化二 literal ============")
i = "haha"
j = 1.111
k = 56
print(F"hello {i}, {j} {k}, {type(k)}")  # 變數裡可運算

# :後面還可以接變數；但:前面就不可以，:後面的意思要看下面的字串格式化三
m = 5
print(f"{k:^{m}}")

# 多行可用 \ 換行，指的是編輯時換行，不是輸出後的換行
print(f"abc{i}, \
      def {j} \
jkl {k}"
      )

print("============ 字串格式化一二，可一起使用 ============")
xxx = "nine"
ooo = 9
print(f"{xxx} is %3d" % ooo)

print("============ 字串格式化三 format方法 ============")
# 參考 https://docs.python.org/3/library/stdtypes.html#str.format
print('1.{1} and {0} and {0}'.format('aaa', 'bbb'))  # 手動指定第幾個參數

# 依參數名稱賦值，k=v 一律放在最後面，不可穿插在中間
print('2.{fa} and {fb} and {0} or {fa}'.format("ccc", fa='aaa', fb='bbb'))

# 參數自動依照順序
print('3.{} and {} and {}'.format('aaa', 'bbb', 'ccc'))  # 參數個數要和花括號相等

# 自動和手動不可放在一起，但自動和手動可和參數名稱混合
# print('4.{} and {0} and {}'.format('aaa', 'bbb', 'ccc'))  # 參數個數要和 {} 相等
# :開頭，如果傳進來的參數位數 > 設定的位數，設定會失效，不會報錯
# :左邊有數字表示第幾個參數，不寫預設為 0
# :前為參數的索引，後面的順序為：補對號長轉(補票、對號入座，票很長可以轉)，補滿、對齊、正負號、逗號、長度、轉進制

print("============ 字串格式化三-數字補滿 ============")
print('{:0>7d}'.format(987))
print('{:#<7d}'.format(987))
print('{:x<7.1f}'.format(987.2418))

print("============ 字串格式化三-對齊 ============")
print('{:<9}'.format(12.3))  # 靠左對齊
print('{:^9}'.format(12.3))  # 置中，如果無法置中會往左一格
print('{:>9}'.format(12.3))  # 靠右對齊，這是預設，也就是不寫 > 也是這樣的結果
print('{0:>9}'.format(12.3))  # 第 0 個參數有 9 格，靠右對齊

print("============ 字串格式化三-正負號 ============")
# 9 和上面一樣，佔 9 位，預設靠右對齊
print('{:+9} {:+9}'.format(12.3, -12.3))  # 正負數前面都會顯示 +-
print('{:-} {:-}'.format(12.3, -12.3))  # 正數不會顯示 +；負數會顯示 -，這是預設值，也就是「-」可以不用打，只剩一個:時也可省略
print('{: } {: }'.format(12.3, -12.3))  # 正數前會有空格；負數會顯示 -，超過一個空格會報錯

# 小數位數
print('{:.2f} {:7.0f} {:0d}'.format(12.3, -12.3, -99))  # 保留幾位小數，「.0f」會四捨五入

print("============ 字串格式化三-轉x進制 ============")
# {:s} 為字串，{:f} 為浮點數
print('{:b}'.format(324))
print('{:d}'.format(324))
print('{:o}'.format(324))
print('{:#o}'.format(324))
print('{:x}'.format(324))
print('{:#x}'.format(324))
print('{:#X}'.format(324))

# 其他
# % 為百分比，也就是乘 100，.2 表示小數兩位；2e 的 2 表示佔幾格，因為超過 2 格，所以會失效；只有 % 會是小數點 6 位
print('{:10.2%} {:%} {:2e}'.format(987.245, 0.25, 789.1234))
print('{:,}'.format(12_3456.7891113))  # 整數位三位一個逗號，只能打逗號；小數位沒有
print('{:,.2f}'.format(12_3456.7891113))  # 整數位三位一個逗號，只能打逗號；小數位沒有

print("============ 字串格式化三-資料結構 ============")
# {0[xxx]} 裡的 0 表示第一個參數
abc = {'a': 111, 'b': 222, 'c': 333.7}
print('{0[c]:f} {0[a]:d} ' '{0[b]:d}'.format(abc))
print('{c:f} {a:d} {b:d}'.format(**abc))

my_list = ['a', 'bc', 'def']
print("{0[0]} {0[1]}".format(my_list))
print("{[0]} {[1]} {[2]}".format(*my_list))
print("{0[0]} {1[1]} {2[2]}".format(*my_list))
