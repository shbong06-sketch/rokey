# hw16_1.py

# 6.
class Stack:
# 리스트를 이용하여 기본적인 스택(stack)을 구현
    def __init__(self):
        self.stack = []
# push(x): 정수 x를 스택에 삽입
    def push(self, data):
        self.stack.append(data)
# pop(): 스택에서 가장 위의 값을 제거하고 반환. 만약 스택이 비어 있다면 -1을 반환
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return -1
# top(): 스택의 가장 위에 있는 값을 반환. 만약 스택이 비어 있다면 -1을 반환
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return -1
# is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환
    def is_empty(self):
        # if len(self.stack) == 0:
        #     return True
        # return False
        return len(self.stack) == 0    
    
if __name__ == "__main__":
    s1 = Stack()
    s1.push(1)
    print(s1.top())
    print(s1.pop())
    print(s1.top())
    print(s1.pop())
    print(s1.is_empty())

print("---------------------------------")
# 7.
# 후위 표기법(Postfix Notation, Reverse Polish Notation)으로
# 주어진 수식을 계산하는 프로그램을 작성하세요.
# 후위 표기법에서는 연산자가 피연산자 뒤에 위치합니다.
# 예를 들어, 3 4 +는 3 + 4를 의미하며, 결과는 7입니다.
# 연산자는 +, -, *, /만 고려합니다. (복수 연산자도 처리 가능해야 함.)

def is_number(s:str):   # 문자열이 숫자로 이루어져있는지 확인(음수 포함)
    try :
        float(s)
        return True
    except ValueError:
        return False

def postfix_notation(text):
    # 1. 빈 스택 생성
    stack = []
    # 2. 문자열에서 연산자 가져오기
    for char in text.split():
        # 3. 스택에 숫자 넣기(정수형)
        if is_number(char) :
            stack.append(float(char))  # stack = [3, 5, 2]
        # 4. 문자열에서 연산자와 만나면 계산 실행
        elif char in "+-*/":
            # 4-1. 스택 개수가 2보다 작은 경우 => 숫자가 부족 ; 예) "3 +"
            if len(stack) < 2:
                raise ValueError("잘못된 식 형태입니다.")
            # 계산할 숫자(후위 2개) 꺼내오기
            n1 = stack.pop()
            n2 = stack.pop()
            # if char == "+":
            #     value =  n2 + n1
            # elif char == "-":
            #     value = n2 - n1
            # elif char == "*":
            #     value = n2 * n1
            # elif char == "/":
            #     try:
            #         value = n2 / n1
            #     except ZeroDivisionError:
            #         raise ValueError("0으로 나눌 수 없습니다.")
                
            # 디스패치 테이블 => 조건문 4번 반복. 복잡 => 딕셔너리로 키 값을 받아서 계산하는 식으로 변경
            # 연산자에 따라 계산 실행
            ops = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b
            }
            value = ops[char](n2, n1)
            # 계산 결과를 다시 스택에 push하여 남은 계산 진행
            stack.append(value)
        # 4-2. 숫자와 연산자 이외에 다른 문자가 오는 경우 => 예) 3 4 a +
        else:
            raise ValueError("잘못된 식 형태입니다.")
    # 4-3. 연산자 숫자가 부족한 경우 => 예) 3 4
    if len(stack) != 1:
        raise ValueError("잘못된 식 형태입니다.")
    return stack.pop()

print(postfix_notation("3 4 +"))
print(postfix_notation("3 5 2 * +"))
print(postfix_notation("3 +"))
print(postfix_notation("3 4"))
print(postfix_notation("3 14 a +"))


# 3+5*2, 출력: 352*+