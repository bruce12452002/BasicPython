# 字串、list、tuple 都適用，set、dict 不支援索引，所以不適用
# [開始索引:結束索引:步長] 預設為 [0:變數的長度:1]，至少要寫一個 : 或數字
# 所以 [:] = [0:] = [0:變數的長度] = [0:變數的長度:1] = 全部
my_tuple = ("a", "b", "c", "d", "e", "f")
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
print(my_tuple[::-1])  # 負數在最後面是倒著取
print(my_tuple[4:1:-1])  # edc
print(my_tuple[::-1][0:2])  # 倒著取之後再取前兩個，所以是 fe


