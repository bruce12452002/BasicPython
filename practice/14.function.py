print("============ 畫出如下的階層圖 ============")
"""
1
1 2
1 2 6
1 2 6 24
1 2 6 24 120
"""

number = 5


def factorial_triangle_for(n):
    """
    外迴圈控制上下； 內迴圈控制左右
    """
    for out in range(1, n + 1):
        c = 1  # 尤於內迴圈控制左右，內部迴圈每次都是從1開始，所以這裡每次進入內迴圈之前都將之前的值改回1
        for inner in range(1, out + 1):
            c *= inner
            print(c, end=" ")
        print()


# factorial_triangle_for(number)


def factorial_triangle_while(n):
    i = 1
    while i <= n:
        i += 1
        j = c = 1
        while j < i:
            c *= j
            print(c, end=" ")
            j += 1
        print()


# factorial_triangle_while(number)


def factorial_triangle_recursive(n):
    if n == 1:
        print(1)
    else:
        factorial_triangle_recursive(n - 1)  # 不是 1 進來會先進入，隨著遞減，最後都會印出 if 的 1
        # print(n)  # 測試用 1~5
        for c in range(1, n + 1):
            print(one_multiply_n(c), end=" ")
        print()


def one_multiply_n(n):
    """
    n 階層
    """
    if n == 1:
        return 1
    else:
        return n * one_multiply_n(n - 1)


factorial_triangle_recursive(number)

print("============ 求最大公因數 ============")


def gcd_while(p1, p2):
    """
    輾轉相除法
    6105, 8251
     p1 /  p2=商...餘
    6105/8251=0...6105
    8251/6105=1...2146 (發現除數和被除數剛好相反，所以最好是 p1 > p2，這樣可以少一次迴圈)
    6105/2146=2...1813
    2146/1813=1...333
    1813/333 =5...148
    333 /148 =2...37
    148 / 37 =4...0
    答案為 37
    公式為兩個互除後，一直 p2/餘數，除到餘數為0，如果都沒有最後也會是 1
    """

    #  這 if 判斷只是加快結束而已
    if p1 < p2:
        p2, p1 = p1, p2
    elif p1 == p2:
        return p1

    while p2 != 0:
        p1, p2 = p2, p1 % p2  # 算出來的 p2 賦值給 p1，而 p2 是兩數相除的餘數，如此一直循環直到餘數為 0
    return p1


# print(gcd_while(6105, 8251))
# print(gcd_while(1000, 499))
# print(gcd_while(1000, 1000))


def gcd_for(p1, p2):
    """
    短除法
    兩個整數取較小的數開始除，除完就減1，直到這個數字能一起將兩個數字整除或減到1為止，都沒有就回傳1，因為至少會有1這個公因數
    """
    if p1 < p2:
        p2, p1 = p1, p2
    elif p1 == p2:
        return p1

    for i in range(p2, 0, -1):
        if p1 % i == 0 and p2 % i == 0:
            return i  # 都能整除就是最大公因數
    return 1


print(gcd_for(6105, 8251))


def gcd_recursive(p1, p2):
    if p2 == 0:
        return p1
    else:
        return gcd_recursive(p2, p1 % p2)

# print(gcd_recursive(6105, 8251))
