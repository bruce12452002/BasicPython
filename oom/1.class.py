# 定義類別，屬性:屬性類型=預設值，屬性類型可不寫，寫不寫值都可以亂給，只是給使用的人參考，比較不會有例外發生
# self 名稱可亂打，但不建議

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
