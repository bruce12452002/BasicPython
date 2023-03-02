# 不重覆的 list 為 set，不會按照新增的順序排列，也不支援索引，所以無法用 while 遍歷
# set 用的是花括號，但空的花括號指的是 dict，空 set 是 set()

print("============ 初始化 set ============")
my_set1 = {1, 3, 5, 7, 9, 7, 5, 3, 1}  # {} 表示 dict，不是空 set
my_set2 = set("abc")  # 會拆開成三個元素； set() 是空 set； 這種方式初始化，只能是 0 或 1 個元素
print(f"{my_set1}, {type(my_set1)}")
print(f"{my_set2}, {type(my_set2)}")
print(set({"abc": "ddd"}))  # 只會有 key，key 不會拆開
print({"abc": "ddd"})  # 只會有 key，key 不會拆開

print("============ 可 hash ============")
digit = 1
my_float = 2.3
boolean = True
print(digit.__hash__())
print(my_float.__hash__())
print(boolean.__hash__())
print("".__hash__())
print(().__hash__())
# 以上的值都不可變

# print([].__hash__())  # list 報錯
print({}.__hash__)  # dict 為 None
print({1}.__hash__)  # set 為 None

print("============ set 元素只可放可 hash 的 ============")
my_set3 = {()}
print(f"{my_set3}, {type(my_set3)}")
# my_set4 = {{}}  # TypeError: unhashable

print("============ 常用方法-查詢 ============")
print(5 in my_set1)
new_my_set = my_set1.pop()  # 取第一個元素並刪除，但 set 並無順序，加入時不曉得誰會在第一個
print(new_my_set)

print("============ 常用方法-增加 ============")
my_set2.add("d")
my_set2.add("b")
my_set2.add("d")
print(my_set2)
print(my_set2.pop())
print(my_set2)

print("============ 常用方法-修改 ============")
my_set2.update({1: "xxx", "a": "bbb"})  # 將資料結構覆蓋到左邊，如果資料結構是 dict 只取 key
print(my_set2)

print("============ 常用方法-刪除 ============")
my_set2.remove("a")  # 元素必需存在，否則報錯
my_set2.discard("a")  # 元素不存在也不會報錯
print(my_set2)

my_set2.clear()
print(my_set2)

print("============ set 運算-str ============")
# 聯集 union，等同 |
# 交集 intersection，等同 &
# 差集 difference，等同 -
# 互斥 symmetric_difference，等同 ^

a = set('abracadabra')
b = set('alacazam')
print(f"{a}, {b}")
print(a | b)  # 將兩個組成一個 set
print(a.union(b))
print(a & b)  # 以左為主，將「不同」的去除
print(a.intersection(b))
print(a - b)  # 以左為主，將「相同」的去除
print(a.difference(b))
print(a ^ b)  # XOR，左有右沒有或者右有左沒有的就留下
print(a.symmetric_difference(b))
print(f"{a}, {b}")  # 以上都不會改變原值

print("============ set 運算-set ============")
diff1 = {9, 5, 8, 4}
diff2 = {7, 3, 2, 9}
new_diff = diff1.difference(diff2)  # 845 回傳左有右沒有的元素，「不會」改變兩組原集合
print(diff1 - diff2, new_diff)

diff1.difference_update(diff2)  # 和 difference 一樣，但「會」改變左邊的原集合
print(diff1)  # 845
print(diff2)

new_diff2 = diff1.union(diff2)  # 回傳合併的兩組元素，「不會」改變原集合
print(diff1 | diff2, new_diff2)
print(len(new_diff2))

print("============ 子 set ============")
# issubset()，等同 <=，左邊是否為右邊的子 set
# issuperset()，等同 >=，右邊是否為左邊的子 set

diff1 = {9, 5, 8, 4}
diff2 = {4, 8, 5, 9, 7}
print(diff1.issubset(diff2))
print(diff1 <= diff2)
print(diff2.issuperset(diff1))
print(diff2 >= diff1)

print("============ 轉換 ============")
my_set2 = {1, 2, 3}
s1 = list(my_set2)
s2 = tuple(my_set2)
print(f"{s1}, {type(s1)}")
print(f"{s2}, {type(s2)}")
# dict 不可轉換成 list、tuple、set，但相反可以，但只取的到 key

print("============ for + set ============")
for e in new_diff2:
    print(e)

print("============ 類別去重 ============")


class Cat:
    def __init__(self, num, name) -> None:
        self.num = num
        self.name = name

    def __hash__(self) -> int:
        return self.num

    def __eq__(self, o: object) -> bool:
        return self.num == o.num


c1 = Cat(22, "kiki")
c2 = Cat(55, "kaka")
c3 = Cat(22, "mimi")
c4 = Cat(66, "haha")
c5 = Cat(22, "kuku")
s = {c1, c2, c3, c4, c5}
for i in s:
    print(f"{i.name}, {i.num}")

print(c1 == c2)
print(c1 == c3)
