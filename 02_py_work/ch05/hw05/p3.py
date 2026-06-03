# p3.py

# # p.32 아래 순서도대로 while문을 사용하여 프로그램을 작성.

# MyName = ""

# while True :
#     print("이름을 입력하세요.")
#     MyName = input()
#     if MyName != "hongkildong" :
#         continue
#     print("패스워드를 입력하세요")
#     MyPass = input()
#     if MyPass == "hahaha" :
#         break

# print("확인되었습니다.")


print("------------------------------")
# p.33 1단 구구단 출력. for문 사용

for j in range(1, 10) :
    print("%d * %d = %d" %(1, j, 1*j))


print("------------------------------")
# p.34 1단과 2단 구구단 출력. for문 사용

for i in range(1,10) :
    for j in range(1, 3) :
        print("%d * %d = %d" %(j, i, i*j), end="\t")
    print()

print("------------------------------")
# p.35 1단부터 5단까지 구구단 출력. 이중 for문 사용
for i in range(1,10) :
    for j in range(1, 6) :
        print("%d * %d = %d" %(j, i, i*j), end="\t")
    print()

print("------------------------------")
# p.37 이중 for문을 사용하여 다음과 같은 출력을 만드는 프로그램을 작성해보자.

for i in range(1, 6) :
    for j in range(1, i+1) :
        print(j, end = " ")
    print()

print("------------------------------")

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(1, 6) :
    alpha = alphabet[0 : i]
    for j in alpha :
        print(j, end = " ")
    print()

print("------------------------------")

for i in range(1, 6) :
    for j in range(i) :
        print(alphabet[j], end = " ")
    print()
