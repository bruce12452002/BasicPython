# 1.將考試分數分成四個等級 60 80 90 100，不及格~59、60~79、80~89、90~100，顯示 D C B A 等級
score = int(input("請輸入考試分數："))
if score <= 59:
    print("D")
elif score <= 79:
    print("C")
elif score <= 89:
    print("B")
elif score <= 100:
    print("A")

# 2.將電影分級： 0~5歲為普遍級； 6~11歲為保護級； 12~17為輔導級; 18以上為限制級
age = 8
if age <= 5:
    print("普遍級")
elif age <= 11:
    print("保護級")
elif age <= 17:
    print("輔導級")
elif age >= 18:
    print("限制級")

# 3.輸入一個整數，判斷是否為奇數，是就顯示奇數；不是顯示偶數
i = 50
if i % 2 == 0:
    print("偶數")
else:
    print("奇數")

# 4.輸入兩個整數，判斷第一個整數是否是第二個整數的倍數，是就顯示是；不是就顯示不是
a = 100
b = 50
if a % b == 0:
    print("是")
else:
    print("不是")

# 5.輸入兩個整數，一個年份和一個月份，顯示這個月有多少天
# 提示：4 的倍數是閏年，但 100 的倍數不是閏年，又 400 的倍數也是閏年
year = 2000
month = 2

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    # 方法一
    if year % 4 == 0:
        if year % 100 == 0:
            # 以下 if-else 可精簡寫法： leap = year % 400 == 0
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    if leap:
        print(29)
    else:
        print(28)

# 方法二
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(29)
else:
    print(28)

# 6.如果 a 是 apple 而且 m 「是」 milk 就顯示蘋果牛奶；如果 a 是 apple 而且 m 「不是」 milk 就顯示蘋果
a = "apple"
m = 'milk'

# 方法一
if a == "apple":
    if m == "milk":
        print("蘋果牛奶")
    else:
        print("蘋果")

# 方法二
if a == "apple" and m == "milk":
    print("蘋果牛奶")
if a == "apple" and m != "milk":
    print("蘋果")
