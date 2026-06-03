# hw09_1.py

# 3, 4
class Phone:
    pass

my_phone = Phone()

print("----------------")
# 5,6,7

class Phone:
    print("휴대폰 생성")    # 클래스 정의 시 실행 ; 객체 생성시 X
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

my_phone = Phone("삼성", 2026, "하양")
print("제조사:", my_phone.brand)
print("출고년도:", my_phone.year)
print("색상:", my_phone.color)

print("--------------------")
# 8.
class Phone:
    print("휴대폰 생성")
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    def info(self):
        print("제조사:", self.brand)
        print("출고년도:", self.year)
        print("색상:", self.color)

my_phone = Phone("삼성", 2026, "하양")
my_phone.info()


print("--------------------")
# 9.

class Phone:
    print("휴대폰 생성")
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    def info(self):
        print("제조사:", self.brand)
        print("출고년도:", self.year)
        print("색상:", self.color)
    def setInfo(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        print("----수정 되었습니다.----")
        

my_phone = Phone("삼성", 2026, "하양")
my_phone.info()
my_phone.setInfo("애플", 2025, "오렌지")
my_phone.info()