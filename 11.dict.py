# key 重覆會被後者覆蓋，也不支援索引，所以不能用 while 遍歷
# dict 用的也是花括號，但裡面是鍵值對
# dict 的 key 只能是可 hash 的；value 都可以

print("============ 初始化 dict 一 ============")
my_dict1 = {"k1": 1, "k2": 2}
my_dict2 = {}
my_dict3 = dict()  # 裡面的元素不會拆開，用法和 my_dict1 一樣
print(f"{my_dict1}, {type(my_dict1)}")
print(f"{my_dict2}, {type(my_dict2)}")
print(f"{my_dict3}, {type(my_dict3)}")
print(my_dict1["k1"])

print("============ 初始化 dict 二 ============")
d1 = dict(a="apple", b="banana", c="cat")
print(f"{d1}, {type(d1)}", end=" ")
print()

d2 = dict([('d', "duck"), ('e', "elephant"), ('f', "fox")])
print(f"{d2}, {type(d2)}", end=" ")
print()

d3 = {x: x**2 for x in (2, 4, 6)}  # x 為 key，value 為平方
print(f"{d3}, {type(d3)}", end=" ")
print()

dt = {'sep': ',', 'end': '\n\n'}
print('hello', 'world', **dt)

print("============ dict 可嵌套 ============")
sango = {
    "關羽": {
        "攻擊力": 98,
        "智力": 85
    },
    "孔明": {
        "攻擊力": 58,
        "智力": 100
    },
    "劉備": {
        "攻擊力": 77,
        "智力": 88
    }
}
print(sango["關羽"])
print(sango["關羽"]["攻擊力"])

print("============ 常用方法-增加 ============")
print("============ 常用方法-修改 ============")
my_dict4 = {"k1": 100, "k2": 20}
my_dict4["k3"] = 300  # key 沒有就增加，有就修改
my_dict4["k2"] = 200  # key 沒有就增加，有就修改
print(my_dict4)

print(my_dict4.pop("k3"))
# print(my_dict4.pop("k3"))  # 不可刪除不存在的key，執行期會報錯
print(my_dict4)

print("============ 常用方法-查詢 ============")
# 取得所有 key 和 values，可以轉成 list set tuple
all_key = my_dict4.keys()
all_values = my_dict4.values()
print(f"{all_key}, {type(all_key)}")
print(f"{all_values}, {type(all_values)}")

print("============ 常用方法-刪除 ============")
del my_dict4["k1"]  # key 不在會報錯
print(my_dict4)

my_dict4.clear()
print(my_dict4)

print("============ loop + dict ============")
my_dict4 = {"k1": 100, "k2": 20}

for d in my_dict4:  # 只會遍歷 key
    print(d, end=" ")
print()

for d in my_dict4.keys():
    print(d, end=" ")
print()

for d in my_dict4.values():
    print(d, end=" ")
print()

for k, v in my_dict4.items():
    print(k, v, end=" ", sep="=")
print()

print(len(my_dict4))
