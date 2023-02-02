# 使用 match-case，將水果翻譯成中文，有以下三種水果：

fruit = "blueberry"
# fruit = "kiwi"
# fruit = "tomato"

match fruit:
    case 'blueberry':
        print("藍苺")
    case 'kiwi':
        print("奇異果")
    case 'tomato':
        print("蕃茄")
    case _:
        print("無對應的水果")
