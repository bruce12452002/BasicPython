# 常見特殊方法 __init__、__str__、__gt__、__lt__、__ge__、__le__、__eq__、__ne__

class Teacher:
    def __init__(self, num, name):  # __init__ 就是建構子，如果寫多個建構子，後者蓋前者
        print("__init__")
        self.num = num
        self.name = name

    """
    __str__ 和 __repr__ 類似 java 的 toString()
    __str__ 給用戶看，str() 會調用
    __repr__ 給開發看，repr() 會調用
    印物件實體時，先調用 __str__，沒有就調用 __repr__； 都沒有印記憶體位址
    """
    def __str__(self):
        return f"num={self.num}, name={self.name}"

    def __repr__(self) -> str:
        return f"name={self.name}, num={self.num}"

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    # def __ge__(self, other):
    #     return self.num >= other.num

    def __eq__(self, other):  # is 比較記憶體位址； == 會調用 __eq__
        print("__eq__")
        if not isinstance(other, Teacher):
            return False
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num

    def __hash__(self) -> int:
        print("__hash__")
        return hash(self.num + self.name)

    """
    bool() 時，先調用 __bool__，沒有就調用__len__
    """
    def __bool__(self):
        print("__bool__")
        return self.num > 5

    def __len__(self):
        print("__len__")
        return len(self.name) - 1

    def __del__(self):  # 物件被回收之前會自動調用
        print("__del__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)


t1 = Teacher(999, "孔子")
print(t1, type(t1))
print(str(t1))
t2 = Teacher(888, "孟子")
print(t1 < t2)  # 類別裡要定義 __lt__ 或 __gt__ 才不會報錯，兩個都寫沒關係
# print(t1 <= t2)  # 類別裡要定義 __le__ 或 __ge__ 才不會報錯，兩個都寫沒關係
# print(t1 == t2)  # 如果沒定義 __eq__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 True，不影響 != 的判斷
# print(t1 != t2)  # 如果沒定義 __ne__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 False，不影響 == 的判斷

set().add(Teacher("999", "孔子"))
print(bool(Teacher))  # 如果沒定義 __bool__，會調用 __len__，再沒有就是 True
print(len(t1))

print("============ __new__ 和 __int__ ============")
# 會先執行 __new__
# 如果 __new__ 回傳的是自己的實體才會再執行 __init__


class Student:
    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        # return super().__new__(cls)
        return super().__new__(Teacher)


s1 = Student()
