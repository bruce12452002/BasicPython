"""
請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開
請將此五個數字加總（Total）並計算平均（Average）

範例輸入
-2 34 18 29 -56
範例輸出
Total = 23
Average = 4.6
"""
all_num = input("請輸入五個數字，數字之間用空白隔開: ")

# 方法一
# word = all_num.split(" ")
# count = 0
# for s in word:
#     count += int(s)
# print(f"Total = {count}")
# print(f"Average = {count / len(word)}")

# 方法二
n = [int(i) for i in all_num.split(" ")]
print(f"Total = {sum(n)}")
print(f"Average = {sum(n) / 5}")
