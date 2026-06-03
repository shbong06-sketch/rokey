# p2_1.py

# p.20 괄호 짝 검사
# 기능: 문자열에 포함된 괄호의 짝이 올바르게 사용되었는지 확인
#       스택 활용(괄호의 종류는 ()소괄호, {}중괄호, []대괄호 세가지)
# 입력: 문자열
# 반환: True/False

def check_brackets(text):
    # 1. 빈 스택 생성
    stack = []
    # 2. 문자열 하나씩 가져와서 괄호 찾기
    for char in text:
        # 3. '시작' 괄호라면 스택에 push
        if char in "({[":
            stack.append(char)
        # 4. '종료' 괄호라면 스택에 pop
        elif char in ")}]":
            # 4-1. 스택이 비었다면(매칭되는 시작 괄호가 없음) => False
            if len(stack)==0:
                return False
            # 5. 동일한 괄호가 서로 매칭되면 스택의 괄호 제거
            top = stack.pop()
            # 4-2. 괄호 짝이 일치하지 않는 경우
            if char == ")" and top != "(" or char == "}" and top != "{" or char == "]" and top != "[" :
                return False
    # 6. 스택이 비었다면 True(짝 맞음)
    return len(stack) == 0

print(check_brackets("(a+b)"))          # True
print(check_brackets("(a+b)]}"))        # False - 6. 빈스택 아님.
print(check_brackets("[{(x+y)+3}-4]"))  # True
print(check_brackets("[{x+y)+3}-4]"))   # False - 4-2. 괄호 짝이 일치하지 않음.
print(check_brackets("a+b)*3}"))        # False - 4-1. 매칭되는 시작 괄호 없음