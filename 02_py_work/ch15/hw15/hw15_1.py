# p2.py

# 6.
numbers = [1, 2, 3, 4, 5]

inums = (x for x in numbers)
for inum in inums:
    print(inum)

print("-----------------------")
# 7.
fruits = ["apple", "banana", "cherry"]
ifruits = iter(fruits)
while True:
    try:
        print(next(ifruits))
    except StopIteration:
        print("끝")
        break

print("-----------------------")
# 8.
numbers = range(10)
isquare = (x for x in numbers)
for i in isquare:
    print(i ** 2)

class Square:
    def __init__(self, num):
        self.data = 0
        self.num = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.data >= self.num:
            raise StopIteration
        result = self.data ** 2
        self.data += 1
        return result
    
isquare = Square(10)

for i in isquare:
    print(i)

print("-----------------------")
# 9.
ieven = (x for x in range(10) if x % 2 ==0)
for i in ieven:
    print(i)

print("-----------------------")
# 10.

class MyRange:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("step must not be zero.")
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
            (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else :
            result = self.current
            self.current += self.step
            return result

start = 1
stop = 10
step = 2
my_range = MyRange(start, stop, step)
for num in my_range: 
    print(num)

print(list(range(start, stop, step)))