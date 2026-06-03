# dict1.py
# 딕셔너리 생성
# 변수명 = {키1 : 값1, 키2 : 값2, 키3 : 값3}

my_dict1 = {}           # 빈 딕셔너리
print(my_dict1)
print(type(my_dict1))   # dict

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2)

my_dict3 = {'이름': '앨리스', '나이':10, '시력':[1.0, 1.2]}
print(my_dict3)

# 값 접근하기
print(my_dict3['이름'])
print(my_dict3['나이'])
print(my_dict3['시력'])

print(my_dict3.get('이름'))

# 값 추가하기
my_dict3['성별'] = '여성'
print(my_dict3)

# 값 변경하기
my_dict3['나이'] = 11
print(my_dict3)

print("---------------------")
# 값 추가하기
clover = {'나이': 27, '직업': '병사'}
print(clover)

clover['번호'] = 9
print(clover)

# 값 변경하기
clover['번호'] = 8
print(clover)

clover1 = {'나이': 37, '직업': '마법사', '능력':{'체력': 70, '마력':30}}
print(clover1)

print("---------------------")

# 1. 이름, 나이, 성별, 원하는 데이터 1가지 를 활용하여
# 딕셔너리를 생성하시오.
# 2. 생성된 딕셔너리에 전화번호와 주소를 추가하시오.
# 3. 생성된 데이터에 접근하시오.

my_data = {'이름': '봉승현', '나이': 25, '성별':'남성', '취미': ['테니스', '헬스']}
print(my_data)

my_data['전화번호'] = '010-7113-0612'
my_data['주소'] = '경기도 남양주'
print(my_data)

print(my_data['전화번호'])
print(my_data.get('주소'))

# 나이를 +1 하여 수정하시오.
my_data['나이'] = 26
print(my_data)

print("---------------------")
print(my_data.items())

print(my_data.keys())

print(my_data.values())

# 활용 방법
# 추후 다룰 예정