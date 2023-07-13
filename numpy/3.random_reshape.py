import numpy as np

print("============ 以下的值都是隨機值 ============")
print(np.random.rand())  # 產生 1 個 0 維陣列
print(np.random.rand(1))  # 產生 1 個 1 維陣列
print(np.random.rand(3))  # 產生 3 個 1 維陣列

print(np.random.rand(3, 2))  # 產生 3 橫 2 直的二維陣列
print(np.random.rand(3, 2, 4))  # 產生 3*2*4 的三維陣列

print("============ reshape，整理成新的陣列 ============")
reshape = np.arange(6).reshape(2, 3)  # 重整成 2 維陣列，元素有 3 個，無法平均分配會報錯
print(reshape, type(reshape))
print(reshape + 1)  # 可直接對陣列做操作
print(reshape ** 2)  # 可直接對陣列做操作
r = np.random.rand(2, 3)
print(reshape + r)  # 形狀一樣可直接操作
