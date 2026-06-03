# priority.py

num1 = 2 * (3 - 5)
print(num1)

num2 = 1 > (2 and 3) * 3
print(num2)                 # False

print(2 and 3)              # 3
print(0 and 3)              # 0
# 앞의 값이 True(0이 아니면) => 뒤 값 반환
# 앞의 값이 False(0이면) => 앞 값 반환


print("----------------")
print(9 > 4 and 3 > 2)
# True and True
# True
print(9 < 4 and 3 > 2)
# False and True
# False
print(9 < 4 or 3 < 2)
# False or False
# False
print(9 < 4 or 3 > 2)
# False or True
# True

print("----------------")
# 문제 1
print(9 < 4 or 3 < 2 and 4 > 2)
# False or False and True
# False or False
# False

# 문제 2
print((3 - 5) + 3 < 1 and 3 - 5 > 1)
# -2 + 3 <1 and 3 - 5 >1
# 1 < 1 and -2 > 1
# False and False
# False

# 연산자 우선순위
# 괄호 > 산술 > 비교 > 논리 > 대입
# 논리 연산자 내 우선순위
# not > and > or
# 산술 연산자 내 우선순위
# ** > 단항연산자(+x, -x; 음수, 양수 표현) > * / // % > + =

