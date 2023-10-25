"""
請撰寫一程式，讓使用者輸入一個句子（至少有五個詞，以空白隔開），
並輸出該句子倒數三個詞

範例輸入
Many foreign students study in FJU
範例輸出
study in FJU
"""
st = "Many foreign students study in FJU"
all_word = st.split(" ")
for i in all_word[-3::]:
    print(i, end=" ")
