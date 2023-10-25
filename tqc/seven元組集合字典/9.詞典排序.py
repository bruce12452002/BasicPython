"""
請撰寫一程式，輸入一顏色詞典color_dict
（以輸入鍵值”end”作為輸入結束點，詞典中將不包含鍵值”end”），
再根據key值的字母由小到大排序並輸出。

輸入與輸出會交雜如下，輸出的部份以粗體字表示
**Key: **Green Yellow
**Value: **#ADFF2F
**Key: **Snow
**Value: **#FFFAFA
**Key: **Gold
**Value: **#FFD700
**Key: **Red
**Value: **#FF0000
**Key: **White
**Value: **#FFFFFF
**Key: **Green
**Value: **#008000
**Key: **Black
**Value: **#000000
**Key: **end

Black: #000000
Gold:#ffd700
Green: #008000
Green Yellow:#ADFF2F
Red:#ff0000
Snow:#FFFAFA
White:#ffffff
"""

# 注意 708 key 有說不可重覆，但這題 709 key 沒說，可能是要重覆

my_list = []
while True:
    my_dict = {}
    k = input("Key: ")
    if k == 'end':
        break
    v = input("Value: ")
    my_dict[k] = v
    my_list.append(my_dict)

new_list = []
for i in my_list:
    for k in i.items():
        new_list.append(k)
new_list.sort()

for m in new_list:
    print(m[0], m[1], sep=": ")
