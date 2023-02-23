from bs4 import BeautifulSoup

html_str = "<p><ul><li></li></ul><a id='a1'>a1<p>p</p></a><a id='a2'>a2</a><a>a3</a><ul><li></li></ul></p>"

data = BeautifulSoup(markup=html_str, features="html.parser")
print(data)
print(data.p.contents)  # 如果子 tag 還有子 tag，會是一個整體，enter 也算一個
print("============ 取得子 tag ============")
for i, d in enumerate(data.p.children):
    print(i, d)

print("============ 取得父 tag ============")
# print(data.a.parent)  tag 所在層的所有 tag 為 parent
for i, d in enumerate(data.a.parent):
    print(i, d)

print("============ 取得祖先 tag ============")
# print(data.a.parents)
for i, d in enumerate(data.a.parents):
    print(i, d)

print("============ 取得下一個兄弟節點 ============")
# print(data.a.next_sibling)
print(list(enumerate(data.a.next_sibling)))

print("============ 取得所有下一個兄弟節點 ============")
# print(data.a.next_siblings)
print(list(enumerate(data.a.next_siblings)))

print("============ 取得上一個兄弟節點 ============")
print(data.a.previous_slibling)
print(data.find(id="a2").previous_sibling)

print("============ 取得所有上一個兄弟節點 ============")
print(data.a.previous_sliblings)
for sibling in data.find(id="a2").previous_siblings:
    print(sibling)
