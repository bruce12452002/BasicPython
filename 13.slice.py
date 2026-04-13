# 字串、list、tuple 都適用，set、dict 不支援索引，所以不適用
# 取單值時，一個數字即可，有支援負數
# 取多值時，至少要寫一個 「:」[開始索引:結束索引:步長]
# 正序預設為 [0:變數的長度:1]； 倒序只要最後一個為負數就是倒序，預設為 -1:-長度-1:負數
# [a:b:c] c 如果是負數是從後取前的意思，這時 b 要小於 a 才會有值，否則是空的
my_tuple = ("a", "b", "c", "d", "e", "f")
# print(my_tuple[0:len(my_tuple):1]) # 正序
# print(my_tuple[-1:-len(my_tuple)-1:-1]) # 倒序
print(my_tuple[1:5])  # b~e
print(my_tuple[-2:-1])  # e
print(my_tuple[-1])  # f
print(my_tuple[0:5:2])  # ace
print(my_tuple[2::2])  # ce
print(my_tuple[2:])  # c~f
print(my_tuple[:])  # 全部
print(my_tuple[0:])  # 全部
print(my_tuple[0::])  # 全部
print(my_tuple[0::1])  # 全部
print(my_tuple[1:-2:]) # bcd，從 1 開始取，而 -2 也是 4
print(my_tuple[::-1])  # 負數在最後面是倒著取
print(my_tuple[4:1:-1])  # edc
print(my_tuple[-2:-6:-1]) # edcb
print(my_tuple[1:-7:-1]) # ba，從 1 開始取，而1也是 -5，然後往前取到 a
print(my_tuple[::-1][0:2])  # 倒著取之後再取前兩個，所以是 fe


