class GrandPapa:
    __money = 100_0000

    def get_money(self):
        return self.__money


class Papa(GrandPapa):
    __house = 1

    def get_house(self):
        return self.__house


class Me(Papa):
    pass  # 類別裡什麼都沒有，但不寫語法會報錯，所以用 pass 關鍵字


me = Me()
print(me.get_money())
print(me.get_house())

papa = Papa()
print(papa.get_money())
print(papa.get_house())

grandPapa = GrandPapa()
print(grandPapa.get_money())


class Mama:
    __house = 2

    def get_house(self):
        return self.__house


class Sister(Papa, Mama):  # 多繼承，如果有同名方法，會從左邊類別開始找，找到就用
    pass


class Brother(Mama, Papa):
    pass


sister = Sister()
print(sister.get_house())
brother = Brother()
print(brother.get_house())

print("============ __init__ ============")


class GrandPapa:
    a = 4

    def __init__(self):
        self.name = "xxx"

    def yeah(self):
        return self.a


class Papa(GrandPapa):
    a = "abc"
    """
    沒有寫 __init__ 時，會自動幫我們調用父類別的 __init__，但自己寫了 __init__ 之後，要自己顯示調用才行
    """

    # def __init__(self):
    #     super().__init__()  # super 有圓括號
    #     self.address = "ooo"


papa = Papa()
print(papa.name)
print(isinstance(papa, Papa))  # True，自己是自己的實體
print(isinstance(papa, GrandPapa))  # True
print(isinstance(GrandPapa(), Papa))  # False

print(issubclass(Papa, Papa))  # True，自己也算是自己的子類
print(issubclass(Papa, GrandPapa))  # True
print(issubclass(GrandPapa, Papa))  # False

print("============ 方法參數是 class ============")


def get_a(g: GrandPapa):  # 參數是 GrandPapa，也可傳 GrandPapa 的子類別
    print(g.a)
    print(g.yeah())


get_a(papa)
get_a(GrandPapa())
