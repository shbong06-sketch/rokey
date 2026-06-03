# p1.py

# p.21
def draw_stars(num):
    print('*' * num)

# * => 문자열 반복 연산자
# 형태: 문자열 * 숫자 : 문자열을 몇번 반복해서 사용할지 숫자로 지정!
print('hi' * 4)

draw_stars(3)
draw_stars(2)
draw_stars(1)

print("-----------------------")
# p.22
def fadd(pa, pb):
    return pa + pb
def fsub(pa, pb):
    return pa - pb
def fmul(pa, pb):
    return pa * pb
def fdiv(pa, pb):
    return pa / pb

na = 100
nb = 3

print("%d + %d = %d" %(na, nb, fadd(na, nb)))
print("%d + %d = %d" %(na, nb, fsub(na, nb)))
print("%d + %d = %d" %(na, nb, fmul(na, nb)))
print("%d + %d = %d" %(na, nb, fdiv(na, nb)))

print("-----------------------")
# p.23
na = int(input("숫자 입력: "))
nb = int(input("숫자 입력: "))
print("%d + %d = %d" %(na, nb, fadd(na, nb)))
print("%d + %d = %d" %(na, nb, fsub(na, nb)))
print("%d + %d = %d" %(na, nb, fmul(na, nb)))
print("%d + %d = %f" %(na, nb, fdiv(na, nb)))

print("-----------------------")
# p.24
sta = "python example"
lena = len(sta)             # 내장함수
print(lena)                 # 14

# 사용자 정의 함수
def string_length(stb):
    i = 0
    for _ in stb:
        i += 1
    return i

lena = string_length(sta)
print(lena)

print("-----------------------")
# p.25
def fdiv(pa, pb):
    if pb == 0:
        # print("0으로 나눌수 없다.")
        return "0으로 나눌수 없다."
    else :
        return pa / pb

na = float(input("숫자 입력: "))
nb = float(input("숫자 입력: "))
nc = fdiv(na, nb)
print(na, "/", nb, "=", nc)

print("-----------------------")
# p.26
# def mul_sum(num):
#     value = 0
#     for i in range(1, 101):
#         if i % num == 0:
#             value += i
#     return value

def mul_sum(num):
    value = 0
    for i in range(num, 101, num):
        value += i
    return value

n = int(input('1부터 9까지의 정수 중 하나를 입력하세요:'))
if 1 <= n <= 9:
    print("1부터 100까지 %d 배수의 합은 %d입니다." %(n, mul_sum(n)))
else :
    print("1부터 9 사이의 정수를 입력하세요.")

print("-----------------------")
# p.27
def funca(num):
    value = 0
    for i in range(num, 101, num):
        value += i
    return value

def mul_sum(num):
    value =  funca(num)
    return value

n = int(input('1부터 9까지의 정수 중 하나를 입력하세요:'))
if 1 <= n <= 9:
    print("1부터 100까지 %d 배수의 합은 %d입니다." %(n, mul_sum(n)))
else :
    print("1부터 9 사이의 정수를 입력하세요.")