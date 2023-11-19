# 變數範圍以找最近的變數為主，沒有就往上找，不會往下找
# global：在最外層設定或取得變數
# nonlocal：從本層開始找，找到 global，但不包括 global，只要一找到就用

def outer():
    # a = 2

    def inner():
        # a = 3

        # 最接近自己的先找，一直找到 global，但如果用的不是自己的變數就不能改值
        print("inner", a)
        # a = 5

    inner()


a = 1
outer()
print("最外層a =", a)
