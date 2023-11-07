class MyEncapsulate:
    __field = 1  # 私有屬性

    def __function(self):
        print("封裝方法")

    # print 時，會調用 __str__ 方法
    def __str__(self):
        return f"============ {self.__field} ============"


me = MyEncapsulate()
# print(me.__field)  # 取不到私有屬性
me.__field = 999  # 這不是修改私有屬性，是動態賦值
print(me.__field)
print(me)

print("============ 破解私有屬性 ============")
# 可以使用 實體._類別名稱(類別私有屬性或類別私有方法)
print(me._MyEncapsulate__field)
me._MyEncapsulate__function()

# 有可修改
me._MyEncapsulate__field = 11
print(me._MyEncapsulate__field)

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
