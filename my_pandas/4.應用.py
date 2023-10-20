import pandas as pd

print("============ DataFrame ============")
c = pd.read_csv("./csv_file.csv")
print(c['姓名'], type(c['姓名']))  # 一個欄位回傳 Series
print(c[['姓名', '電話']], type(c[['姓名', '電話']]))  # 多個欄位回傳 DataFrame

print("============ 查一行 ============")
print(c.loc[1], type(c.loc[1]))  # 查第 1 行，從 0 開始，是 Series 型態

print("============ 查多行 ============")
print(c.loc[1:3], type(c.loc[1:3]))  # 這裡和 list 不太一樣，會包括最後的數字，是 DataFrame 型態

print("============ update1 ============")
c.set_index('姓名', inplace=True)
print(c.loc[:, '電話'])
c.loc[:, '電話'] = c['電話'] + 1000  # 數字增減
print(c.head())
print(c.dtypes)

print("============ update2 ============")
w = pd.read_csv("./weather.csv")
print(w.head())
w.set_index('ymd', inplace=True)
print(w.loc[:, 'high'])  # index 不能設定
w.loc[:, 'high'] = w['high'].str.replace('°C', '')  # 字串增減
w.loc[:, 'low'] = w['low'].str.replace('°C', '').astype('int32')  # 字串增減 TODO astype 轉換型態失敗
print(w.dtypes)
print(w.head())

print("============ 精確查詢 ============")
print(w.loc[['2022-01-01', '2022-01-03', '2022-01-05'], 'high'])
print(w.loc[['2022-01-01', '2022-01-03', '2022-01-05'], ['low', 'high']])

print("============ 範圍查詢 ============")
print(w.loc['2022-01-03': '2022-01-05', 'high'])

print("============ 條件查詢 ============")
print(c.loc[c['電話'] > 10000, :])  # : 可省略
print(c.loc[(c['電話'] > 10000) & (c['血型'] == 'A')])

print("============ lambda ============")
print(c.loc[lambda lc: (c['電話'] > 10000) & (c['血型'] == 'A'), :])


def query(w2):
    return w2.index.str.startswith('2022-01-01') & (w2['high'] == '15')


print(w.loc[query, :])
