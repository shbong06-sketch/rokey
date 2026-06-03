# id2.py

# 함수 기능:
# 1. ca 리스트의 원소 총합 계산
# 2. ca 리스트의 마지막 원소를 총합으로 대체

def fk(cb):
    total = 0   # 지역변수

    for sb in range(0, 3, 1):
        total += cb[sb]

    cb[2] = total
    return cb

ca = [10, 20, 30]
print(ca)

cd = fk(ca)
print(ca)
print(cd)
print(type(cd))