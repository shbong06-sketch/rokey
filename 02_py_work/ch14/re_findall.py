# re_findall.py

import re
p = re.compile("[a-z]+")
# m = p.findall("life is too short")
# print(m)      # ['life', 'is', 'too', 'short']
m = p.findall("3 py8thon")
print(m)        # ['py', 'thon']

print("--------------------")
p = re.compile("Python")
m = p.findall('The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.')
print(m)        # ['Python', 'Python', 'Python']