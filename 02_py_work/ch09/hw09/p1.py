# p1.py

# p.13
class Cadd:
    def fadd(self, x, y):
        self.x = x
        self.y = y
        self.hap = self.x + self.y

obj = Cadd()
obj.fadd(10, 20)
print("객체 obj 내의 인스턴스 변수 x의 값은", obj.x)
print("객체 obj 내의 인스턴스 변수 y의 값은", obj.y)
print("객체 obj 내의 인스턴스 변수 hap의 값은", obj.hap)

print("--------------------------")
# p.21
def fadd(a = 1, b = 2):
    a = a
    b = b
    return a + b
ohap = fadd(10, 20)
print("ohap의 값은", ohap)
ohap2 = fadd(10)
print("ohap2의 값은", ohap2)
ohap3 = fadd()
print("ohap3의 값은", ohap3)

print("----------------------------")
# p.22
class Cadd:
    def fadd(self, a = 1, b = 2):
        self.a = a
        self.b = b
        self.hap = self.a + self.b
    
obj = Cadd()
obj.fadd(10, 20)
print("객체 obj 내의 인스턴스 변수 hap의 값은", obj.hap)
obj.fadd(10)
print("객체 obj 내의 인스턴스 변수 hap의 값은", obj.hap)
obj.fadd()
print("객체 obj 내의 인스턴스 변수 hap의 값은", obj.hap)

print("----------------------------")
# p.23
# 속성(데이터, 명사): 변수 => 고양이
# 기능(동작, 동사): 함수 => 야옹 소리내다

class Animal:
    def __init__(self, name, asound):
        self.name = name
        self.asound = asound
    def sound(self):
        print("'" + self.asound + "'", "소리내다.")

cat = Animal('고양이', '야옹')
print("이름 =", cat.name)
cat.sound()

print("----------------------------")
# p.23
# 속성(데이터, 명사): 변수 => 이름, 색상
# 기능(동작, 동사): 함수 => 맛이 나다

class Fruit:
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor
    def taste(self):
        print(self.flavor, "맛이 나다.")

orange = Fruit("오렌지", "노란색", "새콤하다")
print("이름 =", orange.name, ", 색상 =", orange.color)
orange.taste()