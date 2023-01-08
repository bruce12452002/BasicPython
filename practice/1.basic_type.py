# 在一行內印出 i 和 s，中間用「,」隔開
i = 5
s = "str"

print(i, s, sep=",")

# 印出 bool 型態
b = True
print(type(b))

# 寫出 1+2+3+...+100 的公式，公式為：(前項+後項)乘項數除2，然後轉成整數型態，並在最後印出「 yeah\n」，全部只有一行
print(int((1 + 100) * 100 / 2), end="yeah\n")

# 在一行內印出 7 除 3的商和餘數，商沒有小數點
i1 = 7
i2 = 3
print(i1 // i2, i1 % i2)

# 用兩種格式化的方式，印出「今天我撿到 5 元」
money = 5

# 將以下字串分開成獨立的五種水果，並刪除不需要的空格
fruits = "blueberry, pineapple, durian, kiwi,tomato"
