# Bag.py

# 클래스: 가방
# 객체: 숄더백, 백팩, 핸드백, 에코백, 클러치백, 크로스백, 토트백
# 속성(데이터, 변수, 명사): 재질, 색상, 무게, 브랜드, 수납개수, 가격
# 기능(동작, 함수, 동사): 넣다, 꺼내다, 꾸미다, 보호하다, ...

class Bag:
    # 클래스 맴버변수
    call_name = "가방"
    # 맴버 함수(메서드)
    # def info(self):
    def __init__(self, kind, color):          # __init__() 객체 처음 생성 시, 처음 실행되는 함수(별도의 구현 필요X)
        # print("초기화 수행")
        # 인스턴스 맴버변수
        self.kind = kind
        self.color = color
        self.data = []           # 가방 내 물건 정보

    def add(self, x):            # 넣다
        self.data.append(x)

    def addtwice(self, x):       # 두번 넣다
        self.add(x)
        self.add(x)

shoulder = Bag("숄더백", "검정")                 # 인스턴스 객체 생성
print(shoulder.kind)
print(shoulder.color)
print(shoulder.call_name)
# shoulder.info()
shoulder.add("휴대폰")
shoulder.addtwice("돈")
print(shoulder.data)

handbag = Bag("핸드백", "흰색")
print(handbag.kind)
print(handbag.color)
# handbag.info()
handbag.add("지갑")
handbag.addtwice("책")
print(handbag.data)

# crossbag = Bag()
# # crossbag.info()
# crossbag.addtwice("사탕")
# crossbag.add("물")
# print(crossbag.data)