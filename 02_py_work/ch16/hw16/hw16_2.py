# hw16_2.py

# 8.
class Queue:
    # 리스트를 사용하여 기본적인 큐(queue)를 구현
    def __init__(self):
        self.queue = []
    # enqueue(x): 정수 x를 큐의 끝에 추가
    def enqueue(self, data):
        self.queue.append(data)
    # dequeue(): 큐의 앞에서 값을 제거하고 반환.
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        # 만약 큐가 비어 있다면 -1을 반환
        return -1
    # is_empty(): 큐가 비어 있으면 True, 아니면 False를 반환
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    # front(): 큐의 앞에 있는 값을 반환.
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        # 만약 큐가 비어 있다면 -1을 반환
        return -1
    
if __name__=="__main__":
    queue = Queue()
    queue.enqueue(1)
    print(queue.front())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.front())
    print(queue.is_empty())
    print(queue.dequeue())


print("-------------------------------")
# 은행에 도착한 고객 순서대로 업무를 처리하는
# 선입선출(FIFO) 구조의 큐 프로그램을 작성
# 리스트를 활용하여 아래 기능을 수행하는 코드를 작성
# 조건:



# 3. 현재 대기 중인 고객 명단을 확인하는 기능을 포함하세요.
class Bank(Queue):
    def status_queue(self):
        if not super().is_empty():
            return self.queue
bank = Bank()
# 1. 고객이 도착하면 이름을 큐에 추가합니다 (Enqueue). 
bank.enqueue("김철수")
bank.enqueue("이영희")
bank.enqueue("박민수")
print(f"현재 대기열: {bank.status_queue()}")
# 2. 업무 처리가 시작되면 가장 먼저 온 고객부터 이름을 출력하고
#   큐에서 제거합니다 (Dequeue). 
print(f"업무 처리 중인 고객: {bank.dequeue()}")
print(f"현재 남은 대기 고객: {bank.status_queue()}")