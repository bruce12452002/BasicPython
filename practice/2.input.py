# 使用 input 和使用者互動，一開始提示「請輸入您的名字：」，然後印出「歡迎『輸入的名字』進入」
# 再提示「『輸入的名字』 有幾張悠遊卡？」，最後印出「『輸入的名字』 有 『卡的數量』 張悠遊卡」

name = input("請輸入您的名字：")
print("歡迎 " + name + " 進入")  # 方法一
print("歡迎 %s 進入" % name)  # 方法二
print(f"歡迎 {name} 進入")  # 方法三
print("歡迎 {name} 進入".format(name=name))  # 方法四

card = input(name + "有幾張悠遊卡？")
print(name + "有 %s 張悠遊卡" % card)
