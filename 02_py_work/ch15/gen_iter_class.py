# gen_iter_class.py

# 제너레이터와 동일한 이터레이터 클래스 생성
# gen = (i * i for i in range(1, 10))

# 간단하고 한번 흐르게 할 데이터 => 제너레이터 컴프리헨션
# 상태/제어/재사용 필요 => 이터레이터 클래스

class MyIterator:
    def __init__(self):
        self.data = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.data * self.data
        if self.data >= 10:
            raise StopIteration
        self.data += 1
        return result

my_iter = MyIterator()
print(type(my_iter))

print(next(my_iter))
for item in my_iter:
    print(item)
print(next(my_iter))    # StopIteration

