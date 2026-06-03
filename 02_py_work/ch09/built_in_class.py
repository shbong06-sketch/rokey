# built_in_class.py

# 문자열 '10'을 na 변수명으로 할당
# 문자열 => 정수형 자료형 변경.
na = "10"
na = int("10")
print(type(na))

# class int:
#     def __init__(self, data):
#         self.data = data
#         # 기능: 정수형으로 변환

print("--------------------------")
strb = str("abc")
print(strb)

strc = strb.capitalize()
print(strc)

# class str:
#     def __init__(self, data):
#         self.data = data
#         # 기능: 문자열로 변환
#     def capitalize(self):
#         # 기능: 첫 자를 대문자로 변환
#         return 첫자 대문자 문자열

help(print)