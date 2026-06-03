# Car.py

class Car:
    def __init__(self, num, speed):
        self.num = num
        self.speed = speed
    def fprint(self):
        print("차량번호", self.num)
        print("차량속도", self.speed)
    
new_car = Car(2023, 90)
new_car.fprint()