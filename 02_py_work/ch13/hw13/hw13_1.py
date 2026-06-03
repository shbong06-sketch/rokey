# hw13_1.py

# 6.
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')


print("-----------------------")
# 7.
try:
    raise KeyError('Key is missing')
except KeyError as e:
    print(e)


print("-----------------------")
# 8.
# 람다(lambda)를 사용하여 x와 y값을 입력 받고
# 두 변수의 값을 더하여 add 변수에 할당하는 프로그램을 작성하시오.
# 그리고 인수로 3과 5를 입력 받는 add 함수를 호출하고 결과값을 출력하시오.

add = (lambda x, y: x + y)
print(add(3, 5))


print("-----------------------")
# 9.
# 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다.
# 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)


print("-----------------------")
# 10.
# 다음과 같이 리스트가 주어져 있을 때, 
# 사용자로부터 인덱스를 입력 받아 해당 위치의 원소를 출력하는 프로그램을 작성하시오.
# 범위를 벗어난 인덱스를 입력할 경우 IndexError를 처리하여 
# "잘못된 인덱스입니다." 라는 메시지를 출력하시오.
# 또한 숫자가 아닌 값이 입력으로 들어오는 경우도 예외 처리하시오.

numbers = [10, 20, 30]
try:
    idx = int(input("인덱스 숫자를 입력하세요:"))
    print(numbers[idx])
except IndexError:
    print("잘못된 인덱스입니다.")
except ValueError:
    print("정수를 입력해야 합니다.")