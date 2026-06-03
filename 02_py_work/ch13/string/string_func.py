# string_func.py
# 함수 사용 시 확인할 내용
# 1. 기능/동작
# 2. 매개변수
# 3. 반환값

# '문자열'.split(구분자)
# 1. 기능/동작 : 문자열을 구분자 기준 분리
# 2. 매개변수 : 구분자 / 디폴트값 = 공백
# 3. 반환값 : 구분된 문자열 => list

my_string = 'Python is a popular progrmaing language'
# split_list = my_string.split(' ')
split_list = my_string.split()
print(split_list)
print(split_list[4])

## 이스케이프(escape) 코드: 사전 정의된 문자 조합
# '\n' = new line = LF(line feed)
# '\t' = tab
# '\b\ = backspace
# '\'' = 작은따옴표 표시    '안녕! 난 \'민\'이라고 해~'
# "\""" = 큰따옴표 표시
# '\\' = 역슬래시 표시
# '\r' = CR(carriage return) (커서를 현재 줄 가장 앞으로 이동)
# 그 외에도 form feed('\f'), Vertical Tab('\v') 등등

print('hello\t \'great\' world!!', end = '\n')
print('abcde\bthanks!', end = '\r')
print("hi")

print('------------------')
# '문자열'.strip()
# 1. 기능/동작 : 문자열 양 끝 공백문자(whitespace)를 제거
# 2. 매개변수 : 제거할 문자(생략 시 공백)
# 3. 반환값 : 수정된 문자열 -> str
my_string = '   Python is awsome!   '
stripped_string = my_string.strip()
print(stripped_string)

my_string = '\t   Python is awsome! \n'
stripped_string = my_string.strip()
print(my_string)
print(stripped_string)

# my_string.lstrip()
# my_string.rstrip()

my_string = 'hi, there. h'
stripped_string = my_string.strip('h')
print(stripped_string)

print('------------------')
# '구분자'.join(문자열집합)
# 1. 기능/동작 : iterable의 요소들을 문자열로 연결
# 2. 매개변수 : iterable(문자열 요소 집합 ; 반복 가능한)
# 3. 반환값 : 연결된 문자열 -> str
my_list = ['apple', 'banana', 'cherry']

# joined_string = '-'.join(my_list)
joined_string = '/'.join(my_list)
print(joined_string)