print("============ 實體屬性 ============")


class Teacher:
    # 預設建構子
    # def __init__(self):
    #     pass

    # __init__ 就是建構子，如果寫多個建構子，後者蓋前者
    def __init__(self, num, name):
        self.num = num
        self.name = name


# Teacher()  # 執行期會報錯，因為必須要傳兩個參數
t1 = Teacher(999, "孔子")
print(t1.num, t1.name)

t2 = Teacher(888, "孟子")
print(t2.num, t2.name)
print(t1.num, t1.name)  # 實體和實體不會被影響

print("============ 類別屬性 ============")


class Teacher2:
    class_set = set()  # 寫在這，類別屬性會影響所有實體

    def __init__(self, num):
        self.class_set.add(num)
        self.self_set = set()  # 寫在這，所有實體會有自己的 self_set

    def add_name(self, name):
        self.self_set.add(name)


tea1 = Teacher2(888)
tea1.add_name("xxx")
print(tea1.class_set, tea1.self_set)

tea2 = Teacher2(999)
tea2.add_name("ooo")
print(tea2.class_set, tea2.self_set)
print(tea1.class_set, tea1.self_set)
