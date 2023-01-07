print("============ 屬性是單一型態 ============")


class Teacher:
    # 建構子如果有包括這兩個屬性，且是單一型態，連寫都不用寫，當然寫也不會報錯
    # num: int = None
    # name: str = None

    def __init__(self, num, name):  # __init__ 就是建構子，如果寫多個建構子，後者蓋前者
        self.num = num
        self.name = name


# Teacher()  # 執行期會報錯，因為必須要傳兩個參數
t1 = Teacher(999, "孔子")
print(t1.num, t1.name)

t2 = Teacher(888, "孟子")
print(t2.num, t2.name)
print(t1.num, t1.name)  # 單一型態寫在 class 裡，t1 不會被影響

print("============ 屬性是複合型態 ============")
"""
複合型態不可變和單一型態相同，因為無法變動元素
※list set dict 可變； tuple 不可變
"""


class Teacher2:
    num = set()  # 寫在這，複合屬性會影響所有實體

    def __init__(self, num):
        self.num.add(num)
        self.name = set()  # 寫在這，所有實體會有自己的 name

    def add_name(self, name):
        self.name.add(name)


teacher1 = Teacher2(888)
teacher1.add_name("xxx")
print(teacher1.num, teacher1.name)

teacher2 = Teacher2(999)
teacher2.add_name("ooo")
print(teacher2.num, teacher2.name)
print(teacher1.num, teacher1.name)
