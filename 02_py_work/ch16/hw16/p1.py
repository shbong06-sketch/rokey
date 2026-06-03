# p1.py

# 문제1. 은행 번호표 시스템
# 은행에서 고객 상담을 위해 번호표 대기 시스템을 만들려고 합니다.
# 앞서 학습한 2가지 자료구조 중 하나를 선택하여 프로그램을 작성하시오.
# => Queue
# 번호표 => 1: 철수, 2: 영희, 3: 민수
from queue_class import Queue
bank = Queue()
bank.enqueue("철수")
bank.enqueue("영희")
bank.enqueue("민수")
print(bank.status_queue())
bank.dequeue()              # 첫번째 상담자
print(bank.status_queue())

print("--------------------------------------")
# 문제2. 브라우저 뒤로가기 시스템
# 웹 브라우저 방문 기록을 관리하는 프로그램을 작성하세요.
# 앞서 학습한 2가지 자료구조 중 하나를 선택하여 프로그램을 작성하시오.
# => Stack
from stack_class import Stack
browser = Stack()
browser.push("네이버")
browser.push("유튜브")
browser.push("구글")
print(browser.status_queue())
browser.pop()               # 뒤로가기 버튼 클릭
print(browser.peak())       # 현재 위치한 사이트
print(browser.status_queue())