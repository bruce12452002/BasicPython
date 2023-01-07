# 封裝的概念
# 加了 @property 的方法，無法被賦值和刪除
# 可視需要加上 @xxx.setter 和 @xxx.deleter

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

    @name.setter  # name.的字串名稱要和 @property 的方法名稱一樣
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
