import pandas as pd

'''
DataFrame：長*寬(二維陣列)
'''
print('============ DataFrame ============')
df = pd.DataFrame({'name': ['apple', 'banana', 'strawberry', 'pineapple'],
                   'price': [25, 17, 38, 40]})
print(df, end='\n=====\n')
print(df['price'], end='\n=====\n')  # 取 column
print(df.iloc[1], df.loc[1])  # 取 row

print('============ 建立索引 ============')
# 建了索引之後，loc 就只能放索引值了，但仍然可以用 iloc
df = pd.DataFrame({'name': ['apple', 'banana', 'strawberry', 'pineapple'],
                   'price': [25, 17, 38, 40]}, index=['a', 'b', 'c', 'd'])
print(df.iloc[1], df.loc['b'])  # 取 row
print(df.size, df.shape)
print(df.index)
print(df.values)  # [['apple' 25] ['banana' 17] ['strawberry' 38]
print(df.values[1])  # ['banana' 17]
print(df.values[1][1])  # 17

print('============ 字串操作 ============')
print(df['name'].str.upper())

print('============ 增加 column ============')
# df['place'] = ['日本', '德國', '非洲', '義大利']

# 以下的方式也行，但不指定 index，資料是 NaN
df['place'] = pd.Series(['日本', '德國', '非洲', '義大利'], index=['b', 'c', 'a', 'd'])
print(df)

# 根據舊資料給新資料
df['xxx'] = df["price"] * 2
print(df)
