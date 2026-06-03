# hw07_1.py

# return 값 사용 및 함수 호출
def add_numbers(a, b):
    result = a + b
    return result
print(add_numbers(10, 5))

# global 키워드 사용
def add_numbers(a, b):
    global result
    result = a + b

add_numbers(10, 5)
print(result)

print("---------------------------")
# 정수를 매개변수로 입력 받아 해당 정수가 짝수인지 홀수인지 문자열로 반환하는 함수를 작성하세요.

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"

print(check_odd_even(4))   # 출력: Even
print(check_odd_even(7))   # 출력: Odd

print("----------------------------")
# 매개변수로 주어진 임의의 숫자 리스트의 평균을 계산하는 프로그램을 작성하시오.
# 테스트 예시
def calculate_average(list):
    value = 0
    for i in list:
        value += i
    return value / (len(list))

num_list = [10, 20, 30, 40, 50]
average = calculate_average(num_list)
print("평균: ", average)
