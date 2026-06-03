# swap.py

# 변수 간 데이터 swap (1)
na = 10
nb = 11
print("na 값:", na, end = " ")
print("nb 값:", nb)

temp = na
na = nb
nb = temp
print("na 값:", na, end = " ")
print("nb 값:", nb)

print("------------------")
# 변수 간 데이터 swap (2)
na = 10
nb = 11
print("na 값:", na, end = " ")
print("nb 값:", nb)

na, nb = nb, na
# 내부적으로 튜플이 사용됨: (nb, na)
print("na 값:", na, end = " ")
print("nb 값:", nb)