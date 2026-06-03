# week04_4.py

class ListIteration:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("리스트를 입력해야 합니다.")
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
        
my_list = [1, 2, 3, 4, 5]
iterator = ListIteration(my_list)

for item in iterator:
    print(item)

print("---------------------")
try: 
    n = int(input("숫자를 입력하세요 :"))
    sqr = (x**2 for x in range(1, n+1))
    for num in sqr:
        print(num)
except (ValueError) as e:
    print(e)

print("2번 답지 풀이------------")

def square_generator(n):
    # 1부터 n까지 숫자의 제곱 생성하는 제너레이터
    for i in range(1, n+1):
        yield i ** 2

try: 
    n = int(input("숫자를 입력하세요: "))
    for square in square_generator(n):
        print(square, end=' ')
except (ValueError) as e:
    print(e)