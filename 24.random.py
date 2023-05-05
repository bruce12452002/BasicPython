import random

print("============ random、uniform，回傳 float ============")
print(random.random())  # 回傳 0.0~1.0 之間的浮點數，不包括 1.0
print(random.uniform(5.3, 7.8))  # 回傳兩數之間的浮點數，有可能包括第二個參數，取決於 random() 的捨入，看源碼

print("============ randint、randrange，回傳 int ============")
# 只能傳整數，之前的版本可傳浮點數
print(random.randint(3, 4))  # 回傳兩個參數之間的整數，兩個參數會包括

print(random.randrange(3, 4))  # 回傳兩個參數之間的整數，「不」包括第二個參數
print(random.randrange(1, 6, 2))  # 回傳兩個參數之間的整數，「不」包括第二個參數，間隔為2，所以這個例子只會出現1 3 5

print("============ choice，回傳 int ============")
# choice 接收 seq，以下都只會取得 1 5 9
print(random.choice([1, 5, 9]))
print(random.choice((1, 5, 9)))
print(random.choice(range(1, 10, 4)))

print("============ shuffle ============")
# 打亂 list 的位置，只支援 list
my_list = [9, 5, 2, 7]
random.shuffle(my_list)
print(my_list)

print("============ sample，回傳 list ============")
print(random.sample("abcde", 3))  # 從 a~e 隨機產生不重覆的 3 個，超過 5 會報錯
print(random.sample(["a", 'b', "c", 'd', "e"], 3))
print(random.sample(("a", 'b', "c", 'd', "e"), 3))
print(random.sample(range(97, 102), 3))
print(random.sample(list(r for ch in range(97, 102) for r in chr(ch)), 3))
