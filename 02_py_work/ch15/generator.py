# generator.py

def simple_generator():
    print("실행")   # 객체에서 next 함수 실행 시 동작.
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
print(type(g))      # generator

print(next(g))
print(next(g))
print(next(g))
# print(next(g))      # StopIteration

# 제너레이터 ㄷ 이터레이터 (포함 관계)
# : 이터레이터가 더 큰 개념이고, 제너레이터는 구현 방법 중 하나
print("------------------")
print(dir(g))

print("__iter__" in dir(g)) # True
print("__next__" in dir(g)) # True