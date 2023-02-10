# 常見特殊方法 __init__、__str__、__gt__、__lt__、__ge__、__le__、__eq__、__ne__

class Teacher:
    def __init__(self, num, name):  # __init__ 就是建構子，如果寫多個建構子，後者蓋前者
        self.num = num
        self.name = name

    def __str__(self):  # 印物件實體或 str()時調用
        return f"name={self.num}, name={self.name}"

    def __repr__(self) -> str:  # repr()
        return f"name={self.name}, name={self.num}"

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    # def __ge__(self, other):
    #     return self.num >= other.num

    def __eq__(self, other):
        print("__eq__")
        if not isinstance(other, Teacher):
            return False
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num

    def __hash__(self) -> int:
        print("__hash__")
        return hash(self.num + self.name)

    def __bool__(self):
        print("__bool__")
        return self.num > 5

    def __len__(self):
        print("__len__")
        return len(self.name) - 1

    def __del__(self):  # 物件被回收之前會自動調用
        print("__del__")


t1 = Teacher(999, "孔子")
print(t1)
print(str(t1))
t2 = Teacher(888, "孟子")
print(t1 < t2)  # 類別裡要定義 __lt__ 或 __gt__ 才不會報錯，兩個都寫沒關係
# print(t1 <= t2)  # 類別裡要定義 __le__ 或 __ge__ 才不會報錯，兩個都寫沒關係
# print(t1 == t2)  # 如果沒定義 __eq__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 True，不影響 != 的判斷
# print(t1 != t2)  # 如果沒定義 __ne__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 False，不影響 == 的判斷

set().add(Teacher("999", "孔子"))
print(bool(Teacher))  # 如果沒定義 __bool__，會調用 __len__，再沒有就是 True
print(len(t1))
