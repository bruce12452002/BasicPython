"""
No17.
n=['Lendy','Mary','Bill','John']
1. 請用正向index取出'Mary'
2. 請用負向index取出'Mary'
3. 請用正向index取出'Mary'到'John'
4. 請用正向index取出'Mary'到最後
5. 請用負向index取出'Mary'到-1
6. 請用負向index取出'Mary'到最後
7. 請用正向index，從頭取到最後
8. 請透過間距為-1的方法，從'John'取到'Lendy'
9. 請用正向index搭配負向index，取出'Mary'到'Bill'
10. 請用負向index搭配正向index，取出'Mary'到'Bill'
11. 請透過間距為-1的方法，用正向index搭配負向index，取出'Bill'到'Mary'
12. 請透過間距為-1的方法，用負向index搭配正向index，取出'Bill'到'Mary'
"""
n = ['Lendy', 'Mary', 'Bill', 'John']
# print("1.", n[1])
# print("2.", n[-3])
# print("3.", n[1:4])
# print("4.", n[1:])
# print("5.", n[-3::1])
# print("6.", n[-3:])
# print("7.", n[::])
# print("8.", n[::-1])
# print("9.", n[1:-1:1])
# print("10.", n[-3:3:1])
# print("11.", n[2:0:-1])
# print("12.", n[-2:-4:-1])

"""
No18.
n='LMBJ'
1. 請用正向index取出'M'
2. 請用負向index取出'M'
3. 請用正向index取出'M'到'J'
4. 請用正向index取出'M'到最後
5. 請用負向index取出'M'到-1
6. 請用負向index取出'M'到最後
7. 請用正向index，從頭取到最後
8. 請透過間距為-1的方法，從'J'取到'L'
9. 請用正向index搭配負向index，取出'M'到'B'
10. 請用負向index搭配正向index，取出'M'到'B'
11. 請透過間距為-1的方法，用正向index搭配負向index，取出'B'到'M'
12. 請透過間距為-1的方法，用負向index搭配正向index，取出'B'到'M'
"""
n = 'LMBJ'
print("1.", n[1])
print("2.", n[-3])
print("3.", n[1:4])
print("4.", n[1:])
print("5.", n[-3::1])
print("6.", n[-3:])
print("7.", n[::])
print("8.", n[::-1])
print("9.", n[1:-1:1])
print("10.", n[-3:3:1])
print("11.", n[2:0:-1])
print("12.", n[-2:-4:-1])
