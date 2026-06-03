# file_open.py

import os

 # 작업디렉터리 확인
print(os.getcwd())

 # \를 /로 바꾸는 이유: \와 문자가 조합되면 특별한 의미로 쓰이기도 한다.("\n" : 줄바꿈(newline))
#  r : raw(날것의, 원형의) => \ 원래 그대로의 의미로 사용하라는 의미.

# 파일 열기
# f = open(r'C:\rokey\py_work\ch12\file1.txt')    # 절대경로
f = open(r'ch12\file1.txt', 'w')                     # 상대경로(작업디렉터리 기준)
# f.메서드명  # 파일객체의 멤버함수
# f.변수명    # 파일객체의 멤버변수

# 파일 닫기
f.close()    # 파일 닫아야 메모리 낭비 막을 수 있다.