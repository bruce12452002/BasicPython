"""
請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，
接著輸出這兩個矩陣的內容以及它們相加的結果

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter matrix 1:
[1, 1]: 3
[1, 2]: 5
[2, 1]: 7
[2, 2]: 5
Enter matrix 2:
[1, 1]: 6
[1, 2]: 9
[2, 1]: 8
[2, 2]: 3

Matrix 1:
3 5
7 5
Matrix 2:
6 9
8 3
Sum of 2 matrices:
9 14
15 8
"""
print("========== 方法一 ==========")
my_list1 = []
my_list2 = []
for o in range(1, 2 + 1):
    print(f"Enter matrix {o}:")
    for i in range(1, 2 + 1):
        for j in range(1, 2 + 1):
            n = int(input(f"[{i}, {j}]: "))
            if o == 1:
                my_list1.append(n)
            if o == 2:
                my_list2.append(n)

my_list = [my_list1, my_list2]
for o in range(len(my_list)):
    print(f"Matrix {o + 1}:")
    for i in range(len(my_list[o])):
        if i == 2:
            print()
        print(my_list[o][i], end=" ")
    print()

print("Sum of 2 matrices:")
for i in range(len(my_list) // 2):
    for j in range(len(my_list[i])):
        if j == 2:
            print()
        print(my_list[i][j] + my_list[i + 1][j], end=" ")

print("========== 方法二 ==========")
n = 2
my_list = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]

for o in range(len(my_list)):
    print(f"Enter matrix {o + 1}:")
    for i in range(n):
        for j in range(n):
            num = int(input(f"[{i + 1}, {j + 1}]: "))
            my_list[o][i][j] = num

for o in range(len(my_list)):
    print(f"Matrix {o + 1}:")
    for i in range(len(my_list[o])):
        for j in range(len(my_list[o][i])):
            print(my_list[o][i][j], end=" ")
        print()
    print()

print(f"Sum of {len(my_list)} matrices:")
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[0][i][j] + my_list[1][i][j], end=" ")
    print()
