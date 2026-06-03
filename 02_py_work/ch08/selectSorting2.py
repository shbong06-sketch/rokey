# selectSorting2.py
# 선택 정렬2

ca = [21, 10, 11, 15, 13]
mina = ca[0]
minix = 0

for sb in range(1, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp

print(ca)
# 1차 목표: [10, 21, 11, 15, 13]

print("-------------------")
mina = ca[1]     # 현 최솟값
minix = 1        # 현 최솟값 위치(인덱스)

for sb in range(2, 5, 1):   # 2, 3, 4
    if mina > ca[sb]:       # 21 > 11 => True
        mina = ca[sb]       # mina = 11
        minix = sb          # minix = 2

temp = ca[1]
ca[1] = ca[minix]
ca[minix] = temp

print(ca)
# 2차 목표: [10, 11, 21, 15, 13]

