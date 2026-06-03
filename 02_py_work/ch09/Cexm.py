# Cexm.py

class Cexm:
    def fsam(self):
        print("맴버 함수(메소드)")
    def fsbm(self, pa):
        self.x = pa     # 인스턴스 맴버 변수
        print("맴버 변수 x는", self.x)

ca = Cexm()     # 인스턴스 객체 생성
ca.fsam()       # 메서드 호출
ca.fsbm(10)     # 매서드 호출_인수 전달해 값을 할당
print(ca.x)

cb = Cexm()     # 인스턴스 객체 생성
cb.fsam()
cb.fsbm(20)
print(cb.x)     # 맴버 함수 종료 후에도, 맴버 변수는 사라지지 않는다.

# 파이썬의 변수
# 1. 전역변수
# 2. 함수의 지역변수
# 3. 클래스/인스턴스 변수 ; 별개의 개념으로 정리할 것!

