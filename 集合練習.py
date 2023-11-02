import random as r

my_list = []
with open("集合.txt", encoding="UTF-8") as f:
    for data in f.readlines():
        my_list.append(data.strip().split(","))

while True:
    n = r.randrange(0, len(my_list))
    keyIn = input(my_list[n][0] + ": ")
    if keyIn.strip().lower() != my_list[n][1].strip().lower():
        print(f"答錯了！正確答案是: {my_list[n][1].strip()}")
    else:
        print("正確！下一題")
