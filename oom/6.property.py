# 封裝的概念
# 加了 @property 的方法，無法被賦值和刪除，也只能有 self 參數
# 可視需要加上 @xxx.setter 和 @xxx.deleter
# @xxx.setter 只能有兩個參數， self 參數和自定義參數

class Animal:
    @property
    def name(self) -> str:
        return "monkey"


a = Animal()
print(a.name)


# a.name = "dog"  # 加了 @property 後，無法被賦值
# del a.name  # 加了 @property 後，無法被刪除

class Animal2:
    def __init__(self):
        self.__n = "monkey"  # __開頭才不會被實體修改

    @property
    def name(self) -> str:
        return self.__n

    @name.setter  # 方法名稱、name.的字串名稱、@property 的方法名稱都要一樣
    def name(self, value):
        self.__n = value

    # @name.deleter
    # def name(self):
    #     del self._n
    #     print('del name')


a2 = Animal2()
print(a2.name)
a2.name = "dog"
print(a2.name)
# del a2.name
