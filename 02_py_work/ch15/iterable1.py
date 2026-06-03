# iterable1.py

a = [1, 2, 3]
# next(a)         # TypeError
# 'list' object is not an iterator

# 이터레이터 생성 방법1 : iter() 함수 사용
iter_a = iter(a)
print(type(iter_a))

print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))

for i in iter_a:
    print(i)
    
for i in iter_a:
    print(i)

print(next(iter_a))      # StopIteration