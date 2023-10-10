# list 用的是方括號
# list、tuple、range 都叫 sequence

print("============ 初始化 list 一 ============")
a = list("abc")  # 會拆開成三個元素； 這種方式初始化，只能是 0 或 1 個元素
# a = list(1)  # is not iterable
print(f"{a}, {type(a)}")  # 會拆開成三個元素

print("============ 初始化 list 二 ============")
myList1 = [1, 2, 3]
myList2 = ["1", 2, False]
print(f"{myList1}, {type(myList1)}")
print(f"{myList2}, {type(myList2)}")
print(list({"abc": "ddd"}))  # 只會有 key，key 不會拆開

print("============ list 可嵌套 ============")
myList3 = [[1, 2, 3], ["1", 2, False]]
print(f"{myList3}, {type(myList3)}")
print(myList1[0], myList1[1], myList1[-1])
# print(myList1[3])  # list index out of range
print(myList3[0][1])
print(myList3[1][2])

print("============ 常用方法-查詢 ============")
list2_index = myList2.index(False)  # 取得第一次得到的索引值，因為 list 可重覆
print(f"list2.index={list2_index}")
# list2_index_error = myList2.index("xxx")  # 找不到報錯

e = myList2.pop(-1)  # 將元素取出並刪除，如果 pop 不給參數，就是刪最後一個，也就是 stack 的功能
print(myList2)
print(e)

myList2.reverse()
print(myList2)

myList4 = ["o", "x", "x", "o", "o", "x"]
print(myList4.count("x"))
print(len(myList4))

print("x" in myList4)

print("============ 常用方法-修改 ============")
myList2[1] = 999
print(myList2)
myList2[-1] = None
print(myList2)
# myList2.sort()  # 由小到大排序，會修改原本的 list，但要注意，內容必需是同樣的型態

print("============ 常用方法-增加 ============")
myList2.append("end")  # 在最後增加元素
print(myList2)
myList2.insert(1, "hahaha")  # 在指定索引增加元素，原來的值到最後會往後移
print(myList2)
myList2.extend(["a", "b"])  # 在最後一次增加多個元素
print(myList2)

print("============ 常用方法-刪除 ============")
del myList2[-1]  # 只有 list 可對索引刪除，如沒有索引是刪除整個變數
print(myList2)
myList2.remove("a")  # 刪除第一次得到的值，元素必需存在，否則報錯
myList2.clear()
print(myList2)

print("============ 常用方法-其他 ============")
myList5 = [7, 6.2, 5, 4.5]
print(sum(myList5), max(myList5), min(myList5))  # 只支援數字和浮點數

print("============ 轉換 ============")
myList2 = [1, 2, 3]
s1 = set(myList2)
s2 = tuple(myList2)
print(f"{s1}, {type(s1)}")
print(f"{s2}, {type(s2)}")
# dict 不可轉換成 list、tuple、set，但相反可以，但只取的到 key

print("============ loop + list ============")


def list_while():
    """
    使用 while 循環 list
    :return: None
    """
    my_list = ["a", "b", "c"]

    i = 0
    while i < len(my_list):
        element = my_list[i]
        print(f"元素為{element}", end=' ')
        i += 1


list_while()
print()


def list_for():
    """
    使用 for 循環 list
    :return: None
    """
    my_list = ["a", "b", "c"]

    i = 0
    for m in my_list:
        print(f"元素為{m}", end=' ')
        i += 1


list_for()
print()


def list_for_range():
    """
        使用 for-range 循環 list
        :return: None
        """
    my_list = ["a", "b", "c"]

    i = 0
    for m in range(len(my_list)):
        v = my_list[m]
        print(f"元素為{v}", end=' ')
        i += 1


list_for_range()
print()

my_list = ["a", "b", "c"]
for i, v in enumerate(my_list):
    print(i, v, sep="=")

print("============ for + list 刪除 ============")
# for + list 刪除時，index 會自動往上，所以如果有連續相同的資料，後面會刪不到
my_list = ["a", "b", "b", "c"]
KEY = "b"
for i in my_list:
    if i == KEY:
        my_list.remove(KEY)
print(my_list)

# 解決方法是從後面開始刪除
my_list = ["a", "b", "b", "c"]
KEY = "b"
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == KEY:
        my_list.remove(KEY)
print(my_list)

print("============ 雙向佇列 ============")
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.popleft()  # 只用 popleft 為佇列的功能，先進先出
print(queue)
