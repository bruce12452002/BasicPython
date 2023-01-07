class GrandPapa:
    money = 100_0000

    def get_money(self):
        return self.money


class Papa(GrandPapa):
    money = 10_0000

    def get_money(self):
        return self.money  # 從子類開始找 money，都找不到才是自己的 money
        # return Papa.money  # 自己的 money
        # return super().money  # 父類的 money


class Me(Papa):
    money = 1_0000

    def get_money(self):
        return self.money

    def use_papa(self):
        print("使用 papa 開始")
        print(Papa.money)
        print(Papa.get_money(self))  # 不寫 self，會執行期錯誤
        print(super().money)
        print(super().get_money())  # 不可寫 self，會執行期錯誤
        print("使用 papa 結束")

    def use_grand_papa(self):
        print("使用 grand_papa 開始")
        print(GrandPapa.money)
        print(GrandPapa.get_money(self))  # 將自己傳給父類，但剛好 money 這個屬性覆蓋了父類，所以還是抓到自己的 money 屬性
        # print(super().super())  # 無法連續多個 super()，只能自己和父別都寫 super() 來達到目的
        print("使用 grand_papa 結束")


me = Me()
print(me.get_money())
print(me.money)

papa = Papa()
print(papa.get_money())
print(papa.money)

grandPapa = GrandPapa()
print(grandPapa.get_money())
print(grandPapa.money)

me.use_papa()
me.use_grand_papa()


