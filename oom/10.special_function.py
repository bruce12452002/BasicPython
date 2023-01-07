# 常見特殊方法 __init__、__str__、__gt__、__lt__、__ge__、__le__、__eq__、__ne__

class Teacher:
    def __init__(self, num, name):  # __init__ 就是建構子，如果寫多個建構子，後者蓋前者
        self.num = num
        self.name = name

    def __str__(self):  # 印出物件時，會自動調用，如沒定義，或使用 str() 會印出記憶體位址
        return f"name={self.num}, name={self.name}"

    def __gt__(self, other):
        return self.num > other.num

    def __lt__(self, other):
        return self.num < other.num

    # def __ge__(self, other):
    #     return self.num >= other.num

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num


t1 = Teacher(999, "孔子")
print(t1)
print(str(t1))
t2 = Teacher(888, "孟子")
print(t1 < t2)  # 類別裡要定義 __lt__ 或 __gt__ 才不會報錯，兩個都寫沒關係
# print(t1 <= t2)  # 類別裡要定義 __le__ 或 __ge__ 才不會報錯，兩個都寫沒關係
# print(t1 == t2)  # 如果沒定義 __eq__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 True，不影響 != 的判斷
# print(t1 != t2)  # 如果沒定義 __ne__，比較的是記憶體位址. 有定義的話 9 和 9.0 會是 False，不影響 == 的判斷
