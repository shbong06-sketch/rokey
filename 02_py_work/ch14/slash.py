# slash.py

import re
# 패턴객체 = re.compile("정규표현식")
# 패턴객체.match("검색대상문자열")

# 예) "\section" 문자열 검색x``

# p = re.compile("\section")        # None ; SyntaxWarning: invalid escape sequence '\s'
# p = re.compile("\\section")       # None
# p = re.compile("\\\\section")     # match='\\section'
p = re.compile(r"\\section")        # match='\\section'
print(p.match("\section python hello thanks"))

# '\\section' 으로 보이는 이유?
# 문자열 안의 역슬래시를 구분하기 위해 escape해서 보여주기 때문

# 1. 파이썬 리터럴 규칙(이스케이프)     두가지가 각각 동작.
# "\\" => "\"
# "\\\\" => "\\"
# 2. "\s" 정규표현식 화이트스페이스 의미
# "\\section" => "\section"

## raw string
# => 파이썬 문자열 리터럴 안에서
# \n, \t 같은 "이스케이프 코드 처리"를 없애주는 역할

print("------------------------")
# p = re.compile("\\new")         # match = '\new'
p = re.compile(r"\new")         # match = '\new'
print(p.match("\new python hello thanks"))

# 1. 파이썬 리터럴 규칙(이스케이프)     두가지가 각각 동작.
# "\\" => "\"