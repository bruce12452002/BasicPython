def display(data):
    for index in range(0, len(data), 1):
        yield data[index]  # generator 用 yield 回傳


for c in display("abc"):
    print(c)
