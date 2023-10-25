"""
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字
若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】

範例輸入1
329-48-4977
範例輸出1
Valid SSN

範例輸入2
837-a3-3000
範例輸出2
Invalid SSN
"""
st = input("請輸入社會安全碼SSN，格式為ddd-dd-dddd，d表示數字: ")

# 方法一
# num = st.split("-")
#
# for s in num:
#     if not s.isdigit():
#         print("Invalid SSN")
#         break
# else:
#     print("Valid SSN")

# 方法二
if st.replace("-", "").isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")
