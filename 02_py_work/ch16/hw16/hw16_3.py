# hw16_3.py

# 10.
class Deque:
    # 리스트를 이용하여 덱(deque, 양방향 큐)을 구현
    def __init__(self):
        self.deque = []
    # push_front(x): 정수 x를 덱의 앞에 추가
    def push_front(self, x):
        self.deque.insert(0, x)
    # push_back(x): 정수 x를 덱의 뒤에 추가  
    def push_back(self, x):
        self.deque.append(x)
    # pop_front(): 덱의 앞에서 값을 제거하고 반환
    # (비어 있다면 -1)
    def pop_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return
    # pop_back(): 덱의 뒤에서 값을 제거하고 반환
    # (비어 있다면 -1)
    def pop_back(self):
        if not self.is_empty():
            return self.deque.pop()
        return
    # 덱 안의 데이터 유무 확인
    def is_empty(self):
        if len(self.deque) == 0:
            return True
        return False
    
if __name__ == "__main__":
    s1 = Deque()
    s1.push_front(2)
    s1.push_front(1)
    s1.push_back(3)
    s1.push_back(4)
    print(s1.pop_back())
    print(s1.pop_front())
    print(s1.is_empty())