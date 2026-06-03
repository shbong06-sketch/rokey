# p3.py

# p.22
# 회전 큐 구현
# 데이터를 양방향으로 삽입하거나 제거할 수 있는 회전 큐를 구현.

# # 1. 덱 사용
# from collections import deque
# rotate_queue = deque([1, 2, 3, 4])
# # 마지막에 삽입
# rotate_queue.append(5)
# # 처음에 삽입
# rotate_queue.appendleft(0)
# # 마지막 제거
# rotate_queue.pop()
# # 처음 제거
# rotate_queue.popleft()

# # 왼쪽으로 n(-> 2) 만큼 회전
# n = 2
# for _ in range(n):
#     rotate_queue.rotate(-1)
# print(rotate_queue)

# 2. 리스트로 구현
class Rotate_Queue:
    def __init__(self):
        self.r_queue = []
    # 마지막에 삽입
    def append(self, data):
        self.r_queue.append(data)
    # 처음에 삽입
    def appendleft(self, data):
        self.r_queue.insert(0, data)
    # 마지막 제거
    def pop(self):
        if not len(self.r_queue) == 0:
            return self.r_queue.pop()
        return
    # 처음 제거
    def popleft(self):
        if not len(self.r_queue) == 0:
            return self.r_queue.pop(0)
        return
    # 왼쪽으로 회전
    def rotate_to_left(self):
        if not len(self.r_queue) == 0:
            return self.append(self.r_queue.pop(0))
        return
    # 오른쪽으로 회전
    def rotate_to_right(self):
        if not len(self.r_queue) == 0:
            return self.appendleft(self.r_queue.pop())
        return
    # 현재 큐 확인
    def status_queue(self):
        return self.r_queue
    
rotate_queue = Rotate_Queue()

# 마지막에 삽입
rotate_queue.append(3)
rotate_queue.append(4)
rotate_queue.append(5)
# 처음에 삽입
rotate_queue.appendleft(2)
rotate_queue.appendleft(1)
rotate_queue.appendleft(0)
# 마지막 제거
rotate_queue.pop()
# 처음 제거
rotate_queue.popleft()

# 왼쪽으로 n(-> 2) 만큼 회전
n = 2
for _ in range(n):
    rotate_queue.rotate_to_left()
print(rotate_queue.status_queue())