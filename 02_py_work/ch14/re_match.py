# re_match.py

import re
p = re.compile("[a-z]+")
m = p.match("python")       # match='python'
# m = p.match("3 python")       # None
# print(m)
if m:   # match 객체가 있으면 True / None 이면 False
    print("Match found:", m.group())
else:
    print("No match")
