# hw05_1.py

# 2번
for 변수 in [10, 20, 30] :
    print("변수 =", 변수)

print("-------------------------")
# 3번
prices = [100, 200, 300]
tax = 10

for price in prices :
    print(price+tax)

print("-------------------------")
# 4번
animals = ['dog', 'cat', 'parrot']

for animal in animals :
    print(animal, len(animal))

print("-------------------------")
# 5번
kors = ['가', '나', '다', '라']

# for kor in kors :
#     if kor == '가':
#         continue
#     print(kor)

for kor in kors[1:]:
    print(kor)


print("-------------------------")
# 6번
nums = [3, -20, -3, 44]

for num in nums :
    if num < 0 :
        print(num)

print("-------------------------")
# 7번

for i in range(2002, 2051, 4) :
    print(i)

print("-------------------------")
# 9번

# i = 1
# value = 0
# while True :
#     if i>100 :
#         break
#     value += i
#     i += 1
# print(value)

i = 1
value = 0
while i < 101 :
    value += i
    i += 1
print(value)

print("-------------------------")
# 10, 11번
odd_list = []
even_list = []

# for i in range(1, 31) :
#     print(i, ":", end = " ")
#     if i % 2 == 0:
#         print("짝수")
#         even_list.append(i)
#     else :
#         print("홀수")
#         odd_list.append(i)
# print("짝수 모음:", even_list)
# print("홀수 모음:", odd_list)

num = 1
while num <= 30:
    if num % 2 == 0:
        even_list.append(num)
        # print("짝수")

    else :
        odd_list.append(num)
        # print("홀수")

    num += 1
print("짝수 모음:", even_list)
print("홀수 모음:", odd_list)
