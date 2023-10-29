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
print(my_dict1["k1"], my_dict1.get("k1"))  # 用[]取值，如 key 沒有會報錯；但 get 不會

print("============ 初始化 dict 二 ============")
d1 = dict(a="apple", b="banana", c="cat")
print(f"{d1}, {type(d1)}", end=" ")
print()

d2 = dict([('d', "duck"), ('e', "elephant"), ('f', "fox")])
print(f"{d2}, {type(d2)}", end=" ")
print()

d3 = {x: x ** 2 for x in (2, 4, 6)}  # x 為 key，value 為平方
print(f"{d3}, {type(d3)}", end=" ")
print()

dt = {'sep': ',', 'end': '\n\n'}
print('hello', 'world', **dt)

print("============ dict 可嵌套、可巢狀 ============")
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
print(my_dict3)
my_dict3.setdefault("a", 1)  # 如果 key 沒有才新增, 這行還沒有1，所以會新增進去，且回傳值為 1
kk = my_dict3.setdefault("a", 100)  # 因為已經有 a 了，所以不會新增成功，回傳值為目前已有的值 1
my_dict3.setdefault("b")  # 只有一個參數時，value 為 None
my_dict3['c'] = 'xxx'
print(my_dict3, kk)

# 從其他資料結構轉成 dict，如果有第二個參數為 key 的 value
print(dict.fromkeys(["a", "b"]))
print(dict.fromkeys(("a", "b")))
print(dict.fromkeys({"a", "b"}, 100))
print(dict.fromkeys(my_dict3))  # 原本已有的 dict 的 key，value 是 None

print("============ 常用方法-修改 ============")
my_dict4 = {"k1": 100, "k2": 20}
my_dict4["k3"] = 300  # key 沒有就增加，有就修改
my_dict4["k2"] = 200  # key 沒有就增加，有就修改
print(my_dict4)
my_dict4_b = dict(k2=2000, k4=40)
my_dict4.update(my_dict4_b)  # 將右邊的 dict 覆蓋到左邊的 dict
print(my_dict4)

print("============ 常用方法-查詢 ============")
# 取得所有 key 和 values，可以轉成 list set tuple
all_key = my_dict4.keys()
all_values = my_dict4.values()
print(f"{all_key}, {type(all_key)}")
print(f"{all_values}, {type(all_values)}")

print(my_dict4.get("k1"), my_dict4.get("k3"), my_dict4.get("k3", 50))  # 取得對應的值，沒有就回傳 None 或第二個參數
print("a" in my_dict4)  # 判斷 key 是否存在

print("============ 常用方法-刪除 ============")
print(my_dict4.pop("k3"))  # 回傳並刪除
print(my_dict4.pop("k3", "yeah"))  # 不可刪除不存在的key，執行期會報錯，但如果有第二個參數，會回傳第二個參數
print(my_dict4.popitem())  # 隨機回傳一個元素並刪除，但空元素還是會報錯
print(my_dict4)

del my_dict4["k1"]  # key 不在會報錯
print(my_dict4)

my_dict4.clear()
print(my_dict4)

print("============ loop + dict ============")
my_dict4 = {"k1": 100, "k2": 20}

for d in my_dict4.keys():
    print(d, end=" ")
print()

for d in my_dict4.values():
    print(d, end=" ")
print()

for k, v in my_dict4.items():
    print(k, v, end=" ", sep="=")
print()

print("============ 以下用法了解即可，很少用 ============")
for d in my_dict4:  # 只會遍歷 key
    print(d, end=" ")
print()

for k1a, k1b in my_dict4:  # k1 和 k2 都是 2 長，所以可用兩個變數加；如果 3 長就用 3 個變數接
    print(f"{k1a}:", k1b, end=" ")
print()

for kv in my_dict4.items():
    print(kv)
    print(kv[0], kv[1], sep="=")
print()

print(len(my_dict4))
