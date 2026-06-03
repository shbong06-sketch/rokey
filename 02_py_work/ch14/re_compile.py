# re_compile.py

import re

# 축약 전 형태
p = re.compile("[a-z]+")
m = p.match("python")       # match='python'
# m = p.match("3 py8thon")
print(m)

print("-----------------------")
# 축약 후 형태
# 매치객체 = re.match("정규식", "검색 대상 문자열")
m = re.match("[a-z]+", "python")
print(m)
m = re.search("[a-z]+", "3 py8thon")
print(m)

# 한번만 검색할 때는 축약 후 형태
# 패턴을 만들고 여러번 활용이 이뤄질 경우, 축약 전 형태