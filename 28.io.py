import io

f1 = io.StringIO()
f1.write("Hello!")
f1.write("io.")
print(f1.getvalue())

f2 = io.StringIO('Hi! io')
for data in f2:
    print(data)

while True:
    data = f2.readline()
    if data == "":
        break
    print(data)

for i in io.StringIO('12\n34\n56').readlines():
    print(i)
