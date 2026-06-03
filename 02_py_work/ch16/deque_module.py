# deque_module.py

from collections import deque

dq = deque()      # 덱 생성
print(type(dq))   # class 'collections.deque'

dq.append(1)      # 뒤로 삽입
print(dq)

dq.appendleft(2)  # 앞으로 삽입
print(dq)
print(len(dq))    # 길이/크기 확인

dq.pop()          # 마지막 데이터 제거
print(dq)
if not dq:
    print("비어있음")

dq.popleft()      # 처음 데이터 제거
print(dq)
if not dq:
    print("비어있음")

# 초기값 설정
dq2 = deque([1, 2, 3, 4])

# 오른쪽(1)/왼쪽(-1) 회전
dq2.rotate(1)
print(dq2)      # [4, 1, 2, 3]
dq2.rotate(-1)
print(dq2)      # [1, 2, 3, 4]