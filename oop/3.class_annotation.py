# @staticmethod：
#   1. 沒有 cls 和 self 屬性，「不可」直接調用屬性；
#   2. 和寫在全域方法一樣，只不過定義在 class 裡而已，但一寫會報錯，所以加了這個裝飾器
# @classmethod：
#   1. 第一個參數一定要是 cls(可亂打，但不建議)，表示此類別，「可」直接調用屬性；
#   2. 如果操作的是同一個變數，類別會影響實體；但實體不會影響到類別

class Animal:
    """動物的類別"""
    num = None
    name: str = None
    attack: float = None

    @staticmethod  # @開頭的語法在 python 裡，叫裝飾器 decorator
    def my_static_method():
        print(f"static method, name={Animal.name}")

    @classmethod
    def my_class_method(cls):  # cls 是一定要的，且一定要在第一個
        print(f"class method, name={cls.name}")


print("============ 調用靜態方法 ============")
Animal.my_static_method()
a1 = Animal()
a1.my_static_method()

print("============ 調用類別方法 ============")
Animal.my_class_method()
a1.my_class_method()

print("============ 類別.屬性 ============")
print(a1.name)
Animal.name = "monkey"
Animal.my_class_method()
a1.my_class_method()
print(a1.name)  # 被類別影響了

print("============ 修改實體屬性不影響類別屬性 ============")
a2 = Animal()
a2.name = "dog"
a2.my_class_method()  # 實體調用 @classmethod 也不會變 dog
a1.my_class_method()  # 實體調用 @classmethod 也不會變 dog
print(a2.name)

print("============ self 屬性和類別屬性名稱一樣時 ============")


class Xxx:
    name = 'xxx'

    def __init__(self, name):
        self.name = name


x = Xxx('aaa')
# x = Xxx()
print(x.name, Xxx.name)  # aaa xxx
Xxx.name = 'ooo'
print(x.name, Xxx.name)  # aaa ooo，這裡的 aaa 不會被影響是因為 x 取得的 name 是 self 的
x.name = 'zzz'
print(x.name, Xxx.name)  # zzz ooo
