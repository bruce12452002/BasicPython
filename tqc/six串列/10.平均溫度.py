"""
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度
提示1：平均溫度輸出到小數點後第二位
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1

輸入與輸出會交雜如下，輸出的部份以粗體字表示，輸入值以紅字表示
Week 1:
Day 1:23.1
Day 2:24
Day 3:23.5

Week 2:
Day 1:32
Day 2:33
Day 3:35.5

Week 3:
Day 1:29
Day 2:30
Day 3:26

Week 4:
Day 1:27.6
Day 2:25
Day 3:28.8
Average: 28.13
Highest: 35.5
Lowest: 23.1
"""
week = 4
day = 3
first = True
highest = 0
lowest = 0
count = 0

for w in range(week):
    print(f"Week {w + 1}:")
    for d in range(day):
        degree = float(input(f"Day {d + 1}:"))
        count += degree

        if first:
            highest = degree
            lowest = degree
            first = False

        if highest < degree:
            highest = degree

        if lowest > degree:
            lowest = degree

print("Average: {:.2f}".format(count / (week * day)))
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
