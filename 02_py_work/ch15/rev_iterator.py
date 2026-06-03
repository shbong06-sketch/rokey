# rev_iterator.py

class ReverseIterator:    
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

ri = ReverseIterator([1, 2, 3, 4, 5])
print(type(ri))
print(next(ri))         # 5
# print(ri.__next__())    # 4

for item in ri:         # 3 2 1
    print(item)

# print(next(ri))         # StopIteration

# 이터레이터 판단 기준
# 즉, 객체에 다음 메서드가 있으면 이터레이터로 인식
# __iter__
# __next__
# dir() : 객체의 속성을 보여주는 함수
print(dir(ri))      # list 형태로 내부에 정의되어 있는 내용 확인.

print('__iter__' in dir(ri))    # True
print('__next__' in dir(ri))    # True