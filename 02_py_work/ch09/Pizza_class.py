# Pizza_class.py

# class 클래스명:
#     # 1. 맴버변수
#     맴버변수명 = 속성값
#     # 2. 맴버함수(메서드)
#     def 함수명(self, 매개변수): # self: 객체 그 자신을 가리킨다. ; 반드시 매개변수 맨 앞에 self 적어야
#         self.맴버변수 = 속성값 # 함수 내부에 맴버변수가 쓰이는 경우, self. 붙이기
#         return 반환값

# 객체변수명 = 클래스명()

# 객체변수명.메서드(인수)
# 객체변수명.맴버변수

# 빈 클래스
# class 클래스명:
#     pass    # 코드 작성 시, 설계할 때 pass 활용하기도; 코드블록 내용이 아예 비워두면 error 발생

# 클래스 정의(기억)
class Pizzaclass:
    def order(self):
        print("주문하다.")
        self.kind = 10

# 객체 생성(클래스 사용)
na = Pizzaclass()   # (객체)생성자 함수(초기화 함수) # class 사용 : class 내부 내용을 실행할 준비

na.order()      # 객체.메서드() ; class 내부 함수 사용/ 메서드에 대한 실행
print(na.kind)  # 객체.맴버변수

# list라는 클래스에 대해 실행되는 함수 = 메서드
# .append, 등