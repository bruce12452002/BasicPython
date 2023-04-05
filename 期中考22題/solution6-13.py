names = ['Lendy', "Mary", 'Bill', "John"]
scores = [90, 72, 88, 92]
"""
No6.
請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
python
names=[....] # 存放姓名
scores=[....] # 存放成績
for ... range(...)  # 用 range，並計算串列長度(len)來進行 for迴圈
"""
# for i in range(len(names)):
#     print("%s:%d" % (names[i], scores[i]))

"""
No7.
請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
輸出姓名和成績，其格式為，姓名:成績。
請依照下面程式範例與要求撰寫程式。
names=list(...) # 存放姓名
scores=list(...) # 存放成績

for ... range(...)  # 用range，並計算串列長度來進行for迴圈
"""
# names = list(('Lendy', "Mary", 'Bill', "John"))
# scores = list([90, 72, 88, 92])
# for i in range(len(names)):
#     print("%s:%d" % (names[i], scores[i]))

"""
No8. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請計算全班平均。
"""
# print(sum(scores) / len(names))

"""
No9. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請找出全班最高分與最低分的人，並輸出姓名和成績，其格式為:
最高分:姓名:成績。
最低分:姓名:成績。
提示:index方法
"""
# sorted_scores = sorted(scores)
# lowest_index = scores.index(sorted_scores[0])
# highest = len(scores) - 1
# highest_index = scores.index(sorted_scores[highest])
# print("%s:%d" % (names[lowest_index], sorted_scores[0]))
# print("%s:%d" % (names[highest_index], sorted_scores[highest]))

"""
No10. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績。
請使用sorted方法。
建議:建立先的變數scores_sorted代表排序後的scores。
"""
# sorted_scores = sorted(scores)
# for i in sorted_scores:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))
#
# for i in sorted_scores[::-1]:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))

"""

No11. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績。 
請使用sorted和reversed方法。
"""
# sorted_scores = sorted(scores)
# for i in sorted_scores:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))
# sorted_scores.reverse()
# for i in sorted_scores:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))
#

"""
No12. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績。 
請使用sort方法。
提示:適切使用copy()
"""
# scores_copy = scores.copy()
# scores_copy.sort()
# for i in scores_copy:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))
#
# for i in scores_copy[::-1]:
#     index = scores.index(i)
#     print("%s:%d" % (names[index - 1], i))

"""
No13. 請設計兩個串列，names和scores，分別存放姓名和成績。
姓名為Lendy，其成績為90、姓名為Mary，其成績為72、
姓名為Bill，其成績為88和姓名為John，其成績為92。
請從最低分到最高分，輸出姓名和成績。再從最高分到最低分，輸出姓名和成績。 
請使用sort和reverse方法。
提示:適切使用copy()
"""
scores_copy = scores.copy()
scores_copy.sort()
for i in scores_copy:
    index = scores.index(i)
    print("%s:%d" % (names[index - 1], i))
scores_copy.reverse()
for i in scores_copy:
    index = scores.index(i)
    print("%s:%d" % (names[index - 1], i))
