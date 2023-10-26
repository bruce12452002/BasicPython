"""
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數
輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

範例輸入
read.txt
3
範例輸出
a
is
programming

read.txt檔案內容
What is Python language
Python is a widely used high level general purpose interpreted dynamic programming language
Its design philosophy emphasizes code readability and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C or Java
Python supports multiple programming paradigms including object oriented imperative and functional programming or procedural styles
It features a dynamic type system and automatic memory management and has a large and comprehensive standard library
The best way we learn anything is by practice and exercise questions We have started this section for those beginner to intermediate who are familiar with Python
"""
with open("read908.txt", mode="r") as f:
    n = int(input("請輸入想出現單字出現的次數: "))

    my_dict = {}
    for i in f.read().split(" "):
        if i in my_dict:
            my_dict[i] = my_dict.get(i) + 1
        else:
            my_dict[i] = 1

    my_list = []
    for k, v in my_dict.items():
        if v == n:
            my_list.append(k)

    my_list.sort()
    for result in my_list:
        print(result)

