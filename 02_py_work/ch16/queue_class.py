# queue_class.py
class Queue:
    # 0. 큐 리스트 생성: 데이터 공간 초기화
    def __init__(self):
        self.queue = []

    # 1. Enqueue : 데이터 삽입
    # 기능: 큐에 데이터 넣기
    # 입력: 데이터
    # 출력: 없음
    def enqueue(self, data):
        self.queue.append(data)
    
    # 2. Dequeue : 데이터 제거
    # 기능: 큐에서 데이터 제거
    # 입력: 없음
    # 출력: 큐 내 맨 앞 데이터
    def dequeue(self):
        # 큐가 비어있는 경우 고려
        if not self.is_empty():
            return self.queue.pop(0)
        return
    
    # 3. 큐가 비어있는지 확인
    # 기능: 큐 내 데이터 유무 확인
    # 입력: 없음
    # 출력: True/False
    def is_empty(self):
        if len(self.queue) == 0 :
            return True
        return False
    
    # 4. 큐 상태 반환
    # 기능: 큐 상태 반환
    # 입력: 없음
    # 출력: 현재 큐
    def status_queue(self):
        return self.queue
    
if __name__ == "__main__":
    q1 = Queue()        # 큐 생성
    q1.dequeue()
    q1.enqueue(1)       # 1
    q1.enqueue(2)       # 1, 2
    q1.dequeue()        # 2
    print(q1.status_queue())
    q1.enqueue(3)       # 2, 3
    q1.enqueue(4)       # 2, 3, 4
    print(q1.status_queue())