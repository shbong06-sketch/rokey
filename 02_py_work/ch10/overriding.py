# overriding.py

# 추상적
class Animal:
    def eat(self):
        print("먹다.")
    def move(self):
        print("이동하다.")
    def sound(self):
        print("소리내다.")

# 구체적
class Cat(Animal):
    def eat(self):
        print("잡식하다.")
    def sound(self):
        print("야옹~", end = "")
        super().sound()

dog = Animal()
tiger = Animal()
lion = Animal()
dog.eat()
dog.move()
dog.sound()

print("--------------------")
cat1 = Cat()
cat1.eat()
cat1.sound()
cat1.move()
