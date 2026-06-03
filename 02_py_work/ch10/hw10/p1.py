# p1.py

# p.21
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

car = Car(4, 3000)
print(car.wheel)
print(car.price)

print("--------------------------")
# p.22, 23
class Bicycle(Car):
    def __init__(self, year, wheel, price):
        self.year = year
        super().__init__(wheel, price)

bicycle = Bicycle(2021, 2, 100)
print(bicycle.year)
print(bicycle.wheel)
print(bicycle.price)

print("--------------------------")
# p.24
class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year = year
        self.drivetrain = drivetrain
        super().__init__(wheel, price)

bicycle = Bicycle(2021, 2, 100, "시마노")
print(bicycle.drivetrain)


print("--------------------------")
# p.25

class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year = year
        self.drivetrain = drivetrain
        super().__init__(wheel, price)
    
    def info(self):
        print("year :", self.year)
        print("wheel :", self.wheel)
        print("price :", self.price)

bicycle = Bicycle(2021, 2, 100, "시마노")
bicycle.info()

print("--------------------------")
# p.26

class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year = year
        self.drivetrain = drivetrain
        super().__init__(wheel, price)
    
    def info(self):
        print("year :", self.year)
        print("wheel :", self.wheel)
        print("price :", self.price)
        print("drivetrain :", self.drivetrain)

bicycle = Bicycle(2021, 2, 100, "시마노")
bicycle.info()