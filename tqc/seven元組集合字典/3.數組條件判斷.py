"""
請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），以字串”end”為結束點（數組中不包含字串”end”）
接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素

範例輸入
president
dean
chair
staff
teacher
student
end
範例輸出
('president', 'dean', 'chair', 'staff', 'teacher', 'student')
('president', 'dean', 'chair')
('staff', 'teacher', 'student')
"""
my_list = []
while True:
    s = input("請輸入字串:")
    if s == 'end':
        if len(my_list) < 5:
            continue
        break
    my_list.append(s)

print(tuple(my_list))
print(tuple(my_list[0:3]))
print(tuple(my_list[-3:]))
