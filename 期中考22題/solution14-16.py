names = ['Lendy', "Mary", 'Bill', "John"]
scores = [90, 72, 88, 92]
"""
No14.
請設計兩個串列，names和scores，分別存放使用者輸入的姓名和成績。
直到輸入姓名為空為止。並輸出使用者輸入的姓名和成績，其格式為，姓名:成績。
輸入的姓名和成績，姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88。
提示:使用while迴圈
"""
# i = 0
# while i < len(names):
#     print("%s:%d" % (names[i], scores[i]))
#     i += 1

"""
No15. 
請設計兩個串列，names和scores，分別存放使用者輸入的姓名和成績。
直到輸入姓名為空為止。並依照成績，從大到小，再從小到大，
輸出使用者輸入的姓名和成績，其格式為，姓名:成績。
輸入的姓名和成績，姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88。
提示:使用while迴圈、sorted和reversed方法。
"""
# sorted_scores = sorted(scores)
# i = 0
# while i < len(names):
#     index = scores.index(sorted_scores[i])
#     print("%s:%d" % (names[index], sorted_scores[i]))
#     i += 1
# sorted_scores.reverse()
# i = 0
# while i < len(names):
#     index = scores.index(sorted_scores[i])
#     print("%s:%d" % (names[index], sorted_scores[i]))
#     i += 1

"""
No16. 
請設計兩個串列，names和scores，分別存放使用者輸入的姓名和成績。
直到輸入姓名為空為止。並依照成績，從大到小，再從小到大，
輸出使用者輸入的姓名和成績，其格式為，姓名:成績。
輸入的姓名和成績，姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88。
提示:使用while迴圈，使用sorted方法
"""
sorted_scores = sorted(scores)
i = 0
while i < len(names):
    index = scores.index(sorted_scores[i])
    print("%s:%d" % (names[index], sorted_scores[i]))
    i += 1

while i >= 0:
    i -= 1
    index = scores.index(sorted_scores[i])
    print("%s:%d" % (names[index], sorted_scores[i]))
