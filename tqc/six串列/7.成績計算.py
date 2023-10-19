"""
請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數
平均分數輸出到小數點後第二位

輸入與輸出會交雜如下，輸出的部份以粗體字表示
The 1st student:
78
89
88
70
60
The 2nd student:
90
78
66
68
78
The 3rd student:
69
97
70
89
90
Student 1
#sum 385
#average 77.00
Student 2
#sum 380
#average 76.00
Student 3
#sum 415
#average 83.00
"""
score = 5


def compute(sid):
    person = ['1st', '2nd', '3rd']

    result = [0] * sid
    for i in range(sid):
        total = 0

        print(f"The {person[i]} student:")
        for j in range(score):
            n = int(input())
            total += n
        result[i] = total
    return result


p = 3
rtn = compute(p)
for r in range(p):
    print(f"Student {r + 1}")
    print(f"#sum {rtn[r]}")
    print(f"#average {rtn[r] / score:.2f}")
