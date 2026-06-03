# p2.py

# p.20 괄호 짝 검사
# 기능: 문자열에 포함된 괄호의 짝이 올바르게 사용되었는지 확인
#       스택 활용(괄호의 종류는 ()소괄호, {}중괄호, []대괄호 세가지)
# 입력: 문자열
# 반환: True/False

# 1. 괄호를 담을 빈 스택을 생성
# 2. 문자열 내 문자를 가져옴.
# 3. 만약, 문자가 '시작' 괄호라면 스택에 push
# 4. 문자를 순차적으로 확인하다가 '종료'괄호가 있다면 스택에서 pop
#   4-1. 만약, 스택이 비었다면(매칭되는 시작 괄호가 없음) => False
#   4-2. pop 한 괄호를 확인했는데 서로 일치하지 않음 => False
# 5. 동일한 괄호가 서로 매칭되면 스택의 괄호 제거
# 6. 스택이 비었다면 True(짝 맞음)

def check_brackets(text):
    stack = []                      # 1. 빈 스택 생성

    for char in text:               # 2. 문자열 내 문자 가져옴
        if char in "({[":           # 3. '시작' 괄호라면 스택에 push
            stack.append(char)  
        elif char in ')}]':         # 4. '종료' 괄호라면 스택에 pop
            if not stack:           # 4-1.
                return False
            top = stack.pop()       # 5. 동일 괄호 매칭되면 스택 괄호 제거

        # 4-2. 괄호 짝이 일치하지 않는 경우
    if (char == ")" and top != "(") or \
        (char == "}" and top != "{") or \
        (char == "]" and top != "["):
        return False    # 짝이 안맞음
    return len(stack) == 0          # 6. 스택이 비었다면 짝 맞음

print(check_brackets("(a+b)"))     # True
print(check_brackets("(a+b)]}"))    # False
print(check_brackets("[{(x+y)+3}-4]"))    # True
print(check_brackets("[{x+y)+3}-4]"))    # False