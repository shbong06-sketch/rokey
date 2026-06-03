# pinput.py

print("첫 번째 정수를 입력하세요: ")
ra = input()        # 20
print(type(ra))     # str
ra = int(ra)        # 20
print(type(ra))     # int


rb = input("두 번째 정수를 입력하세요: ")   #5
print(type(rb))     # str
rb = int(rb)        # 5
print(type(rb))     # int

# 1. 문자열 연결 연산자 : str + str
# 2. 산술연산자 : int + int
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다.")
# print("{} + {} = {}".format(ra, rb, rc))

rd = ra - rb
print("{} - {} 결괏값은 {}이다." .format(ra, rb, rd))