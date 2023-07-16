import numpy as np

a = np.arange(1, 11).reshape(2, 5)
b = np.arange(1, 6)

print("============ basic ============")
print(np.min(a))
print(np.max(a))
print(np.average(a))  # 同 np.mean(a)
print(np.median([7, 11, 5, 20]))  # 排序後，如果是偶數，將中間兩個值相加/2
print(np.median([7, 11, 5, 20, 27]))  # 排序後，如果是奇數，取最中間的值
print(np.sum(a))  # 1+2+3+...10
print(np.prod(b))  # 1*2*3*4*5
print(np.cumsum(a))  # 01相加 12相加...的結果
print(np.cumprod(b))  # 01相乘 12相乘...的結果
