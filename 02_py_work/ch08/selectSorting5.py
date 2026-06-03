# selectSorting5.py
# 선택 정렬5_오름차순
# 중첩된 for문으로 코드 줄이기
# 4번 반복
# 변수 처리해야될 내용 확인
ca = [21, 10, 11, 15, 13]

for i in range(0, len(ca)-1, 1):    # 0, 1, 2, 3
    mina = ca[i]
    minix = i

    for sb in range(i+1, len(ca), 1):
        if mina > ca[sb]:
            mina = ca[sb]
            minix = sb

    temp = ca[i]
    ca[i] = ca[minix]
    ca[minix] = temp
print(ca)
