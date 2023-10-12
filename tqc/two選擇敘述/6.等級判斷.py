"""
請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：

分數	    等級
80 ~ 100	A
70 ~ 79	    B
60 ~ 69	    C
<= 59	    F

範例輸入
79
範例輸出
B
"""
score = 79

if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("C")
else:
    print("D")
