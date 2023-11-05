# 定義類別，屬性:屬性類型=預設值，屬性類型可不寫，寫不寫值都可以亂給，只是給使用的人參考，比較不會有例外發生
# self 名稱可亂打，但不建議，表示實體自己
# java 的靜態屬性相當於 python 的類別屬性

class Animal1:
    """動物的類別"""
    c: int = 1  # 類別屬性

    def m(self) -> int:
        return self.c


print("============ 類別 ============")
print(Animal1.__doc__)  # 查看註解內容，使用 help(Animal) 也可以
print(Animal1.__name__)  # 類別名稱，str 型態
print(help(Animal1))

print("============ 類別和實體 ============")
# 要查詢實體的值要用實體去點；要查詢類別的值要用類別去點
a = Animal1()
print(a.c)  # 1
a.c = 2  # 修改實體屬性
print(f"{a.c} {a.m()} {Animal1.c}")  # 2 2 1
Animal1.c = 3  # 修改類別屬性
print(f"{a.c} {a.m()} {Animal1.c}")  # 2 2 3

print("============ 類別和實體2 ============")


class Animal2:
    def __init__(self):  # 建構子為程式的進入點，注意是 init，不是 int
        self.c: int = 1  # 實體屬性

    def m(self) -> int:
        return self.c


a = Animal2()
print(a.c)  # 1
a.c = 2
# print(Animal2.c)  # c是實體屬性，不是類別屬性，所以報錯
print(f"{a.c} {a.m()}")  # 2 2
Animal2.c = 3
print(f"{a.c} {a.m()}")  # 2 2

print("============ 類別和實體3 ============")


# 類別和實體的屬性一樣時，不會影響

class Animal3:
    """動物的類別"""
    c: int = 1

    def __init__(self):
        self.c: int = 1

    def m(self) -> int:
        return self.c


a = Animal3()
print(a.c)  # 1
a.c = 2
print(f"{a.c} {a.m()} {Animal3.c}")  # 2 2 1
Animal3.c = 3
print(f"{a.c} {a.m()} {Animal3.c}")  # 2 2 3

print("============ 每個實體有不同的位址 ============")
a1 = Animal1()
a2 = Animal1()
print(a1, a2)  # 可查看每個實體的位址(16進位)
print(id(a1), id(a2))  # id() 可查看每個實體的位址(10進位)
print(type(a1), type(Animal1))  # 實體可看出什麼型態；所有物件的型態都是 type
print(hex(id(a1)), hex(id(a2)))  # 將 id 轉成 16 進制
print(isinstance(a1, Animal1))  # a1 是否是 Animal 的實體
