# re_search.py

import re
p = re.compile("[a-z]+")
# m = p.search("python")         # match='python'
# m = p.search("3 python")       # match='python'
m = p.search("3 py8thon")       # match='py' ; 처음부터 읽다가 먼저 검출된 'py'를 검색. 하나만 검색 가능.
# print(m)
if m:   # search 객체가 있으면 True / None 이면 False
    print("Match found:", m.group())
    print("위치:", m.span())
else:
    print("No match")

print("--------------------")
p = re.compile("Python")
m = p.search('The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.')
# Search는 여러개 중 가장 먼저 검색된 것 하나만 검출.
print(m)    # span: 검출된 위치에 대한 정보

print("--------------------")
