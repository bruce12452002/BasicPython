# @staticmethod：
#   1. 沒有 cls 和 self 屬性，「不可」直接調用屬性；
#   2. 和寫在全域方法一樣，只不過定義在 class 裡而已，但一寫會報錯，所以加了這個裝飾器
# @classmethod：
#   1. 第一個參數一定要是 cls(可亂打，但不建議)，表示此類別，「可」直接調用屬性；
#   2. 如果操作的是同一個變數，類別會影響實體；但實體不會影響到類別

class Animal:
    """動物的類別"""
    name: str = None

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
