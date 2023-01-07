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
