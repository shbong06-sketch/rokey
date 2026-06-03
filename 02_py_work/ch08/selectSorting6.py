# selectSorting6.py
# 선택 정렬6
# fselsort 함수로 정의 및 호출

def fselsort(ca):
    for i in range(0, len(ca)-1, 1):
        mina = ca[i]
        minix = i

        for sb in range(i+1, len(ca), 1):
            if mina > ca[sb]:
                mina = ca[sb]
                minix = sb

        temp = ca[i]
        ca[i] = ca[minix]
        ca[minix] = temp
    return ca

ca = [21, 10, 11, 15, 13]
print(fselsort(ca))
ca = [31, 40, 19, 57, 17]
print(fselsort(ca))



print("-------------------")
# 재귀함수 연습해보기

# def fselsort(ca):
#     # len(ca)-1번 반복

    
#     if i == len(ca):
#         return

#     mina = ca[i]
#     minix = i
#     for sb in range(i+1, len(ca), 1):
#         if mina > ca[sb]:
#             mina = ca[sb]
#             minix = sb
#     temp = ca[i]
#     ca[i] = ca[minix]
#     ca[minix] = temp
    