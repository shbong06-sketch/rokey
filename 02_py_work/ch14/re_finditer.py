# re_finditer.py

import re
p = re.compile("[a-z]+")
result = p.finditer("life is too short")
print(result)       # iterator object(반복자 객체)
# match 객체 집합

for r in result:
    print(r)        # Match object

print("--------------------")
p = re.compile("Python")
result = p.finditer('The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.')

# print(list(result))
for m in result:
    print('매치 문자열:', m.group())
    print('문자열 위치:', m.span())
    print('문자열 시작 위치:', m.start())
    print('문자열 끝 위치:', m.end())

