# 1.將考試分數分成四個等級 60 80 90 100，不及格~59、60~79、80~89、90~100，顯示 D C B A 等級
# score = input("請輸入考試分數：")

# 2.將電影分級： 0~5歲為普遍級； 6~11歲為保護級； 12~17為輔導級; 18以上為限制級

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
year = 2000
month = 2

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
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

    # 一行的寫法 year % 4 == 0 and (year % 100 != 0 || year % 400 == 0)


# 6.如果 a 是 apple 而且 m 「是」 milk 就顯示蘋果牛奶；如果 a 是 apple 而且 m 「不是」 milk 就顯示蘋果
a = "apple"
m = 'milk'
