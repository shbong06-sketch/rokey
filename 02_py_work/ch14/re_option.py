# re_option.py
# 컴파일 옵션

import re

# 패턴객체 = re.compile("정규식", 옵션)

# DOTALL, S
# p = re.compile("a.b", re.DOTALL)
p = re.compile("a.b", re.S)
print(p.match("a\nb"))      # None => match= 'a\nb'

print("------------------------")
# IGNORECASE, I
# p = re.compile("[a-z]+", re.IGNORECASE)
p = re.compile("[a-z]+", re.I)
print(p.match("python"))      # match='python'
print(p.match("Python"))      # match='Python'
print(p.match("PYTHON"))      # match='PYTHON'

print("------------------------")
# MULTILINE, M
# p = re.compile("^python\s\w+")
# p = re.compile("[a-z]+", re.MULTILINE)
# p = re.compile("^python\s\w+", re.M)    # \s: 화이트 스페이스, \w: 모든 문자+숫자+_
# p = re.compile("\w+\sthree$")
p = re.compile("\w+\sthree$", re.M)

data = '''python one
life is too short
python two
life three
you need python
python three'''

print(p.findall(data))
# ['python one'] ; 시작을 첫 줄에 대해서만 인식
# ['python one', 'python two', 'python three'] ; 각각의 라인을 모두 시작점으로 인식

# ['python three']
# ['life three', 'python three']

print("------------------------")
# VERBOSE, X
# p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# p = re.compile(r'''
# &[#]                    # 숫자형 엔티티(문자 개체 참조) 시작
# (
#     0[0-7]+             # Octal form(8진수 형식)
#     | [0-9]+            # Decimal form(10진수 형식)
#     | x[0-9a-fA-F]+     # Hexadecimal form(16진수 형식)
# )
# ;                       # 후행 semicolon
# ''', re.VERBOSE)

p = re.compile(r'''
&[#]                    # 숫자형 엔티티(문자 개체 참조) 시작 ; VERVOSE했을 때, #은 주석 처리 의미. -> 대괄호 필요
(
    0[0-7]+             # Octal form(8진수 형식)
    | [0-9]+            # Decimal form(10진수 형식)
    | x[0-9a-fA-F]+     # Hexadecimal form(16진수 형식)
)
;                       # 후행 semicolon
''', re.X)

data = '&#07; &#8; &#x0A;'
print(p.findall(data))  # ['07', '8', 'x0A']