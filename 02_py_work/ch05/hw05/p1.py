# p1.py

for num in [3, 1, 2] :
    print(num)

print("-------------------")

for num in range(2) :
    print(num)

print("-------------------")

clovers = ['clover1', 'clover2', 'clover3']
for clover in clovers :
    print(clover)

print("-------------------")
clovers = ['clover1', 'clover2', 'clover3']
for num in range(3) :
    print(clovers[num])

print("-------------------")
count = 0
while count < 3:
    print(count)
    count += 1

print("-------------------")
count = 1
while count < 4 :
    count += 1
    print(count)

print("-------------------")
# 동작/기능 => 범위 내 홀수 출력
count = 0
while count <= 5:
    if count %2 != 0:
        print(count)
    count += 1

print("-------------------")
# price = 0
# while price != -1 :
#     price = int(input("가격을 입력하세요(종료: -1): "))
#     if price > 10000 :
#         print("너무 비싸요.")
#     elif price >5000 :
#         print("괜찮은 가격이네요.")
#     elif price > 0 :
#         print("정말 싸요.")

print("-------------------")

for i in range(101) :
    if i % 3 == 0 :
        print(i, end=" ")
print()

print("-------------------")
i = 1
for j in range(1, 10) :
    print("%d * %d = %d" %(i, j, i*j))

print("-------------------")
for i in range(1,10) :
    for j in range(1, 10) :
        print("%d * %d = %d" %(j, i, i*j), end="\t")
    print()