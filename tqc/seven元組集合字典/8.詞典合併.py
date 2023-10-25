"""
請撰寫一程式，自行輸入兩個詞典
（以輸入鍵值”end”作為輸入結束點，詞典中將不包含鍵值”end”）
將此兩詞典合併，並根據key值字母由小到大排序輸出
如有重複key值，後輸入的key值將覆蓋前一key值。

輸入與輸出會交雜如下，輸出的部份以粗體字表示
**Create dict1:**
**Key:** a
**Value:** apple
**Key:** b
**Value:** banana
**Key:** d
**Value:** durian
**Key:** end

**Create dict2:**
*Key:** c
*Value:** cat
*Key:** e
**Value:** elephant
**Key:** end

a: apple
b: banana
c: cat
d: durian
e: elephant
"""
my_title = ["Create dict1:", "Create dict2:"]
my_dict_in_list = [{}, {}]

for i in range(len(my_title)):
    print(my_title[i])
    while True:
        k = input("Key: ")
        if k == 'end':
            break
        v = input("Value: ")
        my_dict_in_list[i][k] = v

one = my_dict_in_list[0]
two = my_dict_in_list[1]
one.update(two)
rtn = sorted(one.items())

for k, v in rtn:
    print(f"{k}:", v)
