import random as r
import time as t

my_list = []
with open("eng_word.txt", encoding="UTF-8") as f:
    for data in f.readlines():
        my_list.append(data.strip().split(","))

second = 3  # 幾秒跑一次
while True:
    n = r.randrange(len(my_list))
    print(my_list[n][0], end=' ')
    t.sleep(second)
    print(my_list[n][1])
