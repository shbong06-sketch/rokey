# map_func.py

# map(함수, 이터레이터)
# 1. 기능/동작: 이터레이터에 함수 적용
# 2. 매개변수: 적용함수, 이터레이터
# 3. 반환값: 이터레이터에 함수를 적용한 결과 -> map 객체 (이터레이터)

def square(x):
    return x**2
print(square(3))

print("-----------------")
square = lambda x: x**2
print(square(3))

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)
# print(squared_numbers)    # 맵 객체
print(list(squared_numbers))

print("-----------------")
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))