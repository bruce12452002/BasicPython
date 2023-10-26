"""
請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則
密碼規則如下：
a. 必須至少八個字元
b. 只包含英文字母和數字
c. 至少要有一個大寫英文字母
d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，
否則顯示【Invalid password】

範例輸入1
39Gfjkd98
範例輸出1
Valid password

範例輸入2
39dk8fh
範例輸出2
Invalid password
"""


# 主要是 「c. 至少要有一個大寫英文字母」要寫的好看在難寫


def check(password):
    upper = False
    if len(password) < 8:
        return False
    else:
        for s in password:
            if not s.isalnum():
                return False
            if not upper and 65 <= ord(s) <= 90:
                upper = True
    return upper


print("Valid password" if check(input("請輸入密碼: ")) else "Invalid password")
