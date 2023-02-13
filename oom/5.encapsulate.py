class MyEncapsulate:
    __field = 1
    field = 2

    def __function(self):
        print("封裝方法")

    def my_field(self):
        self.__function()
        print("field = %d" % self.__field)

    def __str__(self):
        return f"{self.field} {self.__field}"


me = MyEncapsulate()
me.my_field()
me.field = 999
me.__field = 999  # 修改無效，但也不報錯
print(me)
# print(me.__field)  # __ 開頭的是封裝方法和封裝屬性，不可被外部訪問，只能內部使用
# 可以使用 實體._類別名稱(類別私有屬性或類別私有方法)
# print(me._MyEncapsulate__field)
# me._MyEncapsulate__function()

print("============ property ============")


class Animal3:
    def __init__(self, num: int):
        self.__num = num

    def get_num(self):
        print("getter")
        return self.__num

    def set_num(self, num):
        print("setter")
        if num <= 0:
            raise Exception("num 不可 <= 0")
        self.__num = num
    num = property(fget=get_num, fset=set_num)


a3 = Animal3(7)
# a3.num = -8
print(a3.num)
