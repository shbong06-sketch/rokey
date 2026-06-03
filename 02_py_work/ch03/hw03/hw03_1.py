# hw03_1.py

# 6번.
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.

# num = input("정수를 입력하세요: ")
# num = int(num)

# if num % 2 == 0 :
#     print("짝수")
# else :
#     print("홀수")


# 7번.
# 사용자로부터 값을 입력 받은 후 해당 값에 20을 더한 값을 출력하라.
# 단, 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.

# num = input("숫자를 입력하세요: ")
# num = int(num)
# num += 20

# if num > 255 :
#     print(255)
# else :
#     print(num)

# 8번.
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단 출력 값의 범위는 0~255이다.
# 예를 들어 결과값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.

num = input("숫자를 입력하세요: ")
num = int(num)
num -= 20

# if num >= 0 and num <= 255 :
#     print(num)
# elif num >255 :
#     print(255)
# else :
#     print(0)

if num > 255:
    print(255)
elif num < 0 :
    print(0)
else :
    print(num)