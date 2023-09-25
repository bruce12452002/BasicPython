# list set dict str tuple
# len()  長度
# max()　最大值，只支援數字和浮點數，dict 只會抓 key
# min()　最小值，只支援數字和浮點數，dict 只會抓 key
# sum()  加總，只支援數字和浮點數，dict 只會抓 key
# list() 轉 list，可以自己轉自己，dict 只會保留 key，字串會每個字分開
# tuple() 轉 tuple，可以自己轉自己，dict 只會保留 key，字串會每個字分開
# str() 轉 string，可以自己轉自己，dict 「會」保留 key-value
# set() 轉 set，可以自己轉自己，dict 只會保留 key，字串會每個字分開
# 無法轉 dict，因為 dict 要 k-v pair
# + 和 *：只支援 list 和 tuple，在最後增加元素和元素增加幾倍的意思
# in 和 not in：判斷元素是否在四種資料結構裡 "a" in [1, 2, 3]

print("============ 多重賦值-str ============")
x, y, z = 1, 2.3, "ooo"
print(x, y)
x, *y = 1, 2.3, "ooo"
print(x, y)
x, *y, z = 1, 2.3, "ooo"
print(x, y)

print("============ 多重賦值-list tuple set ============")
myList1 = [1, 2.3, "ooo"]
x, y, z = myList1
print(x, y)
# x, y = myList1
# print(x, y)
x, *y = myList1
print(x, y)

print("============ 排序 ============")
# sorted 排序過後，不會變動原來的資料結構，且型態都會變成 list
my_list = [9, 1, 5, 73, 7, 88]
result = sorted(my_list)
print(f"{result}, {type(result)}, {my_list}")

my_tuple = (9, 1, 5, 73, 7, 88)
result = sorted(my_tuple, reverse=True)  # 倒序
print(f"{result}, {type(result)}, {my_tuple}")

my_str = "一二三四五六"
result = sorted(my_str)
print(f"{result}, {type(result)}, {my_str}")

print("============ 產生器運算式 ============")
# 快速初始化
my_list = ["ab,c", "d,ef", "ghi"]
my_set = {"ab,c", "d,ef", "ghi"}
my_tuple = ("ab,c", "d,ef", "ghi")

print(set(a for li in my_list for a in li.split(",")))
print(tuple(a for li in my_list for a in li.split(",")))

print(list(b for li in my_set for b in li.split(",")))
print(tuple(b for li in my_set for b in li.split(",")))

print(list(b for li in my_tuple for b in li.split(",")))
print(set(a for li in my_tuple for a in li.split(",")))

# 快速加總
print(sum(i * 2 for i in range(10)))

a_data = [5, 6, 7]
b_data = [3, 4, 5]
print(sum(i * j for i, j in zip(a_data, b_data)))


# 快速取最大、最小
class Animal:
    def __init__(self, num, name):
        self.num = num
        self.name = name


my_animal = [Animal(50, "五十"), Animal(7, "七"), Animal(24, "二十四")]
print(max((a.num, a.name) for a in my_animal))
print(min((a.num, a.name) for a in my_animal))

# 快速倒取並放在複合型態裡
data = "abcde"
print(tuple(data[i] for i in range(len(data) - 1, -1, -1)))

print("============ map ============")
scores = [50, 70, 90, 28]


def add_score(scores: list):
    result = []
    for s in scores:
        result.append(s + 5)
    return result


print(add_score(scores))


def add_score2(s: int):
    return s + 5


# print(map(add_score2, scores))
print(list(map(add_score2, scores)))
print(list(map(lambda s: s + 5, scores)))
print(tuple(map(lambda s: s + 5 if s < 60 else s, scores)))

# 例二
students_scores = [('孫悟空', 50), ('牛魔王', 70), ('豬八戒', 90)]
print(list(map(lambda s: s[1], students_scores)))

print("============ filter ============")
print(list(filter(lambda s: s < 60, scores)))
print(set(map(lambda s: s + 5, filter(lambda s: s < 60, scores))))
