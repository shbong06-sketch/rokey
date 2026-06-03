# Singer.py

# 클래스: 객체들
# 가수: 아이유, BTS, ...
# 속성(데이터, 명사): 변수 => 이름
# 기능(동작, 동사): 함수 => 노래부르다

class Singer:
    # name = "아이유"
    job = "가수"               # 클래스 맴버 변수
    def call_name(self, name):
        self.name = name       # 인스턴스 맴버 변수
    # def sing(self):
    #     print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~")
    def sing(self):
        print(self.name, "님이 노래를 부릅니다.")

print(Singer.job)   # 클래스 맴버 변수 사용 ; 객체 생성 전부터 접근 가능. 클래스 이름으로 접근 가능
iu = Singer()       # 생성자 함수
# print(iu.name)    # 속성 확인
iu.call_name("아이유")
print(iu.name)      # 인스턴스 변수 사용
iu.sing()           # 기능 확인

print(Singer.job)
bts = Singer()
# print(bts.name)
bts.call_name("bts")
print(bts.name)
bts.sing()

# 단순 클래스에서 데이터 가져와서 쓰는 방법에 대한 예시
# 객체 다양하게 만들 때는 적절하지 않다.
# 실제로는, 객체 생성 시 초기화 -> 속성 데이터 입력 받아 수행하는 식으로 코드를 작성한다.

