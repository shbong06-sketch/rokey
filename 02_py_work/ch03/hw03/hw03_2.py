# 9번
# 사용자로부터 입력 받은 시간이 정각인지 다음과 같이 판별하라.
# >> 현재시간: 02:00
# 정각 입니다.
# >> 현재시간: 03:10
# 정각이 아닙니다

time = input("시간을 입력하세요(에시. 02:00): ")
print("현재시간:", time)
# print(time[3], time[4])

# if time[3] == '0' and time[4] == '0' :
#     print("정각 입니다.")
# else :
#     print("정각이 아닙니다.")

if time[-2:] == "00":
    print("정각입니다.")
else :
    print("정각이 아닙니다.")

# 10번.
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A

score = input("점수를 입력하세요: ")
score = int(score)

if 100 >= score >= 81 :
    grade = "A"
elif 80 >= score >= 61 :
    grade = "B"
elif 60 >= score >= 41 :
    grade = "C"
elif 40 >= score >= 21 :
    grade = "D"
elif 20 >= score >= 0 :
    grade = "E"
else :
    grade = "NONE"
    print("지정된 점수 범위가 아닙니다.")

print("score: %d" %score)
print("grade is", grade)