# hw06_1.py

# 5번
def print_hello():
    print("안녕하세요")

# 6번
print_hello()

# 7번
for i in range(100):
    print_hello()

print("-----------------------------")

# 8번
# def great(name='Guest'):
#     print('Hello, {}!' .format(name))

def great(name='Guest'):
    return f"Hello, {name}!"    # f string ; 문자열 안에 변수 값 직접 삽입

print(great('Alice'))