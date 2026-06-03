# list_swap1.py

ca = [10, 11]
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

print("-----------------------------")
def funca(na, nb):
    temp = na
    na = nb
    nb = temp

ca = [10, 11]
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

funca(ca[0], ca[1])
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

print("-----------------------------")
ca = [10, 11]
cb = ca
print("ca:", ca)
print("cb:", cb)

temp = cb[0]
cb[0] = cb[1]
cb[1] = temp
print("ca:", ca)
print("cb:", cb)
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])
print("cb[0]의 값은", cb[0], end = " ")
print("cb[1]의 값은", cb[1])

print("-----------------------------")
def funca(cb):
    print("리스트 cb 주소:", id(cb))
    temp = cb[0]
    cb[0] = cb[1]
    cb[1] = temp

ca = [10, 11]
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

print("리스트 ca 주소:", id(ca))
funca(ca)
print("ca[0]의 값은", ca[0], end = " ")
print("ca[1]의 값은", ca[1])

