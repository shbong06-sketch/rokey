# comprehension.py

# 리스트 컴프리헨션 : 새 리스트 생성
# [표현식 for 요소 in 이터러블 (if 조건)]
# 표현식(Expression) = "값을 만들어내는 코드"

numbers = [1, 2, 3, 4]
squared = [x**2 for x in numbers]
print(squared)          # [1, 4, 9, 16]

# 조건문이 참인 경우, 요소를 포함하여 표현식 수행
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)     # [2, 4]

squared = [x**2+1 for x in numbers if x % 2 == 0]
print(squared)         # [5, 17]

print("------------------------------")
# 딕셔너리 컴프리헨션 : 새 딕셔너리 생성
# {key: value, key: value, key:value}
# {key표현식:value표현식 for 요소 in 이터러블 (if 조건)}

squared_dict = {x:x**2 for x in range(0,5)}
print(squared_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

even_squared_dict = {x : x**2 for x in range(10) if x % 2 == 0}
print(even_squared_dict)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 과목별 점수를 표함한 딕셔너리 생성
subjects = ['수학', '영어', '역사']     # 나중에 점수를 추가로 입력받아 활용할 수 있는 과목 별 시험 점수를 나타내는 딕셔너리를 생성
scores = {subject : 0 for subject in subjects}
print(scores)

print("------------------------------")
# 제너레이터 생성 방법2
# 제너레이터 컴프리헨션 : 새 제너레이터 생성
# (표현식 for 요소 in 이터러블 [if 조건])
gen = (i * i for i in range(1, 10))
print(type(gen))    # generator

print(next(gen))    # 1
for item in gen:
    print(item)     # 4 9 16 ... 81
print(next(gen))    # StopIteration

