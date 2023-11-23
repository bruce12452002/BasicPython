from decimal import *

print("============ 有誤差的浮點數 ============")
print(0.2 * 0.7)
print(Decimal(0.2) * Decimal(0.7))
print(Decimal("0.2") * Decimal("0.7"))

print("============ 四則運算 ============")
f1 = 0.1
f2 = 0.2
print(Decimal.from_float(f1))
print(Decimal(f1) + Decimal(f2))
getcontext().prec = 3  # 全部有幾位(不包括.)，預設 28，Decimal 運算過後才有效果
getcontext().rounding = ROUND_HALF_UP  # 預設是 ROUND_HALF_EVEN
print(Decimal("2.222") + Decimal("3.333"))  # 因為 prec = 3 會是 5.555 之後，然後再做捨入
f1f2 = Decimal(f1) + Decimal(f2)
print(f1f2)
print(f1f2.normalize())  # 將後面的 0 刪除

print("============ 捨入模式-無條件 ============")
# decimal.ROUND_UP       無條件進位，不分正負數
# decimal.ROUND_CEILING  無條件進位，分正負數，往正捨入

# decimal.ROUND_DOWN     無條件捨去，不分正負數
# decimal.ROUND_FLOOR    無條件捨去，分正負數，往負捨入

test = Decimal("2.543")
scale = '.0'
print(test.quantize(Decimal(scale), rounding=ROUND_UP))  # 2.6
print(test.quantize(Decimal(scale), rounding=ROUND_CEILING))  # 2.6
print(test.quantize(Decimal(scale), rounding=ROUND_DOWN))  # 2.5
print(test.quantize(Decimal(scale), rounding=ROUND_FLOOR))  # 2.5

test = Decimal("-2.543")
print(test.quantize(Decimal(scale), rounding=ROUND_UP))  # -2.6
print(test.quantize(Decimal(scale), rounding=ROUND_CEILING))  # -2.5
print(test.quantize(Decimal(scale), rounding=ROUND_DOWN))  # -2.5
print(test.quantize(Decimal(scale), rounding=ROUND_FLOOR))  # -2.6

print("============ 捨入模式-x捨y入 ============")
# 以下 normalize 後，遇到 5 的時候才有差，其他數字和四捨五入一樣，正負數只差負號而已

# decimal.ROUND_HALF_UP  四捨五入

# decimal.ROUND_HALF_DOWN
# 假設要取整，如果小數第一位是 5，還要再看第二位之後有沒有數字，有就進位；沒有則不進位

# ROUND_HALF_EVEN
# 奇數時是 ROUND_HALF_UP；偶數時是 ROUND_HALF_DOWN，假設要取整，那就看整數位是奇數還偶數
# round() 也是這個

# decimal.ROUND_05UP：假設要取整，整數位為 5 或 0 就進位，但沒小數位不進位(最後連續的0不算)

print("============ 1 ============")
# 以下測試，Decimal 放字串和浮點，結果相同
f = 5.5
test = Decimal(str(f))
scale = '1.'
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_UP))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_DOWN))  # 5
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_EVEN))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_05UP))  # 6
print(round(f))  # 6

print("============ 2 ============")
f = 5.55
test = Decimal(str(f))
scale = '1.'
print(test.quantize(Decimal(scale)))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_UP))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_DOWN))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_EVEN))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_05UP))  # 6
print(round(f))  # 6

print("============ 3 ============")
f = 6.5
test = Decimal(str(f))
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_UP))  # 7
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_DOWN))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_EVEN))  # 6
print(test.quantize(Decimal(scale), rounding=ROUND_05UP))  # 6
print(round(f))  # 6

print("============ 4 ============")
f = 6.51
test = Decimal(str(f))
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_UP))  # 7
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_DOWN))  # 7
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_EVEN))  # 7
print(test.quantize(Decimal(scale), rounding=ROUND_05UP))  # 6
print(round(f))  # 7

print("============ 5 ============")
f = 64.52
test = Decimal(str(f))
scale = '.0'
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_UP))  # 64.5
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_DOWN))  # 64.5
print(test.quantize(Decimal(scale), rounding=ROUND_HALF_EVEN))  # 64.5
print(test.quantize(Decimal(scale), rounding=ROUND_05UP))  # 64.6
print(round(f, 1))  # 64.5
print()
