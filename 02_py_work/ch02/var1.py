# var1.py

na = 20
print(na)
print(type(na))         # 데이터 타입(int)

rainbow = "빨주노초파남보"
print(rainbow)
print(type(rainbow))    # 데이터 타입(str)

count = 0               # 초기화
print(count)
print(id(count))        #주소번지

count = 1               # 재할당(메모리도 새롭게 할당)
print(count)
print(id(count))        #주소번지

count = 0               # 재할당
print(count)
print(id(count))        #주소번지

count = count + 1       # 재할당
print(count)
print(id(count))        #주소번지

pi = 3.14
print(type(pi))         # float(부동 소수점)

pi = "3.14"
print(type(pi))         # str
