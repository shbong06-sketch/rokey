# default1.py

def persona(width, height):
    print("함수 디폴트 값 없음")
    print("width =", width, end = ' ')
    print("height =", height)

def personb(width = 4, height = 3):
    print("함수 디폴트 값 있음")
    print("width =", width, end = ' ')
    print("height =", height)

persona(10, 20)
# persona()         # 인수가 없어서 에러 발생
persona(30, 40)
personb()           # 인수가 없지만 정상 실행
personb(50, 60)     # 기본 값보다 인수 우선순위 높음.
