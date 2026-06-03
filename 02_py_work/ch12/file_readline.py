# file_readline.py
# 파일 객체설정 및 모드 설정
# 파일을 읽기 위한 함수

# 파일객체명.readline()

f = open(r'ch12\file1.txt', 'r') # 인코딩 확인 필요 ; 해당 파일이 utf-8로 생성된 경우, 오류 발생
# f = open(r'ch12\file1.txt', 'r', encoding='utf-8')

# line1 = f.readline(5)   # 5글자까지만 읽기
# line2 = f.readline()
# line3 = f.readline()

# 특정 줄만 읽어서 출력
# for i, line in enumerate(f, start=1):
#     if i == 3:
#         print(i, line)

# print(line1)
# print(line2)
# print(line3)

f.close()