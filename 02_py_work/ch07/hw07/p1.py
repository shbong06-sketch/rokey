# p1.py

# p.26
x = 10
def fadd(num):
    b = x + num
    print("변수 x값은", x)
    print("변수 b값은", b)

fadd(10)

print("----------------------------")
# x = 10
# def fadd(num):
#     x = x + num
#     print("변수 x값은", x)

# fadd(10)

x = 10
def fadd(num):
    global x
    x = x + num
    print("변수 x값은", x)
fadd(10)

print("-------------------------")
# p.27
def print_lower_price(price):
    price = int(price * 0.9)
    print("10% 할인된 가격은", price)
    return price

print_lower_price(1000)

print("-------------------------")
# p.28
def func1(num):
    return num + 4

a = func1(10)
b = func1(a)
c = func1(b)
print(c)