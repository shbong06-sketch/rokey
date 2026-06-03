# p2.py

# p.23 0부터 100까지의 정수 중 3의 배수만 출력하는 프로그램

for i in range(101) : 
    if i % 3 == 0 :
        print(i, end = " ")

print("------------------------------")
# p.24 3,6,9게임 만들기
# continue 문을 이용하여 1부터 10까지의 수를 차례대로 출력하지만 3의 배수는 출력하지 않는 프로그램을 작성.

for i in range(1,11) :
    if i % 3 == 0 :
        print("짝", end = " ")
        continue
    print(i, end = " ")

print("------------------------------")
# p.25 다음과 같이 화면 출력 결과가 나올 수 있게 입력받은 정수까지의 총합을 구하는 프로그램을 작성해 보세요.
# 총합을 구하려는 수를 입력하세요. 10
# 1부터 10까지의 총합은 55이다.

i = input("총합을 구하려는 수를 입력하세요.")
i = int(i)
value = 0

for j in range(1, i+1) :
    value += j

print("1부터 %d 까지의 총합은 %d 이다." %(i, value))

print("------------------------------")
# p.26 결과 확인
for sb in range(1, 11, 1):
    total = 0
    total += sb
print(total)

print("------------------------------")
total = 0
for sb in range(1, 11, 1):
    total += sb
print(total, end = "    ")
print("끝")

print("------------------------------")
total = 0
for sb in range(1, 11, 1):
    total += sb
print(total)

print("------------------------------")
total = 0
for sb in range(1, 11, 1):
    total += 1
print(total)

print("------------------------------")
for sb in range(1, 11, 1):
    total = 0
    total += 1
print(total)

print("------------------------------")
# p.27 1부터 입력받은 정수까지의 총합을 구하는 프로그램을 while문으로 작성.
i = input("총합을 구하려는 수를 입력하세요.")
i = int(i)

value = 0
j = 1

while j <= i:
    value += j
    j += 1

print("1부터 %d 까지의 총합은 %d 이다." %(i, value))

print("------------------------------")
# p.28 앞서 작성한 1부터 임의의 수까지의 총합을 구하는 프로그램을 break 문을 사용한 것으로 변경하세요.
i = input("총합을 구하려는 수를 입력하세요.")
i = int(i)

value = 0
j = 1

while True:
    if j>i :
        break
    value += j
    j += 1

print("1부터 %d 까지의 총합은 %d 이다." %(i, value))

print("------------------------------")
# p.29 총합을 구할 첫 번째 수와 두 번째 수를 입력받아 총합을 구하는 프로그램을 for 문과 while 문으로 작성.
# for 문
i = input("총합을 구하려는 첫 번째 수를 입력하세요.")
j = input("총합을 구하려는 두 번째 수를 입력하세요.")
i = int(i)
j = int(j)

value = 0

if j>i:
    start = i
    end = j
else :
    start = j
    end = i

for k in range(start, end+1) :
    value += k

print("%d부터 %d 까지의 총합은 %d 이다." %(start, end, value))

print("------------------------------")
# while 문
i = input("총합을 구하려는 첫 번째 수를 입력하세요.")
j = input("총합을 구하려는 두 번째 수를 입력하세요.")
i = int(i)
j = int(j)

value = 0

if j>i:
    start = i
    end = j
else :
    start = j
    end = i

k = start

while k<=end :
    value += k
    k += 1

print("%d부터 %d 까지의 총합은 %d 이다." %(start, end, value))

print("------------------------------")
# p.30 앞서 작성한 프로그램을 3의 배수 총합을 구하는 프로그램으로 for문과 while문으로 변경.
# for 문

i = input("3의 배수의 총합을 구하려는 첫 번째 수를 입력하세요.")
j = input("3의 배수의 총합을 구하려는 두 번째 수를 입력하세요.")
i = int(i)
j = int(j)

value = 0

if j>i:
    start = i
    end = j
else :
    start = j
    end = i

for k in range(start, end+1) :
    if k % 3 ==0 :
        value += k

print("%d부터 %d 까지의 총합은 %d 이다." %(start, end, value))

print("------------------------------")
# while 문
i = input("3의 배수의 총합을 구하려는 첫 번째 수를 입력하세요.")
j = input("3의 배수의 총합을 구하려는 두 번째 수를 입력하세요.")
i = int(i)
j = int(j)

value = 0

if j>i:
    start = i
    end = j
else :
    start = j
    end = i

k = start

while k<=end :
    if k % 3 == 0 :
        value += k
    k += 1

print("%d부터 %d 까지의 총합은 %d 이다." %(start, end, value))

print("------------------------------")
# p.31 아래 순서도대로 while 문을 사용하여 프로그램을 작성.

MyName = ""

while True :
    print("이름을 입력하세요.")
    MyName = input()
    if MyName == "hongkildong" :
        break
print("확인되었습니다.")

