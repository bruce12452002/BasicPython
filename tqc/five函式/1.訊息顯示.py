"""
請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、
學號（Student ID）和姓名（Name）並顯示這些訊息

範例輸入
Information Management
123456789
Tina Chen
範例輸出
Department: Information Management
Student ID: 123456789
Name: Tina Chen
"""


def compute():
    depart = input("請輸入系別:")
    student_id = int(input("請輸入學號:"))
    name = input("請輸入姓名:")

    print("Department:  %s" % depart)
    print("Student ID:  %s" % student_id)
    print("Name:  %s" % name)


compute()
