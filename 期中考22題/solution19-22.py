"""
No19.
請設計三個串列，names、java_scores 和 python_scores，
分別存放使用者輸入的姓名，java成績和 python成績。直到輸入姓名為空為止。
並輸出使用者輸入的姓名，java成績和python成績，
其格式為，姓名:java成績:python成績。
輸入的姓名和成績，姓名為 Lendy，其java成績成績為90，python成績成績為88、
姓名為 Mary，其java成績成績為72，python成績成績為90、姓名為 Bill，
其java成績成績為88，python成績成績為78。
提示:使用while迴圈
"""
# names = ['Lendy', 'Mary', 'Bill']
# java_scores = [90, 72, 88]
# python_scores = [88, 90, 78]
# i = 0
# while i < len(names):
#     print(f"{names[i]}:{java_scores[i]}:{python_scores[i]}")
#     i += 1


students = [{'Lendy': [90, 88]}, {'Mary': [72, 90]}, {'Bill': [88, 78]}]
"""
No20. 
請使用辭典搭配串列students，透過辭典存放使用者輸入的姓名，
java成績和 python成績。直到輸入姓名為空為止。並輸出使用者輸入的姓名，
java成績和 python成績，其格式為，姓名:java成績:python成績。
輸入的姓名和成績，姓名為 Lendy，其java成績成績為90，python成績成績為88、
姓名為 Mary，其java成績成績為72，python成績成績為90、姓名為 Bill，
其java成績成績為88，python成績成績為78。
提示:使用while迴圈
"""
# i = 0
# while i < len(students):
#     for k, v in students[i].items():
#         print(f"{k}:{v[0]}:{v[1]}")
#     i += 1


"""
No21. 
請使用辭典搭配串列 students，透過辭典存放使用者輸入的姓名，
java 成績和 python成績。直到輸入姓名為空為止。
並依照java成績，從小到大，輸出使用者輸入的姓名，java成績和python成績，
其格式為，姓名:java成績:python成績。
輸入的姓名和成績，姓名為Lendy，其java成績成績為90，python成績成績為88、
姓名為Mary，其java成績成績為72，python成績成績為90、
姓名為Bill，其java成績成績為88，python成績成績為78。
提示:使用while迴圈
"""
java_scores = []

# # 將 java 分數排正序開始
# i = 0
# while i < len(students):
#     for k, v in students[i].items():
#         java_scores.append(v[0])
#     i += 1
# java_scores.sort()
# # 將 java 分數排正序結束
#
# for i in java_scores:
#     for j in students:
#         for k, v in j.items():
#             if v[0] == i:
#                 print(f"{k}:{v[0]}:{v[1]}")
#                 break

"""
No22. 
請使用辭典搭配串列 students，透過辭典存放使用者輸入的姓名，
java成績和 python成績。直到輸入姓名為空為止。
並依照java成績，從大到小，輸出使用者輸入的姓名，java成績和python成績，
其格式為，姓名:java成績:python成績。
輸入的姓名和成績，姓名為Lendy，其java成績成績為90，python成績成績為88、
姓名為Mary，其java成績成績為72，python成績成績為90、
姓名為Bill，其java成績成績為88，python成績成績為78。
提示:使用while迴圈
"""
java_scores = []

# 將 java 分數排倒序開始
i = 0
while i < len(students):
    for k, v in students[i].items():
        java_scores.append(v[0])
    i += 1
java_scores.sort()
java_scores.reverse()
# 將 java 分數排倒序結束

for i in java_scores:
    for j in students:
        for k, v in j.items():
            if v[0] == i:
                print(f"{k}:{v[0]}:{v[1]}")
                break
