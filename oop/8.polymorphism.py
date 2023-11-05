class Animal:
    def move(self):  # 方法內容為 pass，所以叫抽象方法，所在的類別叫抽象類別
        pass


class Dragon(Animal):
    def move(self):
        print("fly")


class Dog(Animal):
    def move(self):
        print("run")


def start(a: Animal):
    a.move()


start(Dragon())
start(Dog())
