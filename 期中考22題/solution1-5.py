students = ['Lendy', 90, 'Mary', 72, 'Bill', 88, 'John', 92]
"""
No1. 請設計一個串列，students，分別於index為0,2,4...處存放姓名，
和 index 為 1,3,5...處存放成績。
姓名為 Lendy，其成績為 90、姓名為 Mary，其成績為 72、
姓名為 Bill，其成績為 88 和姓名為 John，其成績為 92。
輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
students=[....] # index 為 0,2,4...處存放姓名。index 為 1,3,5...處存放成績
for ... range(...)  # 用 range，並計算串列長度(len)來進行for迴圈
"""
#
# for i in range(0, len(students), 2):
#     print(f"{students[i]}:{students[i + 1]}")


"""
No2. 請設計一個串列，students，分別於index為0,2,4...處存放姓名，
和index為1,3,5...處存放成績。
姓名為Lendy，其成績為90、姓名為Mary，
其成績為72、姓名為Bill，其成績為88和姓名為John，其成績為92。
請找出全班最高分與最低分的人，並輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
students=[....] # index為0,2,4...處存放姓名。index為1,3,5...處存放成績
students[1::2] # 取出成績
提示:index函式、slice、max和min函式。
"""
# highest = max(students[1::2])
# lowest = min(students[1::2])
# highest_index = students.index(highest)
# lowest_index = students.index(lowest)
# print(f"{students[highest_index - 1]}:{highest}")
# print(f"{students[lowest_index - 1]}:{lowest}")

"""
No3. 請設計一個串列，students，分別於index為0,2,4...處存放姓名，
和index為1,3,5...處存放成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、姓名為Bill，
其成績為88和姓名為John，其成績為92。
請找出全班最高分與最低分的人，並輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
students=[....] # index為0,2,4...處存放姓名。index為1,3,5...處存放成績
students[1::2] # 取出成績
提示:index函式、slice和sort函式。
"""
# score_list = students[1::2]
# score_list.sort()
# lowest_index = students.index(score_list[0])
# highest = len(students) // 2 - 1  # 最高分在最右邊
# highest_index = students.index(score_list[highest])
# print("%s:%d" % (students[lowest_index - 1], score_list[0]))
# print("%s:%d" % (students[highest_index - 1], score_list[highest]))

"""
No4. 請設計一個串列，students，分別於index為0,2,4...處存放姓名，
和index為1,3,5...處存放成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
students=[....] # index為0,2,4...處存放姓名。index為1,3,5...處存放成績
提示:index函式、slice和sort函式。
"""
students = ['Lendy', 90, 'Mary', 72, 'Bill', 88, 'John', 92]
score_list = students[1::2]
score_list.sort()  # 72 88 90 92

for i in score_list:
    index = students.index(i)
    print("%s:%d" % (students[index - 1], i))

for i in score_list[::-1]:
    index = students.index(i)
    print("%s:%d" % (students[index - 1], i))

"""
No5. 請設計一個串列，students，分別於index為0,2,4...處存放姓名，
和index為1,3,5...處存放成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
students=[....] # index為0,2,4...處存放姓名。index為1,3,5...處存放成績
提示:index函式、slice、sort和reverse函式。
"""
# for i in score_list:
#     index = students.index(i)
#     print("%s:%d" % (students[index - 1], i))
# score_list.reverse()
# for i in score_list:
#     index = students.index(i)
#     print("%s:%d" % (students[index - 1], i))
