# list set dict str tuple
# len()  長度
# max()　最大值，只支援數字和浮點數，dict 只會抓 key
# min()　最小值，只支援數字和浮點數，dict 只會抓 key
# sum()  加總，只支援數字和浮點數，dict 只會抓 key

l = [3, 2, 1]
s = {3, 2, 1}
d = {3:'c', 2: 'b', 1:'a'}
st = '321'
t = (3, 2, 1)

print('============ len ============')
print(len(l))
print(len(s))
print(len(d))
print(len(st))
print(len(t))
print('============ max ============')
print(max(l))
print(max(s))
print(max(d))
print(max(st))
print(max(t))
print('============ min ============')
print(min(l))
print(min(s))
print(min(d))
print(min(st))
print(min(t))
print('============ sum ============')
print(sum(l))
print(sum(s))
print(sum(d))
# print(sum(st)) # 字串無法加總
print(sum(t))
print('============ sorted ============')
# sorted 「不會」變動原來的資料，且型態都會變成 list
# 倒序可加參數 reverse=True
sl = sorted(l)
ss = sorted(s)
sd = sorted(d)
sst = sorted(st)
st2 = sorted(t)
print('原本的資料')
print(l)
print(s)
print(d)
print(st)
print(t)
print('排序過後的資料')
print(sl, type(sl))
print(ss, type(ss))
print(sd, type(sd))
print(sst, type(sst))
print(st2, type(st2))
print('============ sort ============')
# sorted 「會」變動原來的資料，但只有 list 有這個方法
# 倒序可加參數 reverse=True
l.sort()
# s.sort()
# d.sort()
# st.sort()
# t.sort()
print(l)


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

print("============ 產生器運算式 ============")
xxx = (a for a in range(5))
for i in xxx:
    print(i, end=" ")
print('產生器只能跑一次')
for i in xxx:
    print(i)
print("=====")
# 初始化
my_list = ["ab,c", "d,ef", "ghi"]
my_set = {"ab,c", "d,ef", "ghi"}
my_tuple = ("ab,c", "d,ef", "ghi")

print(set(a for li in my_list for a in li.split(",")))
print(tuple(a for li in my_list for a in li.split(",")))

print(list(b for li in my_set for b in li.split(",")))
print(tuple(b for li in my_set for b in li.split(",")))

print(list(b for li in my_tuple for b in li.split(",")))
print(set(a for li in my_tuple for a in li.split(",")))

# 加總
print(sum(i * 2 for i in range(3)))

a_data = [5, 6, 7]
b_data = [3, 4, 5]
# zip 方法可以把多個「可迭代物件」一一對應打包在一起 [(5, 3), (6, 4), (7, 5)]
print(sum(i * j for i, j in zip(a_data, b_data))) #  5*3 + 6*4 + 7*5

# 快速倒取並放在複合型態裡
data = "abcde"
print(tuple(data[i] for i in range(len(data) - 1, -1, -1)))
