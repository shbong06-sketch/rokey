# default2.py
# 파이썬에서는 함수의 오버로딩 지원하지 않는다.
# 동일한 이름의 함수; 나중 함수가 기존 함수를 덮어쓴다.

def persona(width, height):     # 해당 함수가 무시된다.
    print("함수 디폴트 값 없음")
    print("width =", width, end = ' ')
    print("height =", height)

def persona():
    print("매개변수 없는 함수")

def personb(width = 4, height = 3):
    print("함수 디폴트 값 있음")
    print("width =", width, end = ' ')
    print("height =", height)

# 함수가 재정의 되면 기존 함수보다 재정의 함수의 우선순위가 높음.
# persona(10, 20)     # 인수가 없어야 동작
persona()           # 정상 동작
personb()
personb(50, 60)
