# @staticmethod： 沒有 cls 和 self 屬性，「不可」直接調用屬性
# @classmethod：第一個參數一定要是 cls(可亂打，但不建議)，表示此類別，「可」直接調用屬性；會被類別.屬性影響，不會被實體影響

class Animal:
    """動物的類別"""
    num = None
    name: str = None
    attack: float = None

    def my_self(self):
        print(f"{self.name}")

    @staticmethod  # @開頭的語法在 python 裡，叫裝飾器 decorator
    def my_static_method():
        print(f"static method, name={Animal.name}")

    @classmethod
    def my_class_method(cls):  # cls 是一定要的，且一定要在第一個
        print(f"class method, name={cls.name}")
        Animal.my_static_method()


print("============ 調用靜態方法 ============")
Animal.my_static_method()
a1 = Animal()
a1.my_static_method()

print("============ 調用類別方法 ============")
Animal.my_class_method()
a1.my_class_method()

print("============ 類別.屬性 ============")
Animal.name = "monkey"
Animal.my_class_method()
a1.my_class_method()

print("============ 實體屬性和類別屬性互不影響 ============")
a2 = Animal()
a2.name = "dog"
a2.my_class_method()  # 實體調用 @classmethod 也不會變 dog
a1.my_class_method()  # 實體調用 @classmethod 也不會變 dog
print(a2.name)
