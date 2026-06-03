# iterator.py
# 이터레이터 생성 방법2 : 클래스 구현 -> 내가 구현하고자 하는 프로그램에 맞게끔 사용 가능
class MyIterator:
    # 1. 멤버 변수
    # 2. 멤버 함수(메서드)
    def __init__(self, data):
        self.data = data
        self.position = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position >= len(self.data) :
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

i = MyIterator([1, 2, 3])
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

print(type(i))

for item in i:
    print(item)

## 이터레이터 사용 목적
# : 데이터를 한번에 다 들고 있지 않고,
#   필요할 때마다 하나씩 꺼내 쓰기 위해
# - 리스트: 모든 값을 메모리에 저장해 사용
# - 이터레이터: 값을 하나씩 생성 => 메모리 거의 안씀 ; 파일, 로그, 네트워킹 등 활용(큰 데이터)

