# while1.py

# (조건식에 사용된)변수 초기화
# while 조건(식) :
#     코드블록
#     (while문을 빠져 나올수 있는)증감식

# while True :
#     print('Crtl + C를 누르세요')


a = 10
b = 5
a = a - b
print(a)

a = 10
b = 5
a -= b
print(a)

# 연산자        의미          예시         결과
# --------------------------------------------------
# *=      곱하기 후 대입     a *= 3      a = a * 3
# /=      나누기 후 대입     a /= 3      a = a / 3
# //=     몫 나누기         a //= 3     a = a // 3
# %=      나머지             a %= 3      a = a % 3
# **=     거듭제곱          a **= 3     a = a ** 3


print("----------------------")
num = 0
while num < 3 :
    print("안녕거북이", num)
    # num = num + 1
    num += 1

print("----------------------")
stra = "파이썬"
strb = "프로그래밍"
stra = stra + strb
print(stra)

stra = "파이썬"
strb = "프로그래밍"
stra += strb
print(stra)
