class Animal:
    def hi(self):
        print("animal hi")

    def hello(self):
        print("animal hello")


class Fly:
    # def hi(self, s: str):
    def hi(self):
        print("fly hi")

    def hello(self):
        print("fly hello")


class ItsMe(Animal, Fly):
    """
    如果有些方法要調用第一個繼承的類別、有方法要調用第二個類別
    這時只好將需要調用的方法覆寫，然後改裡面的內容
    """
    # def hi(self):
    #     super().hi()  # super() 只會調用第一個繼承的類別
    #
    # def hello(self):
    #     Fly.hello(self)
    pass


i = ItsMe()
i.hi()  # 以繼承的第一個為主，就算是不同參數也一樣
# i.hi("")
i.hello()
