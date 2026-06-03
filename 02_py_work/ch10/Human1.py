# Human1.py

class Human:
    # 1. 멤버 변수
    eyes = 2     # 클래스 멤버 변수
    nose = 1
    mouth = 1
    # 2. 멤버 함수(메서드)
    def __init__(self, name, age):
        self.name = name    # 인스턴스 멤버 변수
        self.age = age
    
    def introduce(self):
        print("이름:", self.name)
        print("나이:", self.age)

    def eat(self):
        print("먹다.")

    def sleep(self):
        print("자다.")

    def talk(self):
        print("말하다.")

class Student(Human):
    # 1. 멤버 변수(속성)

    # 2. 멤버 함수(메서드)(기능/동작)
    def __init__(self, name, age, studentNum):
        # self.name = name    # 인스턴스 멤버 변수
        # self.age = age
        super().__init__(name, age)
        self.studentNum = studentNum

    def introduce(self):
        # print("이름:", self.name)
        # print("나이:", self.age)
        super().introduce()
        print("학번:", self.studentNum)

    def study(self):
        print("공부하다.")

print("눈 개수 :", Human.eyes)  # 클래스 변수 접근
lee = Human("이수근", 49)   # 객체 생성 및 초기 데이터 설정(생성자)
print(lee.name)     # 인스턴스 변수 접근
lee.introduce()     # 메서드 접근
lee.eat()
# lee.study()         # AttributeError ; 상속 받았을 때에만 가능

print("--------------------")
print("눈 개수 :", Student.eyes)    # 부모 속성 데이터를 상속한다.
print("코 개수 :", Student.nose)
kim = Student("김수로", 56, 20260423)
print(kim.name)
kim.introduce()     # 자식 클래스 멤버 우선순위 높음
kim.study()
kim.eat()       # 부모 기능/동작 상속
kim.sleep()
print(kim.studentNum)