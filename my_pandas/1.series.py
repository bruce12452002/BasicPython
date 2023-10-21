import pandas as pd

# 官網連結
# https://pandas.pydata.org/docs/user_guide/index.html
'''
Series：長或寬(一維陣列)
'''
print("============ Series ============")
s = pd.Series([17, 25, 85, 7, 16, 77])
print(s.shape)  # (6,)
print(s.max())  # 85
print(s.min())  # 7
print(s.mean())  # 平均值
print(s.median())  # 21.0 中位數，如果是偶數，那取中間兩個除以2
print(s.sum())  # 227

# 最大和最小的前兩個數，會包括編號，如果有設定索引，會用索引取代編號
print(s.nlargest(2))
print(s.nsmallest(2))
print(s, s[1])  # 用編號取得
s *= 2  # 全部資料 * 2
print(s, s[1])
s2 = s <= 100  # 回傳布林 List
print(s2)

print('============ 建立索引 ============')
s = pd.Series([17, 25, 85, 7, 16, 77], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s, s[1], s['b'])  # 用編號和索引取得，索引要存在才不會報錯
print(s.dtype, s.size)
print(s.index)
print(s.values, s.values[2])
print(type(s.values[2]))  # 單值的型態是 numpy 裡的型態

print("============ 取多值 ============")
print(s[['a', 'b']])
print(type(s[['a', 'b']]))  # 多值的型態是 Series

print("============ 將字典轉成 Series ============")
d = {"k1": 1, "k2": 2, "k3": 3}
sd = pd.Series(d)
print(sd, sd.index)

print('============ 字串操作 ============')
s = pd.Series(['aBc', 'a哇哈哈Z'])
# 字串操作要先變成 pandas 的 str
print(type(s.str))  # 並不是 str
print(s.str.lower())
print(s.str.cat(sep="--"))
print(s.str.len())

# contains replace
