# slicing.py

week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])
print(type(week[2:5]))
print(week)

print("--------------------")
# 문제1: 토/일 데이터를 출력하시오.
print(week[5:7])

# 문제2: 월~목 데이터를 출력하시오.
print(week[0:4])

print("음수 인덱싱 ------------------")
print(week[-1])
print(week[-2])
print(week[-3])

print("음수 슬라이싱 ------------------")
# 리스트명[시작인덱스:끝인덱스+1]
print(week[-3:-1])
print(week[-5:5])
# 슬라이싱 범위 설정 시: 좌 => 우 로 지정!
print(week[-1:-3])
print(week[7:5])

print(week[-3:-1])  # ['금', '토']
print(week[-3:6])   # ['금', '토']

print("인덱스 번호 생략하는 경우----------")
# 1. 시작 인덱스 생략
print(week[:5])             # week[0:5]

# 2. 끝 인덱스 생략
print(week[-3:])            # week[-3:마지막인덱스+1]
print(week[-3:7])

# 3. 모든 인덱스 생략 => 전체 데이터 대상
print(week[:])              # week[0:마지막인덱스+1]


# print(week[::-1])