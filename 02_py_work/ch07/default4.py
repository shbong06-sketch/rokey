# default4.py

def persona(width = 11, height = 21):
    print("함수 디폴트 값 없음")
    print("width =", width, end = ' ')
    print("height =", height)

def personb(width = 4, height = 3):
    print("함수 디폴트 값 있음")
    print("width =", width, end = ' ')
    print("height =", height)

persona(10, 20)     # 인수 우선순위가 더 높음.
persona()           
personb()

# 1. 모든 매개변수에 기본값 설정 가능
# 2. 인수 전달시 앞에서부터 설정 가능
# 3. 기본값이 있더라도 인수 설정 가능(인수 우선 처리)
# 4. 부분 매개변수에 기본값 설정시 뒤에서 부터 설정할 것 **위치 인수와 연결해서 생각해볼 수 있어.

print("--------------------")
# 위치 인수: 순서대로 전달하는 인수
persona(10)         # 인수 1개만 주어진 경우
# 키워드 인수: 이름을 지정해서 전달하는 인수
persona(height = 30)



print("----------------------------")
# person_lee 사람 함수 생성
# 기능/동작: 3가지 데이터를 확인(출력)
# 함수 내 전달되는 데이터(매개변수): 몸무게, 키, 나이
# 반환값: 없음

# def person_lee(weight = 70, height = 175, age = 30):
#     print("체중 :", weight, end = ' ')
#     print("\t신장 :", height, end = ' ')
#     print("\t나이 :", age)

# def person_lee(weight, height, age = 30):
#     print("체중 :", weight, end = ' ')
#     print("\t신장 :", height, end = ' ')
#     print("\t나이 :", age)

def person_lee(weight, height = 170, age = 30):
    print("체중 :", weight, end = ' ')
    print("\t신장 :", height, end = ' ')
    print("\t나이 :", age)

# 1. 모든 매개변수에 기본값 설정 가능
# person_lee()

# 2. 인수 전달시 앞에서부터 설정 가능
person_lee(55)
person_lee(55, 168)
# person_lee(55, age = 20)

# 3. 기본값이 있더라도 인수 설정 가능(인수 우선 처리)
person_lee(55, 160, 21)
# person_lee(age = 20)

# 4. 부분 매개변수에 기본값 설정