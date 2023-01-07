import abc


class Animal(abc.ABC):
    name: str = None

    @abc.abstractmethod
    def abs_method(self):
        print("abs_method")  # 調用就會發生錯誤，這行不會印

    @staticmethod
    def my_static_method():
        print("static method")

    @classmethod
    def my_class_method(cls):  # cls 是一定要的，且一定要在第一個
        print(f"class method, name={cls.name}")


class Monkey(Animal):
    def abs_method(self):
        print("monkey")


class Dog(Animal):
    def abs_method(self):
        print("dog")


Monkey().abs_method()
Dog().abs_method()
# Animal().abs_method()
Animal.my_static_method()
Animal.my_class_method()
