# file_append.py

path = r'ch12\file1.txt'
mode = 'a'
f = open(path, mode)
# f = open(path, mode, encoding='utf-8')

for i in range(11,21):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)

f.close()

# f = open(path, 'r')
# print(f.read())
# f.close()

# 모드 종류
# 'r' : read
# 'w' : write
# 'a' : append
# 'r+' : read + write => 파일을 읽고 쓰기 ; 기 데이터 존재해야
# 'w+' : write + read => 파일을 새로 만들거나 비우고 쓰고 읽기
# 'a+' : append + read

