# selectSorting1.py

# 정렬 종류
# ca = [21, 10, 11, 15, 13]
# 오름차순 => [10, 11, 13, 15, 21]
# 내림차순 => [21, 15, 13, 11, 10]

# 1. 제일 작은 수의 인덱스 번호 찾기
# 2. 찾은 인덱스를 활용해 0번 인덱스에 최솟값을 위치 하기
ca = [21, 10, 11, 15, 13]
mina = ca[0]     # 현 최솟값
minix = 0       # 현 최솟값 위치(인덱스)

for sb in range(1, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

# 두 데이터를 swap
temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp

print(ca)
# 1차 목표: [10, 21, 11, 15, 13]

