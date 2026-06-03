# p1.py

# p.27
su = [5, 4, 7, 10, 6]

def fmin(fu):
    min = fu[0]
    for sfu in fu:
        if min > sfu :
            min = sfu
    return min

mina = fmin(su)
print("최소값 mina는", mina)