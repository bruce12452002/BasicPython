# tuple 和 list 一樣，只差在 tuple 的「元素」不可變(不可修改)
# tuple 用的是圓括號
print("============ 空 tuple ============")
my_tuple1 = ()
my_tuple2 = tuple()
print(f"{my_tuple1}, {type(my_tuple1)}")
print(f"{my_tuple2}, {type(my_tuple2)}")

print("============ 一個元素的 tuple ============")
my_tuple3 = tuple("abc")  # 會拆開成三個元素； 這種方式初始化，只能是 0 或 1 個元素
# my_tuple4 = (False)  # 這樣子還是 bool 型態
my_tuple5 = (False,)  # 這樣子才是 tuple 型態，可不用圓括號
print(f"{my_tuple3}, {type(my_tuple3)}")  # 會拆開成三個元素
# print(f"{my_tuple4}, {type(my_tuple4)}")
print(f"{my_tuple5}, {type(my_tuple5)}")
print(tuple({"abc": "ddd"}))  # 只會有 key，key 不會拆開

print("============ 多個元素的 tuple ============")
my_tuple6 = "a", 1, True
my_tuple7 = ("a", 1, True)
my_tuple6a = ["a"], [1], [True]
my_tuple7a = [["a"], [1], [True]]
print(type(my_tuple6a), type(my_tuple7a))  # tuple list

# my_tuple8 = tuple("a", 1, True)  # tuple() 多了 tuple 關鍵字，這時裡面只能是 0 或 1 個元素
print(f"{my_tuple6}, {type(my_tuple6)}")
print(f"{my_tuple7}, {type(my_tuple7)}")
# print(f"{my_tuple8}, {type(my_tuple8)}")
# my_tuple7[0] = "b"  # TypeError: 'tuple' object does not support item assignment
my_tuple7 = "haha"  # 內容不可變，但可以將整個變數指向的記憶體改掉
print(f"my_tuple7 = {my_tuple7}, {type(my_tuple7)}")

print("============ 常用方法 ============")
my_tuple8 = 1.1, False, "hehe", 1.1, "haha", 1.1
print(my_tuple8.index("hehe"))  # 給 key 回傳索引值，找不到會報錯
# 要注意 key 是 bool 時，可以找到 0、0.0、False、1、1.0、True
# 0 表示 False；1 表示 True，會從最左邊開始找，找到就會回傳索引值

print(my_tuple8.count(1.1))  # 找不到為 0
print(my_tuple8[0])
print(my_tuple8[-2])
print("haha" in my_tuple8)

print("============ tuple 可嵌套、可巢狀 ============")
my_tuple_tuple = ((1, 2, 3), ("a", "b"), [True, False])
print(my_tuple_tuple)
print(type(my_tuple_tuple))
print(my_tuple_tuple[0][1])
print(my_tuple_tuple[1][0])
print(my_tuple_tuple[2][0])
# print(my_tuple_tuple[3])  # IndexError: tuple index out of range
# my_tuple_tuple[0][1] = 4
# print(my_tuple_tuple)  # TypeError: 'tuple' object does not support item assignment
my_tuple_tuple[2][0] = False  # tuple 裡有 list，list 是可變的，所以可以修改
print(my_tuple_tuple[2])

print("============ 轉換 ============")
s1 = list(my_tuple_tuple[0])
s2 = set(my_tuple_tuple[0])
print(f"{s1}, {type(s1)}")
print(f"{s2}, {type(s2)}")
# dict 不可轉換成 list、tuple、set，但相反可以，但只取的到 key

print("============ loop + tuple ============")


def tuple_while():
    """
    使用 while 循環 tuple
    :return: None
    """
    my_tuple = ("a", "b", "c")

    i = 0
    while i < len(my_tuple):
        element = my_tuple[i]
        print(f"元素為{element}", end=' ')
        i += 1


tuple_while()
print()


def tuple_for():
    """
    使用 for 循環 tuple
    :return: None
    """
    my_tuple = ("a", "b", "c")

    i = 0
    for m in my_tuple:
        print(f"元素為{m}", end=' ')
        i += 1


tuple_for()
print()


def tuple_for_range():
    """
        使用 for-range 循環 tuple
        :return: None
        """
    my_tuple = ("a", "b", "c")

    i = 0
    for m in range(len(my_tuple)):
        v = my_tuple[m]
        print(f"元素為{v}", end=' ')
        i += 1


tuple_for_range()
print()

print("============ loop + tuple 裡是集合 ============")
tupled = ({"ab": "111", "cd": "222"})
tuples = ({"a", "b"}, {"c", "d"})
tuplet = (("a", "b"), ("c", "d"))
tuplel = (["a", "b"], ["c", "d"])

# k, v 是兩個變數，所以集合裡都得是兩個
# 注意 dict，只會取得 key，會 key 的長度，如果是 2 長，就可用 2 個變數
# 注意 set 的值，key value 有可能會調換
for k, v in tuplel:
    print(f"{k}:", v)
