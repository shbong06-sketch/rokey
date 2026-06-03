# week.py
# 어떤 프로그램? => 요일 영어로 번역하는 프로그램
# 프로그램 동작 예시
# "영어로 번역하고 싶은 요일을 입력하세요(예시: 월요일): "
# 금요일
# Friday
# 슴요일
# 한글 요일을 잘 못 입력하셨습니다.

yoil = input("영어로 번역하고 싶은 요일을 입력하세요(예시: 월요일) :")
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

i = 0
if yoil in ("월요일" or "월"):
# if yoil == ("월요일" or "월") # 값 선택 의미; 불가
# if yoil == "월요일" or yoil == "월" :
    print(week[i])
elif yoil == "화요일" :
    i = 1
    print(week[i])
elif yoil == "수요일" :
    i = 2
    print(week[i])
elif yoil == "목요일" :
    i = 3
    print(week[i])
elif yoil == "금요일" :
    i = 4
    print(week[i])
elif yoil == "토요일" :
    i = 5
    print(week[i])
elif yoil == "일요일" :
    i = 6
    print(week[i])
else :
    print("한글 요일을 잘 못 입력하셨습니다.")

print("if 문 종료.")

# in => 포함되어 있는지 확인
# 값 in 자료형      => True/False(불리언 타입으로 return)
# if yoil in ("월요일", "월") :
# if youl == "월요일" or yoil == "월" :

# ("월요일" or "월") => "월요일" ; 불명확한 코드. 잘 안쓰는 코드
