# 變數範圍以找最近的變數為主，沒有就往上找，不會往下找
# global：在最外層設定變數
# nonlocal：從本層到最外層，將變數傳播在中間層，也就是沒有本層和最外層

def scope():
    def do_local():
        a = "222"

    def do_nonlocal():
        # nonlocal a
        # a = "333"

        def do_nonlocal2():
            nonlocal a  # 如果 a 在之前定義會報錯；此行的 a 並不是 None
            a = "333"  # 這行如果沒定義 a，會抓外層的

        do_nonlocal2()

    def do_global():
        global a
        a = "444"

    a = "111"
    do_local()
    print("do_local 之後，a=", a)
    do_nonlocal()
    print("do_nonlocal 之後，a=", a)
    do_global()
    print("do_global 之後，a=", a)


scope()
print("最外層a=", a)
# 寫在這層的變數就是 global
