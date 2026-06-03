# Human.py

class Human:
    eyes = 2
    nose = 1
    mouse = 1
    def __init__(self, age, name):
        # 인스턴스 변수
        self.age = age
        self.name = name

    # 기능: 자기소개하다.
    def introduce(self):
        print(str(self.age) + "살", end = " ")
        print(self.name + "입니다.")

    # 기능: 먹다.
    def eat(self, food):
        self.food = food
        print(self.food + "을", "먹다.")

    # 기능: 자다.
    def sleep(self):
        print("잔다.")

    # 기능: 말하다.
    def talk(self):
        print("말하다.")

print("눈 개수:", Human.eyes)
print("코 개수:", Human.nose)
print("입 개수:", Human.mouse)

# 객체 생성
kim = Human(29, "김상형")
kim.introduce()
kim.eat("마라탕")

lee = Human(45, "이승우")
lee.introduce()
lee.eat("피자")

# 추가로 기능 구현 해보세요.
# '먹다.', '자다.', '말하다.' 를 출력하는 기능/동작 구현

kim.sleep()
kim.talk()