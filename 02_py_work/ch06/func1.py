# func1.py

# 함수 정의(기억)
# def 함수명(매개변수1, 매개변수2, ...):
#     코드블록
#     return 반환값

# def 함수명():
#     코드블록

# 함수명(인수1, 인수2, ...)

# 기능/동작: 토끼에게 인사
# 입력(매개변수): 없음
# 출력(반환값): 없음
def my_func():
    print("토끼야 안녕!")
    print("거북아 안녕!")
    print("사자야 안녕!")
    print("코끼리야 안녕!")

# 호출(사용)
my_func()
my_func()
my_func()

# 매개변수 = 인수
print("---------------------------------")
def fhello() :
    print("매개변수 없는 함수 호출하기")

fhello()

print("---------------------------------")
# 매개변수 : 매개(전달) 역할을 하는 변수
def funca(na, nb) :
    nc = na + nb
    print("%d + %d = %d" %(na, nb, nc))

funca(10, 20)
# na = 10
# nb = 20
funca(1, 2)
# na = 1
# nb = 2

print("---------------------------------")
# add() 함수 구현
# 함수 정의
def add(num1, num2) :
    # sum = num1 + num2
    # return sum
    return num1 + num2

print(add(2, 3))

print("---------------------------------")
# num1에서 num2를 빼는 연산을 수행하는 sub 함수를 작성하시오.
# 결과값 반환하고 출력.
def sub(num1, num2):
    return num1 - num2

print(sub(10, 3))

print("---------------------------------")
