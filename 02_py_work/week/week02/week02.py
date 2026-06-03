# week02.py

# 1-1번.
# a = 3.14
# b = True
# c = 'False'

# print(type(a))
# print(type(b))
# print(type(c))

# print("---------------------------------")
# 1-2번
# n1 = int(input("첫 번째 숫자를 입력하세요: "))
# n2 = int(input("두 번째 숫자를 입력하세요: "))
# def plus(p1, p2):
#     return p1 + p2
# def sub(p1, p2):
#     return p1 - p2
# def mul(p1, p2):
#     return p1 * p2
# def div(p1, p2):
#     if p2 == 0:
#         return
#     else :
#         return p1 / p2

# print("더하기 결과:", plus(n1, n2))
# print("빼기 결과:", sub(n1, n2))
# print("곱하기 결과:", mul(n1, n2))
# print("나누기 결과:", div(n1, n2))

print("---------------------------------")
# 2-2번
# - 90점 이상: A학점
# - 80점 이상 90점 미만: B학점
# - 70점 이상 80점 미만: C학점
# - 70점 미만: F학점

score = float(input("점수를 입력하세요: "))
grade_list = ['A학점', 'B학점', 'C학점', 'F학점']

if score >= 90 :
    grade = grade_list[0]
elif score >= 80 :
    grade = grade_list[1]
elif score >70 :
    grade = grade_list[2]
else :
    grade = grade_list[3]

print("당신의 학점:", grade)

print("---------------------------------")
# 4-1번
fruits = ['banana', 'peach', 'lemon', 'grape']
for fruit in fruits:
    if fruit == 'lemon':
        print(fruit)

print("---------------------------------")
# 4-2번
student3 = {'나이': 22, '직업': '학생', '취미': '게임'}
student3['도시'] = '수원'
print(student3.keys())

print("---------------------------------")
# 5-1번
Numbers = [1, 2, 3, 4, 5]
for number in Numbers:
    print(number, end = " ")

print()
print("---------------------------------")
# 5-2번
fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
for fruit in fruits:
    print(fruit)
    if fruit == '사과':
        print('사과를 찾았습니다!')

print("---------------------------------")
# 6-1번
def solution(a, b):
	sum = a + b
	sub = a - b
	multi = a * b
	return sum, sub, multi

n1 = float(input("첫 번째 실수를 입력하세요: "))
n2 = float(input("두 번째 실수를 입력하세요: "))
print('%0.2f + %0.2f = %0.2f' %(n1, n2, solution(n1, n2)[0]))
print('%0.2f + %0.2f = %0.2f' %(n1, n2, solution(n1, n2)[1]))
print('%0.2f + %0.2f = %0.2f' %(n1, n2, solution(n1, n2)[2]))

print("---------------------------------")
# 6-2번
def sum(n):
    value = 0
    for i in range(1, n+1):
        value += i
    return value
num = int(input("정수를 입력하세요: "))
print(sum(num))
