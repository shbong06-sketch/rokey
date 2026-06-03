# dictFunc.py

a = {1:"월", 2:"화", 3:"수"}
print(a)

x = a
print(x)

x[1] = '일'
print(x)
print(a)

print("-------------------------")
def fch(x):
    x[1] = '일'

a = {1:"월", 2:"화", 3:"수"}
print(a)
fch(a)      # x = a
print(a)