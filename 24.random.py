import random

print("============ random  ============")
print(random.random())  # 回傳 0.0~1.0 之間的浮點數，不包括 1.0
print(random.uniform(5.3, 7.8))  # 回傳兩數之間的浮點數，有可能包括第二個參數，取決於 random() 的捨入，看源碼

print("============ randint、randrange  ============")
# 只能傳整數，之前的版本可傳浮點數
print(random.randint(3, 4))  # 回傳兩個參數之間的整數，兩個參數會包括

print(random.randrange(3, 4))  # 回傳兩個參數之間的整數，「不」包括第二個參數
print(random.randrange(1, 6, 2))  # 回傳兩個參數之間的整數，「不」包括第二個參數，間隔為2，所以這個例子只會出現1 3 5

print("============ choice  ============")
# choice 接收 seq，以下都只會取得 1 5 10
print(random.choice([1, 5, 10]))
print(random.choice((1, 5, 10)))
print(random.choice(range(1, 6, 4)))

print("============ shuffle  ============")
# 打亂 list 的位置，只支援 list
my_list = [9, 5, 2, 7]
random.shuffle(my_list)
print(my_list)
