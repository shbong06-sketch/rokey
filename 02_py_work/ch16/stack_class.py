# stack_class.py
class Stack:
    # 1. 스택 리스트
    def __init__(self):
        self.stack = []
    
    # 1. push
    # 기능: stack에 데이터 넣기
    # 입력: 데이터
    # 출력: 없음
    def push(self, data):
        self.stack.append(data)

    # 2. pop
    # 기능: stack에서 데이터 제거하기
    # 입력: 없음
    # 출력: stack 내 상단 데이터
    def pop(self):
        # 스택이 비어있는 경우 고려
        if not self.is_empty():
            return self.stack.pop()
        return
    
    # 3. 스택 내 데이터 유무 확인
    # 기능: 스택 내 데이터 유무 확인
    # 입력: 없음
    # 출력: True/False
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # 4. 스택 최상위(Top) 데이터 확인
    # 기능: stack에서 최상위 데이터 확인
    # 입력: 없음
    # 출력: stack 내 최상단 데이터
    def peak(self):
        # 스택이 비어있는 경우 고려
        if not self.is_empty():
            return self.stack[-1]
        return
    
    # 5. 스택 상태 반환
    # 기능: 스택 상태 반환
    # 입력: 없음
    # 출력: 현재 스택
    def status_stack(self):
        return self.stack

if __name__=="__main__":
    s1 = Stack()
    print(s1.peak())
    s1.pop()
    s1.push(1)
    print(s1.status_stack())
    s1.push(2)
    print(s1.status_stack())
    s1.pop()
    print(s1.status_stack())
    s1.push(3)
    s1.push(4)
    print(s1.peak())
    print(s1.status_stack())

# 제대로 동작하는지 확인하려면,
# 분기마다/예외적인 상황까지 테스트가 모두 이루어져야 한다!!