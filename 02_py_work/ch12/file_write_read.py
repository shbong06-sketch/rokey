# file_write_read.py
# 파일포인터

path = r'ch12\file3.txt'
mode = 'w+'
f = open(path, mode)

for i in range(1,11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)

# print(f.read())     # 읽은 내용 출력 X
f.seek(0)           # 파일포인터 위치 재조정
print(f.read())

f.close()

# f.seek(cookie, whence)
# cookie : 파일 내 위치 상태값(포인터 정보)
# whence 값 정리
# 0: 파일 시작
# 1: 현재 위치
# 2: 파일 끝