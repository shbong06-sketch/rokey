# set1.py
# set(세트) : 중복을 허용하지 않는 자료 구조
# 문법: {데이터1, 데이터2, 데이터3}

numbers = {1, 2, 3, 3, 4}
print(numbers)      # {1, 2, 3, 4} ; 중복 데이터 제거

# 요소 추가 및 제거
numbers.add(5)
print(numbers)
numbers.remove(3)
print(numbers)

# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 교집합 : &
print(set1 & set2)      # {3}

# 합집합 : |
print(set1 | set2)      # {1, 2, 3, 4, 5}

# 차집합 : -
print(set1 - set2)      # {1, 2}

# set는 산술 연산을 지원하지 않음.
# 집합 자료형 => 숫자 계산보다 집합 연산을 위해 설계된 자료형
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
# print({1, 2} + {3, 4})  # TypeError
# => set은 순서에 대한 개념이 없다.