# p1.py

foods = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]

# 1번. iter() 함수 활용
ifoods = iter(foods)
print(type(ifoods))
for food in ifoods:
    print(food)

# print(next(ifoods)) # StopIteration

print("-----------------------------")
# 2번. 클래스 작성
class Iter_food:
    def __init__(self, data):
        self.data = data
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num >= len(self.data):
            raise StopIteration
        result = self.data[self.num]
        self.num += 1
        return result

foods_class = Iter_food(foods)
print(type(foods_class))
for food in foods_class:
    print(food)

# print(next(ifoods)) # StopIteration

print("-----------------------------")
# 3번. 제너레이터 생성
foods_gen = (x for x in foods)

print(type(foods_gen))
for food in foods_gen:
    print(food)

# print(next(foods_gen))