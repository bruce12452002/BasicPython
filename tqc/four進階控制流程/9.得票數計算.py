"""
某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。
請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；
輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。
每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；
如最終計算有相同的最高票數者或無法選出最高票者，
顯示【=> No one won the election.】

輸入與輸出會交雜如下，輸出的部份以粗體字表示
2
Total votes of No.1: Nami =  0
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  0
8
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  2
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  3
Total null votes =  1
=> No.2 Chopper won the election.
"""
one = 0
two = 0
other = 0

for i in range(5):
    n = int(input("請輸入候選人號碼:"))

    match n:
        case 1:
            one += 1
        case 2:
            two += 1
        case _:
            other += 1

    print("Total votes of No.1: Nami =  %d" % one)
    print("Total votes of No.2: Chopper =  %d" % two)
    print("Total null votes =  %d" % other)

if one == two:
    print("=> No one won the election.")
elif one > two:
    print("=> No.1 Nami won the election.")
elif one < two:
    print("=> No.2 Chopper won the election.")
