import abc

"""
抽象類別裡，如果有抽象方法就不可被實體化
"""


class Animal(abc.ABC):
    name: str = None

    @abc.abstractmethod
    def abs_method(self):
        print("abs_method")  # 調用就會發生錯誤，這行不會印，所以一般都寫 pass

    @staticmethod
    def my_static_method():
        print("static method")

    @classmethod
    def my_class_method(cls):
        print("class method")


class Monkey(Animal):  # 繼承抽象後，就一定要覆寫方法
    def abs_method(self):
        print("monkey")


class Dog(Animal):
    def abs_method(self):
        print("dog")


Monkey().abs_method()
Dog().abs_method()
# Animal()  # 不可實例化

# @staticmethod、@classmethod 也能取到，當然也能覆寫
Monkey.my_class_method()
Dog.my_static_method()
