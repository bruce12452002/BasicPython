# 1.在一行內印出 i 和 s，中間用「,」隔開
i, s = 5, "str"
#
print(i, s, sep=",")

# 2.印出 bool 型態
b = True
#
print(type(b))

# 3.寫出 1+2+3+...+100 的公式，公式為：(前項+後項)乘項數除2，然後轉成整數型態，並在最後印出「 yeah\n」，全部只有一行
#
print(int((1 + 100) * 100 / 2), end="yeah\n")

# 4.在一行內印出 7 除 3的商和餘數，商沒有小數點
i1, i2 = 7, 3
#
print(i1 // i2, i1 % i2)

# 5.用三種格式化的方式，印出「今天我撿到 5 元」
money = 5
#
print("今天我撿到 %i 元" % money)
print(f"今天我撿到 {money} 元")
print("今天我撿到 {} 元".format(money))

# 6.將以下字串分開成獨立的五種水果，並刪除不需要的空格
fruits = "blueberry@ pineapple@ durian@ kiwi@tomato"
#
print(fruits.replace("@ ", "@").split("@"))

# 7.將變數 f，靠左、置中、靠右對齊
# 7.將變數 f，靠左、置中、靠右對齊，長度為 12
f = 98_7654.321
#
print("{0:<12}".format(f))
print("{0:^12}".format(f))
print("{0:>12}".format(f))

# 8.使用 str 的 format 功能，將 x 印出 + 號、y 前印出空格
# x、y 小數點只能印出 2 位
x, y = 578.6, 67.2
#
print("{:+.2f}".format(x))
print("{: .2f}".format(y))
