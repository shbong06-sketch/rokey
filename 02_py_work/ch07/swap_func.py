# swap_func.py

# def 함수명(매개변수1, 매개변수2) :
#     코드블록
#     return 반환값

def funca(pa, pb):
    temp = pa           # 지역변수
    pa = pb
    pb = temp
    return pa, pb       # 여러 개의 데이터 return ; 내부적으로 tuple 형태로 packing해 처리.

na = 10                 # 전역변수
nb = 11

print("na 값은", na, "nb 값은", nb)

na, nb = funca(na, nb)  # tuple 형식 return 값을 unpacking.
# na = funca(na, nb)[0]
# nb = funca(na, nb)[1]

print("na 값은", na, "nb 값은", nb)
