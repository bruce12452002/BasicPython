# 定義類別，屬性:屬性類型=預設值，屬性類型可不寫，寫不寫值都可以亂給，只是給使用的人參考，比較不會有例外發生
# self 名稱可亂打，但不建議，表示實體自己
# java 的靜態屬性相當於 python 的類別屬性

from pprint import pprint


class Animal:
    """動物的類別"""
    num = None  # 不給值不會有預設值，執行期報錯
    name: str = None
    attack: float = None

    def my_function1(self):  # self 是一定要的，且一定要在第一個，同名方法會後者蓋前者，沒有什麼 overloading
        print(f"{self.name}")

    def my_function2(self, i):
        pass
        # import winsound
        # winsound.Beep(2000, i)  # 頻率和響多久(毫秒)，windows 才可用

        # import os
        # os.system('say -v Bells "dong dong dong dong"; echo "\a\a\a"')  # mac 才可用
        # print(f"{self.name}, {i}")


print("============ 類別. ============")
print(Animal.__doc__)  # 查看註解內容，使用 help(Animal) 也可以
print(Animal.name)  # 所有實體都會影響
print(Animal.my_function1)
print(Animal.my_function1(Animal()))

print("============ 產生實體 ============")
my_animal = Animal()
my_animal.num = 7788
my_animal.name = "虎王"
my_animal.attack = "99"

print(f"{my_animal.num}, {type(my_animal.num)}")
print(f"{my_animal.name}, {type(my_animal.name)}")
print(f"{my_animal.attack}, {type(my_animal.attack)}")
my_animal.my_function1()  # 調用方法時，不用管 self
my_animal.my_function2(1500)  # 調用方法時，不用管 self

print("============ 每個實體有不同的位址 ============")
a1 = Animal()
a2 = Animal()
print(a1, a2)
print(id(a1), id(a2))  # id() 可查看每個實體的位址
print(type(a1), type(Animal))  # 實體可看出什麼型態；所有物件的型態都是 type
print(hex(id(a1)), hex(id(a2)))  # 將 id 轉成 16 進制
print(isinstance(a1, Animal))  # a1 是否是 Animal 的實體

print("============ 變數 ============")


class Xxx:
    abc = 123  # 自定的類別變數


# python 的類別變數相當於 java 的靜態變數
print(Xxx.__name__)  # 內鍵的類別變數

# 取值、賦值、刪除
print(Xxx.abc)
print(Xxx().abc)

Xxx.xyz = 100  # 可以動態賦值
print(Xxx().xyz)  # 實體也能取得到，但自己增加的屬性是實體屬性，只會是實體自己擁有，如 a = Xxx() a.xyz，表示 a 這個實體的 xyz 只有 a 擁有
del Xxx.xyz

print(getattr(Xxx, "abc"))  # 如果取不到就報錯
print(getattr(Xxx, "def", "321"))  # 如果取到就用，取不到就給最後一個參數
setattr(Xxx, "abc", 999)
delattr(Xxx, "abc")

pprint(Xxx.__dict__)  # pprint 將結果格式化，容易看
