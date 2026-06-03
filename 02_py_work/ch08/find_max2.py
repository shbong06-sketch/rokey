# find_max2.py

su = [5, 4, 7, 10, 6]
print("1----------------------")
def fmax(a, b, c, d, e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최댓값:", max)

print("2----------------------")
def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    if max < fu[1]:
        max = fu[1]
    if max < fu[2]:
        max = fu[2]
    if max < fu[3]:
        max = fu[3]
    if max < fu[4]:
        max = fu[4]
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최댓값:", max)

print("3----------------------")
def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최댓값:", max)

print("4----------------------")
def fmax(a, b, c, d, e):
    fu = [a, b, c, d, e]
    max = fu[0]
    # 리스트 크기가 달라져도 적용 가능한 코드로 수정
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최댓값:", max)

print("5----------------------")
def fmax(a, b, c, d, e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0], su[1], su[2], su[3], su[4])
print("최댓값:", max)

print("6----------------------")
# su = [5, 4, 7, 10, 6]
def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su)
print("최댓값:", max)

print("7----------------------")
def fmax(fu):
    max = fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

max = fmax(su)
print("최댓값:", max)

print("8----------------------")
def fmax(fu):
    max = fu[0]
    for i in range(1, len(fu), 1):  # 길이 제한 X
        if max < fu[i]:
            max = fu[i]
    return max

su = [5, 4, 7, 10, 6, 8, 12, 15, 1, 3]
max = fmax(su)
print("최댓값:", max)

