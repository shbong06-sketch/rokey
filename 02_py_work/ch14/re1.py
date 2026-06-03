# re1.py
# 정규표현식(Regular Expression)
# : 문자열 패턴(규칙) 정의해서
# 검색, 검사, 치환, 추출 등 수행하는
# 문자열 처리 규칙

# 패턴: 일정한 규칙성을 가지고 반복적으로 나타나는 형태나 구조

import re
# 패턴객체: "검색대상 문자열"에서 패턴의 발견을 도와주는 객체
# 정규표현식을 정의해서 compile() 함수의 인수로 정규표현식을 전달하면
# 패턴 객체 반환함.

# 메타 문자: 별도의 의미가 담긴 문자

# [] 문자
# - [] 사이에는 대부분 문자(기호) 포함 가능
# - 메타 문자도 사용 가능
#   - (대부분 메타 문자의 별도 의미는 없음. 문자열의 의미만)
#   - 단, 일부 메타 문자는 의미가 있음(예외)

# [abc] : a, b, c 중 한개의 문자와 매치

### 정규표현식 문법
# 패턴객체명 = re.compile("정규표현식")   # 패턴(규칙) 생성
# 패턴객체명.메서드()
# 매치객체명 = 패턴객체명.match('검색대상문자열')
# print(매치객체)

# # match() 함수: '문자열(검색대상문자열)의 처음부터' 검색해서 정규(표현)식과 매치되는지 여부를 조사함.

p = re.compile("[abc]")     # a, b, c 중 하나의 문자와 매치(or 개념)
# m = p.match('a')          # match= 'a' ; [abc] 규칙이 'a'에서 'a'와 일치한다.
# m = p.match('before')     # mathc= 'b'
m = p.match('dude')         # None ; '처음'이 일치하지 않아
print(m)

print("------------------------")
# p = re.compile("[a]")
p = re.compile("[ab]")
print(p.match('apple'))     # match= 'a'
print(p.match('banana'))    # match= 'b' ; 처음만 매칭 여부 판단. 그 이후 문자는 매칭 여부 판단 X
print(p.match('dude'))      # None

# p = re.compile("a")
p = re.compile("ab")        # 'ab' 문자가 검색대상문자열과 일치되는지 여부 판단
print(p.match('apple'))     # None
print(p.match('banana'))    # None
print(p.match('ba'))        # None ; 순서 영향
print(p.match('absolute'))  # match= 'ab'
print(p.match('kabsolute')) # None

print("하이픈(-)---------------")   # 범위 의미
p = re.compile("[a-c]")
print(p.match('apple'))     # match= 'a'
print(p.match('banana'))    # match= 'b'
print(p.match('melon'))     # None

p = re.compile("[0-5]")
print(p.match('1apple'))     # match= '1'
print(p.match('2banana'))    # match= '2'
print(p.match('7melon'))     # None

print("dot(.)---------------")      # 의미 없음
print("plus(+))---------------")    # 의미 없음
p = re.compile("[.abc]")
print(p.match('.apple'))     # match= '.'
p = re.compile("[+abc]")
print(p.match('+banana'))    # match= '+'

print("캐럿(^))---------------")    # 부정(not) 의미
p = re.compile("[^abc]")            # a, b, c 제외 (not a not b not c)
print(p.match('^apple'))            # match= '^'
print(p.match('apple'))             # None
print(p.match('banana'))            # None
print(p.match('melon'))             # match='m'

print("역슬래시(\))---------------")    # 의미가 있는 문자 => 의미 없는 문자
p = re.compile("[\^abc]")          # ^ 문자에 특별한 의미 없음
print(p.match('^apple'))           # match= '^'
p = re.compile("[a\-c]")           # - 문자에 특별한 의미 없음
print(p.match('-apple'))           # match= '-'
print(p.match('banana'))           # None

print("별도 표기법--------------")
p = re.compile("[a-zA-Z]")          # 모든 알파벳
print(p.match('apple'))             # match='a'
print(p.match('Banana'))            # match='B'
print(p.match('melon'))             # match='m'

print("------------------------")
# p = re.compile("[\d]")               # [0-9]
p = re.compile("[\D]")               # [^0-9]
print(p.match('1apple'))             # match='1' => None
print(p.match('Banana'))             # None => match='B'
print(p.match('3melon'))             # match='3' => None

print("------------------------")
p = re.compile("[\s]")               # [ \t\n\r\f\v]
# p = re.compile("[\S]")               # [^ \t\n\r\f\v]
print(p.match(' apple'))             # match=' ' => None
print(p.match('\tBanana'))           # match='\t' => None
print(p.match('\n3melon'))           # match='\n' => None

print("------------------------")
# p = re.compile("[\w]")               # [a-zA-Z0-9_]
p = re.compile("[\W]")               # [^a-zA-Z0-9_]
print(p.match('1apple'))             # match='1' => None
print(p.match('Banana'))             # match='B' => None
print(p.match('3melon'))             # match='3' => None
print(p.match('_orange'))            # match='_' => None

print("------------------------")
# . 문자
p = re.compile(".")
print(p.match('apple'))           # match='a'

p = re.compile("a.b")
print(p.match('aab'))           # match='aab'
print(p.match('a0b'))           # match='a0b'
print(p.match('abc'))           # None
print(p.match('a\tb'))          # match='a\tb'
print(p.match('a\nb'))          # None

print("------------------------")
print(p.match('a12b'))          # None
print(p.match('a1b2'))          # None
p = re.compile("a..b")
print(p.match('a12b'))          # match='a12b'

p = re.compile("a[.]b")
print(p.match('aab'))           # None
print(p.match('a.b'))           # match='a.b'

print("------------------------")
# * 문자
p = re.compile("a*")
print(p.match('apple'))           # match='a'
print(p.match('aaapple'))         # match='aaa'

p = re.compile("ca*t")
print(p.match('ct'))           # match='ct'
print(p.match('cat'))          # match='cat'
print(p.match('caaat'))        # match='caaat'
print(p.match('cbt'))          # None
print(p.match('c t'))          # None

print("------------------------")
# + 문자
p = re.compile("ca+t")
print(p.match('ct'))           # None
print(p.match('cat'))          # match='cat'
print(p.match('caaat'))        # match='caaat'
print(p.match('cbt'))          # None
print(p.match('c t'))          # None

print("------------------------")
# {} 문자: {m}. {m,n}, {m,}, {,n}
p = re.compile("ca{2}t")
print(p.match('ct'))           # None
print(p.match('cat'))          # None
print(p.match('caaat'))        # None

print("------------------------")
p = re.compile("ca{2,5}t")
print(p.match('ct'))           # None
print(p.match('cat'))          # None
print(p.match('caat'))         # match='caat'
print(p.match('caaaat'))       # match='caaaat'
print(p.match('caaaaaaat'))    # None

print("------------------------")
p = re.compile("ca{2,}t")
print(p.match('ct'))           # None
print(p.match('cat'))          # None
print(p.match('caat'))         # match='caat'
print(p.match('caaaat'))       # match='caaaat'
print(p.match('caaaaaaat'))    # match='caaaaaaat'

print("------------------------")
p = re.compile("ca{,1}t")
print(p.match('ct'))           # match='ct'
print(p.match('cat'))          # match='cat'
print(p.match('caat'))         # None

print("------------------------")
# ? 문자: {0,1}
p = re.compile("ca?t")
p = re.compile("ca{0,1}t")
print(p.match('ct'))           # match='ct'
print(p.match('cat'))          # match='cat'
print(p.match('caat'))         # None

print("------------------------")
# ^ 문자
p = re.compile("^hello")
print(p.match('hello world!'))      # match='hello'
print(p.match(' hello world!'))     # None
print(p.match('\nhello world!'))    # None
print(p.match('pello world!'))      # None

print("------------------------")
# $ 문자
p = re.compile("world$")
print(p.match('hello world!'))     # None
print(p.match('hello world '))     # None
print(p.match('hello world\n'))    # None
print(p.match('hello world'))      # None ; match함수 => 첫 글자가 hello
print(p.match('world'))            # match='world'
# p.match() : 문자열의 시작 부분부터 패턴과 일치하는지 확인
#   즉, $를 사용해도 문자열 끝을 찾을 수 없음

print(p.search('hello world!'))     # None
print(p.search('hello world '))     # None
print(p.search('hello world\n'))    # match='world'
print(p.search('hello world'))      # match='world'
# p.search() : 문자열의 전체를 검색하여 패턴 일치하는지 확인
#   $는 search()와 함께 사용하는 것이 일반적!

# 정규식에 ^과 $를 같이 사용하는 경우,
# 해당 문자열과 정확히 동일한 문자열만 매칭됨

p = re.compile("^hello world$")
print(p.search('hello world'))            # match='hello world'
print(p.search('pello world'))            # None
print(p.search('hello world!'))           # None
print(p.search('hello python world'))     # None

