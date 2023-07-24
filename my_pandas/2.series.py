import numpy as np
import pandas as pd

print("============ Series ============")
# Series 相當於一維陣列
s = pd.Series([True, 2, 'yes', 5.5])
print(s, s.index)
print(s.values, s.values[2])

print("============ 自訂索引 ============")
si = pd.Series([True, 2, 'yes', 5.5], index=['i', 'ii', 'iii', 'iiii'])
print(si, si.index)
print(si.values, si.values[2])

print("============ 將字典轉成 Series ============")
d = {"k1": 1, "k2": 2, "k3": 3}
sd = pd.Series(d)
print(sd, sd.index)

print("============ 取值 ============")
# 索引要存在才不會報錯
print(s[3])
print(si['ii'])
print(sd['k2'])

# 仍然可用預設的數字索引，但超過下標就會報錯
# print(s[5])
print(si[0])
print(sd[0])
print(type(sd['k1']))  # 單值的型態是 numpy 型態

print("============ 取多值 ============")
print(si[['ii', 'iii']])
print(type(si[['ii', 'iii']]))  # 多值的型態是 Series
