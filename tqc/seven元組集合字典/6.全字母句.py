"""
全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子
請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，
程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）
不區分大小寫字母

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
3
The quick brown fox jumps over the lazy dog
**True**
Learning Python is funny
**False**
Pack my box with five dozen liquor jugs
**True**

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
2
Quick fox jumps nightly above wizard
**True**
These can be weapons of terror
**False**
"""

for i in range(int(input('請輸入測試次數: '))):
    my_set = set()
    st = input('請輸入測試資料: ')
    for s in st.lower():
        if 97 <= ord(s) <= 122:
            my_set.add(s)
    print(True if len(my_set) == 26 else False)
