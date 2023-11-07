print("============ 類別和實體-動態賦值 ============")


# python 有支援動態賦值，也就是可增加在類別裡沒有的屬性
class Animal4:
    pass


print("類別外增加屬性，實體也會有；相反則不行")
a = Animal4()
a.a1 = 1
print(a.a1)  # 1
# Animal4.a1 類別裡沒這個屬性，會報錯

Animal4.a2 = 2
print(f"{Animal4.a2} {a.a2}")  # 2 2

print("類別或實體-修改")
a.a2 = 3  # 實體屬性增加了和類別屬性一樣的名稱，就會成為實體自己的屬性
print(f"{Animal4.a2} {a.a2}")  # 2 3
Animal4.a2 = 4
print(f"{Animal4.a2} {a.a2}")  # 4 3

print("類別或實體-刪除")
# 刪除實體屬性後，如果名稱和類別屬性名稱一樣，值會變成類別的
# 但刪除類別屬性，只會影響類別屬性
# del a.a2
del Animal4.a2
print(a.a2)
# print(Animal4.a2)

print("============ getattr、setattr、delattr ============")
# getattr 取不到屬性會報錯
a.a3 = 5
print(getattr(a, "a3"))  # 5
# Animal4.a3 = 6
print(getattr(Animal4, "a3", 7))  # 如果取不到屬性，就給第三個參數的值
setattr(a, "a3", 8)
print(getattr(a, "a3"))  # 8
delattr(a, "a3")

# 第一個參數有指定是實體，所以找不到就報錯或第三個參數的值，並不會找類別屬性
# print(getattr(a, "a3"))
