class MyEncapsulate:
    __field = 1

    def __function(self):
        print("封裝方法")

    def my_field(self):
        self.__function()
        print("field = %d" % self.__field)


me = MyEncapsulate()
me.my_field()
# print(me.__field)  # __ 開頭的是封裝方法和封裝屬性，不可被外部訪問，只能內部使用
# 可以使用 實體._類別名稱(類別私有屬性或類別私有方法)
# print(me._MyEncapsulate__field)
# me._MyEncapsulate__function()
