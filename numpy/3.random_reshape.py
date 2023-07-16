import numpy as np

print("============ random 隨機浮點數 [0~1) ============")
print(np.random.random())  # 一個元素
print(np.random.random(3))  # 三個元素

print("============ rand 隨機浮點數 [0~1) ============")
print(np.random.rand())  # 產生 1 個 0 維陣列
print(np.random.rand(1))  # 產生 1 個 1 維陣列
print(np.random.rand(3))  # 產生 3 個 1 維陣列

print(np.random.rand(3, 2))  # 產生 3 橫 2 直的二維陣列
print(np.random.rand(3, 2, 4))  # 產生 3*2*4 的三維陣列

print("============ randint 隨機整數 ============")
print(np.random.randint(5))  # [0~5)
print(np.random.randint(2, 5))  # [2~5)
print(np.random.randint(2, 10, size=(3,)))  # [2~10)，一維陣列有三個值，也就是 1 * 3
print(np.random.randint(2, 10, size=(3, 5)))  # [2~10)，二維陣列，3 行 5 列

print("============ choice 指定的隨機整數 ============")
print(np.random.choice(3))  # [0~3)
print(np.random.choice(3, 5))  # [0~3) 取 5 個
print(np.random.choice(3, (2, 3)))  # [0~3)，二維陣列，2 行 3 列

print(np.random.choice([3, 7, 11, 17], 3))  # 指定的值隨機 取 5 個
print(np.random.choice([3, 7, 11, 17], (2, 3)))  # 指定的值隨機取 2*3 個並轉換成二維陣列

print("============ shuffle 重新洗牌 ============")
# 會改變原來的陣列
a = np.arange(10)
np.random.shuffle(a)
print(a)

b = np.arange(15).reshape((3, 5))
np.random.shuffle(b)  # 一維陣列裡的內容不會重新洗牌，洗的是二維陣列裡的一維陣列的順序
print(b)

print("============ permutation 重新排序 ============")
print(np.random.permutation(10))  # 相當於 arrange 後再 shuffle

# 返回新的陣列，不會改變原陣列，仍然不會改變一維陣列裡的順序
print(np.random.permutation(b))
print(b)

print("============ reshape，整理成新的陣列 ============")
reshape = np.arange(6).reshape(2, 3)  # 重整成 2 維陣列，元素有 3 個，無法平均分配會報錯
print(reshape, type(reshape))
print(reshape + 1)  # 可直接對陣列做操作
print(reshape ** 2)  # 可直接對陣列做操作
r = np.random.rand(2, 3)
print(reshape + r)  # 形狀一樣可直接操作
