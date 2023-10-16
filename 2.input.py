print("============ 輸入 ============")
print("請輸入：")
name0 = input()
print(name0)

name1 = input("請輸入：")
print(name1)

name2 = "Hello! " + input()
print(name2)

name3 = "1 + " + input("請輸入數字：")
print(name3, eval(name3))  # eval 裡只能是字串，且內容只能和數字運算有關

x, y = eval(input("xxx:"))  # eval 可輸入多個值，用逗號隔開
print(x, y)
