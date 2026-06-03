# list_swap2.py
print("--------------")
a = [10, 11, 12, 13]
print("리스트 a 값", a)
print(id(a))
print(id(a[0]), end='\t')
print(id(a[1]), end='\t')
print(id(a[2]), end='\t')
print(id(a[3]))

print("--------------")
a[1] = 21
print("리스트 a 값", a)
print(id(a))
print(id(a[0]), end='\t')
print(id(a[1]), end='\t')
print(id(a[2]), end='\t')
print(id(a[3]))

print("--------------")
b = a
print("리스트 b 값", b)
print(id(b))
print(id(b[0]), end='\t')
print(id(b[1]), end='\t')
print(id(b[2]), end='\t')
print(id(b[3]))

print("--------------")
b = [30, 31, 32, 33]
print("리스트 b 값", b)
print(id(b))
print(id(b[0]), end='\t')
print(id(b[1]), end='\t')
print(id(b[2]), end='\t')
print(id(b[3]))