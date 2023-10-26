"""
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、
所有人的平均身高、平均體重以及最高者、最重者。
輸出浮點數到小數點後第二位。

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg


read.txt檔案內容
Ben 175 65
Cathy 155 55
Tony 172 75
"""
with open("read904.txt") as f:
    count_height = 0
    count_weight = 0
    max_height = 0
    max_weight = 0

    for s in f.readlines():
        print(s)
        data = s.split(" ")
        h = int(data[1])
        w = int(data[2])
        count_height += h
        count_weight += w

        if max_height < h:
            max_height = h

        if max_weight < w:
            max_weight = w

    print(f"Average height: {count_height / 3:.2f}")
    print(f"Average weight: {count_weight / 3:.2f}")
    print(f"The tallest is Ben with {max_height:.2f}cm")
    print(f"The heaviest is Tony with {max_weight:.2f}kg")
