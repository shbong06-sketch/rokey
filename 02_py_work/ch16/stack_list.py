# stack_list.py
# 스택 구현: 리스트 활용

# 빈 스택 구현
stack = []  # 빈 리스트

# push 기능 구현 : 오른쪽(한쪽) 방향으로 데이터가 쌓인다.
stack.append(1)
print(f"stack = {stack}")
stack.append(2)
print(f"stack = {stack}")
stack.append(3)
print(f"stack = {stack}")
stack.append(4)
print(f"stack = {stack}")

# pop 기능 구현
stack.pop()
print(f"stack = {stack}")
stack.pop()
print(f"stack = {stack}")
stack.pop()
print(f"stack = {stack}")

# 스택이 비어있는 경우,
if stack ==[]:
    print("is empty!")
else:
    stack.pop()
    print(f"stack = {stack}")
# stack.pop()                 # IndexError: pop from empty list
# print(f"stack = {stack}")

# 스택 Top(꼭대기) 값 확인
if stack ==[]:
    print("is empty!")
else:
    print(f"top data = {stack[-1]}")    # IndexError

# 스택이 비어있는지 확인이 계속 필요 => 효율성.. => 클래스, 함수 활용