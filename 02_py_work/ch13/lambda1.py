# lambda1.py

# lambda 매개변수: 표현식

# 일반적인 함수 정의 및 호출
# def 함수명(매개변수):
#     코드블록(표현식)
#     return 반환값

# 함수명(인수)
def add(x):
    return x+x
print(add(1))
print(add(2))
print(add(3))

print("-----------------")
# 람다 함수의 정의 및 호출
# 사용 목적 : 이름이 필요 없는 짧은 함수를 한번 사용하기 위해 ; 한번만 사용할 목적
add = lambda x: x+x
print(add(1))
print(add(2))
print(add(3))

print("-----------------")
print( (lambda x: x+x)(1) )

print("-----------------")
square = lambda x: x**2
print(square(3))

print( (lambda x: x**2)(4) )

print("여러개 매개변수 사용----------")
# lambda 매개1, 매개2 : 표현식
print( (lambda x, y: x + y)(3, 10))
print( (lambda x, y=5: x + y)(3))

# 조건문: 가능(단, 표현식 형태만)
# lambda x: 값1 if 조건 else 값2
# 반복문: 불가능