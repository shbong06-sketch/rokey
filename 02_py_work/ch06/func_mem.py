# func_mem.py

# na = 10
# nb = 11

# pa = na     # 10    # na에 연결되던 10이 pa에도 연결
# pb = nb     #11     # nb에 연결되던 11이 pb에도 연결

# nc = pa + pb        # 21
# print(nc)

print("-------------------------")
# def funca(pa, pb):
#     nc = pa + pb                # 함수 내부영역에서 nc 변수 할당됨.

# na = 10
# nb = 11

# funca(na, nb)                   # 함수 내부영역 내용 사라짐. >> nc 내용도 사라짐.
# print(na, "+", nb, "=", nc)     # global영역에서 nc 변수 할당이 되어있지 않음.

print("-------------------------")
def funca(pa, pb):
    nc = pa + pb
    return nc                   # 함수 내부 내용을 바깥으로 return

na = 10
nb = 11

nd = funca(na, nb)              # 함수 내부영역은 소멸. global 영역에서 생성된 nd에 nc 값이 할당.
print(na, "+", nb, "=", nd)