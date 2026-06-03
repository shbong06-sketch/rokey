# if1.py
# if 조건식 :
#     코드블록

score = 90      # 초기화
# score = 79      # 재할당
if score > 80 :
    print("Pass!")
print("End program.")

print("--------------")

score = 60
# score = 88
if score > 80 :
    print("Pass!")
else :
    print("Fail.")
print("End program.")

print("--------------")
# 동작 내용: 짝수 확인
na = 21
na = 20
if na % 2 == 0 :
    print(na, "even number")
print("if 문 종료 됨")

print("--------------")
# 동작 내용: 짝/홀수 확인
na = 21
na = 20
if na % 2 == 0 :
    print(na, "even number")
else :
    print(na, "odd number")
print("if 문 종료 됨")